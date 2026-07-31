#### 4. a) Light an LED through Python program

Here are the steps to light an LED through a Python program:

1. Connect the LED to the Raspberry Pi's GPIO pin: First, connect the anode (positive end) of the LED to one of the GPIO pins (e.g. pin 17) on the Raspberry Pi, and connect the cathode (negative end) to a ground pin on the Raspberry Pi.

2. Open a Python program: Open a new Python program in your text editor of choice (e.g. IDLE, Thonny, etc.).

3. Import the necessary libraries: At the beginning of your Python program, import the necessary libraries to control the GPIO pins. These libraries include "RPi.GPIO" and "time".

   ```
   import RPi.GPIO as GPIO
   import time
   ```

4. Set up the GPIO pin: Set up the GPIO pin that the LED is connected to as an output pin using the GPIO "setup" method.

   ```
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(17, GPIO.OUT)
   ```

5. Turn on the LED: To turn on the LED, set the output of the GPIO pin to "HIGH" using the GPIO "output" method.

   ```
   GPIO.output(17, GPIO.HIGH)
   ```

6. Wait for a few seconds: To keep the LED on for a few seconds, use the "time" library to pause the program for a few seconds.

   ```
   time.sleep(3)
   ```

7. Turn off the LED: To turn off the LED, set the output of the GPIO pin to "LOW" using the GPIO "output" method.

   ```
   GPIO.output(17, GPIO.LOW)
   ```

8. Clean up the GPIO pins: At the end of your Python program, clean up the GPIO pins using the GPIO "cleanup" method.

   ```
   GPIO.cleanup()
   ```

9. Save and run the program: Save your Python program and run it using a terminal or command prompt. The LED should turn on for a few seconds and then turn off.

Note: Make sure to use caution when working with electronics and always follow proper safety precautions.