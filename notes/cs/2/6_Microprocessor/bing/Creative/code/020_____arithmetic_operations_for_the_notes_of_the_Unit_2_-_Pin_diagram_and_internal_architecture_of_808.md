### Arithmetic Operations

Arithmetic operations are the instructions that perform basic mathematical operations on the data stored in the registers or memory locations of the 8085 microprocessor. The 8085 microprocessor supports four types of arithmetic operations: addition, subtraction, increment, and decrement. These operations can be performed on 8-bit or 16-bit data, depending on the instruction format and the addressing mode. The following are some of the characteristics and features of the arithmetic operations in the 8085 microprocessor:

- The arithmetic operations are performed by the arithmetic and logic unit (ALU) of the 8085 microprocessor, which is a part of the internal architecture of the microprocessor.
- The arithmetic operations can be performed on the data stored in the accumulator, which is the primary register of the 8085 microprocessor, or on the data stored in other registers or memory locations, which are specified by the operands of the instruction.
- The arithmetic operations can be performed on immediate data, which are the data that are directly given in the instruction, or on indirect data, which are the data that are stored in the memory locations pointed by the register pairs or the stack pointer.
- The arithmetic operations can affect the flags of the 8085 microprocessor, which are the bits of the status register that indicate the result or the condition of the operation. The flags that are affected by the arithmetic operations are the sign flag (S), the zero flag (Z), the auxiliary carry flag (AC), the parity flag (P), the carry flag (CY), and the overflow flag (OV).
- The arithmetic operations have different mnemonics, which are the symbolic names of the instructions, and different opcodes, which are the binary codes of the instructions. The following table shows the list of the arithmetic operations, their mnemonics, their opcodes, and their operands :

| Operation | Mnemonic | Opcode | Operand |
|-----------|----------|--------|---------|
| Addition | ADD | 80 | r |
| Addition | ADD | 86 | M |
| Addition | ADD | C6 | data |
| Addition with carry | ADC | 88 | r |
| Addition with carry | ADC | 8E | M |
| Addition with carry | ADC | CE | data |
| Subtraction | SUB | 90 | r |
| Subtraction | SUB | 96 | M |
| Subtraction | SUB | D6 | data |
| Subtraction with borrow | SBB | 98 | r |
| Subtraction with borrow | SBB | 9E | M |
| Subtraction with borrow | SBB | DE | data |
| Increment | INR | 04 | r |
| Increment | INR | 34 | M |
| Increment | INX | 03 | rp |
| Decrement | DCR | 05 | r |
| Decrement | DCR | 35 | M |
| Decrement | DCX | 0B | rp |

Here, r -> register; M -> Memory (HL register pair); data -> direct data; rp -> any of the three register pairs.

- The arithmetic operations have different formats, which are the ways of representing the instructions in the memory. The formats of the arithmetic operations depend on the number of bytes, the opcode, and the operands of the instruction. The following are some examples of the formats of the arithmetic operations:

| Mnemonic | Format | Example |
|----------|--------|---------|
| ADD r | 1 byte | ADD B |
| ADD M | 1 byte | ADD M |
| ADD data | 2 bytes | ADD 05 |
| ADC r | 1 byte | ADC C |
| ADC M | 1 byte | ADC M |
| ADC data | 2 bytes | ADC 0A |
| SUB r | 1 byte | SUB D |
| SUB M | 1 byte | SUB M |
| SUB data | 2 bytes | SUB 03 |
| SBB r | 1 byte | SBB E |
| SBB M | 1 byte | SBB M |
| SBB data | 2 bytes | SBB 07 |
| INR r | 1 byte | INR A |
| INR M | 1 byte | INR M |
| INX rp | 1 byte | INX BC |
| DCR r | 1 byte | DCR H |
| DCR M | 1 byte | DCR M |
| DCX rp | 1 byte | DCX DE |

- The arithmetic operations have different