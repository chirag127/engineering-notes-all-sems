## Unit 5 - Programming the Arduino

- Arduino is an open-source platform that consists of a hardware board and a software environment for creating interactive electronic projects.
- The hardware board is based on a microcontroller, which is a small computer that can be programmed to control inputs and outputs such as sensors, LEDs, motors, etc.
- The software environment is called the Arduino IDE (Integrated Development Environment), which is a program that allows you to write, compile, and upload code to the board using a simple programming language called Arduino C/C++.
- To program the Arduino, you need to follow these steps:
  - Connect the board to your computer using a USB cable.
  - Launch the Arduino IDE and select the board and port from the Tools menu.
  - Write your code in the text editor or use one of the examples from the File menu.
  - Verify your code by clicking the check mark button. This will compile your code and check for errors.
  - Upload your code by clicking the arrow button. This will transfer your code to the board and run it.
- The basic structure of an Arduino program consists of two functions: setup() and loop().
  - The setup() function runs once when the board is powered on or reset. It is used to initialize variables, pin modes, libraries, etc.
  - The loop() function runs repeatedly after the setup() function. It is used to implement the main logic of your program, such as reading inputs, controlling outputs, etc.
- The Arduino language has some common elements with other programming languages, such as:
  - Variables: These are names that store values, such as numbers, characters, strings, etc. You can declare variables using data types, such as int, char, String, etc.
  - Operators: These are symbols that perform calculations or comparisons, such as +, -, *, /, ==, !=, etc.
  - Control structures: These are statements that control the flow of your program, such as if, else, for, while, switch, etc.
  - Functions: These are blocks of code that perform a specific task and can be reused. You can define your own functions or use built-in functions, such as pinMode, digitalWrite, analogRead, etc.
  - Comments: These are lines of text that are ignored by the compiler and are used to explain or document your code. You can write comments using // for single-line comments or /* and */ for multi-line comments.