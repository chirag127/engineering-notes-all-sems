#### 4. a) Light an LED through Python program

To light an LED through a Python program, you will need to follow these steps:

1. **Gather the necessary hardware**: You will need a Raspberry Pi, an LED, a resistor, and jumper wires.
2. **Set up the circuit**: Connect the LED to the Raspberry Pi using the jumper wires and the resistor. The resistor is used to limit the current flowing through the LED to prevent it from burning out.
3. **Write the Python code**: Use the RPi.GPIO library to control the GPIO pins on the Raspberry Pi. Set the pin connected to the LED as an output and use the `output()` function to turn the LED on and off.
4. **Run the Python program**: Execute the Python program to light the LED.

Here is an example of a Python program that can be used to light an LED:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(1)
```

This program sets the GPIO pin connected to the LED as an output and then turns the LED on and off with a delay of one second between each state change. You can modify the delay time to change the blinking speed of the LED.