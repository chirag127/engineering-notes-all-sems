# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on the Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on the Pi, you need to have a python interpreter installed on the Pi. The Pi comes with two versions of python: python 2 and python 3. You can check which version you have by typing `python --version` or `python3 --version` in the terminal.
- To write a python program, you can use any text editor, such as nano, vim, or IDLE. IDLE is an integrated development environment (IDE) for python that provides syntax highlighting, debugging, and other features. You can launch IDLE by typing `idle` or `idle3` in the terminal, depending on the python version you want to use.
- To save a python program, you need to give it a name with the `.py` extension, such as `hello.py`. You can save the program in any directory, but it is recommended to create a separate folder for your python projects, such as `~/python_projects`.
- To run a python program, you need to navigate to the directory where you saved the program, and then type `python hello.py` or `python3 hello.py` in the terminal, depending on the python version you used to write the program. You can also run the program from IDLE by pressing F5 or clicking on Run -> Run Module.
- A simple python program that prints "Hello, world!" to the screen is:

```python
# This is a comment. Comments start with a # symbol and are ignored by the interpreter.
# The first line of a python program is usually a shebang line that tells the operating system which interpreter to use.
# The shebang line is optional, but it is good practice to include it.
# The shebang line for python 2 is #!/usr/bin/env python
# The shebang line for python 3 is #!/usr/bin/env python3

# The print function is used to display output to the screen.
# In python 2, print is a statement and does not need parentheses.
# In python 3, print is a function and needs parentheses.
# To make the program compatible with both versions, you can use parentheses for print.

print("Hello, world!")
```

- Some examples of python programs that you can run on the Pi are:

  - A program that blinks an LED connected to the Pi's GPIO pin 17:

  ```python
  #!/usr/bin/env python3

  # Import the GPIO library
  import RPi.GPIO as GPIO
  # Import the time library
  import time

  # Set the GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)
  # Set the GPIO pin 17 as output
  GPIO.setup(17, GPIO.OUT)

  # Create a loop that runs forever
  while True:
    # Turn on the LED
    GPIO.output(17, GPIO.HIGH)
    # Wait for one second
    time.sleep(1)
    # Turn off the LED
    GPIO.output(17, GPIO.LOW)
    # Wait for one second
    time.sleep(1)
  ```

  - A program that displays the current date and time on the Pi's Sense HAT LED matrix:

  ```python
  #!/usr/bin/env python3

  # Import the Sense HAT library
  from sense_hat import SenseHat
  # Import the datetime library
  from datetime import datetime

  # Create a Sense HAT object
  sense = SenseHat()

  # Create a loop that runs forever
  while True:
    # Get the current date and time
    now = datetime.now()
    # Format the date and time as a string
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    # Display the date and time on the LED matrix
    sense.show_message(date_time)
  ```

  - A program that plays a random sound from a list of sound files stored in a folder:

  ```python
  #!/usr/bin/env python3

  # Import the pygame library
  import pygame
  # Import the random library
  import random
  # Import the os library
  import os

  # Initialize the pygame mixer
  pygame.mixer.init()
  # Create a list of sound files in the sounds folder
  sounds = os.listdir("sounds")
  # Remove any files that are not .wav or .mp3
  sounds = [s for s in sounds if s.endswith(".wav") or s.endswith(".mp3")]

```
