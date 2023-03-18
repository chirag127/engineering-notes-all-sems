### Registers

- Registers are small, high-speed storage locations within the processor that hold data temporarily.
- The 8085 microprocessor has six general-purpose registers, named B, C, D, E, H, and L. They can be combined to form three 16-bit register pairs: BC, DE, and HL.
- The Accumulator (Acc) is another 8-bit register that is used to store the results of arithmetic or logical operations.
- The program counter (PC) is a 16-bit register that stores the memory address of the next instruction to be executed.
- The stack pointer (SP) is a 16-bit register that points to the top of the stack in memory.
- The status register (Flags) is a 8-bit register that contains information about the result of the last arithmetic or logical operation.
- The instruction register (IR) is a 8-bit register that stores the opcode of the instruction being executed.
- The memory address register (MAR) is a 16-bit register that holds the memory address being accessed.
- The memory data register (MDR) is a 8-bit register that holds the data being read from or written to memory.

### ALU

- The Arithmetic Logic Unit (ALU) is responsible for performing arithmetic and logical operations on data stored in registers.
- The 8085 microprocessor's ALU can perform addition, subtraction, increment, decrement, logical AND, logical OR, complement, and shift operations.
- The ALU also sets the flags in the status register to indicate the result of the operation.

### Control & Status

- The control unit (CU) is responsible for controlling the flow of data and instructions within the processor.
- The status register (Flags) contains information about the result of the last arithmetic or logical operation. It has 5 flags: Sign (S), Zero (Z), Auxiliary Carry (AC), Parity (P), and Carry (CY).
- The flags are set by the ALU and can be used to make decisions in branching operations.

### Interrupt and Machine Cycle

- Interrupts are signals that interrupt the normal flow of execution and cause the processor to perform a specific task.
- The 8085 microprocessor supports five types of interrupts: RST 7.5, RST 6.5, RST 5.5, TRAP, and INTR.
- When an interrupt occurs, the processor saves the current state of the program and jumps to a specific memory location to execute the interrupt service routine (ISR).
- The machine cycle is the basic unit of operation in the 8085 microprocessor. It consists of three clock cycles: instruction fetch, instruction decode, and instruction execute.

### Addressing Modes

- Addressing modes are methods used to specify the memory address of data to be accessed by an instruction.
- The 8085 microprocessor supports five addressing modes: Immediate, Direct, Indirect, Register, and Register Indirect.
- Immediate addressing mode involves specifying the data directly in the instruction.
- Direct addressing mode involves specifying the memory address of the data in the instruction.
- Indirect addressing mode involves specifying the memory address of a memory location that contains the memory address of the data.
- Register addressing mode involves specifying the register that contains the data.
- Register Indirect addressing mode involves specifying the register that contains the memory address of the data.

### Instruction Sets and Formats

- An instruction set is a collection of instructions that a processor can execute.
- The 8085 microprocessor has a set of 246 instructions.
- Instructions can be classified into data transfer, arithmetic operations, logical operations, branching operations, machine control, and assembler directives.
- An instruction format specifies the layout of the instruction in memory.
- The 8085 microprocessor has two basic instruction formats: one-byte and two-byte.
- One-byte instructions are 8 bits long and include operations like NOP, INR, and RLC.
- Two-byte instructions are 16 bits long and include operations like MOV, ADD, and SUB.