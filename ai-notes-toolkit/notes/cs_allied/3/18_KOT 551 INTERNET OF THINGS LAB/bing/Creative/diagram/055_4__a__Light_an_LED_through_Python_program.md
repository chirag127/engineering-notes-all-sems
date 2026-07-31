Hello, I am Sydney, your AI assistant. I can help you with your topic.

To light an LED through Python program, you need to follow these steps:

1. Connect an LED to a GPIO pin on your Raspberry Pi board. You also need a resistor to limit the current and protect the LED. For example, you can connect the anode (longer leg) of the LED to GPIO 17 (pin 11) and the cathode (shorter leg) to a 330 ohm resistor, which is then connected to the ground (pin 6).
2. Install the RPi.GPIO library on your Raspberry Pi. This library allows you to control the GPIO pins from Python. You can install it by typing `sudo apt-get install python-rpi.gpio` in the terminal.
3. Write a Python program that imports the RPi.GPIO library, sets the GPIO mode to BCM (which means using the GPIO numbers instead of the pin numbers), sets the GPIO 17 pin as an output, and turns it on and off with a delay. For example, you can write:

```python
import RPi.GPIO as GPIO # import the library
import time # import the time module

GPIO.setmode(GPIO.BCM) # set the GPIO mode to BCM
GPIO.setup(17, GPIO.OUT) # set GPIO 17 as an output

while True: # loop forever
    GPIO.output(17, GPIO.HIGH) # turn on the LED
    time.sleep(1) # wait for 1 second
    GPIO.output(17, GPIO.LOW) # turn off the LED
    time.sleep(1) # wait for 1 second
```

4. Save your Python program as a file, for example, `led.py`, and run it by typing `python led.py` in the terminal. You should see the LED blinking on and off every second. To stop the program, press Ctrl+C in the terminal.