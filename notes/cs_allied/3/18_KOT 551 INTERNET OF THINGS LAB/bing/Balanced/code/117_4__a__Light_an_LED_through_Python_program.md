# 4. a) Light an LED through Python program

To light an LED through Python program, you need the following components:

- A Raspberry Pi board with GPIO pins
- An LED
- A resistor (220 ohms)
- Breadboard and jumper wires
- Python 3 installed on the Raspberry Pi

The steps to light an LED through Python program are:

1. Connect the LED to the GPIO pin 18 of the Raspberry Pi and the resistor to the ground pin using the breadboard and jumper wires. The circuit diagram is shown below:

```
    +3.3V  +5V
 1  2
 3  4
 5  6
 7  8
 9  10
11  12
13  14
15  16
17  18  LED+
19  20
21  22
23  24
25  26
27  28
29  30
31  32
33  34
35  36
37  38
39  40
    GND  Resistor  LED-
```

2. Open a terminal on the Raspberry Pi and create a new Python file called led.py using the command:

```
nano led.py
```

3. In the led.py file, import the GPIO library and set the pin 18 as output using the following code:

```
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
```

4. To turn on the LED, write the following code:

```
GPIO.output(18, GPIO.HIGH)
```

5. To turn off the LED, write the following code:

```
GPIO.output(18, GPIO.LOW)
```

6. To blink the LED, write a loop that alternates between turning on and off the LED with a delay of one second using the following code:

```
import time
while True:
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)
    time.sleep(1)
```

7. Save and exit the file using Ctrl+X, Y, and Enter.

8. Run the Python program using the command:

```
python3 led.py
```

9. You should see the LED light up or blink depending on the code you wrote.

10. To stop the program, press Ctrl+C. To clean up the GPIO pins, write the following code at the end of the file:

```
GPIO.cleanup()
```