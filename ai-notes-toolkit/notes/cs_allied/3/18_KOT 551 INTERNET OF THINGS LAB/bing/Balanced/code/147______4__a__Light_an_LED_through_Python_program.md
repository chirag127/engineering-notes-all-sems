#### 4. a) Light an LED through Python program

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
    GND

    LED-
    |
    R
    |
    GND
```

2. Import the GPIO library and the time library in Python:

```python
import RPi.GPIO as GPIO
import time
```

3. Set the GPIO mode to BCM and the pin 18 as output:

```python
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
```

4. Turn on the LED by setting the pin 18 to high and wait for one second:

```python
GPIO.output(18, GPIO.HIGH)
time.sleep(1)
```

5. Turn off the LED by setting the pin 18 to low and wait for one second:

```python
GPIO.output(18, GPIO.LOW)
time.sleep(1)
```

6. Repeat steps 4 and 5 for as many times as you want to blink the LED.

7. Clean up the GPIO pins and exit the program:

```python
GPIO.cleanup()
```

This is how you can light an LED through Python program.