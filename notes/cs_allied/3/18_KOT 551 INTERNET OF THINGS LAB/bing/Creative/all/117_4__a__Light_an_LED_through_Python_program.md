# 4. a) Light an LED through Python program

- To light an LED through Python program, you need the following components:
  - A Raspberry Pi board with GPIO pins
  - An LED
  - A resistor (220 ohms or similar)
  - Breadboard and jumper wires
  - Python 3 installed on the Raspberry Pi
- The steps to light an LED through Python program are as follows:
  1. Connect the LED to the GPIO pin 18 (BCM numbering) and the ground pin of the Raspberry Pi using the resistor, breadboard and jumper wires. The resistor is used to limit the current and protect the LED from burning out. The circuit diagram is shown below:

  ```
  +3.3V o-----+-----o LED o-----/\/\/\-----o GPIO 18
              |                       |
             ---                     ---
             GND                     GND
  ```

  2. Create a Python file named `led.py` and write the following code:

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

  3. Save the file and run it using the command `python3 led.py`. You should see the LED light up for 5 seconds and then turn off.
  4. You can modify the code to change the duration or frequency of the LED blinking by changing the values of `time.sleep()` function. For example, to make the LED blink twice per second, you can use the following code:

  ```python
  # Import the GPIO library
  import RPi.GPIO as GPIO
  # Import the time library
  import time

  # Set the GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)
  # Set the GPIO pin 18 as output
  GPIO.setup(18, GPIO.OUT)

  # Repeat 10 times
  for i in range(10):
    # Turn on the LED
    GPIO.output(18, GPIO.HIGH)
    # Wait for 0.25 seconds
    time.sleep(0.25)
    # Turn off the LED
    GPIO.output(18, GPIO.LOW)
    # Wait for 0.25 seconds
    time.sleep(0.25)

  # Clean up the GPIO pins
  GPIO.cleanup()
  ```