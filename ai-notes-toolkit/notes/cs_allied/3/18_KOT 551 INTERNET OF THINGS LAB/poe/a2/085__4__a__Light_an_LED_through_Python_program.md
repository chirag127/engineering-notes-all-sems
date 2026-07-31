 Here is the content in markdown format without any emojis or external links, written in a formal tone with points:

#### 4. a) Light an LED through Python program.

1. Import the GPIO library to control the GPIO pins of Raspberry Pi.
2. Define the pin numbering mode as BCM. This refers to the chip pin numbers of the Broadcom SoC used in the Raspberry Pi.
3. Define the pin number to which the LED is connected. For example, pin number 18. This will be the output pin.
4. Use the GPIO.setup() function to set pin 18 as an output pin.
5. Use the GPIO.output() function to send a high signal to pin 18. This will light up the LED.
6. Include the time module and use time.sleep() function to specify how long the LED should remain lit. For example, to keep the LED lit for 2 seconds, use time.sleep(2).
7. Again use the GPIO.output() function to send a low signal to pin 18. This will turn off the LED.
8. Use the GPIO.cleanup() function to reset all GPIO pins and free up the resources.

The above steps will execute a Python program to light an LED connected to a Raspberry Pi for a specified period of time and then turn it off. By modifying the time period in step 6, the duration for which the LED remains lit can be changed.