## Unit 5 - Programming the Arduino

- Arduino is an open-source platform that consists of a hardware board and a software environment for creating interactive electronic projects.
- The Arduino board is based on a microcontroller, which is a small computer chip that can run a program and interact with sensors, actuators, and other devices.
- The Arduino software (IDE) is an application that allows you to write, compile, and upload programs to the Arduino board using a simple programming language based on C/C++.
- To program the Arduino, you need to follow these steps:
  - Connect your Arduino board to your computer using a USB cable.
  - Select the right board and port from the Tools menu in the Arduino IDE.
  - Write your program (also called a sketch) in the Arduino IDE or open an example from the File menu.
  - Upload your program to the Arduino board by clicking the Upload button in the Arduino IDE.
  - Monitor the output of your program using the Serial Monitor or the Serial Plotter in the Arduino IDE.
- The basic structure of an Arduino program consists of two required functions: setup() and loop().
  - The setup() function runs once when the program starts and is used to initialize variables, pin modes, and other settings.
  - The loop() function runs repeatedly after the setup() function and is used to perform the main logic of the program.
- An Arduino program can use various functions, values (variables and constants), and structures to control the Arduino board and perform computations.
  - Functions are predefined or user-defined blocks of code that perform a specific task and can be called from anywhere in the program.
  - Values are data that can be stored, manipulated, and used in the program. Variables are values that can change during the program execution, while constants are values that remain fixed.
  - Structures are keywords that define the flow of the program, such as if, else, for, while, switch, case, etc.
- An Arduino program can also use libraries, which are collections of code that provide additional functionality for specific tasks, such as communication, sensors, displays, etc. Libraries can be included in the program using the #include directive and can be accessed using the dot (.) operator.