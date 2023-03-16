# Switch on a relay at a given time using cron

1. **Cron** is a time-based job scheduler in Unix-like operating systems. It is used to schedule commands or scripts to run automatically at a specified time and date.
2. A **relay** is an electrically operated switch. It is used to control a circuit by a separate low-power signal, or where several circuits must be controlled by one signal.
3. To switch on a relay at a given time using cron, the relay's contact terminals must be connected to a load.
4. The first step is to connect the relay to the appropriate GPIO pins on the device, such as a Raspberry Pi.
5. Next, a script must be written to control the relay. This script will use the appropriate commands to switch the relay on and off.
6. Once the script is written and tested, it can be scheduled to run at a specific time using cron. This is done by editing the crontab file and adding a new entry for the script.
7. The entry in the crontab file will specify the time and date when the script should run, as well as the command to run the script.
8. Once the entry is added to the crontab file, cron will automatically run the script at the specified time, switching on the relay and activating the connected load.
