"""
Practical Use Classes
"""
from pyutil.decorators import method_expects

class Date:
    """Class with 3 int attributes: a year, a month, and a day."""

    @method_expects(int, int, int)
    def __init__(self, year, month, day):
        if month > 12 or month < 1:
            raise ValueError("month must be in range 1-12")
        if month == 2:
            if year % 4 == 0:
                last_day = 29
            else:
                last_day = 28
        elif month == (4 or 6 or 9 or 11):
            last_day = 30
        else:
            last_day = 31
        if day > last_day or day < 1:
            raise ValueError("current value of day is impossible")

        self._year = year
        self._month = month
        self._day = day
    
    def __str__(self):
        """a Date's default appearance in console is day/month/year.
        However, use .display() method to return a string in whatever order you'd like."""
        return str(self._day) + "/" + str(self._month) + "/" + str(self._year)

    def __repr__(self):
        return f"(year={str(self._year)} month={str(self._month)} day={str(self._day)})"

    def __eq__(self, other):
        if isinstance(other, Date):
            return self._year == other._year and self._month == other._month and self._day == other._day

    @property
    def year(self):
        """Returns the year attribute of date."""
        return self._year

    @property
    def month(self):
        """Returns the month attribute of date."""
        return self._month

    @property
    def day(self):
        """Returns the day attribute of date."""
        return self._day

    @method_expects(int)
    @year.setter
    def year(self, new_year):
        """Sets the year attribute of date."""
        self._year = new_year

    @method_expects(int)
    @month.setter
    def month(self, new_month):
        """Sets the month attribute of date."""
        self._month = new_month

    @method_expects(int)
    @day.setter
    def day(self, new_day):
        """Sets the day attribute of date."""
        self._day = new_day

    @method_expects(int, int)
    @classmethod
    def random(cls, start=1900, end=2020):
        """Generates a random instance of Date within range start to end (defaults to 1900-2020)"""
        from random import randint, seed
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
        return cls(year, month, day)

    @classmethod
    def today(cls):
        """Uses Date and time.localtime() to return today's date as an instance of Date"""
        from time import localtime
        return cls(localtime()[0], localtime()[1], localtime()[2])

    @classmethod
    def yday(cls):
        """Uses Date and time.localtime() to return yesterday's date as an instance of Date"""
        from time import localtime
        return cls(localtime()[0], localtime()[1], localtime()[2] - 1)

    @classmethod
    def tmw(cls):
        """Uses Date and time.localtime() to return tomorrow's date as an instance of Date"""
        from time import localtime
        return cls(localtime()[0], localtime()[1], localtime()[2] + 1)

    def display(self, order="dmy") -> str:
        """
        Returns str(self) in a customizable order using the order parameter.
        To use the order parameter, simply pass in a string with 3 chars: y, m, d.
        The order of these 3 chars will determine the return's order.
        (ex: Date(2001, 3, 9).display("mdy") -> "3/9/2001")
        """
        if len(order) != 3:
            raise RuntimeError('"' + order + '" must be 3 characters long exactly')
        abbr = {"y": str(self._year), "m": str(self._month), "d": str(self._day)}
        return abbr[order[0]] + "/" + abbr[order[1]] + "/" + abbr[order[2]]\

'''
    def age_get(self) -> int:
        """will return an int of how old someone born on self is at the time of calling age_get."""
        from time import localtime
        crnt_year, crnt_month, crnt_day = localtime()[0], localtime()[1], localtime()[2]

        years_passed = (crnt_year - 1) - self._year
        if crnt_month < self._month:
            return years_passed
        if crnt_month > self._month:
            return years_passed + 1
        if crnt_month == self._month:
            if crnt_day >= self._day:
                return years_passed + 1
            else:
                return years_passed
'''
