### I/O Systems

- I/O systems are the components that enable an embedded system or a real-time operating system (RTOS) to communicate with the external world, such as sensors, actuators, keyboards, displays, etc.
- I/O systems can be classified into two types: parallel and serial.
  - Parallel I/O systems transfer multiple bits of data simultaneously using multiple wires or pins. They are faster but require more hardware resources and wiring complexity. Examples of parallel I/O systems are parallel ports, GPIO (General Purpose Input/Output), and memory-mapped I/O.
  - Serial I/O systems transfer one bit of data at a time using one or few wires or pins. They are slower but require less hardware resources and wiring complexity. Examples of serial I/O systems are serial ports, UART (Universal Asynchronous Receiver/Transmitter), SPI (Serial Peripheral Interface), I2C (Inter-Integrated Circuit), and USB (Universal Serial Bus).
- I/O systems can also be classified into two modes: polling and interrupt.
  - Polling mode is when the processor continuously checks the status of an I/O device to determine if it is ready to send or receive data. Polling mode is simple but consumes more processor time and power. It is suitable for low-speed or infrequent I/O operations.
  - Interrupt mode is when the processor is notified by an I/O device when it is ready to send or receive data. Interrupt mode is complex but saves processor time and power. It is suitable for high-speed or frequent I/O operations.