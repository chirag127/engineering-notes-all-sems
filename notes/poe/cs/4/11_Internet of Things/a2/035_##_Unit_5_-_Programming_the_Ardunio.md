 Here is the content in markdown format for Unit 5 - Programming the Ardunio:

## Unit 5 - Programming the Ardunio

- Arduino is an open-source electronics platform based on easy-to-use hardware and software. It's intended for anyone making interactive projects.
- Arduino boards are able to read inputs - light on a sensor, a finger on a button, or a Twitter message - and turn it into an output - activating a motor, turning on an LED, publishing something online.
- You can tell your Arduino what to do by sending a set of instructions to the microcontroller on the board. These instructions are written in C/C++ programming language and loaded onto the Arduino using the Arduino programming environment.
- The Arduino programming language is very simple and easy to learn. Some key things to know:

- Setup() - Runs once when the board is turned on. Used to initialize variables and pin modes.
- Loop() - Runs continuously after setup finishes. Used to actively control the Arduino board.
- Comments - Denoted by // and ignored by the compiler. Used to leave notes in the code.
- Variables - Used to store data. Must declare type and name before using. Example: int sensorValue = 0;
- Conditional Logic - Used to make decisions and control flow. For example, if/else statements and switch cases.
- Functions - Used to group blocks of code to perform a task. Can pass in parameters and return values.
- Examples: Blinking an LED, Reading a button press, Reading an analog input like temperature

- Some useful tips and Mnemonics:
- Plan your program structure before writing the code. Think about what needs to happen and in what order.
- Keep functions short and focused on a single task. Break complex problems down into simpler steps.
- Use descriptive names for variables and functions. This makes the code easier to understand.
- Comment your code. Even if the code is simple, comments can help you remember what the program is doing later on.
- The Arduino IDE has a number of useful tools to help find and fix errors:
- Check your spelling - misspelled function names and variable names are common errors.
- Use the auto-format tool to consistently format your code and make it easier to read.
- The compiler will flag any syntax errors, helping you fix problems.
- The serial monitor can display data from your Arduino, useful for debugging.