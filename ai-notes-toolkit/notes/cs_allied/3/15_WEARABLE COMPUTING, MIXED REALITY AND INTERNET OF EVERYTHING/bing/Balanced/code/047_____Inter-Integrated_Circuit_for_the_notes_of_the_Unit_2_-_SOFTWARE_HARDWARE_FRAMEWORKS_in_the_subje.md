### Inter-Integrated Circuit

- Inter-Integrated Circuit (I2C) is a serial communication protocol that allows multiple devices to communicate with each other over a shared bus.
- I2C was invented by Philips in 1982 to connect microcontrollers and peripherals on a single board.
- I2C uses two wires: SDA (Serial Data) and SCL (Serial Clock). SDA carries the data and SCL provides the clock signal to synchronize the data transfer.
- I2C supports multiple masters and slaves on the same bus. A master is a device that initiates and controls the communication, while a slave is a device that responds to the master's commands.
- I2C uses 7-bit or 10-bit addressing to identify the devices on the bus. Each device has a unique address that is assigned by the manufacturer or the user.
- I2C supports two modes of operation: standard mode (up to 100 kbit/s) and fast mode (up to 400 kbit/s). Some devices also support high-speed mode (up to 3.4 Mbit/s) and ultra-fast mode (up to 5 Mbit/s).
- I2C uses a start condition and a stop condition to mark the beginning and the end of a communication. A start condition is when SDA goes from high to low while SCL is high, and a stop condition is when SDA goes from low to high while SCL is high.
- I2C uses an acknowledge bit (ACK) and a not-acknowledge bit (NACK) to indicate the status of the communication. An ACK is when SDA is low while SCL is high, and a NACK is when SDA is high while SCL is high.
- I2C uses a read/write bit (R/W) to indicate the direction of the data transfer. A R/W bit of 0 means the master is writing to the slave, and a R/W bit of 1 means the master is reading from the slave.
- I2C uses arbitration and clock stretching to handle collisions and synchronization issues on the bus. Arbitration is when two or more masters try to access the bus at the same time, and the one with the lowest address wins. Clock stretching is when a slave holds the SCL line low to delay the communication until it is ready.