### Serial Peripheral Interface

- Serial Peripheral Interface (SPI) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems.
- SPI is a four-wire bus that consists of a serial clock (SCK), master output/slave input (MOSI), master input/slave output (MISO), and a device select (SS) pin.
- SPI is commonly used to send data between microcontrollers and small peripherals such as sensors, ADCs, DACs, shift registers, SRAM, and SD cards.
- SPI is a full-duplex interface, meaning that data can be sent and received simultaneously.
- SPI is a master-slave interface, meaning that one device (the master) initiates and controls the communication with one or more devices (the slaves).
- SPI does not have a standard protocol or format, meaning that the data transfer rate, mode, bit order, and frame size can vary depending on the devices involved.
- SPI has four modes of operation, determined by the polarity and phase of the clock signal. The modes are numbered from 0 to 3, and each mode defines when the data is sampled and when it is shifted.
- SPI has a device select (SS) pin that is used to select the slave device that the master wants to communicate with. The SS pin is usually active low, meaning that it is pulled low to enable the slave and pulled high to disable it.
- SPI can support multiple slaves using either individual SS pins for each slave, or a daisy-chain configuration where the MISO of one slave is connected to the MOSI of the next slave.
- SPI is a simple and fast interface that can achieve speeds up to 80 MHz, but it also has some limitations, such as the need for more wires, the lack of error detection, and the lack of flow control.