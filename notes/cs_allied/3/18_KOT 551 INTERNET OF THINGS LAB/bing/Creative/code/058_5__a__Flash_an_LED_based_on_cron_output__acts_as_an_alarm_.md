# 5. a) Flash an LED based on cron output (acts as an alarm)

- To flash an LED based on cron output, we need to use a Raspberry Pi, an LED, a resistor, some jumper wires, and a breadboard.
- A Raspberry Pi is a small computer that can run Linux and interact with hardware devices through its GPIO pins.
- An LED is a light-emitting diode that can turn on and off when a voltage is applied across its terminals.
- A resistor is a component that limits the current flow in a circuit and protects the LED from burning out.
- Jumper wires are used to connect the components on the breadboard, which is a platform for prototyping circuits.
- Cron is a Linux utility that allows us to schedule commands or scripts to run at specific times or intervals.
- To flash an LED based on cron output, we need to do the following steps:

  1. Connect the LED and the resistor to the Raspberry Pi's GPIO pins using the jumper wires and the breadboard. For example, we can connect the longer leg of the LED (the anode) to GPIO pin 17, and the shorter leg (the cathode) to the resistor. Then, we can connect the other end of the resistor to a ground pin, such as pin 6.
  2. Write a Python script that can turn the LED on and off using the GPIO library. For example, we can name the script led.py and write the following code:

  ```python
  import RPi.GPIO as GPIO
  import sys

  # Set the GPIO mode to BCM
  GPIO.setmode(GPIO.BCM)

  # Set the LED pin as an output
  LED_PIN = 17
  GPIO.setup(LED_PIN, GPIO.OUT)

  # Get the argument from the command line
  # The argument should be either "on" or "off"
  arg = sys.argv[1]

  # Turn the LED on or off based on the argument
  if arg == "on":
      GPIO.output(LED_PIN, GPIO.HIGH)
  elif arg == "off":
      GPIO.output(LED_PIN, GPIO.LOW)
  else:
      print("Invalid argument")

  # Clean up the GPIO pins
  GPIO.cleanup()
  ```

  3. Make the script executable by running the command `chmod +x led.py` in the terminal.
  4. Test the script by running it with different arguments, such as `./led.py on` or `./led.py off`, and observe the LED's behavior.
  5. Edit the crontab file by running the command `crontab -e` in the terminal. This will open the file in a text editor, where we can add or modify the cron jobs.
  6. Add a cron job that will run the script at a specific time or interval and flash the LED. For example, we can add the following line to the crontab file:

  ```
  # Flash the LED every minute
  * * * * * /home/pi/led.py on; sleep 0.5; /home/pi/led.py off
  ```

  This will run the script with the argument "on", wait for 0.5 seconds, then run the script with the argument "off", every minute. The LED will flash for 0.5 seconds every minute, acting as an alarm.
  7. Save and exit the crontab file. The cron job will start running automatically. We can check the cron output by running the command `tail -f /var/log/syslog` in the terminal.