# Switch on a relay at a given time using cron, where the relay's contact terminals are connected to a load.

- A relay is an electromechanical device that can be used to switch on or off a load using an electric signal.
- A cron is a software utility that can be used to schedule tasks to run at a specified time or interval on a computer system.
- To switch on a relay at a given time using cron, the following steps are required:

  1. Connect the relay's coil terminals to a suitable power source and a control signal, such as a GPIO pin of a microcontroller or a computer.
  2. Connect the relay's contact terminals to the load and another power source, such as a battery or a mains supply.
  3. Write a script or a program that can send a high or low signal to the control pin of the relay, depending on whether the relay should be on or off.
  4. Save the script or program in a file and make it executable, if necessary.
  5. Use the cron utility to create a crontab file that specifies when and how often the script or program should be executed.
  6. Test the cron job and the relay operation by observing the load behavior at the scheduled time.

- An example of a crontab file that switches on a relay at 8:00 AM every day and switches it off at 8:05 AM every day is:

  ```
  # Minute Hour Day Month Weekday Command
  0 8 * * * /path/to/script/relay_on.sh
  5 8 * * * /path/to/script/relay_off.sh
  ```

- An example of a script that switches on a relay connected to GPIO pin 17 of a Raspberry Pi is:

  ```bash
  #!/bin/bash
  # Set GPIO pin 17 as output
  echo "17" > /sys/class/gpio/export
  echo "out" > /sys/class/gpio/gpio17/direction
  # Send high signal to GPIO pin 17
  echo "1" > /sys/class/gpio/gpio17/value
  ```

- An example of a script that switches off a relay connected to GPIO pin 17 of a Raspberry Pi is:

  ```bash
  #!/bin/bash
  # Set GPIO pin 17 as output
  echo "17" > /sys/class/gpio/export
  echo "out" > /sys/class/gpio/gpio17/direction
  # Send low signal to GPIO pin 17
  echo "0" > /sys/class/gpio/gpio17/value
  ```