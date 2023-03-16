# Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter** .
- It is a **serial communication device** that performs parallel-to-serial and serial-to-parallel data conversion .
- It is **universal** because the parameters like transfer speed, data speed, etc. are configurable .
- It is **asynchronous** because there is no clock signal to synchronize the output bits from the transmitting device to the receiving device .
- A UART typically consists of a **transmitter**, a **receiver**, a **data bus**, a **baud rate generator**, and some **control registers** .
- The transmitter and receiver use **start bits**, **stop bits**, and **parity bits** to frame the data and ensure error-free transmission  .
- The data bus connects the UART to the **microcontroller** or the **peripheral device** that uses the serial communication .
- The baud rate generator produces a **clock signal** that determines the **bit rate** or the number of bits per second that can be transmitted or received .
- The control registers store the **configuration settings** and the **status flags** of the UART .
- UART communication can be **full-duplex** or **half-duplex**, depending on whether the data can be sent and received simultaneously or alternately .
- UART communication can be used for various applications, such as **automobiles**, **smart cards**, **SIMs**, **GPS modules**, **Bluetooth modules**, **Wi-Fi modules**, etc  .