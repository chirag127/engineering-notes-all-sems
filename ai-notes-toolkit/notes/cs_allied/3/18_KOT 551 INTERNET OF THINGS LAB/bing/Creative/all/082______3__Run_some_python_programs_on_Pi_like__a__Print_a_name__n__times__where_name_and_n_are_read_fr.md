#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input.

- To run a python program on Pi, you need to have a Raspberry Pi device, a micro SD card with an operating system installed, a monitor, a keyboard, a mouse, and a power supply.
- Connect the Pi to the monitor, keyboard, mouse, and power supply, and boot it up. You should see a desktop environment or a command line interface, depending on the operating system you have chosen.
- Open a terminal window and type `python3` to enter the interactive python shell. Alternatively, you can use a text editor or an IDE to write and save your python code in a file with a `.py` extension, and then run it with the command `python3 filename.py`.
- To print a name 'n' times, where name and n are read from standard input, you can use the following python code:

```python
# Read the name and n from the standard input
name = input("Enter a name: ")
n = int(input("Enter a number: "))

# Print the name n times using a for loop
for i in range(n):
    print(name)
```

- The `input()` function reads a string from the standard input and returns it. The `int()` function converts a string to an integer. The `range()` function generates a sequence of numbers from 0 to n-1. The `print()` function prints a value to the standard output, followed by a newline.
- You can test the program by entering different values for name and n, and see the output on the terminal. For example, if you enter `Alice` and `5`, you should see:

```
Alice
Alice
Alice
Alice
Alice
```