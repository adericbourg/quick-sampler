#!/usr/bin/env python3
import sys

from ui.appgui import AppGui


def main():
    print("Running application")
    gui = AppGui(sys.argv)
    res = gui.show()
    sys.exit(res)


if __name__ == "__main__":
    main()
