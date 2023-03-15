### Bus Architecture

- A bus is a set of electrical wires that connects major components of a computer system, such as CPU, memory and I/O devices.
- A bus can be classified into three functional groups: data lines, address lines and control lines .
- Data lines are used to transfer data between components. The number of data lines determines the data transfer rate and the word size of the system.
- Address lines are used to specify the source or destination of data. The number of address lines determines the address space and the memory capacity of the system.
- Control lines are used to coordinate the activities of components and to signal the type and direction of data transfer. The control lines include read/write, memory request, interrupt request, etc.
- A bus structure can be designed in different ways, such as single bus, multiple bus, crossbar switch, etc.
- A single bus structure has one common bus for all components. It is simple and cheap, but has low performance and scalability.
- A multiple bus structure has more than one bus for different components. It can improve performance and scalability, but increases complexity and cost.
- A crossbar switch structure has a matrix of switches that connects each component to any other component. It can achieve high performance and scalability, but requires a large number of switches and wires.
- A common bus system is a specific type of single bus structure that uses a multiplexer to select the output of one register to the bus, and a demultiplexer to select the input of one register from the bus.