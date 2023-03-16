# I2C/IIC for the notes of the Unit 3 - HARDWARE COMMUNICATION in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

- I2C or IIC stands for Inter-Integrated Circuit, a serial communication protocol made by Philips Semiconductor (now NXP Semiconductor) in 1982 .
- It is intended for communication between chips that reside on the same Printed Circuit Board (PCB) or within a short distance .
- It is a synchronous, multi-master/multi-slave, packet switched, single-ended, serial communication bus.
- It uses two lines to send and receive data: a serial clock line (SCL) and a serial data line (SDA) .
- The clock line is controlled by the master device, which can initiate or terminate a data transfer .
- The data line is used to transmit bits between the master and the slave devices, synchronized to the clock line .
- Each device on the bus has a unique address, which is used to identify it during a data transfer .
- The master device can communicate with one or more slave devices by sending their addresses and the direction of data transfer (read or write) .
- The slave device that matches the address acknowledges the master by pulling the data line low, and then either sends or receives data depending on the direction of transfer .
- The data transfer is terminated by the master sending a stop condition, which is a high-to-low transition on the data line while the clock line is high .
- The I2C protocol has several advantages, such as simplicity, low cost, low power consumption, and flexibility .
- The I2C protocol also has some limitations, such as low speed, limited bus length, and limited number of devices .
- The I2C protocol is widely used in various applications, such as sensors, EEPROMs, LCDs, and microcontrollers  .