# 5. a) Flash an LED based on cron output (acts as an alarm)

- Cron is a software utility that allows users to schedule tasks to run periodically at fixed times, dates, or intervals.
- An LED (light-emitting diode) is a semiconductor device that emits light when an electric current passes through it.
- To flash an LED based on cron output, the following steps are required:

  - Connect an LED to a GPIO (general-purpose input/output) pin on a Raspberry Pi or similar device. For example, connect the anode (longer leg) of the LED to GPIO 17 and the cathode (shorter leg) to a ground pin using a 330 ohm resistor.
  - Write a Python script that controls the LED by setting the GPIO pin to high (on) or low (off) using the RPi.GPIO module. For example, the script could look like this:

    ```python
    import RPi.GPIO as GPIO
    import time

    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set the GPIO pin 17 as output
    GPIO.setup(17, GPIO.OUT)

    # Turn the LED on for 1 second
    GPIO.output(17, GPIO.HIGH)
    time.sleep(1)

    # Turn the LED off for 1 second
    GPIO.output(17, GPIO.LOW)
    time.sleep(1)

    # Clean up the GPIO pins
    GPIO.cleanup()
    ```

  - Save the script as `led.py` and make it executable by running `chmod +x led.py` in the terminal.
  - Edit the crontab file by running `crontab -e` in the terminal. This file contains the commands that cron will execute at specified times.
  - Add a line to the crontab file that tells cron when and how to run the script. For example, to flash the LED every minute, the line could look like this:

    `* * * * * /home/pi/led.py`

  - Save and exit the crontab file. Cron will automatically reload the file and execute the commands according to the schedule.
  - The LED will flash on and off every minute based on the cron output, acting as an alarm.