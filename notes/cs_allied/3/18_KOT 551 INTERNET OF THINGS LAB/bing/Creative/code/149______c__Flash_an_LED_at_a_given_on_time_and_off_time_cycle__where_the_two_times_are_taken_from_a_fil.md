#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

To flash an LED at a given on time and off time cycle, where the two times are taken from a file, the following steps are required:

- Import the necessary modules, such as `GPIO` for controlling the LED pin, `time` for measuring the time intervals, and `sys` for reading the file name from the command line argument.
- Set the LED pin number, such as `17`, and configure it as an output using `GPIO.setup`.
- Open the file using `open` and read the first two lines using `readline`. Convert the lines to floating point numbers using `float` and assign them to variables, such as `on_time` and `off_time`.
- Use a `while` loop to repeat the following actions indefinitely:
  - Turn on the LED using `GPIO.output` and pass the pin number and `True` as arguments.
  - Wait for the on time using `time.sleep` and pass the `on_time` variable as an argument.
  - Turn off the LED using `GPIO.output` and pass the pin number and `False` as arguments.
  - Wait for the off time using `time.sleep` and pass the `off_time` variable as an argument.
- Close the file using `close` and clean up the GPIO pins using `GPIO.cleanup` when the program is terminated.

The code for this task could look something like this:

```python
# Import the modules
import RPi.GPIO as GPIO
import time
import sys

# Set the LED pin number
LED_PIN = 17

# Configure the LED pin as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Open the file and read the on and off times
file_name = sys.argv[1] # Get the file name from the command line argument
file = open(file_name, "r") # Open the file in read mode
on_time = float(file.readline()) # Read the first line and convert it to a float
off_time = float(file.readline()) # Read the second line and convert it to a float

# Flash the LED in a loop
try:
  while True:
    GPIO.output(LED_PIN, True) # Turn on the LED
    time.sleep(on_time) # Wait for the on time
    GPIO.output(LED_PIN, False) # Turn off the LED
    time.sleep(off_time) # Wait for the off time
except KeyboardInterrupt:
  # Close the file and clean up the GPIO pins when the program is terminated
  file.close()
  GPIO.cleanup()
```