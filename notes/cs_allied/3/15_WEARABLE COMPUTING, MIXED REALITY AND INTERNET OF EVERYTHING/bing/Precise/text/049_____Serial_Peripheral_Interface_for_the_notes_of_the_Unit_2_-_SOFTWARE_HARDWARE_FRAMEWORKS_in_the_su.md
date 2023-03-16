### Serial Peripheral Interface

Serial Peripheral Interface (SPI) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems. It is a full-duplex, master-slave communication protocol.

- SPI uses four signal lines: Master Out Slave In (MOSI), Master In Slave Out (MISO), Serial Clock (SCK), and Slave Select (SS).
- The master device initiates the communication and controls the clock signal.
- Data is transmitted between the master and slave devices in 8-bit packets.
- The clock polarity (CPOL) and clock phase (CPHA) can be configured to support different communication modes.
- SPI is commonly used for communication with sensors, memory devices, and display controllers.