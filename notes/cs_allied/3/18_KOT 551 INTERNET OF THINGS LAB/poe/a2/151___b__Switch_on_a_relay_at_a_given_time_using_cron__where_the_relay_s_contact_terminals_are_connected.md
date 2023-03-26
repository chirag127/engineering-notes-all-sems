 Here is the formal content in points on the given topic:

#### b) Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

1. Cron is a time-based job scheduler in Linux. It can be used to schedule tasks to run at a particular time.
2. To switch on a relay at a given time using cron, follow the below steps:

- Connect the relay terminals to the load which needs to be switched on.
- Find the cron syntax to specify the time at which the relay needs to be switched on. For example, to switch on at 8 PM every day, the cron syntax would be "0 8 * * *".
- Write a shell script which will switch on the relay by controlling its GPIO pin.
- Schedule the shell script to run at the required time using cron. To do this, open the cron table using "crontab -e" and add the cron syntax and shell script path in a new line.
- Save the cron table and the relay will be switched on at the given time every day.

3. Cron allows controlling devices at specified times in an automated way without manual intervention. This can be used to automate many time-based tasks.

The content is written in points in a formal tone with markdown formatting and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the answer.