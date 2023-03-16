# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on the Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on the Pi, you need to have a text editor to write your code, and a terminal to execute it.
- There are different ways to run a python program on the Pi, depending on how you want to interact with your code and the output.
- Here are some examples of python programs that you can run on the Pi:

## 2.1. Hello World
- This is the simplest python program that prints "Hello World" to the terminal.
- To run this program, you need to create a file named hello.py with the following code:

```python
# This is a comment
print("Hello World")
```

- Then, you need to open a terminal and navigate to the directory where you saved the file, using the cd command.
- To execute the program, you need to type python3 hello.py and press enter.
- You should see the output "Hello World" on the terminal.

## 2.2. Blink an LED
- This is a python program that uses the GPIO pins of the Pi to control an LED.
- To run this program, you need to have an LED, a resistor, some jumper wires, and a breadboard.
- You need to connect the LED to the GPIO pin 17 of the Pi, and the resistor to the ground pin, as shown in the diagram below:

![LED circuit](https://projects-static.raspberrypi.org/projects/physical-computing/8a2f1a9f1a50a0f28e1a1d07030d8fde8a108d4d/en/images/led-circuit.png)

- Then, you need to create a file named blink.py with the following code:

```python
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
    GPIO.output(17, True)
    # Wait for one second
    time.sleep(1)
    # Turn off the LED
    GPIO.output(17, False)
    # Wait for one second
    time.sleep(1)
```

- Then, you need to open a terminal and navigate to the directory where you saved the file, using the cd command.
- To execute the program, you need to type sudo python3 blink.py and press enter.
- You should see the LED blinking on and off every second.

## 2.3. Sense HAT
- This is a python program that uses the Sense HAT, an add-on board for the Pi that has various sensors and an LED matrix.
- To run this program, you need to have a Sense HAT attached to the Pi, as shown in the picture below:

![Sense HAT](https://projects-static.raspberrypi.org/projects/getting-started-with-the-sense-hat/8c9d0c844d594a2f82bfa8f076d5e743c7b7666a/en/images/sense-hat-attached.jpg)

- Then, you need to create a file named sense.py with the following code:

```python
# Import the Sense HAT library
from sense_hat import SenseHat
# Create a Sense HAT object
sense = SenseHat()

# Set the rotation of the display
sense.set_rotation(180)
# Clear the display
sense.clear()
# Show a message on the display
sense.show_message("Hello Pi")
# Get the temperature from the sensor
temp = sense.get_temperature()
# Print the temperature to the terminal
print("Temperature: {:.1f} C".format(temp))
```

- Then, you need to open a terminal and navigate to the directory where you saved the file, using the cd command.
- To execute the program, you need to type python3 sense.py and press enter.
- You should see the message "Hello Pi" scrolling on the LED matrix, and the temperature printed on the terminal.