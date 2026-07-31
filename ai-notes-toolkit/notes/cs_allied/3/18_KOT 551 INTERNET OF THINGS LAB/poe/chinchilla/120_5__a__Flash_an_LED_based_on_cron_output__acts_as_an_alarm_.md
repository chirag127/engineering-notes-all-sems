##### Flash an LED based on cron output (acts as an alarm)

In this task, we will be using cron, a time-based job scheduler, to flash an LED at a specific time. This can be used as an alarm to remind us of important events or tasks.

Here are the steps to achieve this:

1. Connect an LED to a GPIO pin on the Raspberry Pi board. Make sure to connect the positive leg of the LED to the GPIO pin and the negative leg to the ground pin.

2. Install the python RPi.GPIO library using the following command:
   ```
   sudo apt-get install python-rpi.gpio
   ```

3. Create a python script that turns the LED on and off. Here's an example code:
   ```python
   import RPi.GPIO as GPIO
   import time

   # Set up the GPIO pin
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(11, GPIO.OUT)

   # Turn the LED on
   GPIO.output(11, GPIO.HIGH)

   # Wait for 1 second
   time.sleep(1)

   # Turn the LED off
   GPIO.output(11, GPIO.LOW)

   # Clean up the GPIO
   GPIO.cleanup()
   ```

4. Test the script by running it from the terminal using the following command:
   ```
   python /path/to/script.py
   ```

   The LED should turn on for 1 second and then turn off.

5. Use cron to schedule the script to run at a specific time. To do this, open the cron tab by running the following command:
   ```
   crontab -e
   ```

6. Add the following line to the end of the file:
   ```
   * * * * * python /path/to/script.py
   ```

   This will run the script every minute. To change the timing, you can modify the `* * * * *` part of the line to specify the exact time you want the script to run.

7. Save and exit the file.

8. Wait for the scheduled time and the LED should start flashing as an alarm.

By following these steps, we can easily create a simple alarm system using a Raspberry Pi and an LED. This can be useful for reminding us of important tasks or events.