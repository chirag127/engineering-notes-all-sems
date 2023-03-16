#### 5. a) Flash an LED based on cron output (acts as an alarm)

- Cron is a software utility that allows users to schedule tasks to run periodically at fixed times, dates, or intervals.
- An LED (light-emitting diode) is a semiconductor device that emits light when an electric current passes through it.
- To flash an LED based on cron output, the following steps are required:

  1. Connect an LED to a GPIO (general-purpose input/output) pin on a Raspberry Pi or similar device. For example, connect the anode (longer leg) of the LED to GPIO 17 and the cathode (shorter leg) to a 330 ohm resistor, which is then connected to the ground pin.
  2. Write a Python script that controls the LED using the GPIO library. For example, the script below turns the LED on for one second and then off for one second in an infinite loop.

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use Broadcom pin numbering
GPIO.setup(17, GPIO.OUT) # set GPIO 17 as output

while True: # repeat forever
  GPIO.output(17, GPIO.HIGH) # turn LED on
  time.sleep(1) # wait for one second
  GPIO.output(17, GPIO.LOW) # turn LED off
  time.sleep(1) # wait for one second
```

  3. Save the script as a file, such as led.py, and make it executable by running the command `chmod +x led.py` in the terminal.
  4. Edit the crontab file by running the command `crontab -e` in the terminal. This file contains the list of cron jobs that run for the current user.
  5. Add a line to the crontab file that specifies when and how to run the script. For example, the line below runs the script every day at 8:00 AM.

```bash
0 8 * * * /home/pi/led.py
```

  6. Save and exit the crontab file. The cron job will start running at the next scheduled time.
  7. To stop the cron job, either delete or comment out the line in the crontab file, or kill the script process by running the command `pkill -f led.py` in the terminal.