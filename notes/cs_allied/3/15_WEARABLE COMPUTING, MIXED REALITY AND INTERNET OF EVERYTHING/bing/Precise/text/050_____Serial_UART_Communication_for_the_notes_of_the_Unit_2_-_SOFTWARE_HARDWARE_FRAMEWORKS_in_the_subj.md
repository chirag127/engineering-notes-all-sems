### Serial UART Communication

- UART stands for Universal Asynchronous Receiver/Transmitter.
- It is a hardware device for asynchronous serial communication between devices.
- UARTs transmit data asynchronously, meaning there is no clock signal to synchronize the output of bits from the transmitting UART to the sampling of bits by the receiving UART.
- Instead of a clock signal, the transmitting UART adds start and stop bits to the data packet being transferred. These bits define the beginning and end of the data packet so the receiving UART knows when to start reading the bits.
- The receiving UART samples the data line at a specific rate, known as the baud rate, to determine the value of each bit.
- The baud rate is the rate at which information is transferred in a communication channel. It is usually expressed in bits per second (bps).
- The start bit is always a logic low (0) level and the stop bit is always a logic high (1) level.
- The data packet is framed by the start and stop bits, and the data within the frame is transmitted least significant bit (LSB) first.
- UARTs can be configured to transmit and receive different data packet sizes, typically between 5 and 8 bits.
- Parity bits can also be added to the data packet for error detection.
- UARTs are commonly used in microcontroller-based systems to communicate with other devices, such as computers, sensors, and other microcontrollers.
- UART communication can be implemented using hardware or software, with hardware implementations typically being faster and more reliable.
- Common applications of UART communication include GPS receivers, Bluetooth modules, and wireless radio frequency (RF) modules.