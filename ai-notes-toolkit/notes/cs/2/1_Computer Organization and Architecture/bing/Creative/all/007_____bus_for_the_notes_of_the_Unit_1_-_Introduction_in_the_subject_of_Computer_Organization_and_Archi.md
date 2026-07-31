# Bus

- A bus is a communication system that transfers data between components inside a computer, or between computers.
- A bus consists of a set of electrical wires that can carry one bit of data each.
- A bus can be classified into three types: data bus, address bus, and control bus .
- Data bus: It carries the data between the CPU, memory, and I/O devices. It is bidirectional, meaning that data can flow in both directions. The width of the data bus determines how many bits of data can be transferred at a time .
- Address bus: It carries the address of the memory location or I/O device that the CPU wants to access. It is unidirectional, meaning that data can flow only from the CPU to the memory or I/O devices. The width of the address bus determines how many memory locations or I/O devices can be addressed by the CPU .
- Control bus: It carries the control signals that synchronize the operations of the CPU, memory, and I/O devices. It can be bidirectional or unidirectional, depending on the design of the system. The control signals include read, write, interrupt, reset, etc .
- A common bus system is a system where all the components of the computer share the same bus. This reduces the cost and complexity of the system, but also limits the performance and scalability of the system.
- A common bus system can be further divided into two types: single-bus system and multiple-bus system.
- Single-bus system: It is a system where there is only one bus for data, address, and control. This simplifies the design of the system, but also increases the contention and congestion on the bus. The speed of the system depends on the speed of the slowest component on the bus.
- Multiple-bus system: It is a system where there are separate buses for data, address, and control. This improves the performance and reliability of the system, but also increases the cost and complexity of the system. The speed of the system depends on the speed of the fastest component on the bus.