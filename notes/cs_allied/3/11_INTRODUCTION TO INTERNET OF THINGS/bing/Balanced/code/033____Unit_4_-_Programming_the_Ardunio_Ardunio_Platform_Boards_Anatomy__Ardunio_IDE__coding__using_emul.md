## Unit 4 - Programming the Arduino

Arduino is an open-source platform that combines hardware and software for creating interactive projects. Arduino boards are microcontrollers that can be programmed using the Arduino IDE (Integrated Development Environment) and various libraries. Arduino can be used for IoT (Internet of Things) applications by connecting sensors, actuators, and communication modules.

### Arduino Platform Boards Anatomy

Arduino boards have different components and features depending on the model, but they share some common elements:

- A microcontroller chip that runs the code and controls the pins.
- A USB port or a serial port for uploading the code and communicating with the computer.
- A power jack or a battery connector for supplying power to the board.
- A reset button for restarting the program.
- A built-in LED for testing and debugging.
- Digital pins that can be used as inputs or outputs for digital signals (0 or 1).
- Analog pins that can be used as inputs for analog signals (0 to 5V or 0 to 3.3V depending on the board).
- PWM pins that can be used as outputs for analog signals by modulating the duty cycle of a digital signal (0 to 255).
- Communication pins that can be used for serial, SPI, I2C, or other protocols.
- Special pins that can be used for interrupts, timers, or other functions.

### Arduino IDE

Arduino IDE is a software application that allows users to write, compile, and upload code to Arduino boards. Arduino IDE has the following features:

- A text editor for writing the code in C/C++ language with syntax highlighting and auto-completion.
- A message area for displaying errors, warnings, and other information.
- A console for displaying the serial output from the board.
- A toolbar for accessing common functions such as verifying, uploading, opening, saving, and selecting the board and the port.
- A menu bar for accessing other functions such as preferences, libraries, examples, tools, and help.
- A status bar for showing the current board, port, and sketch size.

### Coding

Arduino code consists of two main parts: setup and loop. The setup function runs once when the board is powered on or reset, and it is used to initialize the variables, pins, and libraries. The loop function runs repeatedly and it is used to implement the main logic of the program.

Arduino code also uses comments, variables, constants, operators, control structures, functions, and libraries. Comments are used to explain the code and they start with // or /* and end with */. Variables are used to store data and they have a name, a type, and a value. Constants are used to store fixed values and they are defined with #define or const. Operators are used to perform calculations and comparisons on the variables and constants. Control structures are used to control the flow of the program and they include if, else, for, while, switch, case, and break. Functions are used to group and reuse code and they have a name, parameters, and a return value. Libraries are used to extend the functionality of the code and they include pre-written functions and variables for specific tasks.

### Using Emulator

An emulator is a software application that simulates the behavior of an Arduino board on a computer. An emulator can be used to test and debug the code without having to connect a physical board. An emulator can also provide additional features such as graphical interfaces, sensors, and actuators.

There are different emulators available for Arduino, such as:

- Tinkercad Circuits: A web-based emulator that allows users to create and simulate circuits with Arduino and other components.
- Proteus: A desktop emulator that allows users to design and simulate circuits with Arduino and other components.
- Simuino: A web-based emulator that allows users to run Arduino code and view the serial output.
- Arduino Simulator: A desktop emulator that allows users to run Arduino code and view the serial output.

### Using Libraries

Libraries are collections of code that provide pre-written functions and variables for specific tasks. Libraries can be used to simplify the code and to add new features and functionalities. Arduino comes with a set of built-in libraries that can be accessed from the IDE menu or by using the #include directive. Some of the built-in libraries are:

- SPI: A library for communicating with devices using the Serial Peripheral Interface (SPI) protocol.
- Wire: A library for communicating with devices using the Inter-Integrated Circuit (I2C) protocol.
- Ethernet: A library for connecting to the internet using the Ethernet shield or module.
- WiFi: A library for connecting to the internet using the WiFi shield or module.
- GSM: A library for connecting to the internet using the GSM shield or module.
- Servo: A library for controlling servo motors.
- Liquid