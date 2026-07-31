#### 4. a) Light an LED through Python program

To light an LED through Python program, you need the following components and steps:

- A Raspberry Pi board with GPIO pins and a power supply
- An LED and a resistor (220 ohms or more)
- A breadboard and jumper wires
- A Python editor or IDE (such as Thonny or IDLE)
- A library to control the GPIO pins (such as RPi.GPIO or gpiozero)

The steps are:

1. Connect the LED and the resistor in series on the breadboard. The longer leg of the LED (the anode) should be connected to the resistor, and the shorter leg (the cathode) should be connected to the ground (GND) pin of the Raspberry Pi.
2. Connect the other end of the resistor to any GPIO pin of the Raspberry Pi. Note the number of the pin, as you will need it in the Python code. For example, you can use pin 18, which is GPIO 24.
3. Open a Python editor or IDE and create a new file. Import the GPIO library and set the mode to BCM, which means the pin numbers are based on the Broadcom chip. For example, you can use the following code:

```python
import RPi.GPIO as GPIO # import the library
GPIO.setmode(GPIO.BCM) # set the mode to BCM
```

4. Set the pin you connected to the LED as an output pin and turn it on. For example, you can use the following code:

```python
LED_PIN = 24 # the pin number of the LED
GPIO.setup(LED_PIN, GPIO.OUT) # set the pin as an output
GPIO.output(LED_PIN, GPIO.HIGH) # turn on the LED
```

5. Save and run the Python file. You should see the LED light up.
6. To turn off the LED, you can either change the GPIO.HIGH to GPIO.LOW in the code, or use the GPIO.cleanup() function to reset the pins to their default state. For example, you can use the following code:

```python
GPIO.output(LED_PIN, GPIO.LOW) # turn off the LED
GPIO.cleanup() # reset the pins
```

7. Experiment with different GPIO pins, LED colors, and resistor values. You can also use a loop or a button to control the LED. For more information and examples, you can refer to the official documentation of the GPIO library: https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/