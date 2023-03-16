# Switch on a relay at a given time using cron

1. **Cron** is a time-based job scheduler in Unix-like operating systems. It is used to schedule commands or scripts to run automatically at a specified time and date.

2. To switch on a relay at a given time using cron, the relay's contact terminals must be connected to a load.

3. The first step is to create a script that will switch on the relay. This can be done using a programming language such as Python or Bash.

4. Once the script is created, it can be scheduled to run at a specific time using the `crontab` command. The `crontab` command is used to edit the crontab file, which contains the schedule of cron jobs.

5. The syntax for the `crontab` command is as follows:
```
crontab [-u user] file
crontab [-u user] [-l | -r | -e]
```

6. To schedule a script to run at a specific time, the following line must be added to the crontab file:
```
m h dom mon dow command
```
where:
- `m` is the minute (0-59)
- `h` is the hour (0-23)
- `dom` is the day of the month (1-31)
- `mon` is the month (1-12)
- `dow` is the day of the week (0-7, where 0 and 7 represent Sunday)
- `command` is the command to be executed

7. For example, to switch on the relay at 6:30 PM every day, the following line can be added to the crontab file:
```
30 18 * * * /path/to/relay_script.sh
```

8. Once the crontab file is saved, the cron daemon will automatically run the specified script at the specified time.

9. It is important to ensure that the script is executable and that the user running the cron job has the necessary permissions to execute the script.

10. In summary, to switch on a relay at a given time using cron, a script must be created to switch on the relay, and this script must be scheduled to run at the specified time using the `crontab` command. The relay's contact terminals must be connected to a load for the relay to function properly.