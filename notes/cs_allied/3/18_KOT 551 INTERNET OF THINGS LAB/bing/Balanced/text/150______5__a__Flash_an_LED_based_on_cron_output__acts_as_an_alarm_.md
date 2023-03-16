#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the WiringPi library on the Raspberry Pi, which provides a simple way to control the GPIO pins using the command line.
- The steps to flash an LED based on cron output are as follows:

  1. Connect the LED to the GPIO pin 17 and the resistor to the ground pin on the breadboard, using the jumper wires. Make sure the longer leg of the LED is connected to the positive side and the shorter leg to the negative side.
  2. Open a terminal on the Raspberry Pi and type `gpio -g mode 17 out` to set the GPIO pin 17 as an output pin.
  3. Type `gpio -g write 17 1` to turn on the LED and `gpio -g write 17 0` to turn off the LED. You can test the LED by typing these commands alternately.
  4. To make the LED flash automatically, we need to use the cron utility, which allows us to schedule tasks to run at specific times or intervals.
  5. Type `crontab -e` to edit the crontab file, which contains the cron jobs for the current user. If this is the first time you use crontab, you may be asked to choose an editor. You can choose nano, which is a simple text editor.
  6. In the crontab file, add a line like this: `* * * * * gpio -g write 17 1; sleep 0.5; gpio -g write 17 0`. This means that every minute, the LED will turn on for 0.5 seconds and then turn off. You can change the numbers to adjust the frequency and duration of the LED flashing. For example, if you want the LED to flash every 10 minutes for 2 seconds, you can write `*/10 * * * * gpio -g write 17 1; sleep 2; gpio -g write 17 0`.
  7. Save and exit the crontab file by pressing Ctrl+O and then Ctrl+X. The cron job will start running in the background.
  8. To stop the LED flashing, you can either delete the line from the crontab file or type `gpio -g write 17 0` to turn off the LED manually.