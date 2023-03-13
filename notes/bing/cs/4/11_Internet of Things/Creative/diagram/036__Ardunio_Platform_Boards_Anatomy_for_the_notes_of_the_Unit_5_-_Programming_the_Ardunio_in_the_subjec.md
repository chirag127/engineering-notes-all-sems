The following diagram illustrates the basic anatomy of an Arduino Uno board, which is a microcontroller development platform that can sense the environment by receiving inputs from many sensors, and affect their surroundings by controlling lights, motors, and other actuators  .

```
+---------------------+  +-----------------+
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
|                     |  |                 |
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+
|                     |  |                 |
+---------------------+  +-----------------+

```

The diagram shows the following components of the Arduino Uno board  :

- **Power jack**: This is where you can plug in a power supply to power the board. The board can accept voltages from 7V to 20V, but the recommended range is 7V to 12V.
- **USB connector**: This is where you can connect the board to a computer or a power source using a USB cable. The board can also communicate with the computer via serial communication through this port.
- **Reset button**: This is a push button that can reset the board and restart the program that is running on it.
- **Power LED**: This is a green LED that indicates that the board is powered on.
- **TX and RX LEDs**: These are yellow LEDs that blink when the board is sending or receiving data through the USB connector or the serial pins (0 and 1).
- **Digital pins**: These are 14 pins that can be used as digital input or output. They can read or write values of either HIGH (5V) or LOW (0V). Some of these pins have special functions, such as PWM (pulse-width modulation), interrupt, or SPI (serial peripheral interface) communication.
- **Analog pins**: These are 6 pins that can be used as analog input. They can read values from 0 to 1023