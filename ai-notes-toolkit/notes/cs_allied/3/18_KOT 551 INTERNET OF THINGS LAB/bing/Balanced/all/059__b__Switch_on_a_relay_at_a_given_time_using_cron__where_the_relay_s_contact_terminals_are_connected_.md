# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- Cron is a software utility that can be used to schedule commands or scripts to run at a specified time or interval on a Linux system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO pin and a ground pin of a microcontroller (such as a Raspberry Pi) that can run Linux and has cron installed.
  2. Connect the relay's contact terminals to the load and a power source (such as a battery or a wall outlet) according to the relay's specifications and the load's requirements.
  3. Write a script or a command that can turn on the GPIO pin and thus activate the relay's coil and close the contact terminals, allowing the current to flow through the load. For example, in Python, the script could look like this:

```python
import RPi.GPIO as GPIO # Import the GPIO library
GPIO.setmode(GPIO.BCM) # Set the GPIO numbering mode
GPIO.setup(18, GPIO.OUT) # Set GPIO pin 18 as output
GPIO.output(18, GPIO.HIGH) # Turn on GPIO pin 18
```

  4. Write a script or a command that can turn off the GPIO pin and thus deactivate the relay's coil and open the contact terminals, stopping the current from flowing through the load. For example, in Python, the script could look like this:

```python
import RPi.GPIO as GPIO # Import the GPIO library
GPIO.setmode(GPIO.BCM) # Set the GPIO numbering mode
GPIO.setup(18, GPIO.OUT) # Set GPIO pin 18 as output
GPIO.output(18, GPIO.LOW) # Turn off GPIO pin 18
```

  5. Save the scripts or commands as executable files in a directory of your choice. For example, you could save them as `relay_on.py` and `relay_off.py` in the `/home/pi` directory.
  6. Use the `crontab -e` command to edit the cron table and add the entries for the scripts or commands to run at the desired time. For example, if you want to switch on the relay at 8:00 AM and switch it off at 10:00 AM every day, you could add the following lines to the cron table:

```bash
0 8 * * * python /home/pi/relay_on.py # Run the relay_on.py script at 8:00 AM every day
0 10 * * * python /home/pi/relay_off.py # Run the relay_off.py script at 10:00 AM every day
```

  7. Save and exit the cron table. The cron service will automatically execute the scripts or commands at the specified time and switch on or off the relay accordingly.