### Unit 4 - Programming the Arduino

#### Arduino Platform Boards Anatomy
- Arduino is an open-source electronics platform based on easy-to-use hardware and software.
- Arduino boards are able to read inputs - light on a sensor, a finger on a button, or a Twitter message - and turn it into an output - activating a motor, turning on an LED, publishing something online.
- There are many different types of Arduino boards, each with its own microcontroller, input/output pins, and form factor.

#### Arduino IDE
- The Arduino Integrated Development Environment (IDE) is a cross-platform application that is written in the programming language Java.
- It is used to write and upload programs to Arduino compatible boards, but also, with the help of 3rd party cores, other vendor development boards.

#### Coding
- The Arduino programming language is based on C/C++.
- The structure of an Arduino sketch includes two main functions: setup() and loop().
- The setup() function is called once when the program starts and is used to initialize variables, pin modes, and libraries.
- The loop() function runs continuously after the setup() function has completed.

#### Using Emulator
- An Arduino emulator is a software application that can simulate the behavior of an Arduino board.
- It allows you to test your code without having to upload it to a physical board.
- There are several Arduino emulators available, such as Simuino, Emulare, and Virtual Breadboard.

#### Using Libraries
- Libraries provide extra functionality for use in sketches, e.g. working with hardware or manipulating data.
- To use a library in a sketch, select it from the Sketch > Import Library menu.
- A library is a collection of code that can be easily added to a sketch.

#### Additions in Arduino
- Shields are boards that can be plugged on top of the Arduino PCB extending its capabilities.
- The different shields follow the same philosophy as the original toolkit: they are easy to mount and cheap to produce.

#### Programming the Arduino for IoT
- The Internet of Things (IoT) is the network of physical objects or "things" embedded with electronics, software, sensors, and connectivity to enable objects to exchange data with the manufacturer, operator and/or other connected devices.
- Arduino can be used to develop interactive objects, taking inputs from a variety of switches or sensors, and controlling a variety of lights, motors, and other physical outputs.
- There are several IoT-specific Arduino boards, such as the Arduino MKR1000, Arduino Yun, and Arduino Uno WiFi Rev2.
