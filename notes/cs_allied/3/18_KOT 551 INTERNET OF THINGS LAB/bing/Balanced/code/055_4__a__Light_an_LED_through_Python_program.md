# 4. a) Light an LED through Python program

To light an LED through Python program, the following steps are required:

- Connect an LED to a GPIO pin of a Raspberry Pi board. The positive terminal of the LED should be connected to the GPIO pin and the negative terminal to a ground pin. A resistor should be added in series to limit the current and protect the LED from burning out. For example, the circuit diagram below shows an LED connected to GPIO 17 and a 330 ohm resistor.

```
    +3.3V
     |
     |
    | |
    | | 330 ohm
    | |
     |
     |    LED
     +---|<|---+
     |        |
     |        |
    GPIO 17  GND
```

- Install the RPi.GPIO library on the Raspberry Pi. This library provides a Python interface to control the GPIO pins. To install the library, run the following command in the terminal:

```
sudo apt-get install python-rpi.gpio
```

- Write a Python program that imports the RPi.GPIO library, sets the GPIO mode to BCM (which means the GPIO numbers are based on the Broadcom chip numbering), sets the GPIO 17 pin as an output, and turns the LED on and off with a delay. For example, the Python program below blinks the LED every second.

```
import RPi.GPIO as GPIO # Import the library
import time # Import the time module

GPIO.setmode(GPIO.BCM) # Set the GPIO mode to BCM
GPIO.setup(17, GPIO.OUT) # Set GPIO 17 as an output

while True: # Loop forever
    GPIO.output(17, GPIO.HIGH) # Turn the LED on
    time.sleep(1) # Wait for one second
    GPIO.output(17, GPIO.LOW) # Turn the LED off
    time.sleep(1) # Wait for one second
```

- Save the Python program as a file with a .py extension, such as led.py, and run it in the terminal with the following command:

```
python led.py
```

- Observe the LED blinking on and off. To stop the program, press Ctrl+C in the terminal. To clean up the GPIO pins, add the following line at the end of the program:

```
GPIO.cleanup()
```