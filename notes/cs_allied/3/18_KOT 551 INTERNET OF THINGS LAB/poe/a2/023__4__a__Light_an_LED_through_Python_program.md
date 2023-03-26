 Here is the content in formal tone without emojis or external links, written in Markdown format with points:

#### 4. a) Light an LED through Python program.

1. Import the GPIO library to access the GPIO pins of Raspberry Pi. `import RPi.GPIO as GPIO`
2. Set the GPIO numbering mode to BCM. `GPIO.setmode(GPIO.BCM)`
3. Set the pin number where the LED is connected as output pin. `GPIO.setup(18, GPIO.OUT)`
4. Write `GPIO.output(18, GPIO.HIGH)` to turn on the LED.
5. Write `GPIO.output(18, GPIO.LOW)` to turn off the LED.
6. Release the pins by writing `GPIO.cleanup()` at the end of the program.

The above Python program will light the LED connected to pin number 18 of the Raspberry Pi when run. The LED will remain on until the program is run again with GPIO.output(18, GPIO.LOW) or the program is ended or the Raspberry Pi is turned off.