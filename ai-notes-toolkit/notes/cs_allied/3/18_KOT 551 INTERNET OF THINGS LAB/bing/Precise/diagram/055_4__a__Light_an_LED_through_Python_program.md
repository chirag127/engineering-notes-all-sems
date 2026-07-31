# 4. a) Light an LED through Python program

To light an LED through a Python program, the following steps can be followed:

1. **Connect the LED**: Connect the LED to the appropriate GPIO pin on the Raspberry Pi or other microcontroller. Make sure to use a resistor to limit the current to the LED.

2. **Install necessary libraries**: Install the necessary libraries for controlling the GPIO pins, such as the RPi.GPIO library for the Raspberry Pi.

3. **Import the libraries**: In the Python program, import the necessary libraries, such as `import RPi.GPIO as GPIO`.

4. **Set up the GPIO pin**: Set up the GPIO pin for output using the `GPIO.setup()` function, for example `GPIO.setup(18, GPIO.OUT)`.

5. **Turn on the LED**: To turn on the LED, use the `GPIO.output()` function to set the GPIO pin to high, for example `GPIO.output(18, GPIO.HIGH)`.

6. **Turn off the LED**: To turn off the LED, use the `GPIO.output()` function to set the GPIO pin to low, for example `GPIO.output(18, GPIO.LOW)`.

Here is an example Python program that turns on an LED connected to GPIO pin 18 for 5 seconds and then turns it off:

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)
time.sleep(5)
GPIO.output(18, GPIO.LOW)

GPIO.cleanup()
```