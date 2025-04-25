from constant_variables import SPEED_OF_LIGHT, MAX_VALUE, DAYS_IN_WEEK, MONTHS_IN_YEAR
from typing import Final

print("Max Value:", MAX_VALUE)
print("SPEED_OF_LIGHT:", SPEED_OF_LIGHT)
print("MONTHS_IN_YEAR:", MONTHS_IN_YEAR)
print("DAYS_IN_WEEK:", DAYS_IN_WEEK)


"""
    Immutable Constant using Final
"""
PI: Final[float] = 3.14159
GRAVITY: Final[float] = 9.81
WEEKDAYS: Final[list] = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("PI:", PI)
print("GRAVITY:", GRAVITY)
print("WEEKDAYS:", WEEKDAYS)