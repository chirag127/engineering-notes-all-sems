#### 4. a) Light an LED through Python program

To light an LED through a Python program, follow these steps:

1. Connect the LED to your Raspberry Pi. The positive leg of the LED should be connected to a GPIO pin, and the negative leg should be connected to a ground pin.

2. Open the Python editor on your Raspberry Pi.

3. Import the GPIO library by typing `import RPi.GPIO as GPIO` at the top of your program.

4. Set the GPIO mode to BCM by typing `GPIO.setmode(GPIO.BCM)`.

5. Set up the GPIO pin that the LED is connected to by typing `GPIO.setup(pin, GPIO.OUT)` where `pin` is the number of the GPIO pin.

6. Turn on the LED by typing `GPIO.output(pin, GPIO.HIGH)`.

7. Wait for a specified amount of time by typing `time.sleep(seconds)` where `seconds` is the number of seconds to wait.

8. Turn off the LED by typing `GPIO.output(pin, GPIO.LOW)`.

9. Save your program and run it by typing `python your_program_name.py` in the terminal.

Congratulations, you have successfully lit an LED through a Python program!