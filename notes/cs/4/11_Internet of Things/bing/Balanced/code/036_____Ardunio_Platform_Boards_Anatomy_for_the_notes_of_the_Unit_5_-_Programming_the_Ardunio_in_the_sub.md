### Arduino Platform Boards Anatomy

Arduino boards are the microcontroller development platform that will be at the heart of your projects. When making something you will be building the circuits and interfaces for interaction, and telling the microcontroller how to interface with other components. Here the anatomy of Arduino Uno  , which is one of the most popular Arduino boards.

- **Power LED indicator**: This LED lights up when the board is powered on. It is connected to the 5V pin and can be used to check if the board is receiving power.
- **Digital I/O pins**: These pins can be used as either input or output pins. They can read or write digital values of either HIGH or LOW. Some of these pins have special functions, such as PWM, serial communication, or external interrupts.
- **TX and RX LEDs**: These LEDs indicate the serial data transmission and reception between the board and the computer or other devices. They blink when data is being transferred.
- **Main IC**: This is the microcontroller chip that runs your code. It is an ATmega328P, which has 32 KB of flash memory, 2 KB of SRAM, and 1 KB of EEPROM. It also has an internal oscillator that runs at 16 MHz.
- **Voltage regulator**: This component regulates the input voltage to a stable 5V that the board needs. It can accept an input voltage of 7-12V from the power jack or the Vin pin.
- **Power jack**: This is where you can plug in an external power source, such as a battery or an AC adapter. The recommended voltage range is 7-12V.
- **USB connector**: This is where you can connect the board to your computer using a USB cable. You can use this connection to upload code, communicate with the serial monitor, or power the board.
- **Reset button**: This button resets the board and restarts your code. You can use it to troubleshoot your code or to enter the bootloader mode for uploading code.
- **Analog input pins**: These pins can read analog values from 0 to 5V. They have a 10-bit resolution, which means they can distinguish 1024 different levels. You can use these pins to connect sensors that output analog signals, such as potentiometers, light sensors, or temperature sensors.
- **ICSP header**: This is a set of pins that can be used to program the board using an external programmer, such as another Arduino board or an AVR ISP. You can use this header to burn the bootloader or upload code without using the USB connection.
- **3.3V pin**: This pin provides a regulated 3.3V output that can be used to power some sensors or modules that require a lower voltage than 5V.
- **5V pin**: This pin provides a regulated 5V output that can be used to power some sensors or modules that require 5V. It is connected to the output of the voltage regulator or the USB connector, depending on the power source.
- **GND pins**: These pins provide a common ground connection for the board and the components. You need to connect one of these pins to the negative terminal of your power source or the ground of your circuit.
- **AREF pin**: This pin can be used to set the reference voltage for the analog input pins. By default, the reference voltage is 5V, but you can change it by using the analogReference() function in your code. You can use this pin to connect an external reference voltage, such as a precision voltage source or a potentiometer.