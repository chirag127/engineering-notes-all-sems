### I2C/IIC

- I2C stands for Inter-Integrated Circuit. It is a serial communication protocol for exchanging data between multiple devices on a single bus .
- It was originally designed by Philips Semiconductor in 1982  and is now widely used for short-distance communication in embedded systems, sensors, microcontrollers, etc.
- It is a half-duplex, bi-directional, two-wire bus system that uses a clock line (SCL) and a data line (SDA) to transmit and receive data .
- It supports multiple masters and multiple slaves, where each device has a unique 7-bit or 10-bit address  .
- It uses a start condition (S) and a stop condition (P) to initiate and terminate a data transfer, and an acknowledge bit (ACK) or a not-acknowledge bit (NACK) to indicate the status of the communication  .
- It operates in four modes: standard mode (up to 100 kbit/s), fast mode (up to 400 kbit/s), fast mode plus (up to 1 Mbit/s), and high-speed mode (up to 3.4 Mbit/s) .
- It has several advantages, such as simplicity, low cost, low power consumption, noise immunity, and scalability  .
- It also has some limitations, such as limited speed, limited bus length, limited number of devices, and arbitration issues  .