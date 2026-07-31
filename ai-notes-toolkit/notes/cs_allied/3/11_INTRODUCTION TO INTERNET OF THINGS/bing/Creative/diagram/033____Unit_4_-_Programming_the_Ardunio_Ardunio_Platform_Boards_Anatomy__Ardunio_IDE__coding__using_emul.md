## Unit 4 - Programming the Arduino

### Arduino Platform Boards Anatomy

- Arduino is an open-source platform that consists of hardware and software components for creating interactive electronic projects.
- Arduino boards are microcontroller-based boards that can be programmed using the Arduino IDE or other compatible software.
- Arduino boards have various input and output pins that can be connected to sensors, actuators, LEDs, buttons, switches, etc.
- Arduino boards also have a USB port that can be used to upload the code from the computer, communicate with the serial monitor, or power the board.
- Arduino boards have a built-in voltage regulator that can accept a range of input voltages from 7V to 20V.
- Arduino boards have a reset button that can be used to restart the program or enter the bootloader mode.
- Arduino boards have an LED that indicates the power status and another LED that is connected to pin 13 and can be controlled by the code.
- Arduino boards have a crystal oscillator that provides a stable clock signal for the microcontroller.
- Arduino boards have different models and variants that differ in size, shape, features, and specifications. Some of the common Arduino boards are:

  - Arduino Uno: The most popular and widely used Arduino board. It has an ATmega328P microcontroller, 14 digital pins, 6 analog pins, 32 KB of flash memory, 2 KB of SRAM, and 1 KB of EEPROM.
  - Arduino Nano: A small and compact Arduino board that has the same functionality as the Arduino Uno but in a smaller form factor. It has an ATmega328P microcontroller, 14 digital pins, 8 analog pins, 32 KB of flash memory, 2 KB of SRAM, and 1 KB of EEPROM.
  - Arduino Mega: A large and powerful Arduino board that has an ATmega2560 microcontroller, 54 digital pins, 16 analog pins, 256 KB of flash memory, 8 KB of SRAM, and 4 KB of EEPROM.
  - Arduino Due: A 32-bit Arduino board that has an ARM Cortex-M3 microcontroller, 54 digital pins, 12 analog pins, 512 KB of flash memory, and 96 KB of SRAM.
  - Arduino Leonardo: An Arduino board that has an ATmega32U4 microcontroller, 20 digital pins, 12 analog pins, 32 KB of flash memory, 2.5 KB of SRAM, and 1 KB of EEPROM. It also has a built-in USB communication feature that allows it to emulate a keyboard, mouse, or MIDI device.
  - Arduino Micro: A tiny Arduino board that has the same functionality as the Arduino Leonardo but in a smaller form factor. It has an ATmega32U4 microcontroller, 20 digital pins, 12 analog pins, 32 KB of flash memory, 2.5 KB of SRAM, and 1 KB of EEPROM.
  - Arduino MKR1000: An Arduino board that has an ATSAMW25 microcontroller, 8 digital pins, 7 analog pins, 256 KB of flash memory, and 32 KB of SRAM. It also has a built-in WiFi module that allows it to connect to the internet and perform IoT applications.

### Arduino IDE

- Arduino IDE is an integrated development environment that allows users to write, compile, and upload code to the Arduino boards.
- Arduino IDE is based on the Processing language and uses a simplified version of C/C++ for programming the Arduino boards.
- Arduino IDE has a user-friendly interface that consists of the following elements:

  - Menu bar: Provides access to various options and settings of the Arduino IDE.
  - Toolbar: Provides shortcuts to common functions such as verify, upload, new, open, save, serial monitor, etc.
  - Text editor: Allows users to write and edit the code for the Arduino boards. It also provides syntax highlighting, auto-completion, and error checking features.
  - Message area: Displays messages and feedback from the Arduino IDE, such as compilation status, error messages, etc.
  - Console: Displays the output of the code, such as serial data, debug messages, etc.
  - Status bar: Shows the current board and port selection, as well as the progress of the verification and upload process.

- Arduino IDE uses a sketch as the basic unit of code for the Arduino boards. A sketch is a file that contains the code for the Arduino boards and has a .ino extension.
- Arduino IDE uses a library as a collection of code that can be reused and shared by different sketches. A library is a folder that contains a header file (.h) and a source file (.cpp) that define the functions and variables of the library. Arduino IDE comes with many built-in