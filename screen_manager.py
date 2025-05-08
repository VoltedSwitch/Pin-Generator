# File Name ---> screen_manager.py
import os
import time


class ScreenManager:
    def __init__(self):
        # ANSI Cursor Control
        self.hideCursor = "\033[?25l"
        self.showCursor = "\033[?25h"

        # ANSI Text Formatting
        self.boldText = "\033[1m"
        self.boldLimit = "\033[22m"

        self.underlineText = "\033[4m"
        self.underlineLimit = "\033[24m"

        # ANSI Normal Color Type
        self.black = "\033[0;30m"
        self.red = "\033[0;31m"
        self.green = "\033[0;32m"
        self.yellow = "\033[0;33m"
        self.blue = "\033[0;34m"
        self.purple = "\033[0;35m"
        self.cyan = "\033[0;36m"
        self.white = "\033[0;37m"

        # ANSI Bright Color Type
        self.brightBlack = "\033[0;90m"
        self.brightRed = "\033[0;91m"
        self.brightGreen = "\033[0;92m"
        self.brightYellow = "\033[0;93m"
        self.brightBlue = "\033[0;94m"
        self.brightPurple = "\033[0;95m"
        self.brightCyan = "\033[0;96m"
        self.brightWhite = "\033[0;97m"

        # ANSI Dark (Bold) Color Type
        self.blackDark = "\033[1;30m"
        self.redDark = "\033[1;31m"
        self.greenDark = "\033[1;32m"
        self.yellowDark = "\033[1;33m"
        self.blueDark = "\033[1;34m"
        self.purpleDark = "\033[1;35m"
        self.cyanDark = "\033[1;36m"
        self.whiteDark = "\033[1;37m"

        # ANSI Color End
        self.colorLimit = "\033[0m"

    def cls(self):
        os.system("cls" if os.name == "nt" else "clear")

    def delay_cls(self, seconds):
        if isinstance(seconds, (int, float)) and seconds >= 0:
            time.sleep(seconds)
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("\033[31mNone\033[0m")

    def delay(self, seconds):
        if isinstance(seconds, (int, float)) and seconds >= 0:
            time.sleep(seconds)
        else:
            print("\033[31mNone\033[0m")

    def hide_cursor(self):
        print("\033[?25l")

    def show_cursor(self):
        print("\033[?25h")

    def bold_text(self):
        print("\033[1m")

    def limit_bold(self):
        print("\033[0m")

    def underline_text(self):
        print("\033[4m")

    def limit_underline(self):
        print("\033[0m")


sm = ScreenManager()
