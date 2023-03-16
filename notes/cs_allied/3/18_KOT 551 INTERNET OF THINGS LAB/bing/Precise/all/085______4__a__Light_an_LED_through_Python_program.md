#### 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a Raspberry Pi, an LED, a breadboard, and some jumper wires.
2. Connect the LED to the Raspberry Pi using the breadboard and jumper wires. The positive leg of the LED should be connected to a GPIO pin on the Raspberry Pi, and the negative leg should be connected to a ground pin.
3. In your Python program, import the `RPi.GPIO` module, which allows you to control the GPIO pins on the Raspberry Pi.
4. Set the GPIO pin connected to the LED as an output pin using the `GPIO.setup()` function.
5. Use the `GPIO.output()` function to turn the LED on and off by setting the output pin to `GPIO.HIGH` or `GPIO.LOW`.
6. You can also control the brightness of the LED by using pulse-width modulation (PWM) to vary the duty cycle of the output pin.

Here is an example Python program that lights an LED connected to GPIO pin 17 on the Raspberry Pi:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
```

This program turns the LED on for one second, then off for one second, in an infinite loop. You can modify the program to control the LED in different ways.