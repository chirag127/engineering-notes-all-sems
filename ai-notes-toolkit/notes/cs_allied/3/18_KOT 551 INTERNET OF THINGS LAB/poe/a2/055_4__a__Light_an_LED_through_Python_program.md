 Here is the formal content in Markdown format without any emojis or external links for the given topic:

# 4. a) Light an LED through Python program

## Introduction
- An LED (Light Emitting Diode) is a semiconductor light source.
- LEDs are increasingly being used for lighting applications due to their high efficiency and long operational life.
- In this section, we will learn how to light up an LED through a Python program by controlling the GPIO pins of a Raspberry Pi.

## Prerequisites
- Raspberry Pi board
- LED
- 330 ohm resistor
- Jumper wires

## Connections
- Connect the positive leg (longer leg) of the LED to GPIO pin 17 of the Raspberry Pi through a 330 ohm resistor.
- Connect the negative leg (shorter leg) of the LED to the ground pin (GND) of the Raspberry Pi.

## Python Program
```
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

GPIO.output(17, GPIO.HIGH)
```

## Explanation
- First, we import the RPi.GPIO library to control the GPIO pins.
- Then, we set the GPIO numbering mode to BCM.
- Next, we set GPIO pin 17 as an output pin.
- Finally, we set GPIO pin 17 to HIGH which lights up the LED.
- The LED will remain ON until the program is terminated.

## Additional Notes
- For the LED to turn OFF, set GPIO pin 17 to LOW in the last line of the program.
- The resistor is used to limit the current flow through the LED and protect it from damage.