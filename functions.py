"""
Practical Use Functions
"""


def clear():
    """Clears the console, regardless of OS."""
    from os import system, name
    
    system("cls" if name == "nt" else "clear")
