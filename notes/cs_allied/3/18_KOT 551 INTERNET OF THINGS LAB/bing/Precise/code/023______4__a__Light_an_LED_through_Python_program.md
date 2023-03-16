#### 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a few components: a Raspberry Pi, an LED, a resistor, and jumper wires.
2. Connect the LED to the Raspberry Pi using the jumper wires and the resistor. The resistor is used to limit the current flowing through the LED to prevent it from burning out.
3. Once the LED is connected, you can use the GPIO library in Python to control the LED. This library allows you to control the GPIO pins on the Raspberry Pi.
4. To turn the LED on, you need to set the GPIO pin connected to the LED to output mode and then set its value to high. Here is an example code snippet that shows how to do this:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.HIGH)
```

5. To turn the LED off, you can set the value of the GPIO pin to low:

```python
GPIO.output(LED_PIN, GPIO.LOW)
```

6. Remember to clean up the GPIO pins when you are done by calling the `GPIO.cleanup()` function. This will reset the GPIO pins to their default state.

```python
GPIO.cleanup()
```