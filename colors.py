"""A module that makes coloring strings in the console easier."""

from os import system

system("")

color_dict = {
    "default": "0",
    "bold": "1",
    "underline": "4",
    "negative": "7",

    "black": "30",
    "dark red": "31",
    "dark green": "32",
    "dark yellow": "33",
    "dark blue": "34",
    "dark purple": "35",
    "dark cyan": "36",

    "hl red": "41",
    "hl green": "42",
    "hl yellow": "43",
    "hl blue": "44",
    "hl purple": "45",
    "hl cyan": "46",
    "hl white": "47",

    "dark gray": "90",
    "red": "91",
    "green": "92",
    "yellow": "93",
    "blue": "94",
    "purple": "95",
    "cyan": "96",
}


def paint(text, *colors):
    """paint(text, *colors)
    if text is not a String, the toString will be used
    if the color name is not found in color_dict, no color is applied
    """
    
    color_codes = []
    
    for color in colors:
        try:
            color_codes.append(color_dict[color.lower()])
        except TypeError:
            if type(color) == int:
                color_codes.append(str(color))
            else:
                raise TypeError(f'"{type(color)}" is not a vaild type for color.')
        except KeyError:
            if color.isdigit():
                color_codes.append(color)
            else:
                raise KeyError(f"invalid color name: {color}.")
    return f"\033[{';'.join(color_codes)}m" + str(text) + "\033[0m"


def main():
    """For use in Debugging..."""
    pass


if __name__ == "__main__":
    main()