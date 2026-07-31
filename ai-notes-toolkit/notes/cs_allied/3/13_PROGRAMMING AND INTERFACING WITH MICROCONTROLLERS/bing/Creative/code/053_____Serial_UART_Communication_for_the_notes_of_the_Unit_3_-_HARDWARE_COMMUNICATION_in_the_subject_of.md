# Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter**  .
- It is a **serial communication device** that performs **parallel-to-serial** and **serial-to-parallel** data conversion .
- It is **universal** because the parameters like **transfer speed**, **data speed**, **parity bit**, etc. are **configurable**  .
- It is **asynchronous** because there is **no clock signal** to synchronize the output bits from the transmitting device to the receiving device .
- It uses two wires: **RX** (receive) and **TX** (transmit).
- It can communicate with **one or more** devices using **point-to-point** or **point-to-multipoint** connections .
- It follows a **protocol** that defines the **format**, **timing**, and **error detection** of the data frames  .
- A data frame consists of a **start bit**, **data bits**, **parity bit** (optional), and **stop bit**  .
- The start bit indicates the beginning of a data frame and is always **low**  .
- The data bits carry the actual information and can be **5 to 9 bits** long  .
- The parity bit is used for **error detection** and can be **even**, **odd**, or **none**  .
- The stop bit indicates the end of a data frame and is always **high**  .
- The baud rate is the **number of bits per second** that can be transmitted or received  .
- The baud rate must be **same** for both the transmitter and the receiver to avoid **data corruption**  .
- A UART is usually an **individual** or **part of an** integrated circuit (IC) used for serial communication over a computer or peripheral device serial port.
- One or more UART peripherals are commonly integrated in **microcontroller** chips.
- Specialized UARTs are used for **automobiles**, **smart cards**, and **SIMs**.