# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on the Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on the Pi, you need to have python installed on your system. You can check if you have python by typing `python --version` in the terminal. If you see a version number, such as `Python 3.7.3`, then you have python installed. If not, you can install it by typing `sudo apt install python3` in the terminal.
- To write a python program, you can use any text editor, such as nano, vim, or IDLE. To open a text editor, you can type its name in the terminal, such as `nano hello.py`. This will create a new file called `hello.py` and open it in nano. You can then type your python code in the editor and save it by pressing `Ctrl+O` and then `Enter`. To exit the editor, press `Ctrl+X`.
- To run a python program, you can type `python3 hello.py` in the terminal, where `hello.py` is the name of your file. This will execute your python code and display the output in the terminal. For example, if your `hello.py` file contains the following code:

```python
print("Hello, world!")
```

Then running it will display:

```bash
Hello, world!
```

- You can also run python programs interactively, by typing `python3` in the terminal. This will open a python shell, where you can type python commands and see the results immediately. For example, you can type:

```python
>>> 2 + 3
5
>>> print("Hello, Pi!")
Hello, Pi!
```

To exit the python shell, press `Ctrl+D` or type `exit()`.
- Some examples of python programs that you can run on the Pi are:

  - A simple calculator that can perform basic arithmetic operations, such as addition, subtraction, multiplication, and division. You can use the `input()` function to get the user's input and the `eval()` function to evaluate the expression. For example:

```python
# A simple calculator
print("Welcome to the simple calculator!")
print("Enter an expression, such as 2 + 3, or q to quit.")
while True:
    expression = input("> ")
    if expression == "q":
        break
    else:
        try:
            result = eval(expression)
            print(result)
        except:
            print("Invalid expression.")
print("Goodbye!")
```

  - A dice simulator that can generate random numbers between 1 and 6, simulating the roll of a dice. You can use the `random` module to generate random numbers and the `time` module to add some delay. For example:

```python
# A dice simulator
import random
import time
print("Welcome to the dice simulator!")
print("Press enter to roll the dice, or q to quit.")
while True:
    choice = input("> ")
    if choice == "q":
        break
    else:
        print("Rolling the dice...")
        time.sleep(1)
        dice = random.randint(1, 6)
        print("You got", dice)
print("Goodbye!")
```

  - A temperature converter that can convert between Celsius and Fahrenheit degrees. You can use the `input()` function to get the user's input and the `float()` function to convert it to a number. You can also use the `format()` function to format the output. For example:

```python
# A temperature converter
print("Welcome to the temperature converter!")
print("Enter a temperature in Celsius or Fahrenheit, such as 25C or 77F, or q to quit.")
while True:
    temperature = input("> ")
    if temperature == "q":
        break
    else:
        try:
            if temperature.endswith("C"):
                celsius = float(temperature[:-1])
                fahrenheit = celsius * 9 / 5 + 32
                print("{}C = {}F".format(celsius, fahrenheit))
            elif temperature.endswith("F"):
                fahrenheit = float(temperature[:-1])
                celsius = (fahrenheit - 32) * 5 / 9
                print("{}F = {}C".format(fahrenheit, celsius))
            else:
                print("Invalid temperature.")
        except:
            print("Invalid temperature.")
print("Goodbye!")
```