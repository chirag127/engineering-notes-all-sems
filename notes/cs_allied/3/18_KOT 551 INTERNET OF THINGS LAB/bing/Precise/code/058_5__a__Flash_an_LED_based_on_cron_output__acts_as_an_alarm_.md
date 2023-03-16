# Flash an LED based on cron output (acts as an alarm)

1. **Cron** is a time-based job scheduler in Unix-like operating systems. It is used to schedule commands or scripts to run automatically at a specific time or date.
2. To flash an LED based on cron output, you will need to have a **single-board computer** such as a Raspberry Pi, an **LED**, and a **resistor**.
3. Connect the LED to one of the GPIO pins on the Raspberry Pi and the resistor to the ground pin.
4. Write a **script** that turns the LED on and off at the desired interval.
5. Use the `crontab` command to **schedule** the script to run at the desired time or date.
6. The LED will flash based on the cron output, acting as an alarm.
