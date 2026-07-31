### I2C/IIC

I2C (Inter-Integrated Circuit), also known as IIC, is a multi-master, multi-slave, packet-switched, single-ended, serial computer bus invented by Philips Semiconductor (now NXP Semiconductors). It is widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-distance, intra-board communication.

Some key features of I2C include:
- It uses only two bidirectional open-drain lines, Serial Data Line (SDA) and Serial Clock Line (SCL), pulled up with resistors.
- It is a half-duplex communication protocol, meaning that data can be transmitted in both directions, but not simultaneously.
- It supports multiple masters and multiple slaves, with arbitration and collision detection.
- It supports 7-bit and 10-bit addressing modes, allowing up to 112 or 1024 devices on the bus, respectively.
- It supports clock stretching, where a slave device can hold the clock line low to slow down or pause the communication.
- It supports speeds up to 5 Mbit/s in Ultra-Fast mode, with standard modes being 100 kbit/s (Standard mode) and 400 kbit/s (Fast mode).

I2C is commonly used for communication between microcontrollers and peripheral devices such as sensors, EEPROMs, ADCs, DACs, real-time clocks, and more. It is also used in applications such as power management, battery charging, and thermal management.
