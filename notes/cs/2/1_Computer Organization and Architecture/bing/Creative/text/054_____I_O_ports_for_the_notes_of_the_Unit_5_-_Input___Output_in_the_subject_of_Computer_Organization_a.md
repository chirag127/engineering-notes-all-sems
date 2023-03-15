### I/O ports

- An I/O port is a socket on a computer that connects the CPU to a peripheral device via a hardware interface or to the network.
- An I/O port can have a memory address or an I/O address, depending on the processor architecture and the I/O mapping scheme.
- There are two types of I/O mapping schemes: memory-mapped I/O and port-mapped I/O.
  - Memory-mapped I/O: The I/O ports are assigned memory addresses and are accessed using the same instructions as memory access. This simplifies the instruction set and the hardware design, but reduces the available memory space.
  - Port-mapped I/O: The I/O ports are assigned I/O addresses and are accessed using special instructions for input and output. This preserves the memory space, but requires more instructions and hardware complexity.
- There are different types of I/O ports based on the data transfer mode and the connector type .
  - Serial port: A port that transfers data one bit at a time over a single wire. It is used for external modems and older computer mice. It has two versions: 9-pin and 25-pin. The data rate is 115 kilobits per second.
  - Parallel port: A port that transfers data multiple bits at a time over multiple wires. It is used for scanners and printers. It has a 25-pin connector. The data rate is up to 2 megabytes per second.
  - Universal Serial Bus (USB) port: A port that transfers data serially over a single wire, but with multiple devices connected to a hub. It is used for various peripherals such as keyboards, mice, cameras, flash drives, etc. It has a 4-pin connector. The data rate is up to 480 megabits per second for USB 2.0 and up to 5 gigabits per second for USB 3.0.
  - Other types of ports include FireWire, Ethernet, HDMI, VGA, etc.