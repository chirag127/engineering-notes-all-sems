# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- Cron is a software utility that can be used to schedule commands or scripts to run at a specified time or interval on a Linux system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO pin and a ground pin of a microcontroller (such as a Raspberry Pi) that can run Linux and has cron installed.
  2. Connect the relay's contact terminals to the load and a power source (such as a battery or a wall outlet) according to the relay's specifications and the load's requirements.
  3. Write a script or a command that can turn on the GPIO pin and thus energize the relay's coil, which will close the contact terminals and switch on the load. For example, in Python, the following code can be used to turn on GPIO pin 17:

     ```python
     import RPi.GPIO as GPIO # Import the GPIO library
     GPIO.setmode(GPIO.BCM) # Set the GPIO numbering mode to BCM
     GPIO.setup(17, GPIO.OUT) # Set GPIO pin 17 as an output
     GPIO.output(17, GPIO.HIGH) # Turn on GPIO pin 17
     ```

  4. Save the script or the command in a file (such as relay_on.py) and make it executable by running the following command in the terminal:

     ```bash
     chmod +x relay_on.py # Make the file executable
     ```

  5. Edit the crontab file by running the following command in the terminal:

     ```bash
     crontab -e # Edit the crontab file
     ```

  6. Add a line to the crontab file that specifies the time and the script or the command to run. For example, to run the relay_on.py script at 8:00 AM every day, the following line can be added:

     ```bash
     0 8 * * * /home/pi/relay_on.py # Run the relay_on.py script at 8:00 AM every day
     ```

  7. Save and exit the crontab file. The cron service will automatically run the script or the command at the specified time and switch on the relay and the load.