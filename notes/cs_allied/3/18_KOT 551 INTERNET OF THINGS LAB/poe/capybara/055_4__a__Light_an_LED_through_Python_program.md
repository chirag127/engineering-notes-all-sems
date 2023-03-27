#### 4. a) Light an LED through Python program

To light an LED through a Python program, you need to follow the steps mentioned below:

1. First, you need to connect the LED to your Raspberry Pi or any other microcontroller board that you are using. Connect the positive leg of the LED to the GPIO pin that you want to use and connect the negative leg of the LED to a ground pin.

2. Next, you need to write a Python program that will control the GPIO pin to which the LED is connected. You can use the RPi.GPIO library in Python to do this.

3. Import the RPi.GPIO library in your Python program using the following command:

   ```python
   import RPi.GPIO as GPIO
   ```

4. Set up the GPIO pin that you want to use as an output pin using the following command:

   ```python
   GPIO.setup(pin, GPIO.OUT)
   ```

   Replace 'pin' with the GPIO pin number that you want to use.

5. Turn on the LED by setting the output of the GPIO pin to high using the following command:

   ```python
   GPIO.output(pin, GPIO.HIGH)
   ```

6. To turn off the LED, set the output of the GPIO pin to low using the following command:

   ```python
   GPIO.output(pin, GPIO.LOW)
   ```

7. Finally, you can clean up the GPIO pins using the following command:

   ```python
   GPIO.cleanup()
   ```

   This command will reset all the GPIO pins that you have used in your program.

Using these steps, you can easily light an LED through a Python program. Make sure you have connected the LED to the correct GPIO pin and ground pin to avoid any damage to your microcontroller board.