### I2C/IIC

I2C (Inter-Integrated Circuit), also known as IIC, is a multi-master, multi-slave, packet-switched, single-ended, serial computer bus invented by Philips Semiconductor (now NXP Semiconductors). It is widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-distance, intra-board communication.

Some key features of I2C include:
- It uses only two bidirectional open-drain lines, Serial Data Line (SDA) and Serial Clock Line (SCL), pulled up with resistors.
- It is a half-duplex communication protocol, meaning that data can be transmitted in both directions, but not simultaneously.
- It supports multiple masters and multiple slaves, with arbitration and collision detection.
- It supports 7-bit and 10-bit addressing modes, allowing up to 112 or 1024 devices on the same bus.
- It supports clock stretching, where a slave device can hold the clock line low to slow down or pause the communication.

I2C is commonly used for communication between microcontrollers and peripheral devices such as sensors, displays, and memory devices. It is also used for communication between multiple microcontrollers or between microcontrollers and other devices such as digital signal processors (DSPs) or field-programmable gate arrays (FPGAs).

I2C is a relatively simple and low-cost communication protocol, making it a popular choice for many applications. However, it has some limitations, such as a relatively low data transfer rate and limited bus length, which may make it unsuitable for some applications. Other communication protocols, such as SPI or UART, may be more suitable for certain applications. It is important to carefully consider the requirements of the application when choosing a communication protocol.