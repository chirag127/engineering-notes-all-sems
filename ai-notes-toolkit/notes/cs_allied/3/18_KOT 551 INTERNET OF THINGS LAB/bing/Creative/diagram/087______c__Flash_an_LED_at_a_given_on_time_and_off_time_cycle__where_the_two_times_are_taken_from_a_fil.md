#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

To flash an LED at a given on time and off time cycle, where the two times are taken from a file, the following steps are required:

- Import the necessary modules, such as `time` and `RPi.GPIO`.
- Set up the GPIO pin that is connected to the LED as an output.
- Open the file that contains the on time and off time values, and read them into variables.
- Use a loop to repeatedly turn the LED on and off, using the `GPIO.output` function and the `time.sleep` function with the on time and off time variables as arguments.
- Close the file and clean up the GPIO pins when the loop is terminated.

A possible code example is:

```python
# Import modules
import time
import RPi.GPIO as GPIO

# Set up GPIO pin
GPIO.setmode(GPIO.BCM) # Use Broadcom pin numbering
GPIO.setup(18, GPIO.OUT) # Set pin 18 as output

# Open file and read on time and off time
file = open("led_times.txt", "r") # Open file in read mode
on_time = float(file.readline()) # Read first line as float
off_time = float(file.readline()) # Read second line as float
file.close() # Close file

# Loop to flash LED
try:
    while True: # Repeat indefinitely
        GPIO.output(18, GPIO.HIGH) # Turn LED on
        time.sleep(on_time) # Wait for on time
        GPIO.output(18, GPIO.LOW) # Turn LED off
        time.sleep(off_time) # Wait for off time
except KeyboardInterrupt: # If user presses Ctrl+C
    GPIO.cleanup() # Clean up GPIO pins
```