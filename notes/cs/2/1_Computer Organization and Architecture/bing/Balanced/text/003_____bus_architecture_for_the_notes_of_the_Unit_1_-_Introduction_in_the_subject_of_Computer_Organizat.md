### Bus Architecture

- A bus is a set of electrical wires that connects major components of a computer system, such as CPU, memory and I/O devices.
- A bus can be classified into three functional groups: data lines, address lines and control lines .
- Data lines are used to transfer data between components. The number of data lines determines the data transfer rate and the word size of the system.
- Address lines are used to specify the source or destination of data. The number of address lines determines the address space and the memory capacity of the system.
- Control lines are used to coordinate the activities of components and to signal the type of operation to be performed. The control lines include read/write, memory request, interrupt request, etc.
- A bus structure can be designed in different ways, depending on the number of buses, the number of components connected to each bus, and the way of arbitration and synchronization.
- A common bus system is a simple and economical design, where all the components share a single bus. However, it has low performance and scalability, as only one component can use the bus at a time.
- A multiple bus system is a more complex and costly design, where there are separate buses for different components or functions. For example, there can be a dedicated bus for CPU and memory, and another bus for I/O devices. This improves the performance and scalability, as multiple components can use different buses simultaneously.
- A bus arbitration is a mechanism to resolve the conflicts and grant access to the bus when multiple components request it. The arbitration can be centralized or distributed, and can use different algorithms, such as priority, round-robin, daisy chain, etc.
- A bus synchronization is a mechanism to coordinate the timing and speed of data transfer on the bus. The synchronization can be synchronous or asynchronous, and can use different methods, such as clock signals, handshaking signals, etc.