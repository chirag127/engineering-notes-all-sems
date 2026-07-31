# 5. a) Flash an LED based on cron output (acts as an alarm)

- Cron is a utility that allows users to schedule tasks to run at specific times or intervals.
- An LED (light-emitting diode) is a device that emits light when an electric current passes through it.
- To flash an LED based on cron output, we need to connect the LED to a GPIO (general-purpose input/output) pin on a microcontroller or a single-board computer, such as Raspberry Pi or Arduino.
- We also need to write a script that controls the LED's state (on or off) and a cron job that executes the script at the desired time or frequency.
- The following steps illustrate how to flash an LED based on cron output using a Raspberry Pi and Python:

  1. Connect the LED to the GPIO pin 18 and a resistor to the ground (GND) pin on the Raspberry Pi. The resistor is needed to limit the current and protect the LED from burning out. The circuit diagram is shown below:

  ```
  +3.3V
   |
   |
   |     LED
   +----|>|----+
   |           |
   |           |
   |           R
   |           |
   |           |
   +-----------+---- GPIO 18
   |
   |
  GND
  ```

  2. Write a Python script that turns the LED on for one second and then off for one second, repeatedly. The script can be named `led_flash.py` and saved in the home directory. The script uses the `RPi.GPIO` module to control the GPIO pins and the `time` module to create delays. The script is shown below:

  ```python
  # Import the modules
  import RPi.GPIO as GPIO
  import time

  # Set the GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)

  # Set the GPIO pin 18 as output
  GPIO.setup(18, GPIO.OUT)

  # Create an infinite loop
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

  3. Write a cron job that runs the script at the desired time or frequency. To edit the cron table, use the command `crontab -e` in the terminal. The cron job can be written as follows:

  ```
  # Run the script every day at 8:00 AM
  0 8 * * * python /home/pi/led_flash.py
  ```

  4. Save and exit the cron table. The cron job will start running the script at the specified time and flash the LED as an alarm. To stop the script, use the command `crontab -r` to remove the cron job or `pkill python` to kill the Python process.