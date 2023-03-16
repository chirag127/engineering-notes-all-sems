#### 4. a) Light an LED through Python program

Lighting an LED through a Python program involves the following steps:

1. **Connect the LED to the Raspberry Pi**: Connect the positive leg of the LED to a GPIO pin on the Raspberry Pi and the negative leg to a ground pin.

2. **Install the necessary libraries**: Install the RPi.GPIO library to control the GPIO pins on the Raspberry Pi.

3. **Write the Python program**: Write a Python program that imports the RPi.GPIO library and sets the GPIO pin connected to the LED as an output. Then, use the `output()` function to turn the LED on and off.

Here is an example Python program that lights an LED connected to GPIO pin 17 on the Raspberry Pi:

```python
import RPi.GPIO as GPIO
import time

# Set the pin numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 17 as an output
GPIO.setup(17, GPIO.OUT)

# Turn the LED on
GPIO.output(17, GPIO.HIGH)

# Wait for 5 seconds
time.sleep(5)

# Turn the LED off
GPIO.output(17, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()
```

This program sets the pin numbering mode to BCM, sets pin 17 as an output, turns the LED on by setting the output of pin 17 to high, waits for 5 seconds, turns the LED off by setting the output of pin 17 to low, and finally cleans up the GPIO pins.