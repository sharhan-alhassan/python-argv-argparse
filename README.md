
### This short tutorial is in two parts. Part 1 is about "sys.argv" and Part 2 about Python's module "argparse"

# Part 1: How to use "sys.argv"
A simple documentation to simplify how to use `sys.argv` to collect arguments passed on the command line


# Some notes to understand about "sys.argv"

- `sys.argv()` is an array for command line arguments in Python
- The first element of the array `sys.argv()` is the name of the program itself (the current file). 
- As you write more command line arguments, they are appended to the array as strings 
- The `sys` module provides functions and variables used to manipulate different parts of the Python runtime environment.


# Sample code in sys_argv.py file
- This sample code first prints out the program itself stored in the `sys.argv[0]`
- `sys.argv` prints out all the loaded arguments inputed from the command
- Code available in `sys_argv.py` file is 
```python
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
```
- Test for yourself with:
```bash
$ python3 sys_argv.py 2 1 3
```
- Output
```bash
This is the name of the program: sys_argv.py
Argument list: ['sys_argv.py', '2', '1', '3']
Sum of ['2', '1', '3'] is: 6.0

```
- The `arg_add()` function takes all the command line arguments (with the exception of the first item in the array(the program itself)) and add them 


# How to run the code
```bash
$ python3 sys_arg.py 
```


# Part 2: Python's module "argparse"
- Find in the following files, an intuitive and straightforward way of using `argparse` to load and use arguments from command line. 
```bash
find_avearage.py
sort_integers.py
sum_numbers.py
```
- A great way start to start building CLI utility tools