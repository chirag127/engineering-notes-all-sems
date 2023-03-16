# 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a few components: a Raspberry Pi, an LED, a resistor, and jumper wires.
2. Connect the LED to the Raspberry Pi using the jumper wires and the resistor. The resistor is used to limit the current flowing through the LED to prevent it from burning out.
3. Once the LED is connected, you can use the GPIO library in Python to control the LED. The GPIO library allows you to control the input and output pins on the Raspberry Pi.
4. To turn the LED on, you will need to set the pin connected to the LED to output mode and then set the output to high. This can be done using the `GPIO.setup()` and `GPIO.output()` functions.
5. Here is an example Python program that will turn on an LED connected to pin 18 on the Raspberry Pi:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(5)
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
```

This program sets up the GPIO library, sets pin 18 to output mode, turns the LED on for 5 seconds, and then turns it off. The `GPIO.cleanup()` function is used to reset the GPIO pins to their default state when the program is finished.