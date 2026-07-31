#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your device. Python is a high-level, interpreted, and general-purpose programming language that can run on various platforms, including Pi.
- You can check if you have python installed by typing `python --version` or `python3 --version` in the terminal. If you see a version number, such as `Python 3.9.2`, then you have python installed. If not, you need to install it using the command `sudo apt install python3`.
- To write a python program, you can use any text editor, such as nano, vim, or IDLE. You can also use an integrated development environment (IDE), such as Thonny, which is a simple and beginner-friendly IDE for python that comes pre-installed on Pi.
- To create a new python file, you can use the command `nano hello.py` in the terminal, where `hello.py` is the name of your file. You can replace `nano` with any other text editor you prefer. This will open a blank file where you can write your python code.
- A simple python program that prints "Hello, world!" to the screen is:

```python
# This is a comment. Comments start with a # symbol and are ignored by the interpreter.
# They are used to explain or document your code.

# The print() function is used to display output to the screen.
# It takes one or more arguments, which are the values or expressions to be printed.
# The arguments are enclosed in parentheses and separated by commas.
# Strings are sequences of characters enclosed in single or double quotes.

print("Hello, world!") # This will print Hello, world! to the screen.
```

- To save your file, press `Ctrl+O` and then press `Enter`. To exit the editor, press `Ctrl+X`.
- To run your python file, you can use the command `python3 hello.py` in the terminal, where `hello.py` is the name of your file. You can replace `python3` with `python` if you are using python 2. This will execute your code and display the output to the screen. You should see something like:

```bash
pi@raspberrypi:~ $ python3 hello.py
Hello, world!
pi@raspberrypi:~ $
```

- Congratulations! You have successfully run your first python program on Pi. You can modify your code and run it again to see the changes. You can also create more complex and interesting programs using python's built-in features and libraries.