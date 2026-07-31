#### 4. a) Light an LED through Python program

To light an LED through Python program, you need to have the following components:

- An LED
- A resistor (220 ohms or similar)
- A breadboard
- Some jumper wires
- A microcontroller board (such as Arduino, Raspberry Pi, or MicroPython)
- A computer with Python installed and a USB cable to connect to the microcontroller board

The steps to light an LED through Python program are:

1. Wire the LED to the microcontroller board. Connect the longer leg of the LED (the anode) to a digital pin of the board (such as pin 13 on Arduino, pin 18 on Raspberry Pi, or pin X2 on MicroPython). Connect the shorter leg of the LED (the cathode) to one end of the resistor. Connect the other end of the resistor to the ground (GND) pin of the board. Use the breadboard and the jumper wires to make the connections.
2. Write a Python program to control the LED. The program should use a library that can communicate with the microcontroller board (such as pyserial for Arduino, RPi.GPIO for Raspberry Pi, or pyb for MicroPython). The program should set the digital pin as an output and use a loop to turn the LED on and off with a delay. For example, the following code can be used for Arduino:

```python
import serial
import time

# create a serial object to communicate with Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# set pin 13 as output
ser.write(b'13,1\n')

# loop to blink the LED
while True:
    # turn the LED on
    ser.write(b'13,2\n')
    # wait for one second
    time.sleep(1)
    # turn the LED off
    ser.write(b'13,3\n')
    # wait for one second
    time.sleep(1)
```

3. Upload the Python program to the microcontroller board. Depending on the board, you may need to use a different method to upload the program. For Arduino, you can use the Arduino IDE to upload a sketch that can receive serial commands from Python. For Raspberry Pi, you can use SSH or VNC to access the board and run the Python program. For MicroPython, you can use a tool like rshell or ampy to copy the Python program to the board and run it.
4. Observe the LED blinking on and off. You should see the LED turning on and off once every second. You can change the delay time or the pin number in the Python program to modify the behavior of the LED.