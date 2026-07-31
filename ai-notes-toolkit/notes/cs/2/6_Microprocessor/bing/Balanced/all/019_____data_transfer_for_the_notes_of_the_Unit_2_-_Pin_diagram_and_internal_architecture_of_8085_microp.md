# Data Transfer for the Notes of the Unit 2

## Pin Diagram and Internal Architecture of 8085 Microprocessor

- The 8085 microprocessor is an 8-bit processor that has 40 pins and operates on a single +5V power supply.
- The pin diagram of the 8085 microprocessor is shown below:

![Pin diagram of 8085 microprocessor](https://www.tutorialspoint.com/microprocessor/images/8085_pin_diagram.jpg)

- The internal architecture of the 8085 microprocessor consists of the following components:

  - Registers: The 8085 has six general-purpose registers (B, C, D, E, H, and L) that can store 8-bit data each. It also has one accumulator (A) that can perform arithmetic and logical operations. Additionally, it has two special-purpose registers: the program counter (PC) that holds the address of the next instruction to be executed, and the stack pointer (SP) that points to the top of the stack in memory.
  - ALU: The arithmetic and logic unit (ALU) performs various operations on the data stored in the registers or memory. It can perform addition, subtraction, increment, decrement, logical AND, OR, XOR, complement, and rotate operations. It also sets the flags in the flag register according to the result of the operation.
  - Control and Status: The control and status unit generates the control signals for the internal and external devices. It also monitors the status of the microprocessor and the external devices. It has five flags: sign (S), zero (Z), auxiliary carry (AC), parity (P), and carry (CY) that indicate the outcome of the ALU operations.
  - Interrupt: The interrupt unit handles the external requests for interrupting the normal execution of the program. It has five interrupt pins: INTR, RST 7.5, RST 6.5, RST 5.5, and TRAP. The INTR is a maskable interrupt that can be enabled or disabled by software. The RST 7.5, RST 6.5, and RST 5.5 are also maskable interrupts that have fixed priority and vector addresses. The TRAP is a non-maskable interrupt that has the highest priority and cannot be disabled by software.
  - Machine Cycle: The machine cycle is the basic unit of time for the microprocessor operations. It consists of three or more clock cycles, depending on the type of operation. There are four types of machine cycles: opcode fetch, memory read, memory write, and I/O. The opcode fetch cycle fetches the instruction from the memory and decodes it. The memory read cycle reads the data from the memory and stores it in the register or accumulator. The memory write cycle writes the data from the register or accumulator to the memory. The I/O cycle transfers the data between the microprocessor and the external devices.

## Instruction Sets

- The instruction set of the 8085 microprocessor is a collection of commands that the microprocessor can execute. Each instruction has a mnemonic, an opcode, and an operand. The mnemonic is a symbolic representation of the instruction, such as ADD, MOV, JMP, etc. The opcode is a binary code that identifies the instruction, such as 10000110, 01000110, 11000011, etc. The operand is the data or the address that the instruction operates on, such as A, B, C, 2000H, etc.
- The instruction set of the 8085 microprocessor can be classified into five groups: data transfer, arithmetic, logical, branching, and machine control.

### Data Transfer

- The data transfer instructions are used to transfer data between the registers, memory, and I/O devices. They do not affect the flags or the ALU operations. Some examples of data transfer instructions are:

  - MOV: This instruction copies the data from the source operand to the destination operand. For example, MOV A, B copies the data from register B to register A.
  - MVI: This instruction loads an 8-bit immediate data to the destination operand. For example, MVI A, 05H loads the hexadecimal value 05 to register A.
  - LDA: This instruction loads an 8-bit data from a 16-bit memory address to the accumulator. For example, LDA 2000H loads the data from the memory location 2000H to the accumulator.
  - STA: This instruction stores an 8-bit data from the accumulator to a 16-bit memory address. For