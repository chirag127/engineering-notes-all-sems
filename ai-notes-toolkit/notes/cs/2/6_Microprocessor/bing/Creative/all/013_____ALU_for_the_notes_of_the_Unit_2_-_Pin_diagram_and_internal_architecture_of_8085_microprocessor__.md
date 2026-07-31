# ALU for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives. in the subject of Microprocessor KCS

- ALU stands for Arithmetic and Logic Unit. It is a functional unit of the 8085 microprocessor that performs arithmetic, logical, I/O and LOAD/STORE operations .
- The ALU is connected to the internal data bus and the accumulator, which is an 8-bit register that stores the result of the ALU operations .
- The ALU can perform the following operations  :
  - Addition and subtraction of 8-bit or 16-bit numbers, with or without carry or borrow.
  - Increment and decrement of 8-bit or 16-bit numbers.
  - Logical operations such as AND, OR, XOR, NOT, and compare.
  - Bitwise operations such as rotate, shift, and complement.
  - I/O operations such as input and output of data from/to external devices.
  - LOAD/STORE operations such as moving data between registers, memory, and accumulator.
- The ALU is controlled by the flags and the instruction decoder, which are part of the control and status unit of the 8085 microprocessor .
- The flags are 5 bits that indicate the status of the ALU operations, such as zero, sign, parity, carry, and auxiliary carry .
- The instruction decoder is a circuit that decodes the opcode of the instruction and generates the appropriate control signals for the ALU and other functional units .
- The ALU is implemented using NMOS technology and consists of several sub-circuits, such as adder, shifter, multiplexer, and logic gates.
- The ALU can handle 8-bit data at a time, but it can also perform 16-bit operations by using two cycles and the carry flag.