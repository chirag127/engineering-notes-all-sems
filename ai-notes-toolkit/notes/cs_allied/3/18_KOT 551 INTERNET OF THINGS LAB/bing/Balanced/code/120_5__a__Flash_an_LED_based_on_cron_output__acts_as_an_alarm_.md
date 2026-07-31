# 5. a) Flash an LED based on cron output (acts as an alarm)

- Cron is a software utility that allows users to schedule tasks to run periodically at fixed times, dates, or intervals.
- An LED (light-emitting diode) is a semiconductor device that emits light when an electric current passes through it.
- To flash an LED based on cron output, the following steps are required:

  1. Connect an LED to a GPIO (general-purpose input/output) pin on a Raspberry Pi or similar device. The GPIO pin can be controlled by software to turn the LED on or off. For example, connect the anode (longer leg) of the LED to GPIO 17 and the cathode (shorter leg) to a ground pin using a 330 ohm resistor in series.
  2. Write a Python script that uses the RPi.GPIO module to set the GPIO pin as an output and toggle its state every second. For example, save the following code as `led.py`:

  ```python
  import RPi.GPIO as GPIO
  import time

  # Set the GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)

  # Set the GPIO pin 17 as an output
  GPIO.setup(17, GPIO.OUT)

  # Loop forever
  while True:
    # Turn the LED on
    GPIO.output(17, GPIO.HIGH)
    # Wait for one second
    time.sleep(1)
    # Turn the LED off
    GPIO.output(17, GPIO.LOW)
    # Wait for one second
    time.sleep(1)
  ```

  3. Test the script by running it in a terminal with the command `python led.py`. The LED should flash on and off every second.
  4. To schedule the script to run at a specific time or interval, use the `crontab` command to edit the user's crontab file. For example, to run the script every day at 8:00 AM, add the following line to the crontab file:

  ```
  0 8 * * * python /home/pi/led.py
  ```

  5. Save and exit the crontab file. The cron daemon will execute the script at the specified time and the LED will flash as an alarm. To stop the script, use the `kill` command to terminate the process or remove the line from the crontab file.