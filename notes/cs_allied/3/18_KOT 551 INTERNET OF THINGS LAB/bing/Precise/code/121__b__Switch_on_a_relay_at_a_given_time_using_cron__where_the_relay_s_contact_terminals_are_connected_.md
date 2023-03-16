# Switching on a Relay at a Given Time Using Cron

1. **Cron** is a time-based job scheduler in Unix-like operating systems. It is used to schedule commands or scripts to run automatically at a specified time and date.

2. A **relay** is an electrically operated switch. It uses an electromagnet to mechanically operate a switch, allowing a low power circuit to control a high power circuit.

3. To switch on a relay at a given time using cron, the relay's contact terminals must be connected to a load.

4. The first step is to write a script that will control the relay. This script will send a signal to the relay to switch it on or off.

5. Next, the script must be scheduled to run at the desired time using the `crontab` command. The `crontab` command is used to edit the cron table, which is a list of commands that are scheduled to run at specified times.

6. The syntax for the `crontab` command is as follows: `crontab -e`. This will open the cron table in the default text editor.

7. The cron table uses a specific syntax to schedule commands. Each line of the cron table represents a separate job, and follows the format: `m h dom mon dow command`.

    - `m`: minute (0-59)
    - `h`: hour (0-23)
    - `dom`: day of the month (1-31)
    - `mon`: month (1-12)
    - `dow`: day of the week (0-6, with 0 representing Sunday)
    - `command`: the command to be executed

8. To schedule the script to run at a specific time, the appropriate values must be entered for `m`, `h`, `dom`, `mon`, and `dow`. The `command` field should contain the path to the script that controls the relay.

9. Once the cron table has been edited and saved, the script will be automatically executed at the specified time, switching on the relay and allowing current to flow to the load.

10. It is important to ensure that the script is executable and that the user has the appropriate permissions to run the `crontab` command.