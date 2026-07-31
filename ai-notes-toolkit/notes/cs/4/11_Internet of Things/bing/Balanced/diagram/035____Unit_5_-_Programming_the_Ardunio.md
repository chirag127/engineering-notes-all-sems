## Unit 5 - Programming the Arduino

- Arduino is an open-source platform that consists of a hardware board and a software IDE (Integrated Development Environment) that can be used to create and program electronic projects.
- The hardware board is based on a microcontroller, which is a small computer that can run a single program repeatedly and interact with sensors and actuators.
- The software IDE is a program that allows you to write, compile, and upload code to the board using a simple programming language called Arduino C/C++.
- The code that you write for the Arduino is called a sketch, which consists of two main functions: setup() and loop().
- The setup() function runs once when the board is powered on or reset, and is used to initialize variables, pin modes, and libraries.
- The loop() function runs continuously after the setup() function, and is used to implement the main logic and behavior of the sketch.
- The Arduino IDE provides a serial monitor that can be used to communicate with the board and display messages or data sent by the sketch.
- The Arduino IDE also provides a library manager that can be used to install and manage additional libraries that extend the functionality of the board and the sketch.
- Some of the basic concepts and syntax of Arduino C/C++ are:

  - Comments: Comments are lines of text that are ignored by the compiler and are used to explain or document the code. Comments can be single-line (//) or multi-line (/* */).
  - Variables: Variables are names that represent values or data that can be used in the sketch. Variables have a type, a name, and an optional value. For example, int ledPin = 13; declares a variable of type int (integer) with the name ledPin and the value 13.
  - Constants: Constants are names that represent fixed values or data that cannot be changed in the sketch. Constants have a type, a name, and a value. For example, const float PI = 3.14; declares a constant of type float (floating-point number) with the name PI and the value 3.14.
  - Operators: Operators are symbols that perform operations on values or variables, such as arithmetic (+, -, *, /, %), logical (&&, ||, !), relational (==, !=, <, >, <=, >=), and assignment (=, +=, -=, *=, /=, %=).
  - Expressions: Expressions are combinations of values, variables, and operators that produce a result. For example, ledPin + 1 is an expression that adds 1 to the value of ledPin and returns the result.
  - Statements: Statements are lines of code that perform actions or control the flow of the sketch. Statements end with a semicolon (;). For example, pinMode(ledPin, OUTPUT); is a statement that sets the mode of the pin ledPin to OUTPUT.
  - Control structures: Control structures are statements that alter the flow of the sketch based on conditions or repetitions. For example, if, else, for, while, do...while, switch, case, break, continue, return, and goto are control structures.
  - Functions: Functions are blocks of code that perform a specific task and can be reused in the sketch. Functions have a name, a return type, a list of parameters, and a body. For example, void blink(int pin, int delay) { ... } defines a function named blink that takes two parameters of type int and returns nothing (void).
  - Arrays: Arrays are variables that store multiple values of the same type in a fixed-size sequence. Arrays have a name, a type, a size, and a list of values. For example, int numbers[5] = {1, 2, 3, 4, 5}; declares an array of type int with the name numbers, the size 5, and the values 1, 2, 3, 4, and 5.
  - Strings: Strings are variables that store sequences of characters. Strings have a name, a type, and a value. For example, String message = "Hello, world!"; declares a string of type String with the name message and the value "Hello, world!".
  - Data types: Data types are categories of values that determine the size, range, and format of the data. For example, int, float, char, bool, String, and void are data types.
  - Scope: Scope is the area of the sketch where a variable or a function is visible and accessible. For example, a variable declared inside a function is local to that function and cannot be used outside of it, while a variable declared outside of any function is global and can be used anywhere in the sketch.