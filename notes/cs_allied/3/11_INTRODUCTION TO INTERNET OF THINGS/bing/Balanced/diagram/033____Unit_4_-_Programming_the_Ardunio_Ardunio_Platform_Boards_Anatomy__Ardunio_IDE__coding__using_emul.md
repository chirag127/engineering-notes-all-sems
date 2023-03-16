## Unit 4 - Programming the Arduino

### Arduino Platform Boards Anatomy

- Arduino boards are the microcontroller development platform that will be at the heart of your projects  .
- Arduino boards sense the environment by receiving inputs from many sensors, and affect their surroundings by controlling lights, motors, and other actuators  .
- Arduino boards have different models, such as Uno, Nano, Mega, etc. Each model has different features and specifications, but they share some common components and functionalities.
- Here is the anatomy of Arduino Uno, one of the most popular and widely used Arduino boards   :

![Arduino Uno Board Anatomy](https://wiki-content.arduino.cc/en/Guide/BoardAnatomy/ArduinoUnoBoardAnatomy.png)

- The main components of Arduino Uno are   :
  - **Power jack**: This is where you can plug a 9V external power supply to power the board.
  - **USB connector**: This is where you can connect the board to your computer via a USB cable. You can use this connection to upload sketches (programs) to the board, or to communicate with the board via serial monitor or serial plotter.
  - **Voltage regulator**: This regulates the voltage from the external power supply or the USB connection to the appropriate level for the board and its components.
  - **ATmega328P microcontroller**: This is the brain of the board. It is a 8-bit microcontroller that runs at 16 MHz and has 32 KB of flash memory, 2 KB of SRAM, and 1 KB of EEPROM. It also has 23 input/output pins, 6 of which can be used as analog inputs, and 6 of which can be used as PWM outputs.
  - **Reset button**: This allows you to reset the board and restart the sketch.
  - **Power LED**: This indicates that the board is powered on.
  - **TX and RX LEDs**: These indicate the data transmission and reception between the board and the computer via the USB connection.
  - **Digital pins**: These are the pins that can be used as digital input or output. They can be set to HIGH (5V) or LOW (0V) states, and can read or write digital signals. Some of these pins have special functions, such as PWM, interrupts, serial communication, SPI, I2C, etc.
  - **Analog pins**: These are the pins that can be used as analog input. They can read analog signals ranging from 0V to 5V, and convert them to digital values ranging from 0 to 1023 using a 10-bit analog-to-digital converter (ADC).
  - **AREF pin**: This is the analog reference pin. It can be used to set the reference voltage for the analog inputs, instead of the default 5V.
  - **GND pins**: These are the ground pins. They provide a common ground for the board and its components.
  - **Vin pin**: This is the input voltage pin. It can be used to supply an external voltage to the board, instead of the power jack or the USB connection.
  - **5V pin**: This is the regulated 5V output pin. It can be used to power other components that require 5V.
  - **3.3V pin**: This is the regulated 3.3V output pin. It can be used to power other components that require 3.3V.
  - **ICSP header**: This is the in-circuit serial programming header. It can be used to program the board using an external programmer, instead of the USB connection.