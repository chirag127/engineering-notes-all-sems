### Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter**  .
- It is a **serial communication device** that performs parallel-to-serial and serial-to-parallel data conversion .
- It is **universal** because the parameters like transfer speed, data speed, etc. are configurable .
- It is **asynchronous** because there is no clock signal to synchronize the output bits from the transmitting device to the receiving device .
- A UART typically consists of a **transmitter** and a **receiver** that communicate using two wires: **TX** and **RX**  .
- The transmitter and receiver must agree on the **baud rate**, which is the number of bits per second, and the **data format**, which includes the number of data bits, parity bits, and stop bits  .
- The transmitter sends a **start bit** to indicate the beginning of a data frame, followed by the data bits, the optional parity bit, and the stop bit(s) to indicate the end of the frame  .
- The receiver detects the start bit and samples the data bits at the middle of each bit period, using the parity bit to check for errors and the stop bit(s) to confirm the end of the frame  .
- A UART can be implemented as an individual or part of an integrated circuit (IC), or as a software module in a microcontroller  .
- UARTs are commonly used for serial communication over a computer or peripheral device serial port, or for connecting devices such as automobiles, smart cards, and SIMs  .