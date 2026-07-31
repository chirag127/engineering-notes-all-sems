### I2C/IIC for the notes of the Unit 3 - HARDWARE COMMUNICATION in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

I2C, also known as IIC, stands for Inter-Integrated Circuit, which is a serial communication protocol initially developed by Philips Semiconductors (now NXP Semiconductors). It is widely used in embedded systems, especially in microcontrollers.

Here are some important points to keep in mind when working with I2C/IIC:

- I2C requires two lines: SDA (Serial Data) and SCL (Serial Clock). SDA is used for transferring data between the master and slave devices, while SCL is used to synchronize the transfer.
- I2C supports multiple devices on the same bus. Each device is identified by a unique address. The address can be 7-bit or 10-bit, depending on the device's capability.
- I2C communication is initiated by the master device. The master device generates the clock signal on the SCL line and sends the start condition (S) to indicate the beginning of the communication.
- The master device sends the slave address along with the read/write bit to indicate the direction of the transfer. If the read/write bit is 0, it means the master is writing to the slave device, and if it is 1, it means the master is reading from the slave device.
- After receiving the slave address, the slave device sends an acknowledgement (ACK) bit to indicate that it has been addressed. If the slave device is not present on the bus, it will not respond, and the master device will detect a NACK (Not ACKnowledge) condition.
- The master device sends the data byte to the slave device, and the slave device sends an ACK bit for each received byte. If the slave device cannot receive any more data, it will send a NACK bit instead.
- After sending all the data bytes, the master device sends a stop condition (P) to indicate the end of the communication.

In summary, I2C is a simple and efficient way of communicating between multiple devices in a microcontroller system. Understanding its principles is essential for anyone working with embedded systems.