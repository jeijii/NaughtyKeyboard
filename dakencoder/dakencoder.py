#!/usr/bin/env python
from __future__ import print_function
import time
import sys
import getopt
import os


class dakEncoder:

    def __init__(self):
        self.modifier_keys = {
            "MODIFIER_CTRL": 0x01,
            "MODIFIER_SHIFT": 0x02,
            "MODIFIER_ALT": 0x04,
            "MODIFIER_GUI": 0x08
        }
        self.keys = {
            "a": 0x4,
            "b": 0x5,
            "c": 0x6,
            "d": 0x7,
            "e": 0x8,
            "f": 0x9,
            "g": 0xA,
            "h": 0xB,
            "i": 0xC,
            "j": 0xD,
            "k": 0xE,
            "l": 0xF,
            "m": 0x10,
            "n": 0x11,
            "o": 0x12,
            "p": 0x13,
            "q": 0x14,
            "r": 0x15,
            "s": 0x16,
            "t": 0x17,
            "u": 0x18,
            "v": 0x19,
            "w": 0x1A,
            "x": 0x1B,
            "y": 0x1C,
            "z": 0x1D,
            "1": 0x1E,
            "2": 0x1F,
            "3": 0x20,
            "4": 0x21,
            "5": 0x22,
            "6": 0x23,
            "7": 0x24,
            "8": 0x25,
            "9": 0x26,
            "0": 0x27,
        }
        self.other_keys = {
            "ENTER": 0x28,
            "ESC": 0x29,
            "BACKSPACE": 0x2A,
            "TAB": 0x2b,
            "SPACE": 0x2c,
            "MINUS": 0x2d,
            "EQUAL": 0x2e,
            "LEFT_BRACE": 0x2f,
            "RIGHT_BRACE": 0x30,
            "BACKSLASH": 0x31,
            "SEMICOLON": 0x33,
            "QUOTE": 0x34,
            "TILDE": 0x35,
            "COMMA": 0x36,
            "PERIOD": 0x37,
            "SLASH": 0x38,
            "CAPS_LOCK": 0x39,
            "F1": 0x3a,
            "F2": 0x3b,
            "F3": 0x3c,
            "F4": 0x3d,
            "F5": 0x3e,
            "F6": 0x3f,
            "F7": 0x40,
            "F8": 0x41,
            "F9": 0x42,
            "F10": 0x43,
            "F11": 0x44,
            "F12": 0x45,
            "PRINTSCREEN": 0x46,
            "SCROLL_LOCK": 0x47,
            "PAUSE" : 0x48,
            "INSERT": 0x49,
            "HOME": 0x4A,
            "PAGEUP": 0x4B,
            "DELETE": 0x4C,
            "END": 0x4D,
            "PAGEDOWN": 0x4E,
            "RIGHT": 0x4F,
            "LEFT": 0x50,
            "DOWN": 0x81,
            "UP": 0x82,
            "LEFT_CTRL": 0xE0,
            "LEFT_SHIFT": 0xE1,
            "LEFT_ALT": 0xE2,
            "LEFT_GUI": 0xE3
        }
        self.arr = []
    def readScript(self, filename):
        readablescript = []
        with open(filename, "r") as f:
            lines = f.readlines()
            retlines = []
        for l in lines:
            # remove comment from line
            l = l.split("//")[0]
            # remove line breaks
            l = l.strip().replace("\r\n", "").replace("\n", "")
            # skip empty lines
            if len(l) == 0:
                continue
            print(l)
            readablescript.append(l)
        self.parseLines(readablescript)


    def parseLines(self, lines):
        for l in lines:
            _ = l.split(" ", 1)
            str = self.parseCommand(_);
            if str is not None:
                str.encode()
                self.arr.append(str)
                release = chr(0)*8
                self.arr.append(release.encode())

        self.sendReport()
        return

    def parseCommand(self, arr):
        if len(arr) == 1:
            if arr[0] == "REM":
                return None
            if arr[0] == "MENU":
                return None
            if arr[0] == "ALT":
                return None
            if arr[0] == "CTRL" or arr[0] == "CONTROL":
                return None
            if arr[0] == "DOWNARROW" or arr[0] == "DOWN":
                return None
            if arr[0] == "LEFTARROW" or arr[0] == "LEFT":
                return None
            if arr[0] == "RIGHTARROW" or arr[0] == "RIGHT":
                return None
            if arr[0] == "UPARROW" or arr[0] == "UP":
                return None
            if arr[0] == "DELETE":
                return None
            if arr[0] == "HOME":
                return None
            if arr[0] == "INSERT":
                return None
            if arr[0] == "NUMLOCK":
                return None
            if arr[0] == "PAGEUP":
                return None
            if arr[0] == "PAGEDOWN":
                return None
            if arr[0] == "PRINTSCREEN":
                return None
            if arr[0] == "SCROLLLOCK":
                return None
            if arr[0] == "SPACE":
                return None
            if arr[0] == "TAB":
                return None
            if arr[0] == "ENTER":
                return chr(0)*2+chr(self.other_keys["ENTER"])+chr(0)*5
        if len(arr) == 2:
            if arr[0] == "ALT":
                return None
            if arr[0] == "DELAY":
                return None
            if arr[0] == "STRING":
                return None
            if arr[0] == "GUI" or arr[0] == "WINDOWS":
                return chr(self.modifier_keys["MODIFIER_GUI"])+chr(0)+chr(self.keys[str(arr[1]).lower()])+chr(0)*5
            if arr[0] == "SHIFT":
                return None
            if arr[0] == "CONTROL" or arr[0] == "CTRL":
                return None
            if arr[0] == "REPEAT":
                return None
        return

    def parseString(self, string):
        return

    def sendReport(self):
        with open('/dev/hidg0', 'rb+') as fd:
            for item in self.arr:
                fd.write(item)
            return

def main(argv):
    encoder = dakEncoder()
    encoder.readScript(argv[0])

if __name__ == "__main__":
    if len(sys.argv) < 1:
        sys.exit()
main(sys.argv[1:])