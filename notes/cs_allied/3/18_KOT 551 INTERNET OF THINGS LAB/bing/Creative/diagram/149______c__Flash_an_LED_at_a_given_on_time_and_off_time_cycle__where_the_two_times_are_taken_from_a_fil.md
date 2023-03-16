#### c) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.

To flash an LED at a given on time and off time cycle, where the two times are taken from a file, the following steps are required:

- Import the necessary modules, such as `time` and `RPi.GPIO`.
- Set up the GPIO pin that is connected to the LED as an output.
- Open the file that contains the on time and off time values, and read them into variables.
- Use a loop to repeatedly turn on the LED, wait for the on time, turn off the LED, and wait for the off time.
- Close the file and clean up the GPIO pin when the loop is terminated.

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
file = open("led_times.txt", "r")
on_time = float(file.readline()) # Read the first line as a float
off_time = float(file.readline()) # Read the second line as a float
file.close()

# Loop to flash LED
try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH) # Turn on LED
        time.sleep(on_time) # Wait for on time
        GPIO.output(LED_PIN, GPIO.LOW) # Turn off LED
        time.sleep(off_time) # Wait for off time
except KeyboardInterrupt:
    # Clean up GPIO pin when the loop is terminated by Ctrl+C
    GPIO.cleanup()
```

The file `led_times.txt` should contain two numbers in separate lines, representing the on time and off time in seconds. For example:

```
0.5
1.0
```

This would flash the LED for 0.5 seconds and turn it off for 1.0 second.