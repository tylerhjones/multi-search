import curses

class Component:
    def __init__(self, stdscr):
        self.stdscr = stdscr

    def activate(self):
        curses.curs_set(0)
        self.component.active = True

    def deactivate(self):
        curses.curs_set(1)
        self.component.active = False

    def create_border(self, color):
        self.stdscr.attron(curses.color_pair(color))

        # vertical borders
        for i in range(self.starty + 1, self.endy):
            self.stdscr.addstr(i, self.startx, "│")
            self.stdscr.addstr(i, self.endx, "│")

        # horizontal borders
        for i in range(self.startx + 1, self.endx):
            self.stdscr.addstr(self.starty, i, "─")
            self.stdscr.addstr(self.endy, i, "─")

        # top left corner
        self.stdscr.addstr(self.starty, self.startx, "╭")

        # top right corner
        self.stdscr.addstr(self.starty, self.endx, "╮")

        # bottom left corner
        self.stdscr.addstr(self.endy, self.startx, "╰")

        # bottom right corner
        self.stdscr.addstr(self.endy, self.endx, "╯")

        # title
        if self.title:
            self.stdscr.addstr(self.starty, self.startx + 2,
                               " " + self.title + " ")

        self.stdscr.attroff(curses.color_pair(color))

    def render(self, status=None):
        if self.interactive:
            self.create_border(5 if self.component.active else 4)
        self.component.render(status)