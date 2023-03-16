#### 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a Raspberry Pi or similar device, an LED, a resistor, and jumper wires.
2. Connect the LED to one of the GPIO pins on the Raspberry Pi using a resistor and jumper wires.
3. In your Python program, import the necessary libraries such as `RPi.GPIO` and `time`.
4. Set the GPIO pin connected to the LED as an output pin using the `GPIO.setup()` function.
5. Use the `GPIO.output()` function to turn the LED on and off.
6. You can use the `time.sleep()` function to control the duration of the LED being on or off.
7. Remember to clean up the GPIO pins using the `GPIO.cleanup()` function when you are finished.

Here is an example Python program that will light an LED connected to GPIO pin 17 on a Raspberry Pi:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 17

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

This program will turn the LED on for one second, then off for one second, and repeat until the program is interrupted. You can modify the `time.sleep()` values to change the duration of the LED being on or off.