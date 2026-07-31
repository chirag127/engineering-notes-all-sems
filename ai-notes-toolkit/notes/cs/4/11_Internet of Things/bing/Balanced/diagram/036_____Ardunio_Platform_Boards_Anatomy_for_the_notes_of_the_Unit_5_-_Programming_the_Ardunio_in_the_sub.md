### Ardunio Platform Boards Anatomy

Arduino boards are the microcontroller development platform that will be at the heart of your projects. When making something you will be building the circuits and interfaces for interaction, and telling the microcontroller how to interface with other components. Here the anatomy of Arduino Uno .

![Arduino Uno Board Anatomy](https://wiki-content.arduino.cc/assets/Guide/BoardAnatomy/ArduinoUnoBoardAnatomy.png)

The main components of an Arduino Uno board are:

- **Microcontroller**: Think of it as a tiny computer, designed to execute only a specific number of things. It is the brain of the board and it can be programmed using the Arduino IDE. The Arduino Uno uses an ATmega328P microcontroller .
- **USB port**: Used to connect the board to your computer and upload the code. It can also provide power to the board and communicate with the microcontroller via serial communication.
- **USB to Serial chip**: This is what makes it possible to program the Arduino board from your computer. It converts the USB signals to serial signals that the microcontroller can understand.
- **Digital pins**: Commonly used for switches and LEDs. They can be configured as inputs or outputs and can send or receive digital signals (0 or 1). Some of them can also perform special functions, such as PWM (Pulse Width Modulation), interrupts, or serial communication .
- **Analog pins**: Used to read the signal from an analog sensor like the humidity sensor or temperature sensor and convert it into a digital value that can be read by the microcontroller. They can also be used as digital pins .
- **Power pins**: Used to provide power to the board and other components. They include 5V, 3.3V, GND (ground), and VIN (voltage input) pins .
- **Reset button**: Used to restart the microcontroller and run the code from the beginning.
- **Power LED**: Indicates that the board is receiving power.
- **TX and RX LEDs**: Indicate the transmission and reception of serial data.
- **L LED**: Connected to digital pin 13 and can be used to test the board or as a status indicator.
- **ICSP header**: Used to program the microcontroller directly using an external programmer.
- **Voltage regulator**: Used to regulate the voltage input to the board and ensure a stable 5V supply to the microcontroller and other components.