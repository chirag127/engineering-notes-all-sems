# Switch on a relay at a given time using cron

- A relay is an electromechanical device that can be used to control a load (such as a lamp, a fan, a motor, etc.) by switching it on or off using an electrical signal.
- A cron is a software utility that can be used to schedule tasks to run at specific times or intervals on a computer system, such as a Raspberry Pi.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay to the Raspberry Pi using the appropriate pins and wires. For example, if the relay has a 5V coil and a normally open (NO) contact, connect the positive terminal of the coil to a 5V pin on the Pi, the negative terminal of the coil to a GPIO pin on the Pi (such as GPIO 17), and the contact terminals to the load and the power source (such as a 12V battery).
  2. Write a Python script that can control the relay by setting the GPIO pin to high or low. For example, the following script can turn on the relay for 10 seconds and then turn it off:

```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use BCM numbering scheme for GPIO pins
GPIO.setup(17, GPIO.OUT) # set GPIO 17 as output

GPIO.output(17, GPIO.HIGH) # turn on relay
time.sleep(10) # wait for 10 seconds
GPIO.output(17, GPIO.LOW) # turn off relay

GPIO.cleanup() # reset GPIO pins
```

  3. Save the script in a suitable location on the Pi, such as `/home/pi/relay.py`, and make it executable by running the command `chmod +x /home/pi/relay.py` in the terminal.
  4. Edit the crontab file by running the command `crontab -e` in the terminal. This will open the file in a text editor, where you can add a line to specify when and how to run the script. For example, the following line will run the script every day at 8:00 AM:

```bash
0 8 * * * /home/pi/relay.py
```

  5. Save and exit the crontab file. The cron service will automatically reload the file and execute the script according to the schedule.