# 4. a) Light an LED through Python program

- To light an LED through Python program, you need the following components:
  - A Raspberry Pi board with GPIO pins
  - An LED
  - A resistor (220 ohms or similar)
  - Jumper wires
  - A breadboard
- The steps to light an LED through Python program are as follows:
  - Connect the LED to the breadboard. The longer leg (anode) of the LED should be connected to one end of the resistor, and the shorter leg (cathode) should be connected to a free row on the breadboard.
  - Connect one end of a jumper wire to the other end of the resistor, and the other end to the GPIO pin 18 on the Raspberry Pi board. This is the positive terminal of the LED circuit.
  - Connect another jumper wire from the free row on the breadboard where the LED cathode is connected, to the ground (GND) pin on the Raspberry Pi board. This is the negative terminal of the LED circuit.
  - The circuit diagram is shown below:

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
   |     |   +-----+
   |     +---| LED |<----+
   |         +-----+     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   |                     |
   +---------------------+
  GPIO 18              GND
  ```

  - Write a Python program to control the LED. The program should import the GPIO library, set the GPIO pin 18 as output, and use a loop to turn the LED on and off with a delay. The program is shown below:

  ```python
  # Import the GPIO library
  import RPi.GPIO as GPIO
  # Import the time library
  import time

  # Set the GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)
  # Set the GPIO pin 18 as output
  GPIO.setup(18, GPIO.OUT)

  # Use a loop to turn the LED on and off
  while True:
    # Turn the LED on
    GPIO.output(18, GPIO.HIGH)
    # Wait for one second
    time.sleep(1)
    # Turn the LED off
    GPIO.output(18, GPIO.LOW)
    # Wait for one second
    time.sleep(1)
  ```

  - Save the program as led.py and run it on the Raspberry Pi using the command:

  ```bash
  python led.py
  ```

  - You should see the LED blinking on and off with a one-second interval. To stop the program, press Ctrl+C on the keyboard.