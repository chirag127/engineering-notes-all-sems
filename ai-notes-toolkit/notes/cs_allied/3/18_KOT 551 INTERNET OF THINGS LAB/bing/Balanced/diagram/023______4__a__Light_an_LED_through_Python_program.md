#### 4. a) Light an LED through Python program

To light an LED through Python program, you need the following components:

- A Raspberry Pi board with GPIO pins
- An LED
- A resistor (220 ohms or higher)
- Jumper wires
- A breadboard

The steps to light an LED through Python program are:

1. Connect the LED to the breadboard. The longer leg of the LED is the positive (+) side and the shorter leg is the negative (-) side.
2. Connect the resistor to the positive side of the LED and the other end to any GPIO pin on the Raspberry Pi board. For example, GPIO 18.
3. Connect the negative side of the LED to the ground (GND) pin on the Raspberry Pi board.
4. Open a Python editor on the Raspberry Pi and write the following code:

```python
# Import the GPIO library
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

5. Save the code and run it. You should see the LED light up for 5 seconds and then turn off.