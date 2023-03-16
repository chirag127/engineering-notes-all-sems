# Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter** .
- It is a **serial communication device** that performs parallel-to-serial and serial-to-parallel data conversion .
- It is **universal** because the parameters like transfer speed, data speed, etc. are configurable.
- It is **asynchronous** because there is no clock signal to synchronize the output bits from the transmitter to the receiver.
- A UART usually consists of a **transmitter**, a **receiver**, a **data bus**, and some **control pins** .
- The transmitter and receiver use **start bits**, **stop bits**, and **parity bits** to frame the data and ensure its integrity  .
- The transmitter and receiver must agree on the **baud rate**, the **number of data bits**, the **parity mode**, and the **number of stop bits** before communication  .
- UARTs are commonly integrated in **microcontroller chips** and used for serial communication with other devices, such as computers, peripherals, sensors, etc.  .
- UARTs can also communicate with other UARTs directly, using **RS-232**, **RS-485**, or **TTL** voltage levels  .
- UARTs are widely used for **full-duplex** serial communication, which means data can be transmitted and received simultaneously  .