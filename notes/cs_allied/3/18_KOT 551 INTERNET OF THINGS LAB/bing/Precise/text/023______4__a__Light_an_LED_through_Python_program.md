#### 4. a) Light an LED through Python program

1. To light an LED through a Python program, you will need a Raspberry Pi, an LED, a breadboard, and some jumper wires.
2. Connect the LED to the breadboard and connect the Raspberry Pi to the breadboard using the jumper wires.
3. Install the necessary libraries on the Raspberry Pi, such as the RPi.GPIO library.
4. Write a Python program that imports the RPi.GPIO library and sets the pin connected to the LED as an output pin.
5. Use the GPIO.output() function to turn the LED on and off.
6. Run the Python program on the Raspberry Pi to light the LED.

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

This program sets the pin connected to the LED as an output pin and then enters an infinite loop that turns the LED on and off with a delay of one second between each state change. You can modify the delay to change the speed at which the LED blinks.