# 4. a) Light an LED through Python program

To light an LED through Python program, you need the following components:

- A Raspberry Pi board with GPIO pins
- An LED
- A resistor (220 ohms or higher)
- Jumper wires
- A breadboard

The steps to light an LED through Python program are:

1. Connect the LED to the breadboard. The longer leg of the LED is the positive (+) side and the shorter leg is the negative (-) side.
2. Connect one end of the resistor to the positive leg of the LED and the other end to any GPIO pin on the Raspberry Pi. For example, GPIO 18.
3. Connect the negative leg of the LED to the ground (GND) pin on the Raspberry Pi. For example, pin 6.
4. The circuit diagram should look like this:

```
    +3.3V  (1) (2)  +5V
 GPIO2  (3) (4)  +5V
 GPIO3  (5) (6)  GND
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
 GPIO17 (11) (12) GPIO18 <-- Resistor --> LED --> GND
 GPIO27 (13) (14) GND
 GPIO22 (15) (16) GPIO23
   +3.3V(17) (18) GPIO24
 GPIO10 (19) (20) GND
 GPIO9  (21) (22) GPIO25
 GPIO11 (23) (24) GPIO8
   GND  (25) (26) GPIO7
```

5. Write a Python program to control the LED. You can use the RPi.GPIO module to access the GPIO pins. For example:

```python
# Import the RPi.GPIO module
import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT)

# Turn on the LED
GPIO.output(18, GPIO.HIGH)

# Wait for 5 seconds
import time
time.sleep(5)

# Turn off the LED
GPIO.output(18, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()
```

6. Save the Python program as led.py and run it on the Raspberry Pi. You should see the LED light up for 5 seconds and then turn off.