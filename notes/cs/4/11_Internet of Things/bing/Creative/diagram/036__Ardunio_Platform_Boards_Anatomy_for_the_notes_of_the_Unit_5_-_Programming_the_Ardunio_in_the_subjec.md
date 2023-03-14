The following diagram illustrates the basic anatomy of an Arduino platform board, using the Arduino Uno as an example. The diagram is drawn using ASCII characters, and is not to scale.

```
+------------------------+  +-----------------+
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
|                        |  |                 |
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+
|                        |  |                 |
+------------------------+  +-----------------+

```

The diagram shows the following components:

- Microcontroller: The brain of the board, which executes the code uploaded to it. The Arduino Uno uses an ATmega328P microcontroller.
- USB port: Used to connect the board to a computer, for power, programming, and serial communication.
- USB to Serial chip: A chip that translates data between the USB port and the microcontroller. The Arduino Uno uses an ATmega16U2 chip for this purpose.
- Digital pins: Pins that can be used for digital input or output, such as reading a switch or controlling an LED. Some of these pins can also be used for PWM (pulse-width modulation) output, which can simulate analog signals, such as fading an LED. These pins are marked with a ~ symbol.
- Analog pins: Pins that can be used for analog input, such as reading a sensor that produces a variable voltage. These pins can also be used for digital input or output, but they have lower current limits than the digital pins.
- 5V / 3.3V pins: Pins that provide a regulated voltage output of 5V or 3.3V, which can be used to power external components. These pins should not be used as inputs, or to power components that draw more than 50 mA of current.
- GND pins: Pins that provide a common ground reference for the board