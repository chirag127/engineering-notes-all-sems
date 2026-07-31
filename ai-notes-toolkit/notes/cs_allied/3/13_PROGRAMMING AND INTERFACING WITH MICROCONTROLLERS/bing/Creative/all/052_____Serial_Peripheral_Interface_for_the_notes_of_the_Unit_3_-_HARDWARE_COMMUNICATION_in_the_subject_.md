# Serial Peripheral Interface

- Serial Peripheral Interface (SPI) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems.
- SPI is a four-wire bus that consists of a serial clock (SCK), master output/slave input (MOSI), master input/slave output (MISO), and a device select (SS) pin.
- SPI is a full-duplex interface, meaning that data can be sent and received simultaneously.
- SPI is a master-slave interface, meaning that one device (the master) initiates and controls the communication with one or more devices (the slaves).
- SPI does not have a standard protocol or format, meaning that the data transfer rate, data order, data length, and mode of operation can vary depending on the devices involved.
- SPI has four modes of operation, determined by the polarity and phase of the clock signal. The modes are numbered from 0 to 3, and each mode defines when the data is sampled and when it is shifted.
- SPI is a simple and fast interface that can achieve speeds up to 80 MHz. However, SPI also has some limitations, such as the need for a separate SS line for each slave device, the lack of error detection and correction, and the lack of flow control.