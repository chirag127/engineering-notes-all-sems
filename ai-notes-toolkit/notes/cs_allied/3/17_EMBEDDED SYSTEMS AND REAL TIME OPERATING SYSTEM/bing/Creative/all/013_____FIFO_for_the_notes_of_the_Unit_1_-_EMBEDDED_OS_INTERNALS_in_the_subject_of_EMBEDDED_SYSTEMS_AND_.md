# FIFO for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- FIFO stands for First In First Out, which means that the data that is inserted first will be extracted first.
- FIFOs are commonly used in embedded systems for buffering and flow control between hardware and software.
- FIFOs can be implemented in hardware or software, depending on the application requirements.
- Hardware FIFOs are usually built of registers, flip-flops, latches or SRAM, and have read and write pointers, storage and control logic .
- Hardware FIFOs can be exclusive read/write or concurrent read/write, depending on whether the reading and writing operations can occur simultaneously or not.
- Hardware FIFOs can reduce the power consumption, data loss and latency of the system by allowing the host MCU to interact with the sensor less frequently.
- Software FIFOs are usually implemented as circular buffers or queues, and have head and tail pointers, storage and control variables.
- Software FIFOs can be accessed by interrupts or polling, depending on the system design.
- Software FIFOs can provide flexibility, portability and scalability to the system, but may also introduce overhead, complexity and errors.