# 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a few components: a Raspberry Pi, an LED, a resistor, breadboard, and jumper wires.
2. Connect the LED to the Raspberry Pi using the breadboard and jumper wires. The LED should be connected to a GPIO pin on the Raspberry Pi and to a ground pin through a resistor.
3. Write a Python program to control the GPIO pin connected to the LED. You can use the RPi.GPIO library to control the GPIO pins on the Raspberry Pi.
4. In the Python program, set the GPIO pin connected to the LED as an output pin and set its value to high to turn on the LED.
5. Run the Python program to light the LED.

Here is an example Python program that can be used to light an LED connected to GPIO pin 17 on a Raspberry Pi:

```python
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the LED GPIO pin
LED_PIN = 17

# Set the LED GPIO pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn on the LED
GPIO.output(LED_PIN, GPIO.HIGH)

# Keep the LED on for 5 seconds
time.sleep(5)

# Turn off the LED
GPIO.output(LED_PIN, GPIO.LOW)

# Cleanup the GPIO
GPIO.cleanup()
```