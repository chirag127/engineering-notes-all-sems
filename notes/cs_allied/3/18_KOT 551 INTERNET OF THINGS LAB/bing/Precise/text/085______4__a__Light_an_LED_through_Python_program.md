#### 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a Raspberry Pi or a similar microcontroller, an LED, a resistor, and jumper wires.
2. Connect the LED to one of the GPIO pins on the Raspberry Pi using a resistor and jumper wires.
3. In the Python program, import the necessary libraries such as `RPi.GPIO` and `time`.
4. Set the GPIO pin connected to the LED as an output pin using the `GPIO.setup()` function.
5. Use the `GPIO.output()` function to turn the LED on and off.
6. You can also use the `time.sleep()` function to control the duration for which the LED stays on or off.
7. Make sure to clean up the GPIO pins using the `GPIO.cleanup()` function before exiting the program.

Here is an example Python program that lights an LED connected to GPIO pin 17 on a Raspberry Pi:

```python
import RPi.GPIO as GPIO
import time

# Set the pin numbering mode
GPIO.setmode(GPIO.BCM)

# Set the pin as an output pin
GPIO.setup(17, GPIO.OUT)

# Turn the LED on
GPIO.output(17, GPIO.HIGH)
time.sleep(1)

# Turn the LED off
GPIO.output(17, GPIO.LOW)
time.sleep(1)

# Clean up the GPIO pins
GPIO.cleanup()
```