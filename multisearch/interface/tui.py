import argparse
import logging
import sys
import time
from threading import Thread, Lock
from multisearch.config import Config, ConfigFactory
from multisearch.interface.input import SearchInput
from curses import wrapper

logging.basicConfig(filename='local_log.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

starttime = time.time()
lock = Lock()


class App:
    def __init__(self, config: Config, stdscr) -> None:
        self.config = config
        self.stdscr = stdscr

        scry, scrx = self.stdscr.getmaxyx()
        logging.debug("Screen size: " + str(scry) + "x" + str(scrx))
        logging.debug("Building search component")
        self.search_component = SearchInput(self.stdscr, self.search)
        self.search_component.activate()

        self.active_component = "search_component"
        self.components = {"search_component": self.search_component}

        self.render()
        event_loop = Thread(target=self.event_loop)
        event_loop.daemon = True
        event_loop.start()
        self.input_loop()

    def render(self):
        with lock:
            self.stdscr.erase()
            self.search_component.render()
            self.stdscr.refresh()

    def input_loop(self):
        while not self.stop:
            try:
                # get input
                key = self.stdscr.getch()
                print("KEY: " + str(key))
                # handle input
                self.components[self.active_component].receive_input(key)
                # todo: move selected result with arrow key

                self.render()
            except KeyboardInterrupt:
                sys.exit(0)

    def event_loop(self):
        while True:
            self.render()
            time.sleep(1 - ((time.time() - starttime) % 1))

    def search(self, query):
        query = query.strip()
        if query and len(query) > 1:
            print("SEARCHING FOR: " + query)
            # todo: clear all events and script outputs event{key}, results{key}
            # todo: call search scripts via primary tooling, passing add_event, add_result


def start_app(stdscr: "_curses._CursesWindow") -> None:
    logging.info("STARTING APP")
    parser = argparse.ArgumentParser(description="Multi Search Tool")
    parser.add_argument("identifier", type=str, help="The identifier to search for")
    logging.debug("building config")
    config: Config = ConfigFactory().build()
    logging.debug("calling app")
    App(config, stdscr)


def main() -> None:
    print("STARTING MAIN")
    try:
      wrapper(start_app)
    except Exception as e:
      print("ERROR: " + str(e))
      sys.exit(1)


if __name__ == "__main__":
    print("STARTING __main__")
    wrapper(start_app)