# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- A cron is a software utility that can be used to schedule tasks to run at a specified time or interval on a computer system, such as a Raspberry Pi.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to the GPIO pins of the Raspberry Pi, and the relay's contact terminals to the load and a power source. For example, if the relay is a 5V relay, connect the coil terminals to GPIO 17 and GPIO 18, and the contact terminals to the load and a 5V power source.
  2. Write a Python script that can control the relay by setting the GPIO pins to high or low. For example, the following script can switch on the relay by setting GPIO 17 to high and GPIO 18 to low, and switch off the relay by setting GPIO 17 to low and GPIO 18 to high.

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use BCM numbering scheme for GPIO pins
GPIO.setup(17, GPIO.OUT) # set GPIO 17 as output
GPIO.setup(18, GPIO.OUT) # set GPIO 18 as output

def switch_on_relay():
  GPIO.output(17, GPIO.HIGH) # set GPIO 17 to high
  GPIO.output(18, GPIO.LOW) # set GPIO 18 to low

def switch_off_relay():
  GPIO.output(17, GPIO.LOW) # set GPIO 17 to low
  GPIO.output(18, GPIO.HIGH) # set GPIO 18 to high

switch_on_relay() # switch on the relay
time.sleep(10) # wait for 10 seconds
switch_off_relay() # switch off the relay
GPIO.cleanup() # reset the GPIO pins
```

  3. Save the Python script as a file, such as relay.py, and make it executable by running the command `chmod +x relay.py` in the terminal.
  4. Edit the crontab file by running the command `crontab -e` in the terminal, and add a line that specifies the time and the command to run the Python script. For example, the following line will run the script at 8:00 AM every day.

```bash
0 8 * * * /home/pi/relay.py
```

  5. Save and exit the crontab file, and verify that the cron job is created by running the command `crontab -l` in the terminal.
  6. Test the cron job by setting the system time to a few minutes before the scheduled time, and observe the relay and the load. For example, if the cron job is set to run at 8:00 AM, set the system time to 7:55 AM by running the command `sudo date -s "2023-03-16 07:55:00"` in the terminal, and wait for 5 minutes. The relay should switch on at 8:00 AM, and switch off after 10 seconds.