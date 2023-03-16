### Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter**  .
- It is a **serial communication device** that performs parallel-to-serial and serial-to-parallel data conversion .
- It is **universal** because the parameters like transfer speed, data speed, etc. are configurable .
- It is **asynchronous** because there is no clock signal to synchronize the output bits from the transmitting device to the receiving device.
- A UART is usually an individual or part of an integrated circuit (IC) used for serial communications over a computer or peripheral device serial port.
- One or more UART peripherals are commonly integrated in microcontroller chips.
- Specialised UARTs are used for automobiles, smart cards and SIMs.
- A UART consists of a **transmitter** and a **receiver**  .
- The transmitter converts parallel data from a data bus into serial data and transmits it to the receiver  .
- The receiver converts serial data from the transmitter into parallel data and sends it to the data bus  .
- The transmitter and the receiver operate independently of each other  .
- The transmitter and the receiver use the same baud rate (bits per second) and data format (number of bits, parity, stop bits) to communicate  .
- The transmitter and the receiver use two wires: **TX** (transmit) and **RX** (receive).
- The TX wire of the transmitter is connected to the RX wire of the receiver, and vice versa.
- The transmitter and the receiver can also use additional wires for flow control, such as **RTS** (request to send) and **CTS** (clear to send).
- UART communication can be **full-duplex** (both devices can transmit and receive at the same time) or **half-duplex** (only one device can transmit or receive at a time) .
- UART communication can be **point-to-point** (between two devices) or **point-to-multipoint** (between one device and multiple devices) .
- UART communication can be **synchronous** (using a clock signal) or **asynchronous** (using start and stop bits) .
- UART communication is widely used for low-speed data transfer between devices, such as sensors, modems, GPS modules, etc. .

: https://www.electronicshub.org/basics-uart-communication/
: https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter
: https://www.codrey.com/embedded-systems/uart-serial-communication-rs232/
: https://www.analog.com/en/analog-dialogue/articles/uart-a-hardware-communication-protocol.html
: https://learn.sparkfun.com/tutorials/serial-communication/all