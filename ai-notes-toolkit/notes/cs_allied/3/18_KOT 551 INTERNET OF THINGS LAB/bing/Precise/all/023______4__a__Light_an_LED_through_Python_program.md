#### 4. a) Light an LED through Python program

To light an LED through a Python program, you will need the following components:
1. A Raspberry Pi or similar single-board computer
2. An LED
3. A resistor
4. Jumper wires
5. A breadboard

Here are the steps to light an LED through a Python program:

1. Connect the LED to the Raspberry Pi using the breadboard and jumper wires. The longer leg of the LED should be connected to a GPIO pin on the Raspberry Pi through a resistor, while the shorter leg should be connected to a ground pin.

2. Install the necessary libraries on the Raspberry Pi. This can be done by running the command `sudo apt-get install python-rpi.gpio python3-rpi.gpio` in the terminal.

3. Write a Python program to control the LED. Here is an example program that will turn the LED on for 5 seconds and then turn it off:

```python
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the pin number for the LED
LED_PIN = 18

# Set the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn the LED on
GPIO.output(LED_PIN, GPIO.HIGH)

# Wait for 5 seconds
time.sleep(5)

# Turn the LED off
GPIO.output(LED_PIN, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()
```

4. Run the Python program on the Raspberry Pi. The LED should turn on for 5 seconds and then turn off.

This is a basic example of how to light an LED through a Python program. You can modify the program to control the LED in different ways, such as blinking or changing its brightness.