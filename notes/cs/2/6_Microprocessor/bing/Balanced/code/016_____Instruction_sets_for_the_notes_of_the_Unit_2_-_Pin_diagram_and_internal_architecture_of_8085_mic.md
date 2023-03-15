# Notes for Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Pin diagram and internal architecture of 8085 microprocessor

- The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time. It has a 16-bit address bus that can address 64 KB of memory. It has 40 pins and operates with +5V power supply.
- The pin diagram of 8085 microprocessor is shown below:

![Pin diagram of 8085 microprocessor](https://electronicsdesk.com/wp-content/uploads/2019/08/Pin-Diagram-of-8085-Microprocessor.png)

- The pins of 8085 microprocessor can be classified into six groups: address bus, data bus, control and status signals, power supply and frequency signals, externally initiated signals, and serial I/O ports  .
- The address bus is a group of 16 lines (A0-A15) that are used to transfer the memory address of the data that needs to be read or written. The address bus is unidirectional, i.e., bits flow in one direction from the microprocessor to the peripheral devices. The address bus also carries the lower 8 bits of the address during the first clock cycle and the higher 8 bits of the address during the second clock cycle.
- The data bus is a group of 8 lines (D0-D7) that are used to transfer the data between the microprocessor and the memory or I/O devices. The data bus is bidirectional, i.e., bits can flow in both directions. The data bus also carries the opcode of the instruction during the first clock cycle and the operand or data during the second clock cycle.
- The control and status signals are a group of 6 lines (ALE, RD, WR, IO/M, S0, S1) that are used to control the operation of the microprocessor and indicate the status of the microprocessor. The control and status signals are as follows :
  - ALE (Address Latch Enable): This is an active high signal that indicates that the address bus contains a valid address. It is used to latch the lower 8 bits of the address from the address bus into an external latch. It is also used to demultiplex the address and data bus.
  - RD (Read): This is an active low signal that indicates that the microprocessor is ready to read data from the memory or I/O device. It is used to enable the output buffer of the memory or I/O device to send data to the data bus.
  - WR (Write): This is an active low signal that indicates that the microprocessor is ready to write data to the memory or I/O device. It is used to enable the input buffer of the memory or I/O device to receive data from the data bus.
  - IO/M (Input/Output or Memory): This is a signal that indicates whether the address on the address bus is for an I/O device or a memory device. It is high for I/O operation and low for memory operation.
  - S0 and S1 (Status): These are two signals that indicate the type of operation being performed by the microprocessor. They are as follows:
    - S0 = 0, S1 = 0: Halt state
    - S0 = 0, S1 = 1: Write state
    - S0 = 1, S1 = 0: Read state
    - S0 = 1, S1 = 1: Fetch state
- The power supply and frequency signals are a group of 3 lines (Vcc, Vss, X1, X2) that are used to provide power and clock frequency to the microprocessor. The power supply and frequency signals are as follows :
  - Vcc: This is the positive power supply pin that provides +5V to the microprocessor.
  - Vss: This is the ground pin that provides 0V to the microprocessor.
  - X1 and X2: These are the crystal or clock pins that are connected to an external oscillator circuit to generate the clock frequency for the microprocessor. The clock frequency determines the