#### 4. a) Light an LED through Python program

- To light an LED through Python program, you need to have a hardware device that can control the LED, such as an Arduino, a Raspberry Pi, or a MicroPython board.
- You also need to connect the LED to the device using wires, resistors, and a breadboard, following the appropriate circuit diagram for your device.
- You need to install Python and the necessary libraries on your computer and on your device, such as pyserial, RPi.GPIO, or pyb.
- You need to write a Python program that can communicate with your device and send commands to turn the LED on and off, using the serial port, the GPIO pins, or the LED object, depending on your device.
- You need to upload the Python program to your device or run it from your computer, and observe the LED blinking according to your program logic.

Here is an example of a Python program that can light an LED connected to an Arduino board:

```python
# Import the serial library
import serial

# Create a serial object and connect to the Arduino
ser = serial.Serial('/dev/ttyACM0', 9600)

# Define a function to turn the LED on and off
def led_on_off():
    # Ask the user to enter L or H
    user_input = input("\n Type L to turn LED on or H to turn LED off :")
    # If the user enters L, send L to the Arduino
    if user_input == 'L':
        print("LED is on...")
        ser.write(b'L')
        led_on_off()
    # If the user enters H, send H to the Arduino
    elif user_input == 'H':
        print("LED is off...")
        ser.write(b'H')
        led_on_off()
    # If the user enters anything else, ask again
    else:
        print("Invalid input. Type L or H.")
        led_on_off()

# Call the function
led_on_off()
```