### Serial Peripheral Interface

- Serial Peripheral Interface (SPI) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems.
- SPI is a four-wire bus that consists of a serial clock (SCK), master output/slave input (MOSI), master input/slave output (MISO), and a device select (SS) pin.
- SPI is a full-duplex interface, meaning that data can be sent and received simultaneously.
- SPI is a master-slave interface, meaning that one device (the master) initiates and controls the communication with one or more devices (the slaves).
- SPI does not have a standard protocol or format, meaning that the data transfer rate, mode, bit order, and frame size can vary depending on the devices involved.
- SPI has four modes of operation, determined by the polarity and phase of the clock signal. The modes are numbered from 0 to 3 and are defined by the following parameters:

| Mode | Clock Polarity (CPOL) | Clock Phase (CPHA) | Data Capture Edge | Data Output Edge |
|------|-----------------------|--------------------|-------------------|------------------|
| 0    | 0                     | 0                  | Rising            | Falling          |
| 1    | 0                     | 1                  | Falling           | Rising           |
| 2    | 1                     | 0                  | Falling           | Rising           |
| 3    | 1                     | 1                  | Rising            | Falling          |

- SPI has several advantages over other serial interfaces, such as high speed, simplicity, flexibility, and full-duplex capability.
- SPI also has some disadvantages, such as lack of error detection, lack of flow control, lack of addressing, and limited number of devices.