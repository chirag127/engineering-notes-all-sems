### Inter-Integrated Circuit

- Inter-Integrated Circuit (I2C) is a serial communication protocol that allows multiple devices to communicate with each other using only two wires: a clock line (SCL) and a data line (SDA)     .
- I2C was invented by Philips Semiconductor (now NXP Semiconductors) in 1982 and is widely used in applications where low cost and ease of implementation are more important than high speed  .
- I2C can support up to 1008 slave devices and multiple masters on the same bus, which can operate at different speeds ranging from 100 kbps to 5 Mbps   .
- I2C uses a packet-based data transfer scheme, where each packet consists of a start condition, an address byte, one or more data bytes, and a stop condition   .
- I2C uses an open-drain or open-collector configuration for the SCL and SDA lines, which means that the devices can only pull the lines low and not drive them high. The lines are pulled high by external resistors, which determine the logic level and the maximum current   .
- I2C uses an acknowledge (ACK) or not acknowledge (NACK) mechanism to indicate the successful or unsuccessful reception of a byte. The transmitter releases the SDA line after sending a byte, and the receiver pulls it low to send an ACK or leaves it high to send a NACK   .
- I2C supports various modes of operation, such as standard mode (100 kbps), fast mode (400 kbps), fast mode plus (1 Mbps), high speed mode (3.4 Mbps), and ultra-fast mode (5 Mbps). The mode is determined by the master device and the capabilities of the slave devices  .
- I2C also supports various features, such as 10-bit addressing, clock stretching, arbitration, bus error detection, general call, software reset, device ID, and power management  .
- I2C is widely used for connecting sensors, memory devices, displays, audio codecs, and other peripherals to microcontrollers, microprocessors, or other host devices    .