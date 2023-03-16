### Unit 2 - SOFTWARE HARDWARE FRAMEWORKS
#### Serial UART Communication

- UART stands for Universal Asynchronous Receiver/Transmitter.
- It is a hardware device for asynchronous serial communication.
- The electric signaling levels and methods are handled by a driver circuit external to the UART.
- A UART is usually an individual integrated circuit used for serial communications over a computer or peripheral device serial port.
- UARTs are now commonly included in microcontrollers.
- A UART is used to convert the data between parallel and serial forms.
- UART transmit data serially, one bit at a time, over a single communication line to a receiver.
- The data format and transmission speeds are configurable.
- The UART usually does not directly generate or receive the external signals used between different items of equipment.
- Instead, the signals are typically input to or output from the UART from or to an external device, such as an RS-232 line driver or receiver.
- The UART takes bytes of data and transmits the individual bits in a sequential fashion.
- At the destination, a second UART re-assembles the bits into complete bytes.
- Each UART contains a shift register, which is the fundamental method of conversion between serial and parallel forms.
- Serial transmission of digital information (bits) through a single wire or other medium is less costly than parallel transmission through multiple wires.
- The UART usually generates an interrupt signaling the CPU that new data has been received and is ready for processing.
- The CPU can then read the data from the UART and process it as needed.
- UARTs are commonly used in conjunction with communication standards such as EIA, RS-232, RS-422 or RS-485.
- The universal designation indicates that the data format and transmission speeds are configurable and that the actual electric signaling levels and methods typically are handled by a special driver circuit external to the UART.