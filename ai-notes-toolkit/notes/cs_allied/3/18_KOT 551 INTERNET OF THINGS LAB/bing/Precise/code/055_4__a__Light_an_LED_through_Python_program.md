# 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a few components: a Raspberry Pi, an LED, a resistor, and jumper wires.
2. Connect the LED to one of the GPIO pins on the Raspberry Pi using a resistor and jumper wires.
3. In your Python program, import the necessary libraries, such as `RPi.GPIO` and `time`.
4. Set the GPIO pin connected to the LED as an output pin using the `GPIO.setup()` function.
5. Use the `GPIO.output()` function to turn the LED on and off.
6. You can also use the `time.sleep()` function to control the duration of the LED being on or off.
7. Remember to clean up the GPIO pins using the `GPIO.cleanup()` function at the end of your program.

Here is an example Python program that lights an LED:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
```