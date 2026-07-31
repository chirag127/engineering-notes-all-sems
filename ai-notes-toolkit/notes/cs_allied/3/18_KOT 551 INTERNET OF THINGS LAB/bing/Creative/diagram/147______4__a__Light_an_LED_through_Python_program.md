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
2. Write a Python program to control the LED. The program should use a library that can communicate with the microcontroller board (such as pyserial for Arduino, RPi.GPIO for Raspberry Pi, or pyb for MicroPython). The program should set the digital pin as an output and use a loop to turn the LED on and off with a delay. For example, the following code can blink an LED connected to pin 13 on Arduino:

```python
import serial
import time

# create a serial object to communicate with Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# loop forever
while True:
    # send 'H' to turn the LED on
    ser.write(b'H')
    # wait for one second
    time.sleep(1)
    # send 'L' to turn the LED off
    ser.write(b'L')
    # wait for one second
    time.sleep(1)
```

3. Upload the Python program to the microcontroller board. Depending on the board, you may need to use different methods to upload the program. For Arduino, you can use the Arduino IDE to upload the program to the board. For Raspberry Pi, you can use SSH or VNC to transfer the program to the board. For MicroPython, you can use a tool like rshell or ampy to copy the program to the board.
4. Run the Python program and observe the LED. You can use the terminal or the Python shell to run the program. You should see the LED blinking on and off according to the program. You can modify the program to change the pin number, the delay time, or the logic of the LED control.