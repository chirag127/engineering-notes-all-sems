#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a command-line utility called `gpio` to control the GPIO pins.
- We need to connect the LED to the GPIO pin 17 (BCM numbering) and the resistor to the ground pin using the jumper wires and the breadboard. The resistor is used to limit the current and protect the LED from burning out.
- We need to write a shell script that uses the `gpio` command to turn the LED on and off. For example, we can create a file called `flash_led.sh` with the following content:

```bash
#!/bin/bash
# flash_led.sh - a script to flash an LED on GPIO 17

# set the GPIO 17 to output mode
gpio -g mode 17 out

# loop 10 times
for i in {1..10}
do
  # turn the LED on
  gpio -g write 17 1
  # wait for 0.5 seconds
  sleep 0.5
  # turn the LED off
  gpio -g write 17 0
  # wait for 0.5 seconds
  sleep 0.5
done
```

- We need to make the script executable by running the command `chmod +x flash_led.sh`.
- We need to use the `crontab` command to schedule the script to run at a specific time or interval. For example, we can run the command `crontab -e` to edit the crontab file and add the following line:

```bash
# flash the LED at 8:00 AM every day
0 8 * * * /home/pi/flash_led.sh
```

- This will flash the LED 10 times at 8:00 AM every day, acting as an alarm. We can save and exit the crontab file and verify that the cron job is set up by running the command `crontab -l`.
- We can also test the script manually by running the command `./flash_led.sh` and observe the LED flashing.