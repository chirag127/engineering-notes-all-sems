# I2C/IIC for the notes of the Unit 3 - HARDWARE COMMUNICATION in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

- I2C or IIC stands for Inter-Integrated Circuit, a serial communication protocol made by Philips Semiconductor (now NXP Semiconductor) in 1982 .
- It is designed for communication between chips on the same Printed Circuit Board (PCB) or within a short distance .
- It is a synchronous, multi-master/multi-slave, packet switched, single-ended, serial communication bus.
- It uses two bidirectional lines, Serial Data Line (SDA) and Serial Clock Line (SCL), to transfer data between devices  .
- The SCL line is controlled by the master device, which generates the clock signal to synchronize the data transfer  .
- The SDA line is used to send and receive data bits, one bit per clock pulse  .
- The data transfer is initiated by the master device, which sends a start condition, followed by the address of the slave device and a read/write bit  .
- The slave device acknowledges the address by pulling the SDA line low, and then either sends or receives data depending on the read/write bit  .
- The data transfer is terminated by the master device, which sends a stop condition, or by a repeated start condition for a new transfer  .
- The I2C protocol supports multiple masters and slaves on the same bus, but only one master can control the bus at a time .
- The I2C protocol supports different data transfer modes, such as standard mode (up to 100 kbit/s), fast mode (up to 400 kbit/s), fast mode plus (up to 1 Mbit/s), high speed mode (up to 3.4 Mbit/s), and ultra-fast mode (up to 5 Mbit/s).
- The I2C protocol is widely used for connecting various peripherals, such as sensors, EEPROMs, LCDs, ADCs, DACs, etc., to microcontrollers and other devices  .