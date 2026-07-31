 Here is the formal content in markdown format without any emojis or external links:

# Switch on a relay at a given time using cron

1. Cron is a time-based job scheduler in Linux systems. It can be used to schedule tasks to run at a specific time or periodically.
2. To switch on a relay at a given time using cron, follow the below steps:

- Connect the relay's contact terminals to the load you want to control.
- Write a shell script that will turn on the relay. For example, you can write a script that toggles the relay on by changing the GPIO pin state to high.
- Open the cron table using `crontab -e` command.
- Add a new cron job line with the following structure:

`<minute> <hour> <day of month> <month> <day of week> /path/to/relay_on.sh`

- Specify the time at which you want the relay to turn on. For example, to turn the relay on at 8 PM every day, specify `0 20 * * * /path/to/relay_on.sh`
- Save the cron table.
- The relay will turn on at the specified time every day as per the cron job.

The key points to note are:

1. Write a shell script to control the relay
2. Add a cron job with the specific time and script path to schedule the task
3. Cron will run the scheduled task at the specified time