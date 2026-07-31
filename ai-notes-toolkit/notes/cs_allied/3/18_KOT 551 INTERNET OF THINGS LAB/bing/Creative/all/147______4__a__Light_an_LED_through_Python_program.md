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
2. Write a Python program to control the LED. Depending on the board you are using, you may need to import different modules or libraries to access the digital pins. For example, on Arduino, you can use the pyserial module to communicate with the board via serial port. On Raspberry Pi, you can use the RPi.GPIO module to control the GPIO pins. On MicroPython, you can use the pyb module to access the board features. The basic logic of the program is to set the pin connected to the LED as an output, and then use a loop to turn the pin on and off with a delay. For example, on Arduino, you can write something like this:

```python
import serial
import time

# create a serial object to communicate with Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# set pin 13 as output
ser.write(b'13,1,o\n')

# loop forever
while True:
    # turn pin 13 on
    ser.write(b'13,1,1\n')
    # wait for 1 second
    time.sleep(1)
    # turn pin 13 off
    ser.write(b'13,1,0\n')
    # wait for 1 second
    time.sleep(1)
```

3. Run the Python program on the computer. Depending on the board you are using, you may need to upload some code to the board first, or connect the board to the computer via USB cable or WiFi. For example, on Arduino, you need to upload a sketch called StandardFirmata to the board using the Arduino IDE. On Raspberry Pi, you need to connect the board to the computer via SSH or VNC. On MicroPython, you need to connect the board to the computer via USB cable and use a terminal program such as PuTTY or screen. Once the board is ready, you can run the Python program on the computer using the command line or an IDE such as IDLE. You should see the LED blinking on and off once every second.