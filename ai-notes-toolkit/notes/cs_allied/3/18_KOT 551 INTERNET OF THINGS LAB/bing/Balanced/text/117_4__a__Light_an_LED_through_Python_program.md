# 4. a) Light an LED through Python program

- To light an LED through Python program, you need to have a Raspberry Pi, an LED, a breadboard, a resistor, and some jumper wires.
- You also need to install the RPi.GPIO library on your Raspberry Pi, which allows you to control the GPIO pins using Python.
- The GPIO pins are the physical pins on the Raspberry Pi that can be used to connect and communicate with external devices, such as LEDs, buttons, sensors, etc.
- The LED has two legs, one longer and one shorter. The longer leg is the positive (+) side and the shorter leg is the negative (-) side.
- The resistor is used to limit the current flowing through the LED, to prevent it from burning out. The resistor value can vary depending on the LED, but a common value is 330 ohms.
- The breadboard is a board with holes that allow you to connect components without soldering. The holes are connected in rows and columns, as shown in the diagram below.

![breadboard diagram](https://www.raspberrypi.org/documentation/usage/gpio/images/gpio-pins-pi2.jpg)

- The jumper wires are used to connect the components on the breadboard to the GPIO pins on the Raspberry Pi.
- To light an LED through Python program, you need to follow these steps:

  1. Connect the longer leg of the LED to one end of the resistor, and the other end of the resistor to a GPIO pin on the Raspberry Pi. For example, you can use GPIO pin 18, which is also known as BCM 18 or physical pin 12.
  2. Connect the shorter leg of the LED to the ground (GND) pin on the Raspberry Pi. For example, you can use physical pin 6, which is next to pin 12.
  3. Open a text editor on your Raspberry Pi and write the following Python code:

```python
# Import the RPi.GPIO library
import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin 18 as output
GPIO.setup(18, GPIO.OUT)

# Turn on the LED by setting the pin to high
GPIO.output(18, GPIO.HIGH)
```

  4. Save the file as led.py and run it in the terminal using the command:

```bash
python led.py
```

  5. You should see the LED light up. To turn off the LED, press Ctrl+C in the terminal to stop the program, or change the last line of the code to:

```python
GPIO.output(18, GPIO.LOW)
```

  6. To clean up the GPIO pins and release the resources, you can add the following line at the end of the code:

```python
GPIO.cleanup()
```

- This is how you can light an LED through Python program. You can also try to control the LED using a button, a potentiometer, or a sensor, by connecting them to other GPIO pins and modifying the code accordingly.