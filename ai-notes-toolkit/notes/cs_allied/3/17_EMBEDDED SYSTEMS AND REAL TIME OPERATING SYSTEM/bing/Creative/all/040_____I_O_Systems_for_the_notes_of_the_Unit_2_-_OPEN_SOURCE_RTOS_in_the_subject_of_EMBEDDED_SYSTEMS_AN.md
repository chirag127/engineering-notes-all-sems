# I/O Systems

- I/O systems are the components that enable an embedded system to interact with the external environment, such as sensors, actuators, displays, keyboards, etc.
- I/O systems can be classified into two types: parallel and serial.
  - Parallel I/O systems transfer multiple bits of data simultaneously using multiple wires or pins. They are faster but require more hardware resources and wiring complexity.
  - Serial I/O systems transfer one bit of data at a time using a single wire or pin. They are slower but require less hardware resources and wiring complexity.
- I/O systems can also be classified into two modes: synchronous and asynchronous.
  - Synchronous I/O systems transfer data at a fixed rate and require a clock signal to synchronize the sender and receiver. They are more reliable but require more bandwidth and power consumption.
  - Asynchronous I/O systems transfer data at a variable rate and do not require a clock signal to synchronize the sender and receiver. They are more flexible but require more error detection and correction mechanisms.
- I/O systems can use different protocols to communicate data, such as UART, SPI, I2C, USB, etc.
  - UART (Universal Asynchronous Receiver/Transmitter) is a serial protocol that uses two wires: TX (transmit) and RX (receive). It is widely used for low-speed communication between devices, such as keyboards, modems, GPS, etc.
  - SPI (Serial Peripheral Interface) is a serial protocol that uses four wires: SCLK (serial clock), MOSI (master out slave in), MISO (master in slave out), and SS (slave select). It is widely used for high-speed communication between devices, such as microcontrollers, sensors, memory cards, etc.
  - I2C (Inter-Integrated Circuit) is a serial protocol that uses two wires: SDA (serial data) and SCL (serial clock). It is widely used for low-speed communication between devices, such as microcontrollers, sensors, LCDs, etc.
  - USB (Universal Serial Bus) is a serial protocol that uses four wires: VCC (power supply), GND (ground), D+ (data plus), and D- (data minus). It is widely used for high-speed communication between devices, such as computers, cameras, printers, etc.
- I/O systems can be controlled by different methods, such as polling, interrupt, DMA, etc.
  - Polling is a method that involves the CPU periodically checking the status of an I/O device to determine if it is ready to send or receive data. It is simple but inefficient and wasteful of CPU time and power.
  - Interrupt is a method that involves the I/O device sending a signal to the CPU when it is ready to send or receive data. It is efficient and saves CPU time and power, but requires more hardware and software complexity and overhead.
  - DMA (Direct Memory Access) is a method that involves a dedicated hardware controller transferring data between the I/O device and the memory without involving the CPU. It is very efficient and fast, but requires more hardware and software complexity and overhead.