# Types of Buses

A bus is a set of wires or lines that carry data, addresses, and control signals between different components of a computer system. Buses can be classified into different types based on their functions, directions, and locations.

## System Bus

The system bus is the main bus that connects the CPU to the main memory and other components on the motherboard. It consists of three types of lines:

- Address lines: These are unidirectional lines that carry the address of the memory location or the I/O device that the CPU wants to access. The number of address lines determines the maximum amount of memory that the CPU can address.
- Data lines: These are bidirectional lines that carry the data to be read or written between the CPU and the memory or the I/O devices. The number of data lines determines the size of data that can be transferred in one cycle.
- Control lines: These are unidirectional or bidirectional lines that carry the control signals that synchronize the operations of the CPU, the memory, and the I/O devices. Some examples of control signals are read, write, reset, interrupt, etc.

The system bus is also called the front-side bus, memory bus, local bus, or host bus.

## Expansion Bus

The expansion bus is a secondary bus that connects the peripheral devices or expansion cards to the system bus. It allows the system to be extended with additional functionality or capacity. Some examples of expansion buses are:

- ISA - Industry Standard Architecture: This is an old standard that supports 8-bit or 16-bit data transfers at a maximum speed of 8.33 MHz. It is mainly used for legacy devices such as modems, sound cards, etc.
- EISA - Extended Industry Standard Architecture: This is an extension of ISA that supports 32-bit data transfers at a maximum speed of 8.33 MHz. It is backward compatible with ISA devices.
- MCA - Micro Channel Architecture: This is a proprietary standard developed by IBM that supports 16-bit or 32-bit data transfers at a maximum speed of 10 MHz. It is not compatible with ISA or EISA devices.
- VESA - Video Electronics Standards Association: This is a standard that supports 32-bit data transfers at a maximum speed of 33 MHz. It is mainly used for video cards and graphics accelerators.
- PCI - Peripheral Component Interconnect: This is a widely used standard that supports 32-bit or 64-bit data transfers at a maximum speed of 33 MHz or 66 MHz. It is faster and more flexible than ISA, EISA, MCA, or VESA buses. It can support multiple devices on a single bus using bus arbitration and device identification.
- PCI Express - Peripheral Component Interconnect Express: This is a newer standard that supports serial data transfers at a maximum speed of 16 GB/s. It is faster and more scalable than PCI buses. It can support multiple lanes of data transfers for each device using point-to-point connections.

## Internal Bus

The internal bus is a bus that connects the internal components of the CPU, such as the arithmetic logic unit (ALU), the registers, the cache, etc. It is also called the back-side bus or the processor bus. It is usually faster and wider than the system bus or the expansion bus. It can have different architectures, such as the Von Neumann architecture or the Harvard architecture.