### Instruction formats and classification for 8085 microprocessor

- The 8085 microprocessor has a set of 246 instructions (74 types) that can perform various operations on data and control the flow of the program  .
- The instructions can be classified based on the following criteria :
  - The size of the instruction in bytes (one, two or three)
  - The addressing mode used by the instruction (immediate, register, direct, indirect or implied)
  - The function performed by the instruction (data transfer, arithmetic, logical, branch, stack, I/O or machine control)
- The instruction format of 8085 microprocessor consists of one or more bytes, where the first byte is always the opcode and the following bytes are the operands .
- The opcode is a 8-bit binary code that specifies the operation to be performed by the microprocessor .
- The operands are the data or the address of the data on which the operation is to be performed .
- The instruction format of 8085 microprocessor can be represented as follows :

| Opcode | Operand 1 | Operand 2 |
|--------|-----------|-----------|
| 8 bits | 8 bits    | 8 bits    |

- Depending on the size of the instruction, the operand 1 and operand 2 may or may not be present .
- For example, the instruction `MOV A, B` has one byte and the opcode is `78H`, which means move the contents of register B to register A .
- The instruction `MVI A, 05H` has two bytes and the opcode is `3EH`, which means move the immediate data `05H` to register A .
- The instruction `LDA 2000H` has three bytes and the opcode is `3AH`, which means load the accumulator with the data stored at the memory address `2000H` .
- The instruction set of 8085 microprocessor can be classified into the following groups based on the function performed by the instruction  :
  - Data transfer instructions: These instructions move data between registers or between memory and registers. For example, `MOV`, `MVI`, `LDA`, `STA`, `LXI`, `LDAX`, `STAX`, `LHLD`, `SHLD`, `XCHG`, `PUSH`, `POP`, `IN`, `OUT` etc.
  - Arithmetic instructions: These instructions perform arithmetic operations on data in registers or memory. For example, `ADD`, `ADC`, `SUB`, `SBB`, `INR`, `DCR`, `INX`, `DCX`, `DAD`, `SUI`, `SBI`, `ADI`, `ACI`, `DAA` etc.
  - Logical instructions: These instructions perform logical and bit manipulation operations on data in registers or memory. For example, `ANA`, `ANI`, `ORA`, `ORI`, `XRA`, `XRI`, `CMP`, `CPI`, `RLC`, `RRC`, `RAL`, `RAR`, `CMA`, `CMC`, `STC` etc.
  - Branch instructions: These instructions alter the sequence of execution of the program based on some conditions. For example, `JMP`, `JC`, `JNC`, `JZ`, `JNZ`, `JP`, `JM`, `JPE`, `JPO`, `CALL`, `CC`, `CNC`, `CZ`, `CNZ`, `CP`, `CM`, `CPE`, `CPO`, `RET`, `RC`, `RNC`, `RZ`, `RNZ`, `RP`, `RM`, `RPE`, `RPO`, `PCHL`, `RST` etc.
  - Machine control instructions: These instructions control the operation of the microprocessor or the external devices. For example, `NOP`, `HLT`, `DI`, `EI`, `SIM`, `RIM` etc.
- The addressing modes of 8085 microprocessor specify how the operands of an instruction are accessed from memory or registers .
- The addressing modes of

- Some mnemonics and learning tricks for 8085 microprocessor are  :
  - To remember the opcode for `MOV r1 r2`, where r1 and r2 are any of the registers A, B, C, D, E, H, L or M, use the formula `MOV r1 r2 = 40H + 8*r1 + r2`, where r1 and r2 are assigned numbers from 0 to 7 as follows: A = 0, B = 1, C = 2, D = 3, E = 4, H = 5, L = 6, M = 7. For example, `MOV A B = 40H + 8*0 + 1 = 41H`, `MOV H M = 40H + 8*5 + 7 = 77H` etc.
  - To remember the opcode for `ORA R`, where R is any of the registers A, B, C, D, E, H, L or M, use the formula `ORA R = B0H + R`, where R is assigned numbers from 0 to 7 as follows: A = 0, B = 1, C = 2, D = 3, E = 4, H = 5, L = 6, M = 7. For example, `ORA A = B0H + 0 = B0H`, `ORA C = B0H + 2 = B2H` etc.
  - To remember the opcode for `ANI d8`, where d8 is any 8-bit data, use the formula `ANI d8 = E6H d8`. For example, `ANI 0FH = E6H 0FH`, `ANI 55H = E6H 55H` etc.
  - To remember the opcode for `ADD R`, where R is any of the registers A, B, C, D, E, H, L or M, use the formula `ADD R = 80H + R`, where R is assigned numbers from 0 to 7 as follows: A = 0, B = 1, C = 2, D = 3, E = 4, H = 5, L = 6, M = 7. For example, `ADD A = 80H + 0 = 80H`, `ADD E = 80H + 4 = 84H` etc.
  - To remember the opcode for `SUB R`, where R is any of the registers A, B, C, D, E, H, L or M, use the formula `SUB R = 90H + R`, where R is assigned numbers from 0 to 7 as follows: A = 0, B = 1, C = 2, D = 3, E = 4, H = 5, L = 6, M = 7. For example, `SUB A = 90H + 0 = 90H`, `SUB L = 90H + 6 = 96H` etc.
  - To remember the opcode for `JMP a16`, where a16 is any 16-bit address, use the formula `JMP a16 = C3H a16`. For example, `JMP 1000H = C3H 1000H`, `JMP 2000H = C3H 2000H` etc.
  - To remember the opcode for `CALL a16`, where a16 is any 16-bit address, use the formula `CALL a16 = CDH a16`. For example, `CALL 1000H = CDH 1000H`, `CALL 2000H = CDH 2000H` etc.
  - To remember the opcode for `RET`, use the formula `RET = C9H`. For example, `RET = C9H`.
  - To remember the opcode for `NOP`, use the formula `NOP = 00H`. For example, `NOP = 00H`.
  - To remember the opcode for `HLT`, use the formula `HLT = 76H`. For example, `HLT = 76H`.