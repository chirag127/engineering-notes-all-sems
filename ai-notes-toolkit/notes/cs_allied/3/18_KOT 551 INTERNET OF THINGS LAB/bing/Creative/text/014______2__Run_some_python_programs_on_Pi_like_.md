#### 2. Run some python programs on Pi like:

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- You also need to have a text editor or an IDE (Integrated Development Environment) to write and edit your python code. You can use the default text editor on Pi, which is called `nano`, or you can install other editors like `Thonny` or `Mu`. To install Thonny, type `sudo apt install thonny`. To install Mu, type `pip3 install mu-editor`.
- To write a python program, you need to create a file with the `.py` extension, such as `hello.py`. You can use any text editor to create and save the file in a directory of your choice. To run the program, you need to navigate to the directory where the file is located, and type `python3 hello.py` in the terminal. This will execute the code in the file and display the output on the screen.
- A simple python program that prints "Hello, world!" on the screen is:

```python
# This is a comment. It starts with a # symbol and is ignored by the interpreter.
# Comments are useful to explain your code or add notes.

# The print() function is used to display text or values on the screen.
# The text or values are enclosed in parentheses and quotation marks.
# You can use single or double quotation marks, but they should match.
print("Hello, world!")
```

- To run this program, save it as `hello.py` and type `python3 hello.py` in the terminal. You should see `Hello, world!` on the screen.
- You can write more complex python programs that use variables, data types, operators, expressions, statements, functions, modules, libraries, etc. You can also use python to interact with the hardware and sensors on your Pi, such as the GPIO pins, the camera, the LED, the button, etc. You can find more examples and tutorials on the official python website (https://www.python.org/) or the Raspberry Pi website (https://www.raspberrypi.org/).