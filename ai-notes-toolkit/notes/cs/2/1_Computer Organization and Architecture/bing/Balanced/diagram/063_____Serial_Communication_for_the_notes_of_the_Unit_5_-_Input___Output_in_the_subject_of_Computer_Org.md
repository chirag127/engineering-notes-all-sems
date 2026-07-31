### Serial Communication

Serial communication is the process of sequentially transferring the information/bits on the same channel. Due to this, the cost of wire will be reduced, but it slows the transmission speed. Serial communication is used for all long-haul communication and most computer networks, where the parallel communication is impractical. Serial communication can either be asynchronous or synchronous.

- **Asynchronous serial communication** is the method of transmitting data without a clock signal. The sender and the receiver agree on a common bit rate and use start and stop bits to indicate the beginning and the end of a data frame. Asynchronous serial communication is simple and widely used, but it has more overhead and less reliability than synchronous serial communication.
- **Synchronous serial communication** is the method of transmitting data with a clock signal. The sender and the receiver synchronize their clocks and use a single wire or a pair of wires to transfer data. Synchronous serial communication has less overhead and more reliability than asynchronous serial communication, but it requires more hardware and wiring.

Some of the well-known interfaces used for serial communication are:

- **RS-232** is a standard for serial communication between a computer and a peripheral device, such as a modem or a printer. RS-232 uses a single-ended signaling, which means that the voltage level of a wire is referenced to a common ground. RS-232 can support up to 25 wires, but only three are essential: transmit data (TX), receive data (RX), and ground (GND). RS-232 has a limited range of up to 15 meters and a maximum bit rate of 20 kbps.
- **RS-485** is a standard for serial communication between multiple devices on a network. RS-485 uses a differential signaling, which means that the voltage level of a wire is referenced to another wire. RS-485 can support up to 32 devices on a single pair of wires, and up to 256 devices with repeaters. RS-485 has a longer range of up to 1200 meters and a higher bit rate of up to 10 Mbps.
- **I2C** is a standard for serial communication between multiple devices on a bus. I2C uses a two-wire interface: serial data (SDA) and serial clock (SCL). I2C can support up to 128 devices on a single bus, and each device has a unique address. I2C has a moderate range of up to 10 meters and a variable bit rate of up to 3.4 Mbps.
- **SPI** is a standard for serial communication between a master device and one or more slave devices on a bus. SPI uses a four-wire interface: serial data out (MOSI), serial data in (MISO), serial clock (SCK), and chip select (CS). SPI can support multiple devices on a single bus, but each device needs a separate CS line. SPI has a short range of up to 2 meters and a high bit rate of up to 50 Mbps.

A data communication processor is an I/O processor that distributes and collects data from numerous remote terminals connected through telephone and other communication lines to the computer. It is a specialized I/O processor designed to communicate with data communication networks. A data communication processor can perform the following functions:

- **Line control** is the function of establishing, maintaining, and terminating the communication lines between the terminals and the computer.
- **Data formatting** is the function of converting the data from the format used by the terminal to the format used by the computer, and vice versa.
- **Error control** is the function of detecting and correcting the errors that may occur during the data transmission.
- **Flow control** is the function of regulating the amount of data that can be sent or received by the terminal or the computer.
- **Routing** is the function of selecting the best path for the data to travel from the source to the destination.
- **Buffering** is the function of temporarily storing the data in the memory until it is ready to be sent or received.

The following diagram shows the serial communication between a computer and a terminal using a data communication processor:

![Serial communication diagram](https://i.imgur.com/8aZx7Qy.png)

: Serial Communication in Computer organization - javat