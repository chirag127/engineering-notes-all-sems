### I2C/IIC for the notes of the Unit 3 - HARDWARE COMMUNICATION in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

- I2C or IIC stands for Inter-Integrated Circuit, a serial communication protocol made by Philips Semiconductor (now NXP Semiconductor) in 1982 .
- It is designed for communication between chips on the same Printed Circuit Board (PCB) or within a short distance .
- It is a synchronous, multi-master/multi-slave, packet switched, single-ended, serial communication bus.
- It uses two bidirectional lines, Serial Data Line (SDA) and Serial Clock Line (SCL), to transfer data between devices  .
- The SCL line is controlled by the master device, which generates the clock signal to synchronize the data transfer  .
- The SDA line is used to send and receive data bits, one bit per clock pulse  .
- The data transfer is initiated by the master device, which sends a start condition, followed by the 7-bit address of the slave device and a read/write bit  .
- The slave device acknowledges the address by pulling the SDA line low for one clock pulse  .
- The master device then sends or receives data bytes, each followed by an acknowledge bit from the slave device  .
- The data transfer is terminated by the master device, which sends a stop condition  .
- The I2C protocol supports multiple masters and slaves on the same bus, as well as 10-bit addressing and clock stretching .
- The I2C protocol is widely used for connecting sensors, memory devices, LCDs, and other peripherals to microcontrollers, such as Arduino  .