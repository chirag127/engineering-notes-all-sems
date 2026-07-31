### Ardunio Platform Boards Anatomy

- Arduino boards are the microcontroller development platform that will be at the heart of your projects .
- Arduino boards sense the environment by receiving inputs from many sensors, and affect their surroundings by controlling lights, motors, and other actuators.
- Arduino boards can be programmed from your computer using the Arduino IDE (Integrated Development Environment).
- Arduino Uno is one of the most popular and widely used Arduino boards.
- The anatomy of Arduino Uno board consists of the following components :

  - **Microcontroller**: Think of it as a tiny computer, designed to execute only a specific number of things. It is the brain of the board and it can be programmed to perform various tasks. The Arduino Uno board uses the ATmega328P microcontroller.
  - **USB port**: Used to connect the board to your computer and upload the code. It also provides power to the board.
  - **USB to Serial chip**: This is what makes it possible to program the Arduino board from your computer. It converts the USB signals to serial signals that the microcontroller can understand.
  - **Power jack**: Used to provide external power to the board. You can use a 9V battery or an AC-to-DC adapter to power the board.
  - **Voltage regulator**: Used to regulate the voltage supplied to the board and prevent damage from overvoltage or undervoltage.
  - **Reset button**: Used to restart the microcontroller and run the code from the beginning.
  - **Digital pins**: Commonly used for switches and LEDs. They can be configured as inputs or outputs and can send or receive digital signals (0 or 1). The Arduino Uno board has 14 digital pins, numbered from 0 to 13.
  - **Analog pins**: Used to read the signal from an analog sensor like the humidity sensor or temperature sensor and convert it into a digital value that can be read by the microcontroller. The Arduino Uno board has 6 analog pins, numbered from A0 to A5.
  - **PWM pins**: A subset of digital pins that can produce a Pulse Width Modulation (PWM) signal. This is a technique to vary the duty cycle of a digital signal and control the brightness of an LED or the speed of a motor. The Arduino Uno board has 6 PWM pins, marked with a tilde (~), numbered from 3 to 11.
  - **I2C pins**: A subset of analog pins that can communicate with other devices using the I2C protocol. This is a two-wire serial communication protocol that allows multiple devices to share data. The Arduino Uno board has 2 I2C pins, marked with SDA and SCL, located on A4 and A5.
  - **SPI pins**: A subset of digital pins that can communicate with other devices using the SPI protocol. This is a four-wire serial communication protocol that allows high-speed data transfer. The Arduino Uno board has 4 SPI pins, marked with SS, MOSI, MISO, and SCK, located on 10, 11, 12, and 13.
  - **LEDs**: Used to indicate the status of the board. The Arduino Uno board has 4 LEDs: power (ON), pin 13 (L), TX (transmit), and RX (receive).

- Here is a diagram of the Arduino Uno board anatomy:

![Arduino Uno Board Anatomy](https://www.arduino.cc/en/uploads/Guide/UnoAnatomy.png)