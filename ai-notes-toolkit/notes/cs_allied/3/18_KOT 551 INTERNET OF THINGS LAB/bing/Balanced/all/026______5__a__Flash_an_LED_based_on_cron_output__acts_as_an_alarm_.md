#### 5. a) Flash an LED based on cron output (acts as an alarm)

- Cron is a utility that allows users to schedule tasks to run at specific times or intervals.
- An LED is a light-emitting diode that can be controlled by a microcontroller or a computer.
- To flash an LED based on cron output, one needs to:
  - Connect the LED to a suitable power source and a GPIO pin of the microcontroller or computer.
  - Write a script or a program that can turn the LED on and off using the GPIO pin.
  - Test the script or program to make sure the LED works as expected.
  - Create a cron job that can run the script or program at the desired time or interval.
  - Save the cron job and enable the cron service.
- The following steps illustrate how to flash an LED based on cron output using a Raspberry Pi and Python:

  - Connect the LED to the 3.3V pin and the GPIO 17 pin of the Raspberry Pi using a resistor and a breadboard. Refer to this diagram for the wiring: ![LED wiring](https://projects-static.raspberrypi.org/projects/physical-computing/8a55526d88a2a0f14ce50a8f3582e06b31d949ff/en/images/gpio-led-pi.png)
  - Write a Python script that can turn the LED on and off using the GPIO library. For example, save the following code as led.py:

    ```python
    import RPi.GPIO as GPIO
    import time

    # Set the GPIO mode to BCM
    GPIO.setmode(GPIO.BCM)

    # Set the GPIO 17 pin as output
    GPIO.setup(17, GPIO.OUT)

    # Turn the LED on for one second
    GPIO.output(17, GPIO.HIGH)
    time.sleep(1)

    # Turn the LED off for one second
    GPIO.output(17, GPIO.LOW)
    time.sleep(1)

    # Clean up the GPIO pins
    GPIO.cleanup()
    ```

  - Test the script by running it in the terminal: `python led.py`
  - Create a cron job that can run the script every minute. To do this, open the crontab file in the terminal: `crontab -e`
  - Add the following line at the end of the file: `* * * * * python /home/pi/led.py`
  - Save and exit the file. The cron service will automatically reload the crontab file.
  - The LED should now flash every minute based on the cron output. To stop the cron job, edit the crontab file again and delete or comment out the line.