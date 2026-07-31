 Here is the content in markdown format without any emojis or external links:

#### 4. a) Light an LED through Python program.

- Import the GPIO library to control the GPIO pins of Raspberry Pi.
- Define the pin number where the LED is connected. For example, pin 18.
- Set the pin as output pin using GPIO.setup() function.
- Use GPIO.output() function to switch on the LED. Pass GPIO.HIGH as argument.
- Use time.sleep() function to keep the LED on for some time. Pass the time in seconds as argument.
- Again use GPIO.output() function to switch off the LED. Pass GPIO.LOW as argument.
- Release the GPIO pin using GPIO.cleanup() function.

This is a basic Python program to light an LED connected to Raspberry Pi. The program imports the GPIO library and defines the GPIO pin number to which the LED is connected. The pin is set as output and switched on using GPIO.output(). The LED is kept on for some time using time.sleep(). After that, the LED is switched off and the GPIO pin is released.

The content is written in points and in a formal tone without any feelings or friendliness as emojis or external links are avoided. The content is written as if it is a study material to read and learn from for exams. Please let me know if you would like me to modify or add anything in the content.