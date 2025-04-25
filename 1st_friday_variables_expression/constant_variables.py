"""
    Constants are variables whose values are not meant to be changed after they are defined. 
    Python does not have built-in constant support, but developers follow naming conventions and best practices to simulate constants.

    Best Practices for Constants : 
        ✔ Use UPPER_SNAKE_CASE for naming.
        ✔ Place constants in a separate file (e.g., constants.py) if reused across modules.
        ✔ Use typing.Final for better code clarity and static checks.
        ✔ Document constants with comments.
"""


"""
    Naming Conventions | Constants are typically defined in UPPER_SNAKE_CASE.
    Example: MAX_VALUE = 100
"""
MAX_VALUE = 100
PI = 3.14159
GRAVITY = 9.81
SPEED_OF_LIGHT = 299792458
DAYS_IN_WEEK = 7
MONTHS_IN_YEAR = 12
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
CIRCUMFERENCE = 2 * PI * 10  # Example of using a constant in a calculation
# Constants are not enforced in Python, but it's a good practice to treat them as immutable.

"""
    Immutable Constant using Tuple
"""
CONSTANTS = (3.14159, 100, 30)
PHI = CONSTANTS[0]  # Accessible but cannot modify CONSTANTS