#### 4. a) Light an LED through Python program

To light an LED through a Python program, follow these steps:

1. Connect the LED to a GPIO pin on your Raspberry Pi.
2. Open a new Python file in your preferred text editor.
3. Import the necessary libraries by adding the following lines of code at the beginning of your file:

   ```
   import RPi.GPIO as GPIO
   import time
   ```

4. Set up the GPIO pin by specifying the pin number and mode. For example, to use pin 17, add the following code:

   ```
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(17, GPIO.OUT)
   ```

5. Use a loop to turn the LED on and off. For example, to blink the LED 10 times, add the following code:

   ```
   for i in range(10):
       GPIO.output(17, GPIO.HIGH)
       time.sleep(1)
       GPIO.output(17, GPIO.LOW)
       time.sleep(1)
   ```

6. Run the program by saving the file and executing it from the command line:

   ```
   python filename.py
   ```

Congratulations, you have successfully lit an LED through a Python program!