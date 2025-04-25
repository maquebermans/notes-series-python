"""
    Expression is a combination of values, variables, operators, and function calls that evaluates to a single value. 
    Expressions can be as simple as a single variable or as complex as a combination of operations.

    How Python Evaluates Expressions
    Python follows operator precedence (similar to math rules):
        - Parentheses () (highest priority)
        - Exponents **
        - Multiplication *, Division /, Floor Division //, Modulus %
        - Addition +, Subtraction -
        - Comparison (<, >, ==, etc.)
        - Logical not, and, or
        - Bitwise operators (&, |, ^, ~)
        - Identity operators (is, is not)
        - Membership operators (in, not in)
        - Assignment operators (=, +=, -=, etc.)
        - Conditional expressions (ternary operator)
        - Lambda expressions (anonymous functions)
    
    Example of operator precedence:
        - result = (5 + 3) * 2 ** 2  # (8) * (4) → 32
        - total = (10 + 5) * 2  # 30
        - if (age >= 18) and (has_id):
            print("Allowed")
        - print("Sum:", (x + y))
"""


"""
    Arithmetic Expressions | Using operators to perform arithmetic operations.
"""
x = 10
y = 5
result = x + y  # Addition --> 15
result = x - y  # Subtraction --> 5
result = x * y  # Multiplication --> 50
result = x / y  # Division --> 2.0
result = x % y  # Modulus --> 0
result = x ** y # Exponentiation --> 100000
result = x // y # Floor Division --> 2


"""
    Comparison Expressions | Using comparison operators to compare values.
"""
x = 10
y = 5
result = x == y  # Equal to --> False
result = x != y  # Not equal to --> True
result = x > y   # Greater than --> True
result = x < y   # Less than --> False
result = x >= y  # Greater than or equal to --> False
result = x <= y  # Less than or equal to --> False


"""
     Logical Expressions | Using logical operators to combine boolean values.
"""
x = True
y = False
result = x and y  # Logical AND --> True if both x and y are True
result = x or y   # Logical OR --> True if either x or y is True
result = not x    # Logical NOT --> False if x is True


"""
     Bitwise Expressions | Using bitwise operators to perform operations on bits.
"""
x = 10  # 1010 in binary
y = 5   # 0101 in binary
result = x & y  # Bitwise AND --> 0
result = x | y  # Bitwise OR --> 15
result = x ^ y  # Bitwise XOR --> 15
result = ~x     # Bitwise NOT --> -11
result = x << 1  # Left shift --> 20
result = x >> 1  # Right shift --> 5


"""
     Identity Expressions | Using identity operators to check if two variables point to the same object.
"""
x = [1, 2, 3]
y = x
result = x is y  # True if x and y point to the same object
result = x is not y  # True if x and y do not point to the same object


"""
     Membership Expressions | Using membership operators to check if a value is in a sequence.
"""
x = [1, 2, 3]
y = 2
result = y in x  # True if y is in x
result = y not in x  # True if y is not in x


"""
    String Expressions | Using string methods to manipulate strings.
"""
x = "Hello"
y = "World"
result = x + " " + y  # Concatenation --> "Hello World"
result = x * 3  # Repetition --> "HelloHelloHello"
result = x.lower()  # Converts to lowercase --> "hello"
result = x.upper()  # Converts to uppercase --> "HELLO"


"""
     Conditional Expressions | Using conditional expressions (ternary operator) to evaluate conditions.
     (a one line if statement)
     Syntax: value_if_true if condition else value_if_false
"""
x = 10
y = 5
result = x if x > y else y  # Returns x if x > y, otherwise returns y


"""
     Lambda Expressions | Using lambda functions to create anonymous functions.
"""
square = lambda x: x ** 2
result = square(5)  # Calls the lambda function --> 25
