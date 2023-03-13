## Unit 5 - Programming the Arduino

- Arduino is an open-source platform that combines hardware and software for creating interactive projects with microcontrollers.
- Arduino programming language is based on C/C++ and supports many standard and custom libraries.
- Arduino IDE (Integrated Development Environment) is the software that allows you to write, compile and upload code to the Arduino board.
- Arduino code is also called a sketch, which consists of two main functions: setup() and loop().
- setup() is executed once when the board is powered on or reset, and it is used to initialize variables, pin modes, libraries, etc..
- loop() is executed repeatedly after setup(), and it is used to implement the main logic of the sketch.
- Arduino code can also have other functions, variables, constants, comments, etc. that follow the C/C++ syntax.
- Arduino code can use input and output (IO) pins to communicate with sensors, actuators, displays, etc..
- Arduino pins can be digital or analog, and they can be configured as input, output, or input_pullup.
- Digital pins can read or write values of HIGH (5V) or LOW (0V).
- Analog pins can read values from 0 to 1023, corresponding to a range of 0 to 5V or 0 to 3.3V, depending on the board.
- Analog pins can also write values using pulse-width modulation (PWM), which is a technique to vary the duty cycle of a digital signal.
- Arduino code can use control structures such as if, else, for, while, switch, etc. to implement conditional and iterative logic.
- Arduino code can use serial communication to send and receive data to and from the computer or other devices.
- Arduino code can use libraries to extend the functionality of the sketch, such as LCD, Servo, Ethernet, etc..
- Arduino code can be debugged using the serial monitor, the serial plotter, or external tools.

Some mnemonics and learning tricks for Unit 5 are:

- Remember the acronym **SLL** for the structure of an Arduino sketch: **S**etup, **L**oop, and **L**ibraries.
- Remember the acronym **DAR** for the types of digital pins: **D**igital, **A**nalog, and **P**WM.
- Remember the formula **V = R * A / 1023** to convert an analog reading to a voltage, where **V** is the voltage, **R** is the reference voltage (5V or 3.3V), and **A** is the analog value.
- Remember the acronym **IFS** for the most common control structures: **I**f, **F**or, and **S**witch.
- Remember the acronym **SER** for the most common serial communication functions: **S**erial.begin, **S**erial.print, and **S**erial.read.