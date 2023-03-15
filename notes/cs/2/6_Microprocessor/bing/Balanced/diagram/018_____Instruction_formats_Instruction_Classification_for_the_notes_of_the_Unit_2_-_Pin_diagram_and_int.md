Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Microprocessor KCS. Here is the content for the topic of instruction formats and instruction classification for the unit 2.

# Instruction Formats and Instruction Classification

## Instruction Formats

- An instruction is a binary pattern that specifies a certain operation to be performed by the microprocessor.
- An instruction consists of one or more bytes that contain an **opcode** and optionally one or more **operands**.
- The opcode is the part of the instruction that specifies the type of operation to be performed, such as data transfer, arithmetic, logical, branching, or machine control.
- The operands are the part of the instruction that specify the data or the address of the data involved in the operation.
- The 8085 microprocessor has three types of instruction formats: **one-byte**, **two-byte**, and **three-byte** instructions.

### One-byte Instructions

- One-byte instructions are instructions that consist of only one byte, which is the opcode.
- One-byte instructions do not have any operands, and they usually perform simple operations that do not involve any data or memory locations.
- Examples of one-byte instructions are:

| Instruction | Opcode | Meaning |
| --- | --- | --- |
| CMA | 2F | Complement the accumulator |
| DAA | 27 | Decimal adjust the accumulator |
| EI | FB | Enable interrupts |
| HLT | 76 | Halt the microprocessor |
| NOP | 00 | No operation |
| RLC | 07 | Rotate the accumulator left through carry |
| RRC | 0F | Rotate the accumulator right through carry |

### Two-byte Instructions

- Two-byte instructions are instructions that consist of two bytes, one for the opcode and one for the operand.
- Two-byte instructions usually have one operand that is an 8-bit data or an 8-bit register.
- Examples of two-byte instructions are:

| Instruction | Opcode | Operand | Meaning |
| --- | --- | --- | --- |
| ADI | C6 | D8 | Add immediate data to the accumulator |
| ANI | E6 | D8 | And immediate data with the accumulator |
| CPI | FE | D8 | Compare immediate data with the accumulator |
| IN | DB | D8 | Input data from a port to the accumulator |
| MVI | 3E | D8 | Move immediate data to the accumulator |
| OUT | D3 | D8 | Output data from the accumulator to a port |
| SUI | D6 | D8 | Subtract immediate data from the accumulator |

### Three-byte Instructions

- Three-byte instructions are instructions that consist of three bytes, one for the opcode and two for the operand.
- Three-byte instructions usually have one operand that is a 16-bit address or a 16-bit data.
- Examples of three-byte instructions are:

| Instruction | Opcode | Operand | Meaning |
| --- | --- | --- | --- |
| JMP | C3 | ADR | Jump to the specified address |
| LDA | 3A | ADR | Load data from the specified address to the accumulator |
| LXI | 21 | D16 | Load immediate data to a register pair |
| SHLD | 22 | ADR | Store the contents of HL register pair to the specified address |
| STA | 32 | ADR | Store the contents of the accumulator to the specified address |
| XTHL | E3 | ADR | Exchange the contents of HL register pair with the top of the stack |

## Instruction Classification

- The 8085 microprocessor has a set of 246 instructions, which can be classified into five categories based on the type of operation they perform: **data transfer**, **arithmetic**, **logical**, **branching**, and **machine control**.
- Additionally, there are some **assembler directives** that are not instructions, but commands for the assembler to perform certain tasks during the assembly process.

### Data Transfer Instructions

- Data transfer instructions are instructions that move data between registers, memory locations, or input/output devices.
- Data transfer instructions do not affect any flags in the flag register, except for the IN and OUT instructions, which may affect the parity flag.
- Examples of data transfer instructions are:

| Instruction | Meaning |
| --- | --- |
| MOV | Move data from one register to another |
| MVI | Move immediate data to a register or a memory location |
| LDA | Load data from a memory location to the accumulator |
| STA | Store data from the accumulator to a memory location |
| LDAX | Load data from a memory location pointed by a register pair to the accumulator |
| STAX | Store data from the accumulator to a memory location pointed