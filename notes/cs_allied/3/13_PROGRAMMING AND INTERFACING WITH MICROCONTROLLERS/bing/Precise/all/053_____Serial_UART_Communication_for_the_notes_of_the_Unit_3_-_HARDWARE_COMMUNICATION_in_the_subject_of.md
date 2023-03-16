# Unit 3 - HARDWARE COMMUNICATION: Serial UART Communication

- UART stands for Universal Asynchronous Receiver/Transmitter.
- It is a hardware device used for asynchronous serial communication between two devices.
- Asynchronous communication means that data is transmitted without a clock signal, and the sender and receiver rely on an agreed-upon data rate to synchronize their communication.
- UARTs transmit data in a serial format, meaning one bit at a time, with a start bit, a configurable number of data bits, an optional parity bit, and one or more stop bits.
- The start bit signals the beginning of a new data frame, and the stop bit signals the end of the frame.
- The parity bit is used for error detection and can be set to even, odd, or none.
- UARTs are commonly used for communication between microcontrollers and peripherals, such as sensors, displays, and other microcontrollers.
- They are also used for communication between a microcontroller and a computer, for example, for debugging or uploading code.
- UARTs can be implemented in hardware or software, and many microcontrollers have built-in hardware UARTs.
- The data rate, or baud rate, of a UART is configurable and is typically between 300 and 115200 bits per second.
- The data rate must be the same for both the sender and receiver for communication to be successful.
- UART communication is half-duplex, meaning that data can be transmitted in one direction at a time.
- Some UARTs support full-duplex communication, where data can be transmitted and received simultaneously.
- UARTs can be connected in a point-to-point configuration, where one sender is connected to one receiver, or in a multi-drop configuration, where multiple devices share a common communication line.
- In a multi-drop configuration, only one device can transmit at a time, and the other devices must listen for their turn to transmit.
- UART communication is widely used due to its simplicity, flexibility, and low cost.
