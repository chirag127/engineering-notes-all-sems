 Here is the formal content in Markdown format without emojis or external links:

# Switch on a relay at a given time using cron

1. Connect the relay to the Raspberry Pi GPIO pins. The relay coil terminals are connected to a power source and the contact terminals are connected to the load which needs to be switched on/off.
2. Write a Python script which will turn on the relay at a specific time. Import the RPi.GPIO library and use the GPIO.output() function to control the relay.
3. Schedule the Python script to run at a specified time using cron. Cron is a time-based job scheduler on Unix-like systems.
4. Open the crontab for editing using `crontab -e` and add a new cron entry. The entry will be of the format `* * * * * /path/to/python/script.py`. The five fields represent minute, hour, day of month, month, day of week respectively. Use appropriate values to schedule the job at the required time.
5. Save the changes to the crontab and the job will be scheduled. The relay will turn on at the given time when the cron job runs.

The content is written in points in Markdown format without any emojis or external links as required. The tone is formal and no feelings are expressed. Please let me know if you would like me to modify or expand the answer.