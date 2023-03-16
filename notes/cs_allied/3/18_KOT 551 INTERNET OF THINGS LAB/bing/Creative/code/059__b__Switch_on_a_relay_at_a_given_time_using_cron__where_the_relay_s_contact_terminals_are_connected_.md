# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load (such as a light, a fan, a motor, etc.) by applying a voltage to its coil terminals.
- A cron is a software utility that can be used to schedule commands or scripts to run at a specified time or interval on a Linux system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a GPIO (general-purpose input/output) pin and a ground pin of a microcontroller or a single-board computer (such as Arduino, Raspberry Pi, etc.).
  2. Connect the relay's contact terminals to the load and a power source (such as a battery, a wall outlet, etc.).
  3. Write a script or a program that can control the GPIO pin to turn on or off the relay by setting it to high or low voltage level.
  4. Save the script or the program in a file with a suitable name and extension (such as relay.py, relay.sh, etc.).
  5. Make the file executable by using the command `chmod +x filename` in the terminal.
  6. Open the crontab file by using the command `crontab -e` in the terminal.
  7. Add a line to the crontab file with the following format: `minute hour day month weekday command`, where `minute` is the minute of the hour (0-59), `hour` is the hour of the day (0-23), `day` is the day of the month (1-31), `month` is the month of the year (1-12), `weekday` is the day of the week (0-6, where 0 is Sunday), and `command` is the path to the file that contains the script or the program.
  8. Save and exit the crontab file by using the command `:wq` in the terminal.
  9. Verify that the cron job is created by using the command `crontab -l` in the terminal.
  10. Wait for the specified time to see if the relay switches on the load as expected.

- For example, if the file that contains the script or the program is named relay.py and is located in the home directory, and the desired time to switch on the relay is 8:30 AM every Monday, the line to be added to the crontab file would be:

  `30 8 * * 1 /home/relay.py`

- This means that the command `/home/relay.py` will be executed at 8:30 AM every Monday, which will turn on the relay and the load connected to it.