#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a simple way to control the GPIO pins using the command line.
- The steps to flash an LED based on cron output are as follows:

  1. Connect the LED to the GPIO pin 17 (BCM numbering) and the ground pin of the Raspberry Pi using the resistor and the jumper wires. The resistor should be between the LED and the ground pin to limit the current and protect the LED. The breadboard can be used to make the connections easier.
  2. Test the LED by running the following commands in the terminal:

     ```bash
     gpio mode 17 out # set the GPIO pin 17 as output
     gpio write 17 1 # turn on the LED
     gpio write 17 0 # turn off the LED
     ```

  3. Create a shell script that will flash the LED for a specified number of times and duration. For example, the following script will flash the LED 10 times, with 0.5 seconds on and 0.5 seconds off:

     ```bash
     #!/bin/bash
     # flash_led.sh
     # flash the LED for a specified number of times and duration

     # get the number of times and duration from the command line arguments
     times=$1
     duration=$2

     # loop for the number of times
     for ((i=1;i<=times;i++))
     do
       # turn on the LED
       gpio write 17 1
       # wait for the duration
       sleep $duration
       # turn off the LED
       gpio write 17 0
       # wait for the duration
       sleep $duration
     done
     ```

  4. Make the script executable by running the following command:

     ```bash
     chmod +x flash_led.sh
     ```

  5. Test the script by running it with some arguments, such as:

     ```bash
     ./flash_led.sh 10 0.5
     ```

  6. To schedule the script to run at a specific time, we can use the cron utility, which allows us to execute commands at specified intervals or times. To edit the crontab file, which contains the cron jobs, we can run the following command:

     ```bash
     crontab -e
     ```

  7. To add a cron job that will flash the LED at 8:00 AM every day, we can append the following line to the crontab file:

     ```bash
     0 8 * * * /home/pi/flash_led.sh 10 0.5
     ```

  8. Save and exit the crontab file. The cron job will run the script at the specified time and flash the LED as an alarm.