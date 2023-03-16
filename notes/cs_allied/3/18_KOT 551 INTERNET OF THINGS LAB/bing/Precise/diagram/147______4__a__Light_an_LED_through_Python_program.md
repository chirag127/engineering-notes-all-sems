#### 4. a) Light an LED through Python program

To light an LED through a Python program, the following steps can be followed:

1. **Connect the LED to the Raspberry Pi**: Connect the positive leg of the LED to a GPIO pin on the Raspberry Pi and the negative leg to a ground pin.
2. **Install the necessary libraries**: Install the RPi.GPIO library to control the GPIO pins on the Raspberry Pi.
3. **Write the Python program**: Write a Python program that imports the RPi.GPIO library and sets the GPIO pin connected to the LED as an output. Then, use the `output()` function to turn the LED on and off.
4. **Run the Python program**: Run the Python program to light the LED.

Here is an example Python program that can be used to light an LED:

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

This program sets the GPIO pin connected to the LED as an output and then turns the LED on and off with a delay of 1 second between each state change. The LED will blink continuously until the program is stopped.