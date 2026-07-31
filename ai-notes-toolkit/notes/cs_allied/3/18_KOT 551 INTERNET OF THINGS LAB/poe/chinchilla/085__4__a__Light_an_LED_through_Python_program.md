#### 4. a) Light an LED through Python program

In order to light an LED through a Python program, one must follow certain steps. These steps are as follows:

1. First, connect the LED to the GPIO pin of the Raspberry Pi.

2. Once the LED is connected, import the necessary libraries in the Python program. These libraries include the RPi.GPIO library and the time library.

3. Next, set the GPIO mode to BCM or Board, depending on the type of connection.

4. Set the GPIO pin to output mode using the "GPIO.setup()" function.

5. Finally, turn on the LED using the "GPIO.output()" function.

6. To turn off the LED, use the same "GPIO.output()" function and set the value to "False".

7. It is important to note that the duration for which the LED stays on can be controlled using the time.sleep() function.

8. One can also use PWM (Pulse Width Modulation) to control the brightness of the LED. This can be achieved using the "GPIO.PWM()" function.

9. The duty cycle for the PWM can be set using the "start()" function, and the frequency can be set using the "ChangeFrequency()" function.

10. It is important to remember to clean up the GPIO pins after the program has finished running using the "GPIO.cleanup()" function.

By following these steps, one can successfully light an LED through a Python program. This is a basic but important step in learning how to control hardware using the Raspberry Pi and Python programming.