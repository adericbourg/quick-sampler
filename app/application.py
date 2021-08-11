#!/usr/bin/env python3
import sys

from ui.appgui import AppGui


def main(args):
    print("Running application")
    gui = AppGui(args)
    res = gui.run()
    sys.exit(res)


if __name__ == "__main__":
    main(sys.argv)
