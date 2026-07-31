#### Light an LED through Python program

To light an LED through a Python program, follow these steps:

1. Connect the LED to the GPIO pin of the Raspberry Pi.
2. Open the Python IDE on the Raspberry Pi.
3. Import the RPi.GPIO library using the following command:

   ```
   import RPi.GPIO as GPIO
   ```

4. Set the mode of the GPIO pins to BCM or BOARD using the following command:

   ```
   GPIO.setmode(GPIO.BCM) # or GPIO.setmode(GPIO.BOARD)
   ```

5. Set the pin number to which the LED is connected as an output pin using the following command:

   ```
   GPIO.setup(pin_number, GPIO.OUT)
   ```

   Replace `pin_number` with the actual pin number to which the LED is connected.

6. Turn on the LED by setting the output of the pin to HIGH using the following command:

   ```
   GPIO.output(pin_number, GPIO.HIGH)
   ```

7. Turn off the LED by setting the output of the pin to LOW using the following command:

   ```
   GPIO.output(pin_number, GPIO.LOW)
   ```

8. To keep the LED on for a certain amount of time, use the `sleep()` function from the `time` module as follows:

   ```
   import time
   
   GPIO.output(pin_number, GPIO.HIGH)
   time.sleep(5) # the LED will be on for 5 seconds
   GPIO.output(pin_number, GPIO.LOW)
   ```

Remember to always use a resistor in series with the LED to limit the current flowing through it and avoid damaging the LED.

By following these steps, you can successfully light an LED through a Python program on a Raspberry Pi.