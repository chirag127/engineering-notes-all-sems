# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light bulb, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- A cron is a software utility that can be used to schedule tasks to run at a specified time or interval on a Linux-based system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO (General Purpose Input Output) pin and a ground pin of a microcontroller (such as a Raspberry Pi, an Arduino, etc.) that can run Linux.
  2. Connect the relay's contact terminals to the load and a power source (such as a battery, a wall outlet, etc.) according to the relay's specifications and the load's requirements.
  3. Write a script (such as a Python script, a Bash script, etc.) that can control the GPIO pin to switch on the relay by setting it to high (or low, depending on the relay's type) and switch off the relay by setting it to low (or high, depending on the relay's type).
  4. Test the script to make sure it can switch on and off the relay and the load as expected.
  5. Use the `crontab -e` command to edit the cron table and add a line that specifies the time and the script to run. For example, if the script is named `relay_on.py` and is located in the home directory, and the desired time to switch on the relay is 8:00 AM every day, the line would be:

     ```
     0 8 * * * python /home/relay_on.py
     ```

  6. Save and exit the cron table. The cron daemon will automatically run the script at the specified time and switch on the relay and the load.