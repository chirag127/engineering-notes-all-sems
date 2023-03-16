# Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter**  .
- It is a **serial communication device** that performs parallel-to-serial and serial-to-parallel data conversion .
- It is **universal** because the parameters like transfer speed, data speed, etc. are configurable .
- It is **asynchronous** because there is no clock signal to synchronize the output bits from the transmitting device to the receiving device .
- A UART typically consists of a **transmitter** and a **receiver** that operate independently of each other  .
- The transmitter and receiver use **start bits**, **stop bits**, and **parity bits** to frame the data and ensure reliable communication   .
- The transmitter and receiver must agree on the **baud rate**, which is the number of bits per second transmitted or received   .
- A UART can communicate with other devices using different protocols, such as **RS-232**, **RS-485**, **SPI**, **I2C**, etc  .
- A UART is usually an individual or part of an integrated circuit (IC) used for serial communication over a computer or peripheral device serial port.
- One or more UART peripherals are commonly integrated in microcontroller chips.
- Specialized UARTs are used for automobiles, smart cards, and SIMs.