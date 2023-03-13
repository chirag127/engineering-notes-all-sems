## Unit 5 - Programming the Arduino

The Arduino is a microcontroller board that can be programmed using the Arduino IDE, a software that allows you to write and upload code to the board. The Arduino IDE uses a simplified version of C++ as the programming language. The code that you write for the Arduino is called a sketch.

A sketch consists of two main parts: the setup() function and the loop() function. The setup() function runs once when the Arduino is powered on or reset, and is used to initialize variables, pin modes, libraries, etc. The loop() function runs continuously after the setup() function, and is used to execute the main logic of the sketch.

The Arduino has a number of input/output (I/O) pins that can be used to interact with other devices, such as sensors, LEDs, buttons, motors, etc. The pins can be configured as digital or analog, depending on the type of signal they receive or send. Digital pins can only read or write two states: HIGH (5V) or LOW (0V). Analog pins can read or write a range of values between 0 and 1023, corresponding to 0V and 5V.

The following diagram illustrates the basic architecture of a sketch and the I/O pins of the Arduino:

```
+------------------------+
|                        |
|    Arduino Sketch      |
|                        |
| +--------------------+ |
| |                    | |
| |    setup()         | |
| |                    | |
| +--------------------+ |
|                        |
| +--------------------+ |
| |                    | |
| |    loop()          | |
| |                    | |
| +--------------------+ |
|                        |
+------------------------+
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
         |       |
+------------------------+
|                        |
|    Arduino Board       |
|                        |
| +--------------------+ |
| |                    | |
| |    Digital Pins    | |
| |                    | |
| +--------------------+ |
|                        |
| +--------------------+ |
| |                    | |
| |    Analog Pins     | |
| |                    | |
| +--------------------+ |
|                        |
+------------------------+
```