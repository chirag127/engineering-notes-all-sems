## Unit 5 - Programming the Arduino

- Arduino is an open-source platform that consists of a hardware board and a software IDE (Integrated Development Environment) that can be used to create and control interactive electronic projects.
- The Arduino board is based on a microcontroller, which is a small computer chip that can execute instructions and store data. The microcontroller can be programmed using the Arduino programming language, which is based on C/C++.
- The Arduino IDE is a software application that allows you to write, compile, and upload code to the Arduino board. The IDE also provides a serial monitor, a code editor, a library manager, and a board manager.
- To program the Arduino board, you need to follow these steps:
  - Connect your Arduino board to your computer using a USB cable.
  - Launch the Arduino IDE and select the right board and port from the toolbar.
  - Write your code (also called sketch) in the code editor. You can use the built-in examples, the online reference, or the Arduino programming notebook as a guide.
  - Compile your code by clicking on the check mark icon in the top left corner. This will check for errors and generate a binary file that can be uploaded to the board.
  - Upload your code by clicking on the arrow icon in the top left corner. This will transfer the binary file to the board and start running it.
  - Monitor the output of your code by opening the serial monitor from the toolbar. This will show you the data sent and received by the board via the USB connection.
- The Arduino programming language has a basic structure that consists of two required functions: setup() and loop(). The setup() function runs once when the board is powered on or reset, and is used to initialize variables, pins, libraries, etc. The loop() function runs repeatedly and is used to perform the main logic of the program. Both functions are enclosed by curly braces and end with a semicolon.
- The Arduino programming language also has various values (variables and constants), operators, control structures, data types, and libraries that can be used to manipulate and store data, perform calculations, make decisions, repeat actions, and access external hardware and software components. You can find more details about these elements in the Arduino reference.