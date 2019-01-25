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
            "enter": 0x28,
            "esc": 0x29,
            "escape": 0x29,
            "backspace": 0x2A,
            "tab": 0x2b,
            "space": 0x2c,
            "minus": 0x2d,
            "equal": 0x2e,
            "left_brace": 0x2f,
            "right_brace": 0x30,
            "backslash": 0x31,
            "semicolon": 0x33,
            "quote": 0x34,
            "tilde": 0x35,
            "comma": 0x36,
            "period": 0x37,
            "slash": 0x38,
            "caps_lock": 0x39,
            "f1": 0x3a,
            "f2": 0x3b,
            "f3": 0x3c,
            "f4": 0x3d,
            "f5": 0x3e,
            "f6": 0x3f,
            "f7": 0x40,
            "f8": 0x41,
            "f9": 0x42,
            "f10": 0x43,
            "f11": 0x44,
            "F12": 0x45,
            "printscreen": 0x46,
            "scrolllock": 0x47,
            "pause": 0x48,
            "insert": 0x49,
            "home": 0x4A,
            "pageup": 0x4B,
            "delete": 0x4C,
            "end": 0x4D,
            "pagedown": 0x4E,
            "right": 0x4F,
            "left": 0x50,
            "down": 0x81,
            "up": 0x82,
            "left_ctrl": 0xE0,
            "left_shift": 0xE1,
            "left_alt": 0xE2,
            "left_gui": 0xE3
        }
        self.arr = []
    def readScript(self, filename):
        readablescript = []
        with open(filename, "r") as f:
            lines = f.readlines()
            retlines = []
        for l in lines:
            # remove comment from line
            #l = l.split("#")[0] breaks urls
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
            str = self.parseCommand(_)
            #if str is not None:
            #    str.encode()
            #    self.arr.append(str)
            #    release = chr(0)*8
            #    self.arr.append(release.encode())
        return

    def parseCommand(self, arr):
        if len(arr) == 1:
            if arr[0] == "ADMIN":
                self.sendReport(chr(self.modifier_keys["MODIFIER_CTRL"]) + chr(0) + unichr(self.keys['left_shift']) + chr(self.keys['enter']) + chr(0) * 4)
                self.releaseKey()
                return None
            if arr[0] == "REM":
                return None
            if arr[0] == "MENU":
                self.sendReport(chr(self.modifier_keys["MODIFIER_GUI"])+chr(0) + chr(self.keys['d']) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "ALT":
                self.sendReport(chr(0) * 2 + chr(self.keys["left_alt"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "CTRL" or arr[0] == "CONTROL":
                self.sendReport(chr(0) * 2 + chr(self.keys["left_ctrl"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "DOWNARROW" or arr[0] == "DOWN":
                self.sendReport(chr(0) * 2 + chr(self.keys["down"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "LEFTARROW" or arr[0] == "LEFT":
                self.sendReport(chr(0) * 2 + chr(self.keys["left"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "RIGHTARROW" or arr[0] == "RIGHT":
                self.sendReport(chr(0) * 2 + chr(self.keys["right"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "UPARROW" or arr[0] == "UP":
                self.sendReport(chr(0) * 2 + chr(self.keys["up"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "DELETE":
                self.sendReport(chr(0) * 2 + chr(self.keys["delete"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "HOME":
                self.sendReport(chr(0) * 2 + chr(self.keys["home"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "INSERT":
                self.sendReport(chr(0) * 2 + chr(self.keys["insert"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "NUMLOCK":
                return None
            if arr[0] == "PAGEUP":
                self.sendReport(chr(0) * 2 + chr(self.keys["pageup"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "PAGEDOWN":
                self.sendReport(chr(0) * 2 + chr(self.keys["pagedown"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "PRINTSCREEN":
                self.sendReport(chr(0) * 2 + chr(self.keys["printscreen"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "SCROLLLOCK":
                self.sendReport(chr(0) * 2 + chr(self.keys["scrolllock"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "SPACE":
                self.sendReport(chr(0) * 2 + chr(self.keys["space"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "TAB":
                self.sendReport(chr(0) * 2 + chr(self.keys["tab"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "ENTER":
                self.sendReport(chr(0)*2+chr(self.keys["enter"])+chr(0)*5)
                self.releaseKey()
                return None
            if arr[0] == "F1":
                self.sendReport(chr(0)*2+chr(self.keys["f1"])+chr(0)*5)
                self.releaseKey()
                return None
            if arr[0] == "F2":
                self.sendReport(chr(0) * 2 + chr(self.keys["f2"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F3":
                self.sendReport(chr(0) * 2 + chr(self.keys["f3"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F4":
                self.sendReport(chr(0) * 2 + chr(self.keys["f4"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F5":
                self.sendReport(chr(0) * 2 + chr(self.keys["f5"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F6":
                self.sendReport(chr(0) * 2 + chr(self.keys["f6"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F7":
                self.sendReport(chr(0) * 2 + chr(self.keys["f7"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F8":
                self.sendReport(chr(0) * 2 + chr(self.keys["f8"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F9":
                self.sendReport(chr(0) * 2 + chr(self.keys["f9"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F10":
                self.sendReport(chr(0) * 2 + chr(self.keys["f10"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F11":
                self.sendReport(chr(0) * 2 + chr(self.keys["f11"]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "F12":
                self.sendReport(chr(0) * 2 + chr(self.keys["f12"]) + chr(0) * 5)
                self.releaseKey()
                return None
        if len(arr) == 2:
            if arr[0] == "ALT":
                if self.keys.__contains__(str(arr[1]).lower()):
                    self.sendReport(chr(self.modifier_keys["MODIFIER_ALT"]) + chr(0) + chr(self.keys[str(arr[1]).lower()]) + chr(0) * 5)
                    self.releaseKey()
                return None
            if arr[0] == "DELAY":
                time.sleep(int(arr[1])/1000)
                return None
            if arr[0] == "STRING":
                self.parseString(arr[1])
                return None
            if arr[0] == "GUI" or arr[0] == "WINDOWS":
                self.sendReport(chr(self.modifier_keys["MODIFIER_GUI"])+chr(0)+chr(self.keys[str(arr[1]).lower()])+chr(0)*5)
                self.releaseKey()
            if arr[0] == "SHIFT":
                self.sendReport(chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys[str(arr[1]).lower()]) + chr(0) * 5)
                self.releaseKey()
                return None
            if arr[0] == "CONTROL" or arr[0] == "CTRL":
                if self.keys.__contains__(str(arr[1]).lower()):
                    self.sendReport(
                        chr(self.modifier_keys["MODIFIER_ALT"]) + chr(0) + chr(self.keys[str(arr[1]).lower()]) + chr(
                            0) * 5)
                    self.releaseKey()
                return None
            if arr[0] == "REPEAT":
                return None
        return

    def parseString(self, string):
        for c in string:
            if str(c).islower() and self.keys.__contains__(str(c).lower()):
                self.sendReport(chr(0)*2+chr(self.keys[str(c).lower()])+chr(0)*5)
                self.releaseKey()
            elif str(c) == ".":
                self.sendReport(chr(0) * 2 + chr(self.keys["period"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == " ":
                self.sendReport(chr(0) * 2 + chr(self.keys["space"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c).isupper() and self.keys.__contains__(str(c).lower()):
                self.sendReport(chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys[str(c).lower()]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "!":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["1"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "@":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["2"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "#":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["3"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "$":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["4"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "%":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["5"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "^":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["6"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "&":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["7"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "*":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["8"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "(":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["9"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == ")":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["0"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "-":
                self.sendReport(chr(0) * 2 + chr(self.keys["minus"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "_":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["minus"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "=":
                self.sendReport(chr(0) * 2 + chr(self.keys["equal"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "+":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["equal"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "[":
                self.sendReport(chr(0) * 2 + chr(self.keys["left_brace"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "{":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["left_brace"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "}":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["right_brace"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "]":
                self.sendReport(
                    chr(0) + chr(0) + chr(self.keys["right_brace"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c) == "\\":
                self.sendReport(chr(0) * 2 + chr(self.keys["backslash"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "|":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["backslash"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c) == "`":
                self.sendReport(chr(0) * 2 + chr(self.keys["tilde"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "~":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["tilde"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c) == ";":
                self.sendReport(chr(0) * 2 + chr(self.keys["semicolon"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == ":":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["semicolon"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c) == ",":
                self.sendReport(chr(0) * 2 + chr(self.keys["comma"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "<":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["comma"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c) == ">":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["period"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c) == "/":
                self.sendReport(chr(0) * 2 + chr(self.keys["slash"]) + chr(0) * 5)
                self.releaseKey()
            elif str(c) == "?":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["slash"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c) == "\'":
                self.sendReport(
                    chr(0) + chr(0) + chr(self.keys["quote"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c) == "\"":
                self.sendReport(
                    chr(self.modifier_keys["MODIFIER_SHIFT"]) + chr(0) + chr(self.keys["quote"]) + chr(
                        0) * 5)
                self.releaseKey()
            elif str(c).isdigit():
                self.sendReport(chr(0) * 2 + chr(self.keys[str(c)]) + chr(0) * 5)
                self.releaseKey()
        return None

    def sendReport(self, report):
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(report.encode("utf-8"))

    def releaseKey(self):
        with open('/dev/hidg0', 'rb+') as fd:
            str = chr(0)*8
            fd.write(str.encode())

def main(argv):
    encoder = dakEncoder()
    encoder.readScript(argv[0])

if __name__ == "__main__":
    if len(sys.argv) < 1:
        sys.exit()
main(sys.argv[1:])
