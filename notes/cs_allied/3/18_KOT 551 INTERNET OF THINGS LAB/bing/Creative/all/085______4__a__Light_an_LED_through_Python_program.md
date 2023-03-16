#### 4. a) Light an LED through Python program

To light an LED through Python program, you need to have the following components:

- An LED
- A resistor (220 ohms or similar)
- A breadboard
- Some jumper wires
- A microcontroller board (such as Arduino, Raspberry Pi, or MicroPython)
- A computer with Python installed and a USB cable

The steps to light an LED through Python program are:

1. Wire the LED to the microcontroller board. Connect the longer leg of the LED (the anode) to a digital pin of the board (such as pin 13 on Arduino, pin 18 on Raspberry Pi, or pin X2 on MicroPython). Connect the shorter leg of the LED (the cathode) to one end of the resistor. Connect the other end of the resistor to the ground (GND) pin of the board. Use the breadboard and the jumper wires to make the connections. See the diagrams below for reference  .

![Arduino LED wiring](https://problemsolvingwithpython.com/11-Python-and-External-Hardware/11.03-Controlling-an-LED/Arduino_LED.png)

![Raspberry Pi LED wiring](https://www.circuitbasics.com/wp-content/uploads/2016/03/Raspberry-Pi-GPIO-Layout-Revision-1.png)

![MicroPython LED wiring](https://docs.micropython.org/en/v1.9.2/pyboard/_images/leds.png)

2. Upload code to the microcontroller board. Depending on the board you are using, you need to upload a different code to the board. The code will enable the board to communicate with the computer via serial port and to control the LED pin. See the code examples below for reference  .

Arduino code:

```c
// Define the LED pin
#define LED_PIN 13

// Initialize the serial port
void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

// Read the serial input and turn the LED on or off
void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();
    if (c == 'H') {
      digitalWrite(LED_PIN, HIGH);
    }
    if (c == 'L') {
      digitalWrite(LED_PIN, LOW);
    }
  }
}
```

Raspberry Pi code:

```python
# Import the GPIO library
import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the LED pin
LED_PIN = 18

# Set the LED pin as output
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn the LED on
GPIO.output(LED_PIN, GPIO.HIGH)

# Turn the LED off
GPIO.output(LED_PIN, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()
```

MicroPython code:

```python
# Import the pyb module
import pyb

# Define the LED pin
LED_PIN = pyb.Pin('X2', pyb.Pin.OUT_PP)

# Turn the LED on
LED_PIN.high()

# Turn the LED off
LED_PIN.low()
```

3. Connect the microcontroller board to the computer. Use the USB cable to connect the board to the computer. Make sure the board is powered on and the LED is wired correctly.

4. Turn the LED on and off with Python. Depending on the board you are using, you need to use a different Python module to communicate with the board via serial port. See the code examples below for reference  .

Arduino Python code:

```python
# Import the serial module
import serial

# Create a serial object
ser = serial.Serial('/dev/ttyACM0', 9600)

# Turn the LED on
ser.write(b'H')

# Turn the LED off
ser.write(b'L')

# Close the serial connection
ser.close()
```

Raspberry Pi Python code:

```python
# Import the GPIO library
import RPi.GPIO as GPIO

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the LED pin
LED_PIN = 18

# Set the LED pin as output
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn the LED on
GPIO.output(LED_PIN, GPIO.HIGH)

# Turn the LED off
GPIO.output(LED_PIN, GPIO.LOW)

# Clean up the GPIO pins
GPIO.cleanup()