### Programmed I/O

- Programmed I/O is a method of transferring data between the CPU and a peripheral device, such as a keyboard, a mouse, a disk, or a network adapter  .
- Programmed I/O operations are the result of I/O instructions written in the computer program  .
- In programmed I/O, each data transfer is initiated by the CPU, and the CPU is in continuous monitoring of the interface .
- Programmed I/O can be implemented in two ways: polling and busy-waiting .
  - Polling: The CPU repeatedly checks the status of the peripheral device until it is ready for data transfer .
  - Busy-waiting: The CPU executes a loop instruction until the peripheral device sets a flag to indicate that it is ready for data transfer .
- Programmed I/O has some advantages and disadvantages :
  - Advantages: It is simple, cheap, and easy to implement. It does not require any additional hardware or software support .
  - Disadvantages: It consumes a lot of CPU time and resources. It reduces the performance and efficiency of the system. It is not suitable for high-speed devices or large data transfers .