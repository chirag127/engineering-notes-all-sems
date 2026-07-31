#### 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a Raspberry Pi, an LED, a resistor, and some jumper wires.
2. Connect the LED to one of the GPIO pins on the Raspberry Pi using a resistor and jumper wires.
3. In your Python program, import the `RPi.GPIO` module, which allows you to control the GPIO pins on the Raspberry Pi.
4. Set the GPIO pin connected to the LED as an output pin using the `GPIO.setup()` function.
5. Use the `GPIO.output()` function to turn the LED on and off by setting the output pin to `GPIO.HIGH` or `GPIO.LOW`.
6. You can control the brightness of the LED by using pulse-width modulation (PWM) to vary the duty cycle of the output pin.
7. To use PWM, create a `GPIO.PWM` object for the output pin and use the `start()`, `ChangeDutyCycle()`, and `stop()` methods to control the duty cycle.

Here is an example Python program that lights an LED connected to GPIO pin 18 on a Raspberry Pi:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

pwm = GPIO.PWM(LED_PIN, 100)
pwm.start(0)

try:
    while True:
        for duty_cycle in range(0, 101, 5):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
        for duty_cycle in range(100, -1, -5):
            pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

pwm.stop()
GPIO.cleanup()
```

This program uses a loop to gradually increase and decrease the duty cycle of the output pin, causing the LED to fade in and out. The `try` and `except` statements are used to handle the `KeyboardInterrupt` exception, which is raised when the user presses `Ctrl-C` to stop the program. When the exception is caught, the `pwm.stop()` and `GPIO.cleanup()` functions are called to clean up the resources used by the program.