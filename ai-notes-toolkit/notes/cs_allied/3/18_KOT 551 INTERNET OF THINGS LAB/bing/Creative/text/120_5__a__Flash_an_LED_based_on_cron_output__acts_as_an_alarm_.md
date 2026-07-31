# Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- A Raspberry Pi is a small computer that can run Linux and interact with hardware devices through its GPIO pins.
- An LED is a light-emitting diode that can turn on and off when current flows through it.
- A resistor is a component that limits the current flow and protects the LED from burning out.
- A breadboard is a board that allows us to connect components without soldering.
- Jumper wires are wires that can connect the components on the breadboard and the Raspberry Pi.
- Cron is a Linux utility that can schedule tasks to run at specific times or intervals.
- To flash an LED based on cron output, we need to do the following steps:

  1. Connect the LED and the resistor to the breadboard and the Raspberry Pi. The positive leg of the LED (the longer one) should go to a GPIO pin (for example, pin 18) and the negative leg (the shorter one) should go to the resistor. The other end of the resistor should go to a ground pin (for example, pin 6).
  2. Write a Python script that can control the LED. The script should import the GPIO library, set the pin mode to BCM, and set the LED pin as an output. Then, it should use a loop to turn the LED on and off with a delay. For example:

```python
import RPi.GPIO as GPIO
import time

LED_PIN = 18 # change this to the pin you are using
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
  GPIO.output(LED_PIN, GPIO.HIGH) # turn on the LED
  time.sleep(1) # wait for 1 second
  GPIO.output(LED_PIN, GPIO.LOW) # turn off the LED
  time.sleep(1) # wait for 1 second
```
  3. Save the script as led.py and make it executable with the command `chmod +x led.py`.
  4. Test the script by running it with the command `./led.py`. You should see the LED flashing on and off every second.
  5. To schedule the script to run at a specific time or interval, we need to use cron. To edit the cron table, use the command `crontab -e`. This will open a text editor where you can add your cron jobs. A cron job has the following format:

```bash
minute hour day month weekday command
```
  - minute: the minute when the command should run (0-59)
  - hour: the hour when the command should run (0-23)
  - day: the day of the month when the command should run (1-31)
  - month: the month when the command should run (1-12)
  - weekday: the day of the week when the command should run (0-6, where 0 is Sunday)
  - command: the command to execute

  For example, to run the led.py script every day at 8:00 AM, we can add the following line to the cron table:

```bash
0 8 * * * /home/pi/led.py
```
  6. Save and exit the cron table. The cron job will be activated and the LED will flash at the specified time. To stop the LED from flashing, we can either kill the script process or remove the cron job.