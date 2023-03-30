"""If, for whatever reason, you don't feel like using datetime."""

from pyutil.decorators import enforce_param_hints
from time import localtime
from random import randint, seed


class Date:
    """Class with 3 int attributes: a year, a month, and a day."""

    @enforce_param_hints
    def __init__(self, year: int, month: int, day: int):
        if month > 12 or month < 1:
            raise ValueError("month must be in range 1-12.")
        last_day = 31
        if month == 2:
            if year % 4 == 0:
                last_day = 29
            else:
                last_day = 28
        elif month == (4 or 6 or 9 or 11):
            last_day = 30
        if day > last_day or day < 1:
            raise ValueError("current value of day is impossible.")

        self.__year = year
        self.__month = month
        self.__day = day

    def __str__(self):
        """a Date's default appearance in console is day/month/year.
        However, use .display() method to return a string in whatever order you'd like.
        """
        return f"{self.__day}/{self.__month}/{self.__year}"

    def __repr__(self):
        return f"Date(year={self.__year=}, month={self.__month}, day={self.__day})"

    def __eq__(self, other):
        if isinstance(other, Date):
            return self.__year == other.__year and self.__month == other.__month and self.__day == other.__day

    @property
    def year(self):
        """Returns the year attribute of date."""
        return self.__year

    @property
    def month(self):
        """Returns the month attribute of date."""
        return self.__month

    @property
    def day(self):
        """Returns the day attribute of date."""
        return self.__day

    @year.setter
    @enforce_param_hints
    def year(self, new_year: int):
        """Sets the year attribute of date."""
        self.__year = new_year

    @month.setter
    @enforce_param_hints
    def month(self, new_month: int):
        """Sets the month attribute of date."""
        if new_month > 12 or new_month < 1:
            raise ValueError("month must be in range 1-12.")
        self.__month = new_month

    @day.setter
    @enforce_param_hints
    def day(self, new_day: int):
        """Sets the day attribute of date."""
        last_day = 31
        if self.__month == 2:
            if self.__year % 4 == 0:
                last_day = 29
            else:
                last_day = 28
        elif self.__month == (4 or 6 or 9 or 11):
            last_day = 30

        if new_day > last_day or new_day < 1:
            raise ValueError("current value of day is impossible.")
        self.__day = new_day

    @staticmethod
    @enforce_param_hints
    def random(start: int = 1900, end: int = localtime()[0]):
        """Generates a random instance of Date within range start to end (defaults to 1900-current)"""
        seed()
        year = randint(start, end)
        month = randint(1, 12)
        if month == 2:
            if year % 4 == 0:
                last_day = 29
            else:
                last_day = 28
        elif month == (4 or 6 or 9 or 11):
            last_day = 30
        else:
            last_day = 31
        day = randint(1, last_day)
        return Date(year, month, day)

    @staticmethod
    def today():
        """Uses Date and time.localtime() to return today's date as an instance of Date"""
        return Date(localtime()[0], localtime()[1], localtime()[2])

    @staticmethod
    def yday():
        """Uses Date and time.localtime() to return yesterday's date as an instance of Date"""
        return Date(localtime()[0], localtime()[1], localtime()[2] - 1)

    @staticmethod
    def tmw():
        """Uses Date and time.localtime() to return tomorrow's date as an instance of Date"""
        return Date(localtime()[0], localtime()[1], localtime()[2] + 1)

    @enforce_param_hints
    def display(self, order: str = "dmy") -> str:
        """Returns str(self) in a customizable order using the order parameter.
        To use the order parameter, simply pass in a string with 3 chars: y, m, d.
        The order of these 3 chars will determine the return's order.
        (ex: Date(2001, 3, 9).display("mdy") -> "3/9/2001")
        """
        if len(order) != 3:
            raise RuntimeError(f'"{order}" must be 3 characters long exactly')
        abbr = {
            "y": str(self.__year),
            "m": str(self.__month),
            "d": str(self.__day),
        }
        return f"{abbr[order[0]]}/{abbr[order[1]]}/{abbr[order[2]]}"


def main():
    """For use in Debugging..."""
    pass


if __name__ == "__main__":
    main()
