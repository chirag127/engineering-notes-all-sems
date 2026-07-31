### Data Transfer Instructions in 8085 Microprocessor

- Data transfer instructions are the instructions that are used to transfer data between registers, memory and I/O devices in the 8085 microprocessor.
- Data transfer instructions can be classified into four categories: register to register, register to memory, memory to register and I/O to register or register to I/O.
- Data transfer instructions do not affect the flags in the 8085 microprocessor, except for the IN and OUT instructions, which affect the parity flag.
- Data transfer instructions have different formats and opcodes depending on the source and destination operands. The following table shows some examples of data transfer instructions and their formats :

| Instruction | Opcode | Format | Description |
| --- | --- | --- | --- |
| MOV r1, r2 | 01DDDSSS | MOV destination, source | Copies the contents of the source register to the destination register |
| MVI r, data | 00DDD110 | MVI destination, data | Loads the 8-bit data into the destination register |
| LDA addr | 00111010 | LDA address | Loads the accumulator with the contents of the memory location specified by the 16-bit address |
| STA addr | 00110010 | STA address | Stores the contents of the accumulator into the memory location specified by the 16-bit address |
| LHLD addr | 00101010 | LHLD address | Loads the H and L registers with the contents of the memory locations specified by the 16-bit address and the next address |
| SHLD addr | 00100010 | SHLD address | Stores the contents of the H and L registers into the memory locations specified by the 16-bit address and the next address |
| LXI rp, data | 00RP0001 | LXI register pair, data | Loads the register pair with the 16-bit data |
| LDAX rp | 00RP1010 | LDAX register pair | Loads the accumulator with the contents of the memory location pointed by the register pair |
| STAX rp | 00RP0010 | STAX register pair | Stores the contents of the accumulator into the memory location pointed by the register pair |
| XCHG | 11101011 | XCHG | Exchanges the contents of the H and L registers with the contents of the D and E registers |
| IN port | 11011011 | IN port | Reads the data from the input port specified by the 8-bit port address and loads it into the accumulator |
| OUT port | 11010011 | OUT port | Writes the data from the accumulator to the output port specified by the 8-bit port address |

- Data transfer instructions are essential for performing various operations on data, such as arithmetic, logic, branch and looping operations, in the 8085 microprocessor.