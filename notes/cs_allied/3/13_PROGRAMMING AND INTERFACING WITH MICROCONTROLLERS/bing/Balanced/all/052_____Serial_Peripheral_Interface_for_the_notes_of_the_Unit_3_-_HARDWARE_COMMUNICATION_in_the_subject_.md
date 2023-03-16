# Serial Peripheral Interface

- Serial Peripheral Interface (SPI) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems.
- SPI is a four-wire bus that consists of a serial clock (SCK), master output/slave input (MOSI), master input/slave output (MISO), and a device select (SS) pin.
- SPI is a full-duplex interface, meaning that data can be sent and received simultaneously.
- SPI is a master-slave interface, meaning that one device (the master) initiates and controls the communication with one or more devices (the slaves).
- SPI does not have a standard protocol or format, meaning that the data transfer rate, mode, bit order, and frame size can vary depending on the devices involved.
- SPI has four modes of operation, determined by the polarity and phase of the clock signal. The modes are numbered from 0 to 3 and are defined by the following parameters:

| Mode | Clock Polarity (CPOL) | Clock Phase (CPHA) | Data Capture Edge | Data Shift Edge |
|------|-----------------------|--------------------|-------------------|-----------------|
| 0    | 0                     | 0                  | Rising            | Falling         |
| 1    | 0                     | 1                  | Falling           | Rising          |
| 2    | 1                     | 0                  | Falling           | Rising          |
| 3    | 1                     | 1                  | Rising            | Falling         |

- SPI communication involves the following steps:
  - The master selects the slave device by pulling the SS line low.
  - The master generates the clock signal on the SCK line.
  - The master and the slave exchange data by shifting bits on the MOSI and MISO lines.
  - The master deselects the slave device by pulling the SS line high.

- SPI has some advantages and disadvantages compared to other serial interfaces, such as:
  - Advantages:
    - High data transfer rate, up to 80 MHz.
    - Simple hardware and software implementation.
    - Full-duplex communication.
    - Multiple slave devices can be connected to a single master device using separate SS lines.
  - Disadvantages:
    - No error detection or correction mechanism.
    - No flow control or acknowledgement mechanism.
    - No standard protocol or format, requiring device-specific configuration.
    - Requires more wires and pins than other interfaces, such as I2C or UART.