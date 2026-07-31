#### 4. a) Light an LED through Python program

To light an LED through a Python program, follow these steps:

1. Connect the LED to a GPIO pin on the Raspberry Pi.
2. Open the Python IDE and create a new file.
3. Import the RPi.GPIO library by typing `import RPi.GPIO as GPIO`.
4. Set the GPIO mode to BCM by typing `GPIO.setmode(GPIO.BCM)`.
5. Set the GPIO pin to output mode by typing `GPIO.setup(pin, GPIO.OUT)`, where `pin` is the number of the GPIO pin connected to the LED.
6. Turn on the LED by typing `GPIO.output(pin, GPIO.HIGH)`.
7. Wait for a few seconds by typing `time.sleep(seconds)`, where `seconds` is the number of seconds to wait.
8. Turn off the LED by typing `GPIO.output(pin, GPIO.LOW)`.
9. Clean up the GPIO pins by typing `GPIO.cleanup()`.

It is important to note that the GPIO pin numbers used in the program may vary depending on the specific Raspberry Pi model being used. Additionally, it is crucial to ensure that the LED is properly connected to the GPIO pin, with the correct polarity. Otherwise, the LED may not light up or may be damaged.

By following these steps, you should be able to successfully light an LED through a Python program.