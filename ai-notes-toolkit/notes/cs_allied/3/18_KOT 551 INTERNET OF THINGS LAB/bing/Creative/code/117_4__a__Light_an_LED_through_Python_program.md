# 4. a) Light an LED through Python program

To light an LED through Python program, you need the following components:

- A Raspberry Pi board with GPIO pins
- An LED
- A resistor (220 ohms or higher)
- Jumper wires
- A breadboard

The steps to light an LED through Python program are:

1. Connect the LED to the breadboard. The longer leg of the LED is the positive (+) side and the shorter leg is the negative (-) side.
2. Connect the resistor to the positive leg of the LED and the other end to any GPIO pin on the Raspberry Pi. For example, GPIO 18.
3. Connect the negative leg of the LED to the ground (GND) pin on the Raspberry Pi. For example, pin 6.
4. Open a Python editor on the Raspberry Pi and create a new file. For example, led.py.
5. Import the GPIO library and set the pin mode to BCM. This means that you can refer to the pins by their GPIO number, not by their physical location.

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
```

6. Set the GPIO pin that you connected to the LED as an output pin. For example, GPIO 18.

```python
GPIO.setup(18, GPIO.OUT)
```

7. Turn on the LED by setting the output pin to high. This means that the pin will provide 3.3V of power to the LED.

```python
GPIO.output(18, GPIO.HIGH)
```

8. Save and run the Python program. You should see the LED light up.
9. To turn off the LED, set the output pin to low. This means that the pin will provide 0V of power to the LED.

```python
GPIO.output(18, GPIO.LOW)
```

10. To clean up the GPIO pins and release the resources, use the following command at the end of the program.

```python
GPIO.cleanup()
```

This is how you can light an LED through Python program. You can also use a loop or a button to control the LED. For more information, you can refer to the official documentation of the GPIO library: https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/