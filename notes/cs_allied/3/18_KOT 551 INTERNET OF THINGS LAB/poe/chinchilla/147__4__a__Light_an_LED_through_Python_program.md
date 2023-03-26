#### 4. a) Light an LED through Python program

In order to light an LED through a Python program, the following steps can be followed:

1. Connect the LED to a GPIO pin on the Raspberry Pi, making sure to connect the positive leg of the LED to the GPIO pin and the negative leg to ground.

2. Open a new Python program in the Raspberry Pi's terminal.

3. Import the RPi.GPIO library by typing `import RPi.GPIO as GPIO` at the top of the program.

4. Set the mode of the GPIO pins by typing `GPIO.setmode(GPIO.BOARD)`.

5. Define the GPIO pin that the LED is connected to by typing `pin = 11` (where 11 is the number of the GPIO pin).

6. Set the direction of the GPIO pin to output by typing `GPIO.setup(pin, GPIO.OUT)`.

7. Turn on the LED by typing `GPIO.output(pin, GPIO.HIGH)`.

8. Wait for a few seconds to see the LED light up.

9. Turn off the LED by typing `GPIO.output(pin, GPIO.LOW)`.

10. Exit the program by typing `GPIO.cleanup()`.

By following these steps, the LED can be easily lit up through a Python program on the Raspberry Pi. It is important to make sure that the correct GPIO pin is defined and that the LED is connected properly to avoid any potential damage to the Raspberry Pi.