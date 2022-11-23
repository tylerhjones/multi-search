import argparse
import asyncio
import logging
from multisearch.config import Config, ConfigFactory
from curses import wrapper


class App:
  def __init__(self, config:Config, stdscr) -> None:
      self.config = config
      self.stdscr = stdscr

  async def run(self):
    pass

async def run(app: App):
  await app.run()

def start_app(stdscr: "_curses._CursesWindow") -> None:
    parser = argparse.ArgumentParser(description='Omni Search Tool')
    parser.add_argument('identifier', type=str,
                        help='The identifier to search for')
    parser.add_argument('--debug', action='store_true',
                    help='Enable debug logging')

    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    config: Config = ConfigFactory().build()
    app = App(config, stdscr)
    return asyncio.run(run(app))

def main() -> None:
    wrapper(start_app)

if __name__ == "__main__":
    wrapper(start_app)