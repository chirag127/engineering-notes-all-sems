# Switch on a relay at a given time using cron

1. **Cron** is a time-based job scheduler in Unix-like operating systems. It is used to schedule commands or scripts to run automatically at a specified time and date.

2. **Relay** is an electrically operated switch. It is used to control a circuit by a separate low-power signal, or where several circuits must be controlled by one signal.

3. To switch on a relay at a given time using cron, the relay's contact terminals must be connected to a load.

4. The first step is to create a script that will switch on the relay. This script can be written in a programming language such as Python or Bash.

5. The script should include commands to control the relay, such as sending a signal to the relay's control pin to switch it on.

6. Once the script is created, it can be scheduled to run at a specific time using cron.

7. To schedule the script, open the crontab file by typing `crontab -e` in the terminal.

8. In the crontab file, add a new line with the time and date when the script should run, followed by the path to the script. For example, to run the script every day at 8:00 AM, the line would be `0 8 * * * /path/to/script`.

9. Save and close the crontab file. The script will now run automatically at the specified time, switching on the relay and controlling the connected load.

10. It is important to ensure that the script is executable and that the user running the cron job has the necessary permissions to execute the script and control the relay.