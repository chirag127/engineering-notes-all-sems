#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a command-line utility called `gpio` to control the GPIO pins.
- We need to connect the LED to the GPIO pin 17 (BCM numbering) and the resistor to the ground pin using the jumper wires and the breadboard. The resistor limits the current and protects the LED from burning out.
- We need to write a shell script that uses the `gpio` command to turn the LED on and off with a delay. For example, we can create a file called `flash.sh` with the following content:

```bash
#!/bin/bash
# flash.sh: flash an LED connected to GPIO 17

# set GPIO 17 as output
gpio -g mode 17 out

# loop 10 times
for i in {1..10}
do
  # turn LED on
  gpio -g write 17 1
  # wait for 0.5 seconds
  sleep 0.5
  # turn LED off
  gpio -g write 17 0
  # wait for 0.5 seconds
  sleep 0.5
done
```

- We need to make the script executable by running `chmod +x flash.sh` in the terminal.
- We need to use the `crontab` command to edit the cron table, which is a file that specifies when and how often a command or a script should be executed. For example, we can run `crontab -e` and add the following line to the end of the file:

```cron
0 8 * * * /home/pi/flash.sh
```

- This line means that the script `flash.sh` will be executed at 8:00 AM every day. The cron table has five fields that specify the minute, hour, day of month, month, and day of week of the execution. We can use `*` to match any value, or a range or a list of values separated by commas. For more details, we can refer to the `man crontab` command or the online documentation.
- We need to save and exit the cron table editor. The cron daemon will automatically reload the cron table and execute the commands or scripts according to the schedule.
- When the script is executed, the LED will flash 10 times, acting as an alarm. We can change the number of flashes, the delay, or the cron schedule according to our preference.