"""A module built over Python's msvcrt to make working with keyboards easier."""
import msvcrt


def kbinput(prompt: str, choices, clear_screen=False):
    """(aka input() but with key presses)
    suspends the program until a character from choices is entered.
    It then returns the Unicode code point for said character.
    clear_screen: determines whether the console screen is cleared
    after the user enters their choice (default is false to mimic input()).
    """
    from os import system, name
    
    print(prompt, end="", flush=True)
    choice_entered = False
    while not choice_entered:
        if msvcrt.kbhit():
            user_input = ord(msvcrt.getch())
            if user_input in choices:
                choice_entered = True
                if clear_screen:
                    system("cls" if name == "nt" else "clear")
    return user_input


def main():
    """For use in Debugging..."""
    pass


if __name__ == "__main__":
    main()
