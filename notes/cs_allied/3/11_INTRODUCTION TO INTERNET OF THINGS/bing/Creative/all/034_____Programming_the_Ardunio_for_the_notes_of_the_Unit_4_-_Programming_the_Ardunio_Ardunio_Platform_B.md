# Programming the Arduino for IoT

## Arduino Platform Boards Anatomy

- Arduino is an open-source platform that consists of hardware and software components for creating interactive electronic projects.
- Arduino boards are microcontroller-based boards that can be programmed using the Arduino IDE or other compatible tools.
- Arduino boards have different features and capabilities depending on the model, such as input/output pins, communication interfaces, sensors, LEDs, etc.
- Some of the most common Arduino boards are:

  - Arduino Uno: The most popular and widely used Arduino board, based on the ATmega328P microcontroller. It has 14 digital input/output pins, 6 analog inputs, a 16 MHz quartz crystal, a USB connection, a power jack, an ICSP header and a reset button.
  - Arduino Nano: A small and compact Arduino board, based on the ATmega328P microcontroller. It has 14 digital input/output pins, 8 analog inputs, a 16 MHz quartz crystal, a mini-USB connection, an ICSP header and a reset button.
  - Arduino Mega: A large and powerful Arduino board, based on the ATmega2560 microcontroller. It has 54 digital input/output pins, 16 analog inputs, a 16 MHz quartz crystal, a USB connection, a power jack, an ICSP header and a reset button.
  - Arduino Nano 33 IoT: A small and versatile Arduino board, based on the SAMD21G18A microcontroller and the NINA-W102 Wi-Fi module. It has 14 digital input/output pins, 6 analog inputs, a 48 MHz crystal oscillator, a micro-USB connection, an ICSP header, a reset button and a built-in IMU sensor.
  - Arduino Nano 33 BLE: A small and powerful Arduino board, based on the nRF52840 microcontroller and the NINA-B306 Bluetooth module. It has 14 digital input/output pins, 6 analog inputs, a 64 MHz crystal oscillator, a micro-USB connection, an ICSP header, a reset button and a built-in IMU sensor.

## Arduino IDE

- Arduino IDE is the official integrated development environment for programming Arduino boards and compatible devices.
- Arduino IDE can be downloaded and installed from the Arduino website or the Microsoft Store for Windows 10 users.
- Arduino IDE provides a simple and user-friendly interface for writing, compiling and uploading code to Arduino boards.
- Arduino IDE supports a variety of programming languages, such as C, C++, Python, etc.
- Arduino IDE also provides a serial monitor, a serial plotter, a library manager, a board manager and a cloud editor.

## Coding

- Coding for Arduino boards is done using the Arduino programming language, which is based on C/C++ and has some simplifications and extensions.
- Arduino code consists of two main functions: setup() and loop().
  - setup(): This function is executed once when the board is powered on or reset. It is used to initialize variables, pin modes, libraries, etc.
  - loop(): This function is executed repeatedly after the setup() function. It is used to implement the main logic and functionality of the program.
- Arduino code can also include other functions, variables, constants, comments, etc.
- Arduino code can be written using the Arduino IDE or other compatible tools, such as Visual Studio Code, Atom, etc.
- Arduino code can be compiled and uploaded to the board using the Arduino IDE or other compatible tools, such as Arduino CLI, PlatformIO, etc.

## Using Emulator

- An emulator is a software tool that simulates the behavior and functionality of a hardware device, such as an Arduino board.
- An emulator can be used to test and debug Arduino code without the need of a physical board and components.
- An emulator can also be used to learn and experiment with Arduino programming and electronics.
- Some of the most popular and widely used Arduino emulators are:

  - Tinkercad: A web-based platform that allows users to create and simulate Arduino circuits and code online. It provides a graphical interface for designing circuits, a code editor for writing Arduino code and a simulator for running and testing the code and the circuit.
  - Proteus: A desktop application that allows users to create and simulate Arduino circuits and code offline. It provides a schematic editor for designing circuits, a code editor for writing Arduino code and a simulator for running and testing the code and the circuit.
  - Wokwi: A web-based platform that allows users to create and simulate Arduino circuits and code online. It provides a graphical interface for designing circuits, a code editor for writing Arduino code and a simulator for running and testing