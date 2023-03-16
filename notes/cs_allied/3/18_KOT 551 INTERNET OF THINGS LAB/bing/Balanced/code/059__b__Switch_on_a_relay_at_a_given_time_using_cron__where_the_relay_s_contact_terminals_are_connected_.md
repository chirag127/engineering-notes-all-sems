# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- Cron is a software utility that can be used to schedule commands or scripts to run at a specified time or interval on a Linux system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO pin and a ground pin of a microcontroller (such as a Raspberry Pi) that can run Linux and has cron installed.
  2. Connect the relay's contact terminals to the load and a power source (such as a battery or a wall outlet) according to the relay's specifications and the load's requirements.
  3. Write a script or a command that can turn on the GPIO pin and thus activate the relay's coil and close the contact terminals, allowing the current to flow through the load. For example, using Python and the RPi.GPIO library, the script could look like this:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # use BCM numbering scheme for GPIO pins
GPIO.setup(18, GPIO.OUT) # set pin 18 as output
GPIO.output(18, GPIO.HIGH) # turn on pin 18 and activate relay
```

  4. Save the script or the command in a file (such as relay_on.py) and make it executable by running the command `chmod +x relay_on.py` in the terminal.
  5. Edit the crontab file by running the command `crontab -e` in the terminal and add a line that specifies the time and the script or the command to run. For example, to switch on the relay at 8:00 AM every day, the line could look like this:

```bash
0 8 * * * /home/pi/relay_on.py
```

  6. Save and exit the crontab file. The cron service will automatically run the script or the command at the specified time and switch on the relay and the load.