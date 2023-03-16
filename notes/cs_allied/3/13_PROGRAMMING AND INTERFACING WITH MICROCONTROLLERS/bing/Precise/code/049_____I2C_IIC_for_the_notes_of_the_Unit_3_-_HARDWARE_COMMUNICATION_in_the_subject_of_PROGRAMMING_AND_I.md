### I2C/IIC

I2C (Inter-Integrated Circuit), also known as IIC, is a multi-master, multi-slave, packet-switched, single-ended, serial computer bus invented by Philips Semiconductor (now NXP Semiconductors). It is widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-distance, intra-board communication.

Some key features of I2C include:
- It uses only two bidirectional open-drain lines, Serial Data Line (SDA) and Serial Clock Line (SCL), pulled up with resistors.
- It is a half-duplex communication protocol.
- It supports multiple masters and slaves on the same bus.
- It supports 7-bit and 10-bit addressing modes.
- It supports clock stretching, where a slave device can hold the clock line low to delay the master and slow down the communication.
- It supports arbitration, where multiple masters can attempt to control the bus at the same time, but only one can win and continue the communication.

I2C is commonly used for communication between microcontrollers and peripheral devices such as sensors, EEPROMs, ADCs, DACs, real-time clocks, and more. It is also used for communication between multiple microcontrollers or between microcontrollers and other devices such as FPGAs or DSPs.

I2C is a simple and flexible communication protocol, but it has some limitations. It is not suitable for high-speed communication or for long-distance communication. It also requires pull-up resistors on the SDA and SCL lines, which can increase the power consumption of the system.

Overall, I2C is a widely used and versatile communication protocol for short-distance, low-speed communication between microcontrollers and peripheral devices. It is an important topic to understand for anyone working with microcontrollers and embedded systems.