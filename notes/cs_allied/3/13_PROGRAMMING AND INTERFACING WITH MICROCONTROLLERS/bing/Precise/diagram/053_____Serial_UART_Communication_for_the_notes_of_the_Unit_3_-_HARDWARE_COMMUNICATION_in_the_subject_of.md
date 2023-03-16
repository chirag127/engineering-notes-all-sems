### Unit 3 - HARDWARE COMMUNICATION: Serial UART Communication

- UART stands for Universal Asynchronous Receiver/Transmitter.
- It is a hardware device that translates data between parallel and serial forms.
- UARTs are commonly used in conjunction with communication standards such as RS-232, RS-422 or RS-485.
- Data is transmitted and received asynchronously, meaning there is no clock signal to synchronize the output and input of data.
- Instead, the transmitting UART adds start and stop bits to the data packet being transmitted.
- The receiving UART uses these bits to determine when the data packet starts and ends.
- The data is transmitted serially, one bit at a time, over a single communication line or pair of lines.
- UARTs are commonly used for serial communication between devices, such as between a computer and a peripheral device like a mouse or modem.
- UARTs can also be used for communication between two microcontrollers or between a microcontroller and a peripheral device.
- UART communication can be full-duplex, meaning data can be transmitted and received simultaneously, or half-duplex, meaning data can only be transmitted or received at any given time.
- The baud rate, or data transfer rate, of a UART is determined by the frequency of the clock signal used to drive the UART and the number of data bits, stop bits, and parity bits used in the data packet.
- Common baud rates for UART communication include 9600, 19200, 38400, 57600, and 115200 bits per second.