### Inter-Integrated Circuit

- Inter-Integrated Circuit (I2C) is a serial communication protocol that allows multiple devices to communicate with each other using only two wires: a clock line (SCL) and a data line (SDA)     .
- I2C was invented by Philips Semiconductor (now NXP Semiconductors) in 1982 and is widely used in applications where low cost and ease of implementation are more important than high speed  .
- I2C can support up to 1008 slave devices and multiple masters on the same bus, which can operate at different speeds ranging from 100 kbps to 5 Mbps  .
- I2C uses a 7-bit or 10-bit address to identify each device on the bus and a read/write bit to indicate the direction of data transfer  .
- I2C uses an acknowledge (ACK) or not acknowledge (NACK) mechanism to confirm the reception of data or to signal the end of transmission  .
- I2C uses a start (S) and a stop (P) condition to initiate and terminate a data transfer, and a repeated start (Sr) condition to switch the direction of data transfer without releasing the bus  .
- I2C uses arbitration and synchronization techniques to ensure that only one master can control the bus at a time and that all devices are synchronized to the same clock signal  .
- I2C is suitable for connecting low-speed peripherals such as sensors, EEPROMs, LCDs, and RTCs to a microcontroller or a microprocessor  .