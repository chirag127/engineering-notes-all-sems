 Here is the content in markdown format:

### Using libraries for the notes of the Unit 5 - Programming the Arduino in the subject of Internet of Things

- Libraries provide pre-written code that can be reused in Arduino sketches, eliminating the need to reinvent the wheel and reducing development time.
- Some of the commonly used libraries for Arduino are:
    - Servo library: Used to control servo motors. It makes it easy to specify the servo angle and handles the lower level details of controlling the servo.
    - Wire library: Used for I2C communication. It allows Arduino boards to communicate with I2C devices.
    - Ethernet library: Used to connect the Arduino to the internet via the Ethernet shield. It provides client and server functionality to handle internet connectivity.
    - SPI library: Used for SPI communication which is a synchronous serial data transfer. It is commonly used to connect sensors and SD cards to the Arduino.
- Advantages of using libraries:
    - Saves time: No need to write all the low-level code for common tasks. The libraries provide tested and optimized functions to get the job done.
    - Better code: The libraries are written by experts and contain well-written, bug-free code. Using libraries results in more robust code.
    - Easy to use: The libraries have easy to use functions and syntax. This makes it easier for beginners to get started without knowing the intricacies of the underlying protocols/interfaces.
- Some disadvantages of using libraries:
    - Dependence: The sketches become dependent on the libraries. If there are bugs in the libraries or if they are updated, it may break the sketches.
    - Additional memory usage: The libraries take up additional program memory. For memory constrained microcontrollers like the Arduino, this can be a limitation.
    - Learning curve: Although the libraries are easy to use, it takes time to understand what the libraries are doing under the hood and how they work. This can be a steep learning curve for beginners.