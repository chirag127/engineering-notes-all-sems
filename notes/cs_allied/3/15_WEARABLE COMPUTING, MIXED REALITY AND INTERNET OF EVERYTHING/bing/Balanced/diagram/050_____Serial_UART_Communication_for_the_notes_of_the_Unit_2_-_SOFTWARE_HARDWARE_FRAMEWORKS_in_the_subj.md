### Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter** .
- It is a **serial communication device** that performs parallel-to-serial and serial-to-parallel data conversion .
- It is **universal** because the parameters like transfer speed, data speed, etc. are configurable .
- It is **asynchronous** because there is no clock signal to synchronize the output bits from the transmitting device to the receiving device .
- A UART usually consists of a **transmitter**, a **receiver**, a **data bus**, and some **control pins** .
- The transmitter and receiver use **start bits**, **stop bits**, and **parity bits** to frame the data and ensure its integrity  .
- The transmitter and receiver must agree on the **baud rate**, which is the number of bits per second, and the **data format**, which is the number of data bits, parity bits, and stop bits per frame  .
- UARTs are commonly integrated in **microcontroller chips** and used for serial communication with other devices, such as computers, peripherals, smart cards, and automobiles  .
- UARTs can also communicate with each other directly, as long as they share the same ground and voltage levels .
- UARTs are widely used for **full-duplex serial communication**, which means that data can be transmitted and received simultaneously .