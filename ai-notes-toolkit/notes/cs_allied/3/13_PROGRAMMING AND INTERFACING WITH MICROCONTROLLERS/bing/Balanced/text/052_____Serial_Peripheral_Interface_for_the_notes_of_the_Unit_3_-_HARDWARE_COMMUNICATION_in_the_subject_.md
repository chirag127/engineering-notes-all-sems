### Serial Peripheral Interface

- Serial Peripheral Interface (SPI) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems.
- SPI is a four-wire bus that consists of a serial clock (SCK), master output/slave input (MOSI), master input/slave output (MISO), and a device select (SS) pin .
- SPI is a full-duplex interface, meaning that data can be sent and received simultaneously.
- SPI is a master-slave interface, meaning that one device (the master) initiates and controls the communication with one or more devices (the slaves).
- SPI does not have a standard protocol or format, meaning that the data transfer rate, clock polarity, clock phase, and data order can vary depending on the devices involved .
- SPI is a simple and fast interface, but it requires more pins and wires than other interfaces such as I2C or UART.
- SPI is commonly used to communicate with peripherals such as sensors, ADCs, DACs, shift registers, SRAM, and SD cards  .

: https://en.wikipedia.org/wiki/Serial_Peripheral_Interface
: https://www.sciencedirect.com/topics/computer-science/serial-peripheral-interface
: https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all
: https://www.analog.com/en/analog-dialogue/articles/introduction-to-spi-interface.html