Hello, I am Sydney, your AI assistant. I can help you with your topic.

# 4. a) Light an LED through Python program

- To light an LED through Python program, you need the following components:
  - A Raspberry Pi board with GPIO pins
  - An LED
  - A resistor (220 ohms)
  - Breadboard and jumper wires
  - Python 3 installed on the Raspberry Pi
- The steps to light an LED through Python program are as follows:
  - Connect the LED to the GPIO pin 18 of the Raspberry Pi and the resistor to the ground pin using the breadboard and jumper wires. The circuit diagram is shown below:

  ```
  +3.3V  +5V
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |
   |     |   +-----+
   |     +---| LED |----+
   |         +-----+    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   |                    |
   +--------------------+---- GND
  ```

  - Create a Python file named led.py and write the following code:

  ```python
  # Import the GPIO library
  import RPi.GPIO as GPIO
  # Import the time library
  import time

  # Set the GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)
  # Set the GPIO pin 18 as output
  GPIO.setup(18, GPIO.OUT)

  # Turn on the LED
  GPIO.output(18, GPIO.HIGH)
  # Wait for 5 seconds
  time.sleep(5)
  # Turn off the LED
  GPIO.output(18, GPIO.LOW)

  # Clean up the GPIO pins
  GPIO.cleanup()
  ```

  - Save and run the Python file using the command:

  ```bash
  python3 led.py
  ```

  - You should see the LED light up for 5 seconds and then turn off. You can change the duration of the LED being on or off by changing the value of the time.sleep() function.