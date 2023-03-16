#### 4. a) Light an LED through Python program

To light an LED through Python program, you need to have the following components:

- An LED
- A resistor (220 ohms or similar)
- A breadboard
- Jumper wires
- A microcontroller board (such as Arduino, Raspberry Pi, or MicroPython)
- A computer with Python installed

The steps to light an LED through Python program are:

1. Wire the LED to the microcontroller board. Connect the longer leg of the LED (the anode) to a digital pin of the board (such as pin 13 on Arduino, pin 18 on Raspberry Pi, or pin X2 on MicroPython). Connect the shorter leg of the LED (the cathode) to one end of the resistor. Connect the other end of the resistor to the ground (GND) pin of the board. Use the breadboard and jumper wires to make the connections.
2. Write a Python program to control the LED. The program should use a library that can communicate with the microcontroller board (such as pyserial for Arduino, RPi.GPIO for Raspberry Pi, or pyb for MicroPython). The program should set the digital pin as an output, and use a loop to turn the LED on and off with a delay. For example, the following code can blink an LED on Arduino:

```python
import serial
import time

# create a serial object to communicate with Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# set pin 13 as an output
ser.write(b'13,1,o\n')

# loop forever
while True:
    # turn the LED on
    ser.write(b'13,1,1\n')
    # wait for one second
    time.sleep(1)
    # turn the LED off
    ser.write(b'13,1,0\n')
    # wait for one second
    time.sleep(1)
```

3. Run the Python program on the computer. Make sure the microcontroller board is connected to the computer via USB cable. Use the terminal or an IDE to run the Python program. You should see the LED blinking on and off once every second.