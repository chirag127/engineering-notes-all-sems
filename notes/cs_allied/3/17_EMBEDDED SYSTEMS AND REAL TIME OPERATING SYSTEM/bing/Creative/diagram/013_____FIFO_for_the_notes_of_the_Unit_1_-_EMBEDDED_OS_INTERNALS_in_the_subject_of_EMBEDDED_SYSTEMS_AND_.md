### FIFO

- FIFO stands for First In First Out, which means that the data that is inserted first will be extracted first.
- FIFOs are commonly used in embedded systems for buffering and flow control between hardware and software components.
- FIFOs can be implemented in hardware or software, depending on the application requirements and the available resources.
- Hardware FIFOs are typically composed of a set of read and write pointers, storage elements, and control logic. They can operate at high speeds and support concurrent read and write operations .
- Software FIFOs are usually implemented as circular buffers or queues, where data is stored in an array and the read and write pointers are updated accordingly. They can be more flexible and adaptable, but they may incur more overhead and latency.
- Some of the benefits of using FIFOs in embedded systems are :
  - They can reduce the host MCU interaction with the sensor or peripheral device, and therefore save power and processing time.
  - They can store information about a movement or event that may be of interest for later analysis or processing.
  - They can avoid losing data when the data rate is higher than the processing rate, or when there are interruptions or delays in the data flow.
  - They can synchronize data between different clock domains or data formats, and provide a consistent data stream for the receiver.
- Some of the challenges or limitations of using FIFOs in embedded systems are :
  - They require additional hardware or software resources, such as memory, logic, or code space, which may be scarce or expensive in some systems.
  - They introduce additional complexity and potential sources of errors, such as overflow, underflow, or data corruption, which need to be detected and handled properly.
  - They may not be suitable for some applications that require strict timing or ordering constraints, such as real-time or deterministic systems.