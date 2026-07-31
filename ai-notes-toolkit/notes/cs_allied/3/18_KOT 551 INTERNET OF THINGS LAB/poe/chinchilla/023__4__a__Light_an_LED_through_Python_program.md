#### 4. a) Light an LED through Python program

To light an LED through a Python program, you can follow these steps:

1. Connect the LED to your computer using a breadboard and a resistor. Connect the positive leg of the LED to a pin on the breadboard and then connect the resistor to the same row. Connect the other end of the resistor to a ground pin on the breadboard.

2. Open a new Python file in your preferred text editor.

3. Import the RPi.GPIO library by adding the following line to the top of your Python file:
```python
import RPi.GPIO as GPIO
```

4. Set the numbering system for the GPIO pins by adding the following line next:
```python
GPIO.setmode(GPIO.BOARD)
```

5. Set up the pin you connected the LED to as an output pin by adding the following line:
```python
GPIO.setup(pin_number, GPIO.OUT)
```
Replace `pin_number` with the actual pin number you connected the LED to.

6. Turn on the LED by adding the following line:
```python
GPIO.output(pin_number, GPIO.HIGH)
```

7. To turn off the LED, add the following line:
```python
GPIO.output(pin_number, GPIO.LOW)
```

8. Save the Python file and run it using the following command:
```python
sudo python filename.py
```
Replace `filename.py` with the name you gave your Python file.

By following these steps, you should be able to light an LED through a Python program on your Raspberry Pi. Remember to always use caution when working with electronics and to double-check your connections before powering on your Raspberry Pi.