# 4. a) Light an LED through Python program

- To light an LED through Python program, you need the following components:
  - A Raspberry Pi board with GPIO pins
  - An LED
  - A resistor (220 ohms or higher)
  - Breadboard and jumper wires
- The steps to light an LED through Python program are as follows:
  - Connect the LED to the GPIO pin 18 of the Raspberry Pi board using a resistor and jumper wires. The longer leg of the LED (anode) should be connected to the GPIO pin 18 and the shorter leg (cathode) should be connected to the ground (GND) pin. You can use any other GPIO pin, but you need to change the code accordingly.
  - Open a Python editor on the Raspberry Pi and create a new file named led.py. Write the following code in the file:

```python
# Import the GPIO library
import RPi.GPIO as GPIO
# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Set the GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT)
# Turn on the LED
GPIO.output(18, GPIO.HIGH)
```

  - Save the file and run it using the command `python led.py`. You should see the LED light up.
  - To turn off the LED, you can either stop the program by pressing Ctrl+C or write another line of code to set the GPIO pin 18 to low:

```python
# Turn off the LED
GPIO.output(18, GPIO.LOW)
```

  - You can also use a loop to make the LED blink. For example, you can write the following code to make the LED blink every second:

```python
# Import the GPIO and time libraries
import RPi.GPIO as GPIO
import time
# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
# Set the GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT)
# Create a loop
while True:
  # Turn on the LED
  GPIO.output(18, GPIO.HIGH)
  # Wait for one second
  time.sleep(1)
  # Turn off the LED
  GPIO.output(18, GPIO.LOW)
  # Wait for one second
  time.sleep(1)
```

  - Save the file and run it using the command `python led.py`. You should see the LED blink every second. To stop the program, press Ctrl+C.