"""A module built over Python's msvcrt to make working with keyboards easier.
"""
import msvcrt


def kbinput(prompt: str, choices, clear_scrn=False):
    """(aka input() but with key presses)
    suspends the program until a character from choices is entered. It then returns the Unicode code point for said character.
    kw args: clear_scrn: determines whether console screen is cleared after user enters their choice (default is false to mimic input())
    """
    from os import system, name
    
    print(prompt, end="", flush=True)
    choice_entered = False
    while not choice_entered:
        if msvcrt.kbhit():
            user_input = ord(msvcrt.getch())
            if user_input in choices:
                choice_entered = True
                if clear_scrn:
                    system("cls" if name == "nt" else "clear")
    return user_input


k = {
    # misc1:
    "<BACKSPACE>": 8,
    "<TAB>": 9,
    
    "<ENTER>": 13,
    
    "<ESC>": 27,
    
    "<SPACE>": 32,
    
    '"': 34,
    "%": 37,
    "&": 38,
    "'": 39,
    "(": 40,
    ")": 41,
    "*": 42,
    "+": 43,
    ",": 44,
    "-": 45,
    ".": 46,
    "/": 47,

    # 0-9:
    "0": 48,
    "1": 49,
    "2": 50,
    "3": 51,
    "4": 52,
    "5": 53,
    "6": 54,
    "7": 55,
    "8": 56,
    "9": 57,

    # misc2:
    ":": 58,
    ";": 59,
    "<": 60,
    "=": 61,
    ">": 62,
    "?": 63,
    "@": 64,

    # UPPERCASE LATIN:
    "A": 65,
    "B": 66,
    "C": 67,
    "D": 68,
    "E": 69,
    "F": 70,
    "G": 71,
    "H": 72,
    "I": 73,
    "J": 74,
    "K": 75,
    "L": 76,
    "M": 77,
    "N": 78,
    "O": 79,
    "P": 80,
    "Q": 81,
    "R": 82,
    "S": 83,
    "T": 84,
    "U": 85,
    "V": 86,
    "W": 87,
    "X": 88,
    "Y": 89,
    "Z": 90,

    # misc3:
    "[": 91,
    "\\": 92,
    "]": 93,
    "^": 94,
    "_": 95,
    "`": 96,

    # lowercase latin:
    "a": 97,
    "b": 98,
    "c": 99,
    "d": 100,
    "e": 101,
    "f": 102,
    "g": 103,
    "h": 104,
    "i": 105,
    "j": 106,
    "k": 107,
    "l": 108,
    "m": 109,
    "n": 110,
    "o": 111,
    "p": 112,
    "q": 113,
    "r": 114,
    "s": 115,
    "t": 116,
    "u": 117,
    "v": 118,
    "w": 119,
    "x": 120,
    "y": 121,
    "z": 122,

    # misc4:
    "{": 123,
    "|": 124,
    "}": 125,
    "~": 126,
}


def main():
    """For use in Debugging..."""
    pass


if __name__ == "__main__":
    main()