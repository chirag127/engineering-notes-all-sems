# 4. a) Light an LED through Python program

- To light an LED through Python program, you need the following components:
  - A Raspberry Pi board with GPIO pins
  - An LED
  - A resistor (220 ohms or similar)
  - Breadboard and jumper wires
- The basic steps are as follows:
  - Connect the LED to the GPIO pin 18 (or any other pin you choose) and the ground pin of the Raspberry Pi using the resistor and the breadboard. The resistor is used to limit the current and protect the LED from burning out.
  - Install the RPi.GPIO library on your Raspberry Pi. This library allows you to control the GPIO pins using Python code.
  - Write a Python program that imports the RPi.GPIO library, sets the GPIO pin 18 as output, and turns it on and off with a delay of one second. You can use the GPIO.output() function to set the pin to high (3.3V) or low (0V) voltage. You can use the time.sleep() function to pause the program for a given number of seconds.
  - Save the Python program as led.py and run it using the command `python led.py` in the terminal. You should see the LED blinking on and off every second.
- A possible Python program for this task is:

```python
# Import the RPi.GPIO library
import RPi.GPIO as GPIO
# Import the time library
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Set the GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT)

# Loop forever
while True:
  # Turn the LED on
  GPIO.output(18, GPIO.HIGH)
  # Wait for one second
  time.sleep(1)
  # Turn the LED off
  GPIO.output(18, GPIO.LOW)
  # Wait for one second
  time.sleep(1)
```