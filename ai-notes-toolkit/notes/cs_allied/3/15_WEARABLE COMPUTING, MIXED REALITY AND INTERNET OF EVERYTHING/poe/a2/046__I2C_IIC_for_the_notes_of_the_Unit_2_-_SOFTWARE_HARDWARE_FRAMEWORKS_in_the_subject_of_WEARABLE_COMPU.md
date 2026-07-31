 Here are the notes on I2C/IIC for the given topic:

### I2C/IIC

- I2C stands for Inter-Integrated Circuit.
- It is a serial communication protocol for connecting low-speed peripherals to a microcontroller.
- It uses only 2 wires: SDA (Serial Data Line) and SCL (Serial Clock Line).
- I2C devices have addresses that are used to identify them on the bus. A master device (usually a microcontroller) communicates with slave devices (sensors, memory chips, etc.) by sending out the slave address and reading/writing data.
- I2C is a multi-master bus, so more than one master device can be connected to the same bus. However, bus arbitration is required to prevent data corruption if two masters initiate a data transfer at the same time.
- I2C is a low-speed protocol with standard modes of 100 kbit/s (fast mode) and 10 kbit/s (standard mode). Some devices support high-speed mode of up to 3.4 Mbit/s.
- The advantages of I2C are:
  - Few wires (only 2)
  - Can have multiple slaves
  - Standardized protocol
  - Low cost
- The disadvantages are:
  - Limited speed compared to SPI
  - There is a limited number of unique addresses, so the number of connectable devices is limited

Notes:
- Be formal and don't include emojis/external links
- Content is written in Markdown format with headers
- Points are used for easy reading