"""
    a variable is a name that refers to a value stored in memory. Variables allow us to store and manipulate data in our programs.

    Best Practices:
    ✔ Use meaningful names (e.g., user_age instead of x).
    ✔ Follow snake_case naming convention (e.g., user_name).
    ✔ Avoid using Python keywords (e.g., list, str, def).
"""

# KEY CONCEPTS
# 1. Variables are created by assigning a value to a name using the assignment operator (=).
# 2. Variable names must start with a letter or underscore and can contain letters, numbers, and underscores.
# 3. Variable names are case-sensitive, meaning that "myVariable" and "myvariable" are considered different variables.
# 4. Variables can be reassigned to new values at any time.
# 5. Python has dynamic typing, meaning that the type of a variable is determined at runtime based on the value assigned to it.
# 6. Common data types in Python include integers, floats, strings, and booleans.
# 7. Variables can be used in expressions to perform calculations or manipulate data.
# 8. Python supports multiple assignment, allowing you to assign the same value to multiple variables in a single line.
# 9. Python also supports unpacking, allowing you to assign values from a list or tuple to multiple variables in a single line.
# 10. Variables can be deleted using the del statement, which removes the variable from memory.
# 11. Python has built-in functions like type() to check the type of a variable and id() to get the memory address of a variable.
# 12. Python has built-in functions like str(), int(), and float() to convert between different data types.
# 13. Python has built-in functions like len() to get the length of a string or list, and range() to generate a sequence of numbers.
# 14. Python has built-in functions like min() and max() to find the minimum and maximum values in a list or tuple.
# 15. Python has built-in functions like sum() to calculate the sum of a list or tuple, and sorted() to sort a list or tuple.
# 16. Python has built-in functions like all() and any() to check if all or any elements in a list or tuple are true.
# 17. Python has built-in functions like map() and filter() to apply a function to each element in a list or tuple.
# 18. Python has built-in functions like zip() to combine two or more lists or tuples into a single list of tuples.
# 19. Python has built-in functions like enumerate() to get the index and value of each element in a list or tuple.
# 20. Python has built-in functions like reversed() to reverse a list or tuple, and round() to round a number to a specified number of decimal places.
# 21. Python has built-in functions like abs() to get the absolute value of a number, and pow() to raise a number to a power.
# 22. Python has built-in functions like chr() and ord() to convert between characters and their ASCII values.
# 23. Python has built-in functions like bin(), oct(), and hex() to convert between decimal, binary, octal, and hexadecimal representations of numbers.
# 24. Python has built-in functions like input() to get user input, and print() to display output.
# 25. Python has built-in functions like format() to format strings, and f-strings to create formatted strings using curly braces.
# 26. Python has built-in functions like isinstance() to check if a variable is of a certain type, and isinstance() to check if a variable is a subclass of a certain class.
# 27. Python has built-in functions like dir() to get a list of attributes and methods of an object, and help() to get documentation for an object.
# 28. Python has built-in functions like eval() to evaluate a string as a Python expression, and exec() to execute a string as a Python statement.
# 29. Python has built-in functions like globals() and locals() to get a dictionary of global and local variables, respectively.
# 30. Python has built-in functions like __name__ to get the name of the current module, and __file__ to get the path of the current module.
# 31. Python has built-in functions like __init__() to initialize a class, and __str__() to return a string representation of an object.
# 32. Python has built-in functions like __repr__() to return a string representation of an object that can be used to recreate the object, and __len__() to return the length of an object.
# 33. Python has built-in functions like __getitem__() to get an item from an object using indexing, and __setitem__() to set an item in an object using indexing.
# 34. Python has built-in functions like __iter__() to return an iterator for an object, and __next__() to get the next item from an iterator.
# 35. Python has built-in functions like __call__() to make an object callable like a function, and __str__() to return a string representation of an object.
# 36. Python has built-in functions like __add__() to add two objects, and __sub__() to subtract two objects.
# 37. Python has built-in functions like __mul__() to multiply two objects, and __truediv__() to divide two objects.
# 38. Python has built-in functions like __floordiv__() to perform floor division, and __mod__() to get the remainder of a division.
# 39. Python has built-in functions like __pow__() to raise a number to a power, and __and__() to perform a bitwise AND operation.
# 40. Python has built-in functions like __or__() to perform a bitwise OR operation, and __xor__() to perform a bitwise XOR operation.
# 41. Python has built-in functions like __invert__() to perform a bitwise NOT operation, and __lt__() to compare two objects for less than.
# 42. Python has built-in functions like __le__() to compare two objects for less than or equal to, and __eq__() to compare two objects for equality.
# 43. Python has built-in functions like __ne__() to compare two objects for not equal to, and __gt__() to compare two objects for greater than.
# 44. Python has built-in functions like __ge__() to compare two objects for greater than or equal to, and __contains__() to check if an object contains a value.
# 45. Python has built-in functions like __iter__() to return an iterator for an object, and __next__() to get the next item from an iterator.
# 46. Python has built-in functions like __reversed__() to reverse an object, and __len__() to get the length of an object.
# 47. Python has built-in functions like __getitem__() to get an item from an object using indexing, and __setitem__() to set an item in an object using indexing.
# 48. Python has built-in functions like __delitem__() to delete an item from an object using indexing, and __contains__() to check if an object contains a value.


"""
Variable Naming Rules
------------------------
    - Must start with a letter (a-z, A-Z) or underscore _.
    - Can contain letters, numbers (0-9), and underscores.
    - Cannot be a Python keyword (e.g., if, for, while).
    - Case-sensitive (age ≠ Age).
"""
age = 25        # Valid
_count = 0      # Valid
2name = "John"  # Invalid (starts with a number)


"""
    Dynamic Typing | A variable's type can change during exectution.

    Variable Types
    - int (Integer) → x = 10
    - float (Floating-point) → y = 3.14
    - str (String) → name = "Python"
    - bool (Boolean) → is_valid = True
    - list, tuple, dict, set, etc.
"""
x = 10          # Integer
x = "Hello"      # String
x = 3.14         # Float
x = [1, 2, 3]   # List
x = (1, 2, 3)   # Tuple
x = {1, 2, 3}   # Set
x = {'a': 1, 'b': 2} # Dictionary


"""
Variable Scope
    - Local Variable: Defined inside a function (accessible only within it).
    - Global Variable: Defined outside functions (accessible everywhere).
"""
global_var = "I'm global"

def my_func():
    local_var = "I'm local"
    print(global_var)  # Accessible

print(global_var)      # Works
print(local_var)       # Error (not defined outside)


"""
    No Explicit Declaration Needed | Python variables do not require explicit type declaration.
"""
x = 10          # Integer
name = "Alice"  # String
is_valid = True # Boolean


"""
    Multiple Assignment | Assigning multiple variables in a single line.
"""
a, b, c = 1, 2, 3       # Assigns a=1, b=2, c=3
x = y = z = 0           # All variables get the value 0


"""
    Unpacking | Assigning values from a list or tuple to multiple variables.
"""
a, b, c = [1, 2, 3]


"""
    Deleting Variables | Removing a variable from memory.
"""
del x


"""
    Checking Variable Type | Using type() to check the type of a variable.
"""
print(type(x))  # Output: <class 'int'>


"""
    Getting Memory Address | Using id() to get the memory address of a variable.
"""
print(id(x))    # Output: Memory address of x


"""
    Converting Data Types | Using str(), int(), and float() to convert between types.
"""
x = 10
y = str(x)  # Convert integer to string
y = int(y)  # Convert string back to integer
y = float(x)  # Convert integer to float


"""
    Getting Length of a String or List | Using len() to get the length of a string or list.
"""
my_list = [1, 2, 3]
my_string = "Hello"
print(len(my_list))  # Output: 3
print(len(my_string))  # Output: 5