# 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input

- To run a python program on Pi, you need to have a Raspberry Pi device, a micro SD card with an operating system installed, a monitor, a keyboard, and a mouse. You also need to have Python installed on your Pi, which is usually the case with most operating systems.
- To write a python program, you can use any text editor of your choice, such as nano, vim, or IDLE. You can also use the Thonny IDE, which is a simple and beginner-friendly editor that comes with the Raspberry Pi OS.
- To save your python program, you need to give it a name with the .py extension, such as hello.py. You can save it in any directory of your Pi, such as the home directory or the Desktop.
- To run your python program, you need to open a terminal window and navigate to the directory where you saved your program. Then, you can use the python3 command followed by the name of your program, such as python3 hello.py. This will execute your program and display the output on the terminal.
- To print a name 'n' times, where name and n are read from standard input, you can use the following python program:

```python
# This program prints a name 'n' times, where name and n are read from standard input

# Ask the user to enter a name
name = input("Enter a name: ")

# Ask the user to enter a number
n = int(input("Enter a number: "))

# Use a for loop to print the name 'n' times
for i in range(n):
    print(name)
```

- To test your program, you can run it on the terminal and enter some values for name and n, such as Alice and 5. You should see the output as:

```text
Alice
Alice
Alice
Alice
Alice
```

- You can also modify your program to print the name in different ways, such as in uppercase, lowercase, or with a separator. You can use the string methods and the print function parameters to achieve this. For example, you can use the following program to print the name in uppercase with a dash as a separator:

```python
# This program prints a name 'n' times in uppercase with a dash as a separator, where name and n are read from standard input

# Ask the user to enter a name
name = input("Enter a name: ")

# Ask the user to enter a number
n = int(input("Enter a number: "))

# Use a for loop to print the name 'n' times in uppercase with a dash as a separator
for i in range(n):
    print(name.upper(), end="-")
```

- To test your program, you can run it on the terminal and enter some values for name and n, such as Bob and 3. You should see the output as:

```text
BOB-BOB-BOB-
```