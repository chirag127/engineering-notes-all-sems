# 4. a) Light an LED through Python program

To light an LED through a Python program, you will need the following components:
1. A single-board computer such as a Raspberry Pi or a microcontroller such as an Arduino.
2. An LED (Light Emitting Diode).
3. A resistor (220-ohm is a common value).
4. Jumper wires to connect the components.

Here are the steps to light an LED through a Python program:
1. Connect the LED to the single-board computer or microcontroller. The longer leg of the LED (the anode) should be connected to a GPIO (General Purpose Input/Output) pin through a resistor. The shorter leg of the LED (the cathode) should be connected to a ground pin.
2. Write a Python program to control the GPIO pin. The program should set the GPIO pin to output mode and then turn it on and off to light the LED. Here is an example Python program that can be used to light an LED on a Raspberry Pi:

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

This program sets the GPIO pin to output mode using the `GPIO.setup()` function. It then enters an infinite loop that turns the LED on and off by setting the GPIO pin to high and low using the `GPIO.output()` function. The `time.sleep()` function is used to pause the program for one second between turning the LED on and off.

3. Run the Python program. The LED should light up and turn off at one-second intervals.

Note that the exact details of how to connect the LED and write the Python program may vary depending on the specific single-board computer or microcontroller you are using. Consult the documentation for your device for more information.