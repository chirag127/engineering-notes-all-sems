### Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter**  .
- It is a **serial communication device** that performs parallel-to-serial and serial-to-parallel data conversion .
- It is **universal** because the parameters like transfer speed, data speed, etc. are configurable .
- It is **asynchronous** because there is no clock signal to synchronize the output bits from the transmitting device to the receiving device .
- A UART is usually an individual or part of an integrated circuit (IC) used for serial communications over a computer or peripheral device serial port.
- One or more UART peripherals are commonly integrated in microcontroller chips.
- Specialised UARTs are used for automobiles, smart cards and SIMs.
- A UART typically consists of a **transmitter** and a **receiver**  .
- The transmitter converts parallel data from a data bus into a serial stream of bits and sends it to the receiver  .
- The receiver converts the serial stream of bits back into parallel data and puts it on a data bus  .
- The transmitter and receiver operate independently of each other, but they must have the same baud rate, data bits, parity bits and stop bits settings  .
- The baud rate is the number of bits per second that are transmitted or received  .
- The data bits are the number of bits that represent the actual data in each frame  .
- The parity bit is an optional bit that is used for error detection  .
- The stop bit is a bit that indicates the end of a frame  .
- A frame is a unit of data that consists of a start bit, data bits, parity bit and stop bit  .
- A start bit is a bit that indicates the beginning of a frame  .
- A UART uses two wires for communication: **RX** and **TX**  .
- RX stands for **receive** and TX stands for **transmit**  .
- The RX pin of one device is connected to the TX pin of another device, and vice versa  .
- A UART can communicate with another UART directly, or with other devices that use serial protocols like RS-232, RS-485, SPI, I2C, etc  .
- A UART can also communicate with a computer through a USB-to-serial converter  .
- A UART can be used for various applications, such as data logging, debugging, wireless communication, GPS, etc  .

: https://www.electronicshub.org/basics-uart-communication/
: https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter
: https://www.codrey.com/embedded-systems/uart-serial-communication-rs232/
: https://www.analog.com/en/analog-dialogue/articles/uart-a-hardware-communication-protocol.html
: https://learn.sparkfun.com/tutorials/serial-communication/all