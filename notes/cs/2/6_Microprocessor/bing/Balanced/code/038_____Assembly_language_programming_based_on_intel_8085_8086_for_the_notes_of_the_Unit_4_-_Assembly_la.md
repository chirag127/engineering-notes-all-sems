### Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent machine instructions.
- Assembly language is specific to a microprocessor, such as intel 8085 or 8086.
- An assembler is a program that converts assembly language to machine language, which is a binary code that the microprocessor can execute.
- Assembly language programming requires knowledge of the microprocessor architecture, instruction set, addressing modes, registers, flags, memory organization, and interfacing devices.
- Assembly language programming provides direct control over the hardware and allows efficient and optimized use of the microprocessor resources.
- Assembly language programming also involves debugging and testing of the code using simulators, emulators, or hardware tools.

#### Instructions

- An instruction is a command that tells the microprocessor what to do.
- An instruction consists of two parts: an operation code (opcode) and an operand.
- The opcode specifies the type of operation to be performed, such as data transfer, arithmetic, logic, branch, or control.
- The operand specifies the data or the address of the data on which the operation is to be performed.
- The operand can be a register, a memory location, an immediate value, or an input/output port.
- The format and size of an instruction depend on the microprocessor and the addressing mode used.
- The instruction set of a microprocessor is the collection of all the instructions that it can execute.
- The instruction set of intel 8085 and 8086 are different, but they have some common instructions and categories.

#### Data transfer instructions

- Data transfer instructions are used to move data between registers, memory, and input/output devices.
- Data transfer instructions do not affect the flags or the program counter.
- Some examples of data transfer instructions are:

  - MOV: moves data from one register to another or from memory to register or vice versa.
  - MVI: moves an immediate value to a register or a memory location.
  - LXI: loads a 16-bit immediate value to a register pair.
  - LDA: loads data from a memory location to the accumulator.
  - STA: stores data from the accumulator to a memory location.
  - LDAX: loads data from a memory location pointed by a register pair to the accumulator.
  - STAX: stores data from the accumulator to a memory location pointed by a register pair.
  - XCHG: exchanges the contents of two register pairs.
  - PUSH: pushes data from a register pair to the stack.
  - POP: pops data from the stack to a register pair.
  - IN: reads data from an input port to the accumulator.
  - OUT: writes data from the accumulator to an output port.

#### Arithmetic instructions

- Arithmetic instructions are used to perform arithmetic operations on data, such as addition, subtraction, multiplication, and division.
- Arithmetic instructions affect the flags and the accumulator, but not the program counter.
- Some examples of arithmetic instructions are:

  - ADD: adds data from a register or a memory location to the accumulator.
  - ADI: adds an immediate value to the accumulator.
  - ADC: adds data from a register or a memory location to the accumulator with carry.
  - ACI: adds an immediate value to the accumulator with carry.
  - SUB: subtracts data from a register or a memory location from the accumulator.
  - SUI: subtracts an immediate value from the accumulator.
  - SBB: subtracts data from a register or a memory location from the accumulator with borrow.
  - SBI: subtracts an immediate value from the accumulator with borrow.
  - INR: increments a register or a memory location by one.
  - DCR: decrements a register or a memory location by one.
  - INX: increments a register pair by one.
  - DCX: decrements a register pair by one.
  - DAD: adds data from a register pair to the HL register pair.
  - DAA: adjusts the accumulator after a binary coded decimal (BCD) operation.

#### Logic instructions

- Logic instructions are used to perform logical operations on data, such as AND, OR, XOR, NOT, and compare.
- Logic instructions affect the flags and the accumulator, but not the program counter.
- Some examples of logic instructions are:

  - ANA: performs bitwise AND operation between data from a register or a memory location and the accumulator.
  - ANI: performs bitwise AND operation between an immediate value and the accumulator.
  - ORA: performs bitwise OR operation between data from a register or a