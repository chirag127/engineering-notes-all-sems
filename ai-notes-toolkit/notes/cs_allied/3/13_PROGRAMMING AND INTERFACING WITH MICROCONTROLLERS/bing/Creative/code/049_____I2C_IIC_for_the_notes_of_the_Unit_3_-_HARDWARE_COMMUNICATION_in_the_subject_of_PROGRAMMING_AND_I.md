### I2C/IIC for the notes of the Unit 3 - HARDWARE COMMUNICATION in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

- I2C or IIC stands for Inter-Integrated Circuit, a serial communication protocol made by Philips Semiconductor (now NXP Semiconductor) in 1982 .
- It is designed for communication between chips on the same Printed Circuit Board (PCB) or within a short distance .
- It is a synchronous, multi-master/multi-slave, packet switched, single-ended, serial communication bus.
- It uses two bidirectional lines, Serial Data Line (SDA) and Serial Clock Line (SCL), to transfer data between devices  .
- The SCL line is controlled by the master device, which generates the clock signal to synchronize the data transfer .
- The SDA line carries the data bits, one bit per clock pulse, and can be driven by either the master or the slave device, depending on the direction of the data transfer .
- Each device on the I2C bus has a unique address, usually 7-bit or 10-bit, that is used to identify it during communication  .
- The I2C protocol supports multiple masters and multiple slaves, but only one master and one slave can communicate at a time .
- The I2C protocol uses special signals, such as start and stop conditions, to initiate and terminate a data transfer  .
- The I2C protocol also uses an acknowledge bit (ACK) or a not acknowledge bit (NACK) to indicate the status of the data transfer  .
- The I2C protocol is widely used for connecting sensors, memory devices, LCD displays, and other peripherals to microcontrollers, such as Arduino .
- The I2C protocol has several advantages, such as simplicity, flexibility, low power consumption, and low cost  .
- The I2C protocol also has some limitations, such as low speed, limited range, and susceptibility to noise  .