#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a simple way to control the GPIO pins using the command line.
- The steps to flash an LED based on cron output are as follows:

  1. Connect the LED to the GPIO pin 17 and the resistor to the ground pin on the breadboard, using the jumper wires. The resistor should be between 220 and 330 ohms, to limit the current and protect the LED.
  2. Test the LED by running the following commands on the Raspberry Pi terminal:

     ```bash
     gpio mode 17 out # set pin 17 as output
     gpio write 17 1 # turn on the LED
     gpio write 17 0 # turn off the LED
     ```

  3. To make the LED flash, we can use a loop that alternates between turning the LED on and off, with a delay in between. For example, the following bash script will flash the LED for 10 seconds:

     ```bash
     #!/bin/bash
     gpio mode 17 out # set pin 17 as output
     for i in {1..10} # loop 10 times
     do
       gpio write 17 1 # turn on the LED
       sleep 0.5 # wait for 0.5 seconds
       gpio write 17 0 # turn off the LED
       sleep 0.5 # wait for 0.5 seconds
     done
     ```

  4. To run the script based on cron output, we need to edit the crontab file, which is a list of commands that are executed at specified intervals. We can use the `crontab -e` command to edit the file, and add a line like this:

     ```bash
     0 8 * * * /home/pi/flash_led.sh # run the script at 8:00 am every day
     ```

  5. To save the changes, we need to press Ctrl+O and then Ctrl+X. The cron daemon will automatically reload the crontab file and execute the commands according to the schedule.
  6. To verify that the LED flashes at the specified time, we can check the syslog file, which records the cron events. We can use the `grep` command to filter the relevant lines, like this:

     ```bash
     grep cron /var/log/syslog # show the cron events
     ```

  7. We should see a line like this, indicating that the script was executed:

     ```bash
     Mar 16 08:00:01 raspberrypi CRON[1234]: (pi) CMD (/home/pi/flash_led.sh)
     ```

- This is how we can flash an LED based on cron output, which can act as an alarm.