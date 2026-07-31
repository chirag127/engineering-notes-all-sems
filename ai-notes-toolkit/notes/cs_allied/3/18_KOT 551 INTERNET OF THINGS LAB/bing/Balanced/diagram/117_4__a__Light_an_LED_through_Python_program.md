To light an LED through Python program, you need to follow these steps:

1. Connect an LED to a GPIO pin of your Raspberry Pi. You can use any pin that supports digital output, such as GPIO 17. You also need a resistor (220 ohms) to limit the current and protect the LED. The circuit diagram is shown below:

```
    +3.3V
     |
     \
     / 220 ohms
     \
     /
     |
     |    LED
     +----|>|----+
     |           |
     |           |
    GPIO 17     GND
```

2. Install the RPi.GPIO library on your Raspberry Pi. This library allows you to control the GPIO pins using Python. You can install it using the command:

```
sudo apt-get install python-rpi.gpio
```

3. Write a Python program that imports the RPi.GPIO library, sets the GPIO pin mode to BCM (Broadcom numbering scheme), sets the GPIO 17 pin as output, and turns the LED on and off in a loop. The program is shown below:

```
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # use Broadcom pin numbering
GPIO.setup(17, GPIO.OUT) # set GPIO 17 as output

while True: # loop forever
    GPIO.output(17, GPIO.HIGH) # turn LED on
    time.sleep(1) # wait for 1 second
    GPIO.output(17, GPIO.LOW) # turn LED off
    time.sleep(1) # wait for 1 second
```

4. Save the program as led.py and run it using the command:

```
python led.py
```

You should see the LED blinking on and off every second. To stop the program, press Ctrl+C. To clean up the GPIO pins, use the command:

```
GPIO.cleanup()
```