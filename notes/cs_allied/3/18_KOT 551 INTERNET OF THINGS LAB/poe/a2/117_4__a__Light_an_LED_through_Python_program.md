 Here is the formal content written in Markdown format without any emojis or external links inside Header 4 as instructed:

#### 4. a) Light an LED through Python program

1. Import the GPIO library to access the GPIO pins of Raspberry Pi.
2. Set up the GPIO pin as an output, where the LED is connected. For example, GPIO17.
3. Set the GPIO pin to high state using GPIO.output(17,GPIO.HIGH) to light up the LED.
4. Set the GPIO pin to low state using GPIO.output(17,GPIO.LOW) to turn off the LED.
5. Release the GPIO pins using GPIO.cleanup() before exiting the program.

The Python program to light an LED connected to GPIO17 is as follows:

import GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH) # LED ON
GPIO.output(17, GPIO.LOW) # LED OFF
GPIO.cleanup()

The content focuses on the steps and code to light an LED through a Python program for a Raspberry Pi without any external stylistic elements as instructed. Please let me know if you would like me to modify or expand the content in any way.