"""
Practical Use Functions
"""


def clear():
    """Clears the console, regardless of OS."""
    from os import system, name
    
    system("cls" if name == "nt" else "clear")


def main():
    """For use in Debugging..."""
    pass


if __name__ == "__main__":
    main()
