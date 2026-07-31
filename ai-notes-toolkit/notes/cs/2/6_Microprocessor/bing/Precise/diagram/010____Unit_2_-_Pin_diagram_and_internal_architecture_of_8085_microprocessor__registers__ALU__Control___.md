## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

### Pin Diagram and Internal Architecture of 8085 Microprocessor
- The 8085 microprocessor is an 8-bit microprocessor with a 40-pin DIP (Dual In-line Package).
- The pins on the microprocessor can be divided into six groups: Address Bus, Data Bus, Control and Status Signals, Power Supply and Frequency Signals, Externally Initiated Signals, and Serial I/O Ports.
- The internal architecture of the 8085 microprocessor consists of several components, including the Arithmetic and Logic Unit (ALU), registers, control and status unit, interrupt control unit, and serial I/O control unit.

### Registers
- The 8085 microprocessor has several registers, including the accumulator, the program counter, the stack pointer, and six general-purpose registers (B, C, D, E, H, and L).
- The accumulator is an 8-bit register used for arithmetic and logical operations.
- The program counter is a 16-bit register that holds the address of the next instruction to be executed.
- The stack pointer is a 16-bit register that points to the top of the stack in memory.

### ALU
- The Arithmetic and Logic Unit (ALU) performs arithmetic and logical operations on data.
- The ALU can perform operations such as addition, subtraction, logical AND, logical OR, and logical XOR.

### Control and Status
- The control and status unit generates control signals to control the flow of data within the microprocessor and to external devices.
- The status signals provide information about the current state of the microprocessor, such as whether an arithmetic operation resulted in a carry or zero result.

### Interrupt and Machine Cycle
- The 8085 microprocessor has five interrupt inputs that can be used to interrupt the normal execution of the microprocessor.
- The machine cycle is the basic unit of time for operations within the microprocessor. A machine cycle consists of several states, including opcode fetch, memory read, memory write, and I/O operations.

### Instruction Sets
- The 8085 microprocessor has a rich instruction set that includes instructions for data transfer, arithmetic operations, logical operations, branching operations, and machine control.
- The instruction set is divided into several groups, including data transfer instructions, arithmetic instructions, logical instructions, branching instructions, and machine control instructions.

### Addressing Modes
- The 8085 microprocessor supports several addressing modes, including immediate, direct, register, register indirect, and indexed.
- In immediate addressing, the operand is specified in the instruction itself.
- In direct addressing, the operand is specified by its memory address.
- In register addressing, the operand is specified by a register.
- In register indirect addressing, the operand is specified by the contents of a register.
- In indexed addressing, the operand is specified by the contents of a register plus an offset.

### Instruction Formats
- The 8085 microprocessor has several instruction formats, including one-byte, two-byte, and three-byte instructions.
- One-byte instructions consist of an opcode only.
- Two-byte instructions consist of an opcode and one operand.
- Three-byte instructions consist of an opcode and two operands.

### Instruction Classification
- The instruction set of the 8085 microprocessor can be classified into several groups, including data transfer instructions, arithmetic instructions, logical instructions, branching instructions, and machine control instructions.
- Data transfer instructions are used to move data between registers, memory, and I/O devices.
- Arithmetic instructions are used to perform arithmetic operations on data.
- Logical instructions are used to perform logical operations on data.
- Branching instructions are used to change the flow of execution.
- Machine control instructions are used to control the operation of the microprocessor.

### Assembler Directives
- Assembler directives are instructions to the assembler, rather than to the microprocessor.
- Assembler directives are used to control the assembly process, such as defining constants, reserving memory, and specifying the starting address of the program.