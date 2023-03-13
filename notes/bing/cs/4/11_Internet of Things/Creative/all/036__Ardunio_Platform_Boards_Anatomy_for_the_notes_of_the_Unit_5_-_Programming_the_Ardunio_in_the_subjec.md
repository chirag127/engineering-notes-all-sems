### Arduino Platform Boards Anatomy for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

- Arduino boards are the microcontroller development platform that will be at the heart of your IoT projects. They can sense the environment by receiving inputs from many sensors, and affect their surroundings by controlling lights, motors, and other actuators  .
- Arduino Uno is one of the most popular and widely used Arduino boards. It is based on the ATmega328P microcontroller, which has 32 KB of flash memory, 2 KB of SRAM, and 1 KB of EEPROM.
- Arduino Uno board has the following main components and features   :

  - **Power jack**: This is where you can connect an external power source, such as a battery or an AC-DC adapter. The board can operate on an external supply of 6 to 20 volts, but the recommended range is 7 to 12 volts.
  - **USB connector**: This is where you can connect the board to your computer via a USB cable. You can use this connection to upload sketches (programs) to the board, or to communicate with the board using serial communication protocols.
  - **Reset button**: This is a small button that you can press to reset the board. This will restart the sketch that is currently running on the board.
  - **Digital pins**: These are 14 pins that can be used as digital input or output. They are labeled from 0 to 13. Some of these pins have special functions, such as PWM (pulse-width modulation), serial communication, or interrupt capabilities.
  - **Analog pins**: These are 6 pins that can be used as analog input. They are labeled from A0 to A5. They can measure analog voltages from 0 to 5 volts, and convert them to digital values from 0 to 1023 using a 10-bit analog-to-digital converter (ADC).
  - **Power pins**: These are pins that provide power to the board or to other components. They include 3.3V, 5V, GND (ground), and VIN (input voltage) pins.
  - **ICSP header**: This is a 6-pin header that can be used to program the board using an external programmer, such as another Arduino board or an AVR ISP.
  - **LEDs**: These are small lights that indicate the status of the board or the sketch. There are four LEDs on the board: power (green), TX (yellow), RX (yellow), and pin 13 (orange). The power LED shows that the board is receiving power. The TX and RX LEDs blink when data is being transmitted or received via the USB connection. The pin 13 LED is connected to the digital pin 13, and can be controlled by the sketch.
  - **Crystal oscillator**: This is a small device that provides a stable clock signal to the microcontroller. The Arduino Uno board uses a 16 MHz ceramic resonator.

- Here is an ASCII diagram of the Arduino Uno board:

```
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
|                        |
+------------------------+
|                        |
|                        |
|