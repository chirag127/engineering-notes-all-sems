
### Serial Peripheral Interface (SPI)

- SPI is a type of synchronous serial communication protocol used to communicate between microcontrollers and peripheral devices. 
- SPI uses four wires to establish communication between two devices: a clock line (SCLK), a master-out-slave-in line (MOSI), a master-in-slave-out line (MISO), and a chip select line (SS). 
- The master device controls the clock line and sends data to the slave device on the MOSI line. The slave device sends data to the master device on the MISO line. 
- The chip select line is used to select the slave device that will receive or send data. 
- SPI is a full-duplex protocol, meaning that data can be sent and received simultaneously. 
- SPI is a popular protocol because it is simple to implement and requires few wires. It is also faster than other synchronous serial protocols such as I2C.