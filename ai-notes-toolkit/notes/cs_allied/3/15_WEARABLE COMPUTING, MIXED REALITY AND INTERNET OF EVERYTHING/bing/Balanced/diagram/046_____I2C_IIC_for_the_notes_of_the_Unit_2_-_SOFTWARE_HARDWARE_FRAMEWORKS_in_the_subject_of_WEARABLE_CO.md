### I2C/IIC

- I2C stands for Inter-Integrated Circuit. It is a serial communication protocol for exchanging data between multiple devices on a single bus.
- It was invented by Philips Semiconductor in 1982 and is widely used for short-distance communication in embedded systems, sensors, microcontrollers, etc.
- It is a half-duplex, bi-directional, two-wire bus system that uses a clock line (SCL) and a data line (SDA) to transmit and receive data between a master device and one or more slave devices.
- It is a synchronous protocol, meaning that the data bits are synchronized to the clock signal shared by the master and the slave.
- It is a multi-master/multi-slave protocol, meaning that more than one device can act as a master or a slave on the same bus, and they can communicate with each other by using unique addresses.
- It is a packet-switched protocol, meaning that the data is transferred in packets or frames that consist of a start condition, an address, a read/write bit, data bytes, an acknowledge bit, and a stop condition.
- It supports different data transfer modes, such as standard mode (100 kbit/s), fast mode (400 kbit/s), fast mode plus (1 Mbit/s), high-speed mode (3.4 Mbit/s), and ultra-fast mode (5 Mbit/s).
- It has some advantages over other serial communication protocols, such as simplicity, low cost, low power consumption, noise immunity, and flexibility.
- It also has some disadvantages, such as limited speed, limited bus length, limited number of devices, and arbitration issues.