# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- Cron is a software utility that can be used to schedule commands or scripts to run at a specified time or interval on a Linux system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO pin and a ground pin of a Raspberry Pi or a similar device that can run Linux and control GPIO pins.
  2. Connect the relay's contact terminals to the load and a power source, such as a battery or a wall outlet, according to the relay's specifications and the load's requirements.
  3. Write a Python script or a shell script that can turn on the GPIO pin connected to the relay's coil, thereby closing the relay's contacts and switching on the load.
  4. Test the script by running it manually and verifying that the relay and the load are working as expected.
  5. Edit the crontab file using the `crontab -e` command and add a line that specifies the time and the script to run, using the cron syntax. For example, to run the script every day at 8:00 AM, the line would be:

     `0 8 * * * /path/to/script`

  6. Save and exit the crontab file. The cron daemon will automatically execute the script at the specified time, switching on the relay and the load.