### Buses

- A bus is a set of electrical wires that connects major components (CPU, memory and I/O devices) of a computer system.
- A bus can transfer data, address or control signals between the components.
- A bus can be classified into three functional groups: data bus, address bus and control bus .
- Data bus: It carries the data between the components. It can be bidirectional, meaning that it can transfer data in both directions .
- Address bus: It carries the address of the memory location or I/O device that is to be accessed by the CPU. It is unidirectional, meaning that it can transfer data only from the CPU to the memory or I/O devices .
- Control bus: It carries the control signals that indicate the type and direction of data transfer, such as read, write, interrupt, etc. It can be bidirectional or unidirectional, depending on the design of the system .
- The width of a bus is the number of wires or bits that it can transfer at a time. The width of a data bus determines the amount of data that can be transferred in one cycle. The width of an address bus determines the maximum number of memory locations or I/O devices that can be addressed by the CPU.
- The speed of a bus is the frequency at which it can transfer data. The speed of a bus is measured in MHz or Mbps. The speed of a bus determines the performance of the system.
- A bus can be designed in different ways, depending on the requirements and constraints of the system. Some common bus designs are:
  - Single bus structure: In this design, there is only one common bus that is used to communicate between the CPU, memory and I/O devices. This design is simple and cheap, but it has disadvantages such as low speed, high contention and limited scalability .
  - Double bus structure: In this design, there are two buses: one for fetching instructions and one for fetching data. This design can improve the speed and efficiency of the system, but it requires more hardware and complexity.
  - Multiple bus structure: In this design, there are more than two buses, such as a local bus, a system bus, an expansion bus, etc. This design can reduce the contention and increase the scalability of the system, but it also requires more hardware, complexity and coordination .
- A bus can also be classified into different types, depending on the protocol and standard that it follows. Some common bus types are:
  - ISA bus: It stands for Industry Standard Architecture. It is an old and slow bus that operates at 8 MHz and can transfer 8 or 16 bits at a time.
  - PCI bus: It stands for Peripheral Component Interconnect. It is a fast and popular bus that operates at 33 or 66 MHz and can transfer 32 or 64 bits at a time.
  - AGP bus: It stands for Accelerated Graphics Port. It is a specialized bus that is used to connect a graphics card to the motherboard. It operates at 66 MHz and can transfer 32 or 64 bits at a time.
  - USB bus: It stands for Universal Serial Bus. It is a serial bus that is used to connect various peripheral devices to the computer. It operates at different speeds, such as 1.5, 12, 480 or 5000 Mbps, depending on the version.
  - FireWire bus: It is also known as IEEE 1394. It is a serial bus that is used to connect high-speed devices, such as digital cameras, scanners, etc. It operates at different speeds, such as 100, 200, 400 or 800 Mbps, depending on the version.

- A bus can be represented by a diagram that shows the components and the wires that connect them. For example, the following diagram shows a single bus structure:

```
    +-----------------+     +-----------------+
    |                 |     |                 |
    |      CPU        |     |      I/O        |
    |                 |     |                 |
    +-----------------+     +-----------------+
        | | | | | | | |       | | | | | | | |
        | | | | | | | |       |

Some possible mnemonics and learning tricks for the topic are:

- To remember the three functional groups of a bus, you can use the acronym DAC: Data, Address, Control.
- To remember the direction of data transfer for each functional group, you can use the following phrases:
  - Data bus: Both ways
  - Address bus: Away from CPU
  - Control bus: Depends on design
- To remember the order of bus speed from slowest to fastest, you can use the following sentence: ISA is slow, PCI is fast, AGP is faster, USB is flexible, FireWire is fiery.
- To remember the order of bus width from smallest to largest, you can use the following sentence: ISA is small, PCI is big, AGP is bigger, USB is serial, FireWire is serial too.