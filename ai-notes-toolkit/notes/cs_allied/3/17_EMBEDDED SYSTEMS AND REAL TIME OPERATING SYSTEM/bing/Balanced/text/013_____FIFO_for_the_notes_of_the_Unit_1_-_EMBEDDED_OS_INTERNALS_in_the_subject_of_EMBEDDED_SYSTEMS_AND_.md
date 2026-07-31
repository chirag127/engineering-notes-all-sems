### FIFO for the notes of the Unit 1 - EMBEDDED OS INTERNALS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- FIFO stands for First In First Out, which means that the data that is inserted first will be extracted first.
- FIFOs are commonly used in embedded systems for buffering and flow control between hardware and software.
- FIFOs can be implemented in hardware or software, depending on the application requirements and the available resources.
- Hardware FIFOs are usually built of registers, flip-flops, latches, or SRAM, and have a set of read and write pointers, storage, and control logic .
- Hardware FIFOs can be used to synchronize data streams between devices that operate at different speeds or frequencies, to store information about a movement or event, to avoid losing data when the processor is busy, or to decrease power consumption by reducing the host MCU interaction with the sensor .
- Software FIFOs are usually implemented as circular buffers or queues, and have a head and a tail pointer, a buffer array, and a counter.
- Software FIFOs can be used to buffer data between tasks or threads, to implement inter-process communication, to handle interrupts or events, or to manage memory allocation.
- FIFOs have some advantages and disadvantages compared to other data structures, such as stacks, lists, or trees. Some of the advantages are:
  - FIFOs are simple and easy to implement and use.
  - FIFOs preserve the order of data and ensure fairness.
  - FIFOs can handle variable-length data and dynamic allocation.
- Some of the disadvantages are:
  - FIFOs may have limited capacity and may overflow or underflow if not managed properly.
  - FIFOs may introduce latency or delay in data processing.
  - FIFOs may not support random access or priority-based scheduling.