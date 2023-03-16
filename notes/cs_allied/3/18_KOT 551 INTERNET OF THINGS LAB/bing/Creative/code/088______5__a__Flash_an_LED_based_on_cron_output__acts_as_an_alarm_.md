#### 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- We also need to install the wiringPi library on the Raspberry Pi, which provides a simple way to control the GPIO pins.
- The steps to flash an LED based on cron output are as follows:

  1. Connect the LED to the GPIO pin 17 and the resistor to the ground pin on the breadboard, using the jumper wires.
  2. Write a C program that uses the wiringPi library to turn the LED on and off with a delay of one second. Save the program as led.c and compile it with the command `gcc -o led led.c -lwiringPi`.
  3. Test the program by running it with the command `sudo ./led`. The LED should flash on and off every second.
  4. To make the program run based on cron output, we need to edit the crontab file with the command `crontab -e`. This file allows us to schedule tasks to run at specific times or intervals.
  5. In the crontab file, we can add a line like this: `0 8 * * * sudo ./led`. This means that the program will run at 8:00 am every day, and flash the LED for one minute (the default duration of cron jobs).
  6. Save and exit the crontab file. The LED will now flash based on cron output, acting as an alarm.