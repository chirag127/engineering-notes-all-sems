#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a command-line utility called `gpio` to control the GPIO pins.
- We need to connect the LED to the GPIO pin 17 (BCM numbering) and the resistor to the ground pin using the jumper wires and the breadboard. The resistor limits the current and prevents the LED from burning out.
- We need to write a shell script that uses the `gpio` command to turn the LED on and off. For example, we can create a file called `flash_led.sh` with the following content:

```bash
#!/bin/bash
# Turn the LED on
gpio -g write 17 1
# Wait for one second
sleep 1
# Turn the LED off
gpio -g write 17 0
# Wait for one second
sleep 1
```

- We need to make the script executable by running `chmod +x flash_led.sh`.
- We need to use the `crontab` command to edit the cron table, which is a file that specifies when and how often a command should be executed. For example, we can run `crontab -e` and add the following line to the end of the file:

```bash
# Flash the LED every minute
* * * * * /home/pi/flash_led.sh
```

- This will run the script every minute and flash the LED twice. We can save and exit the file, and the cron daemon will automatically reload the cron table and execute the command accordingly.
- To verify that the LED is flashing, we can observe the LED or check the cron output by running `crontab -l`. We can also modify the cron expression to change the frequency or timing of the LED flashing. For example, we can change the line to:

```bash
# Flash the LED every hour at 30 minutes past the hour
30 * * * * /home/pi/flash_led.sh
```

- This will act as an hourly alarm that flashes the LED twice at 30 minutes past every hour.