#### b) Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to control high-voltage or high-current devices with low-voltage or low-current signals.
- A relay has two main parts: a coil and a set of contacts. The coil is an electromagnet that can be energized by applying a voltage across its terminals. The contacts are metal pieces that can be opened or closed by the magnetic field of the coil.
- A relay can be connected to a Raspberry Pi GPIO pin to control its coil. The GPIO pin can be set to high or low to turn on or off the relay. The relay's contact terminals can be connected to a load, such as a lamp, a fan, or a motor.
- Cron is a time-based scheduler that can be used to run commands or scripts at specified times or intervals on a Raspberry Pi  . Cron has a configuration file called crontab, which contains the scheduled tasks and their corresponding times using a special syntax  .
- To switch on a relay at a given time using cron, the following steps are required:
  - Connect the relay to the Raspberry Pi GPIO pin and the load to the relay's contact terminals. Make sure the relay and the load are compatible with the Raspberry Pi's voltage and current ratings.
  - Write a Python script that can control the relay by setting the GPIO pin to high or low. For example, the script can be named relay_on.py and contain the following code:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # use BCM numbering scheme for GPIO pins
GPIO.setup(18, GPIO.OUT) # set GPIO 18 as output
GPIO.output(18, GPIO.HIGH) # set GPIO 18 to high to turn on relay
```

  - Make the script executable by running the command `chmod +x relay_on.py` in the terminal.
  - Edit the crontab file by running the command `crontab -e` in the terminal  . This will open the file in a text editor, such as nano or vi.
  - Add a line to the crontab file that specifies the time and the command to run the script. The line should follow the format `minute hour day month weekday command`  . For example, to run the script at 8:00 AM every day, the line can be:

```bash
0 8 * * * /home/pi/relay_on.py
```

  - Save and exit the crontab file. The cron service will automatically reload the file and execute the scheduled tasks  .
- To switch off the relay at a given time using cron, the same steps can be followed, except that the Python script should set the GPIO pin to low to turn off the relay, and the crontab line should specify a different time. For example, the script can be named relay_off.py and contain the following code:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # use BCM numbering scheme for GPIO pins
GPIO.setup(18, GPIO.OUT) # set GPIO 18 as output
GPIO.output(18, GPIO.LOW) # set GPIO 18 to low to turn off relay
```

And the crontab line can be:

```bash
0 20 * * * /home/pi/relay_off.py
```

This will run the script at 8:00 PM every day  .

: Cron Jobs and Task Scheduling on Raspberry Pi OS | Delft Stack
: Raspberry Pi: Control Relay switch via GPIO
: Cron and GPIO relay SOLVED - Raspberry Pi Forums
: Setting Up A Cron Job On The Raspberry Pi - BC Robotics
: Raspberry Pi - Crontab tutorial (How to Schedule Cron jobs)