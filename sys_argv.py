"""
- sys.argv() is an array for command line arguments in Python
- The first element of the array sys.argv() is the name of the program itself (the current file). 
- As you write more command line arguments, they are appended to the array as strings 
- The sys module provides functions and variables used to manipulate different parts of the Python runtime environment.
"""

import sys

print(f"This is the name of the program: {sys.argv[0]}")
print(f"Argument list: {str(sys.argv)}")


def arg_add():
    import sys

    add = 0.0
    n = len(sys.argv)
    for i in range(1, n):
        add += float(sys.argv[i])
    print(f"Sum of {sys.argv[1:]} is: {add}")

arg_add()