#### 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a few components: a Raspberry Pi, an LED, a resistor, and jumper wires.
2. Connect the LED to the Raspberry Pi using the jumper wires and the resistor. The resistor is used to limit the current flowing through the LED to prevent it from burning out.
3. Once the LED is connected, you can write a Python program to control it. Start by importing the necessary libraries, such as the `RPi.GPIO` library which allows you to control the GPIO pins on the Raspberry Pi.
4. Set the GPIO pin connected to the LED as an output pin using the `GPIO.setup()` function.
5. Use the `GPIO.output()` function to turn the LED on and off by setting the output pin to `HIGH` or `LOW`.
6. You can also use a loop and the `time.sleep()` function to make the LED blink at a specific interval.

Here is an example Python program that will light an LED connected to GPIO pin 17 on the Raspberry Pi:

```python
import RPi.GPIO as GPIO
import time

# Set the pin numbering mode
GPIO.setmode(GPIO.BCM)

# Set the LED pin as an output pin
LED_PIN = 17
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

This program will turn the LED on for 5 seconds and then turn it off. You can modify the program to make the LED blink or to control it in other ways.