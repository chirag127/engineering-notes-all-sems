# Inter-Integrated Circuit

- Inter-Integrated Circuit (I2C) is a serial communication protocol that allows multiple devices to communicate with each other using only two wires: a clock line (SCL) and a data line (SDA)    .
- I2C was invented by Philips Semiconductor (now NXP Semiconductors) in 1982 and is widely used in applications where low cost and ease of implementation are more important than high speed  .
- I2C can support up to 1008 slave devices on the same bus, each with a unique address . I2C can also support multiple masters, which can arbitrate the bus access and avoid collisions .
- I2C uses a packet-based data transfer, where each packet consists of a start condition, an address byte, one or more data bytes, and a stop condition . The address byte contains the 7-bit address of the slave device and a read/write bit. The data bytes contain the information to be transmitted or received.
- I2C operates in four modes: standard mode (up to 100 kbit/s), fast mode (up to 400 kbit/s), fast mode plus (up to 1 Mbit/s), and high-speed mode (up to 3.4 Mbit/s) . The mode is determined by the clock frequency and the pull-up resistors on the bus lines.
- I2C has several advantages over other serial communication protocols, such as SPI and UART, such as:
  - Simpler hardware and wiring, as only two wires are needed  .
  - Higher scalability, as more devices can be added to the bus without increasing the number of wires  .
  - Lower power consumption, as the bus lines are open-drain and only pull low when active  .
  - Higher reliability, as the bus lines have built-in noise immunity and error detection  .
- I2C also has some disadvantages, such as:
  - Lower speed, as the bus is shared by multiple devices and the clock frequency is limited by the capacitance of the bus lines  .
  - Higher complexity, as the protocol requires more software and logic to handle the addressing, arbitration, and acknowledgment  .
  - Limited distance, as the bus lines have a maximum length of about 1 meter  .
- I2C is widely used in microcontroller-based systems, such as sensors, displays, EEPROMs, RTCs, ADCs, DACs, and other peripherals   . I2C is also used in some higher-level applications, such as HDMI, SMBus, and PMBus .