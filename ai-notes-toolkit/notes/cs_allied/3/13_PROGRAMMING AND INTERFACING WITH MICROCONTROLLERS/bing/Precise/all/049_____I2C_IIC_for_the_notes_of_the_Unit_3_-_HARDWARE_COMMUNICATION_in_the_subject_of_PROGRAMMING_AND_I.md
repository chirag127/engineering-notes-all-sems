# I2C/IIC Communication Protocol

I2C (Inter-Integrated Circuit) is a serial communication protocol that allows multiple devices to be connected to a single bus. It is commonly used in embedded systems and other applications where a small number of devices need to communicate with each other.

- I2C is a simple and efficient protocol that requires only two wires for communication: a clock line (SCL) and a data line (SDA) .
- It is often used in applications where low-cost, low-power communication is required, such as in sensors, displays, and other peripherals.
- Any number of slaves and any number of masters can be connected to these 2 signals.
- I2C communication is the short form for inter-integrated circuits. It is a communication protocol developed by Philips Semiconductors for the transfer of data between a central processor and multiple ICs on the same circuit board using just two common wires.
- I2C is a serial communication protocol, so data is transferred bit by bit along a single wire (the SDA line). Like SPI, I2C is synchronous, so the output of bits is synchronized to the sampling of bits by a clock signal shared between the master and the slave.
