### I/O Channels and Processors

- I/O channels are extensions of the DMA concept that have the ability to execute I/O instructions using special-purpose processors on I/O channels and complete control over I/O operations .
- The processor does not execute I/O instructions itself, but initiates I/O transfer by instructing the I/O channel to execute a program in memory .
- I/O channels are independent hardware components that coordinate all I/O to a set of controllers .
- I/O channels use separate, independent and low-cost processors for their functioning, which are called channel processors .
- Channel processors are simple, but contain sufficient memory to handle all I/O tasks.
- When I/O transfer is complete or an error is detected, the channel controller communicates with the CPU using an interrupt, and informs the CPU about the error or the task completion.
- Each channel supports one or more controllers or devices.
- There are different types of I/O channels, such as byte multiplexer, block multiplexer, selector, and multiplexor .
- Byte multiplexer is used for low-speed devices, and transmits or accepts characters, interleaving bytes from several devices .
- Block multiplexer is used for high-speed devices, and accepts or transmits blocks of characters, interleaving blocks of bytes from several devices .
- Selector is used for high-speed devices, and transfers data between a single device and memory without interleaving .
- Multiplexor is used for high-speed devices, and transfers data between multiple devices and memory without interleaving .