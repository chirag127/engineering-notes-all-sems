# 4. a) Light an LED through Python program

- To light an LED through Python program, you need to have a hardware device that can control the LED, such as an Arduino, a Raspberry Pi, or a MicroPython board.
- You also need to connect the LED to the device using wires, resistors, and a breadboard, following the appropriate circuit diagram for your device.
- You need to install Python and the necessary libraries on your computer and on your device, such as pyserial, RPi.GPIO, or pyb.
- You need to write a Python program that can communicate with your device and send commands to turn the LED on and off.
- You need to upload the Python program to your device or run it from your computer, depending on your device and configuration.
- You need to test your program and observe the LED blinking or changing colors, according to your program logic.

## Example: Light an LED with Raspberry Pi and Python

- Connect the LED to the Raspberry Pi using a 330 ohm resistor, a breadboard, and jumper wires. Connect the anode (longer leg) of the LED to GPIO pin 18 of the Raspberry Pi, and the cathode (shorter leg) to the ground (GND) pin.
- Install Python and the RPi.GPIO library on your Raspberry Pi, following the instructions from https://sourceforge.net/p/raspberry-gpio-python/wiki/install/.
- Write a Python program that can control the LED using the RPi.GPIO library. For example, save the following code as LED.py:

```python
import RPi.GPIO as GPIO # Import the library
import time # Import the time module

GPIO.setmode(GPIO.BCM) # Set the numbering scheme to BCM
GPIO.setup(18, GPIO.OUT) # Set pin 18 as an output pin

while True: # Loop forever
    GPIO.output(18, GPIO.HIGH) # Turn on the LED
    time.sleep(1) # Wait for 1 second
    GPIO.output(18, GPIO.LOW) # Turn off the LED
    time.sleep(1) # Wait for 1 second
```

- Run the Python program from the Raspberry Pi terminal using the command: `sudo python LED.py`
- You should see the LED blinking on and off once every second. To stop the program, press Ctrl+C.