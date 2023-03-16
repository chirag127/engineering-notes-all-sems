# Unit 4 - Programming the Arduino

## Arduino Platform Boards Anatomy

- Arduino boards are the microcontroller development platform that will be at the heart of your projects. They sense the environment by receiving inputs from many sensors, and affect their surroundings by controlling lights, motors, and other actuators  .
- Arduino Uno is one of the most popular Arduino boards. It is based on the ATmega328P microcontroller, which has 32 KB of flash memory, 2 KB of SRAM, and 1 KB of EEPROM.
- Arduino Uno has 14 digital input/output pins, of which 6 can be used as PWM outputs, 6 analog inputs, a 16 MHz ceramic resonator, a USB connection, a power jack, an ICSP header, and a reset button.
- The digital pins can be configured as inputs or outputs using the pinMode() function. They can also read or write HIGH or LOW values using the digitalRead() and digitalWrite() functions.
- The analog pins can measure the voltage between 0 and 5V using the analogRead() function. They can also output a variable voltage using the analogWrite() function, which uses PWM to simulate an analog signal.
- The USB connection can be used to upload sketches (programs) to the board, or to communicate with the computer or other devices using the Serial library.
- The power jack can be used to supply external power to the board, ranging from 7 to 12V. The board can also be powered by the USB connection or by the VIN pin.
- The ICSP header can be used to program the board using an external programmer, or to connect other devices that use the SPI protocol.
- The reset button can be used to restart the board and run the sketch from the beginning.

## Arduino IDE

- Arduino IDE is the software that allows you to write and upload sketches to the Arduino board. It is available for Windows, Mac OS X, and Linux.
- Arduino IDE has a text editor, a message area, a text console, a toolbar, and a status bar.
- The text editor is where you write your code, using the Arduino language, which is based on C/C++.
- The message area shows feedback on the compilation and upload process, as well as any errors or warnings.
- The text console shows the output of the Serial library, which can be used to print messages or data to the computer or other devices.
- The toolbar has buttons for verifying (compiling), uploading, creating, opening, saving, and serial monitor.
- The status bar shows the board and port selection, as well as the progress of the compilation and upload process.

## Coding

- Coding is the process of writing instructions for the Arduino board to execute. You can use the Arduino language, which is based on C/C++, or other languages that are compatible with the Arduino platform.
- A sketch is the name of a program that runs on the Arduino board. It consists of two main parts: the setup() function and the loop() function.
- The setup() function runs once when the board is powered on or reset. It is used to initialize variables, pin modes, libraries, etc.
- The loop() function runs repeatedly after the setup() function. It is used to perform the main logic of the sketch, such as reading sensors, controlling actuators, communicating with other devices, etc.
- A sketch can also have other functions, variables, constants, and libraries that are used to organize the code and add functionality.
- A sketch can be verified (compiled) and uploaded to the board using the Arduino IDE or other tools.

## Using Emulator

- An emulator is a software that simulates the behavior of the Arduino board and its components on a computer. It can be used to test and debug sketches without having a physical board.
- There are many emulators available for the Arduino platform, such as Tinkercad, Proteus, SimulIDE, etc.
- To use an emulator, you need to create a virtual circuit that matches the physical circuit you want to build. You can drag and drop components, such as LEDs, resistors, buttons, sensors, etc, and connect them to the Arduino board.
- You can also upload your sketch