# How to Run Python Programs on Raspberry Pi

- Raspberry Pi is a small, low-cost computer that can run various operating systems, including Linux and Windows.
- Python is a popular, high-level programming language that can be used for various applications, such as web development, data analysis, machine learning, and robotics.
- To run Python programs on Raspberry Pi, you need to install Python and an editor or IDE (Integrated Development Environment) on your Pi.
- There are different versions of Python, such as Python 2 and Python 3. Python 3 is the latest and recommended version, but some older programs may only work with Python 2.
- To check which version of Python is installed on your Pi, open a terminal window and type `python --version` or `python3 --version`.
- To install Python 3 on your Pi, type `sudo apt update` and `sudo apt install python3` in the terminal.
- To install an editor or IDE for Python, you can choose from various options, such as Thonny, IDLE, PyCharm, or Visual Studio Code. Thonny and IDLE are simple and easy to use, while PyCharm and Visual Studio Code are more advanced and feature-rich.
- To install Thonny, type `sudo apt install thonny` in the terminal.
- To install IDLE, type `sudo apt install idle3` in the terminal.
- To install PyCharm, follow the instructions on https://www.jetbrains.com/pycharm/download/#section=linux.
- To install Visual Studio Code, follow the instructions on https://code.visualstudio.com/docs/setup/linux.
- To run a Python program on your Pi, you can either write your code in the editor or IDE and run it from there, or save your code in a file with the `.py` extension and run it from the terminal.
- To run a Python program from the editor or IDE, open the program and write your code. Then, click on the Run button or press F5 to execute your code. You will see the output in the console or terminal window.
- To run a Python program from the terminal, open a terminal window and navigate to the directory where your file is saved. Then, type `python filename.py` or `python3 filename.py` to execute your code. You will see the output in the terminal window.
- Here are some examples of Python programs that you can run on your Pi:

## Hello World
- This is the simplest Python program that prints "Hello, World!" to the screen.
- To write this program, type the following code in your editor or IDE or save it in a file named `hello.py`:

```python
print("Hello, World!")
```

- To run this program, click on the Run button or press F5 in your editor or IDE, or type `python hello.py` or `python3 hello.py` in the terminal.

## Blink an LED
- This is a Python program that uses the GPIO (General Purpose Input/Output) pins on your Pi to blink an LED (Light Emitting Diode).
- To write this program, you need to connect an LED and a resistor to your Pi. Follow the diagram below to connect the LED to GPIO pin 17 and the resistor to the ground pin:

![LED diagram](https://projects-static.raspberrypi.org/projects/physical-computing/8a9d1f1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3a9a1a1a3