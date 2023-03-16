#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

To flash an LED at a given on time and off time cycle, where the two times are taken from a file, the following steps are required:

- Import the necessary modules, such as `time` and `RPi.GPIO`.
- Set up the GPIO pin that is connected to the LED as an output.
- Open the file that contains the on time and off time values, and read them into variables.
- Use a `while` loop to repeat the following actions:
  - Turn on the LED by setting the GPIO pin to high.
  - Wait for the on time duration using the `time.sleep` function.
  - Turn off the LED by setting the GPIO pin to low.
  - Wait for the off time duration using the `time.sleep` function.
- Close the file and clean up the GPIO pins.

A possible code example is:

```python
# Import modules
import time
import RPi.GPIO as GPIO

# Set up GPIO pin
LED_PIN = 17 # Change this to the pin you are using
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Open file and read on time and off time
file = open("times.txt", "r")
on_time = float(file.readline()) # Read the first line as a float
off_time = float(file.readline()) # Read the second line as a float
file.close()

# Flash LED in a loop
while True:
  GPIO.output(LED_PIN, GPIO.HIGH) # Turn on LED
  time.sleep(on_time) # Wait for on time
  GPIO.output(LED_PIN, GPIO.LOW) # Turn off LED
  time.sleep(off_time) # Wait for off time

# Clean up GPIO pins
GPIO.cleanup()
```