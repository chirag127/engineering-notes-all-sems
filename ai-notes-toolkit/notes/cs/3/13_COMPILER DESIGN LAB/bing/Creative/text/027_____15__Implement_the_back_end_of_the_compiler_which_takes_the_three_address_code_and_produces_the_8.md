### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language

The back end of the compiler is the part that generates the target code from the intermediate code. In this case, the intermediate code is the three address code (TAC) and the target code is the 8086 assembly language.

The 8086 assembly language is a low-level programming language for the Intel 8086 microprocessor, which has a 16-bit data bus and a 20-bit address bus. The 8086 assembly language has the following features:

- It has eight general-purpose registers: AX, BX, CX, DX, SI, DI, BP, and SP. Each register can be accessed as a 16-bit word or as two 8-bit bytes. For example, AX can be accessed as AH and AL, where AH is the high byte and AL is the low byte.
- It has four segment registers: CS, DS, SS, and ES. Each segment register holds the upper 16 bits of a 20-bit segment address, which is used to access memory. The lower 4 bits of the segment address are determined by the offset address, which is a 16-bit value that can be stored in a general-purpose register or an immediate operand. For example, the instruction `MOV AX, [DS:SI]` moves the word at the memory location DS*16 + SI to the AX register, where DS is the value of the DS segment register and SI is the value of the SI general-purpose register.
- It has a flag register, which holds the status of the previous arithmetic or logical operation. The flag register has 16 bits, but only 9 of them are used. The most important flags are the carry flag (CF), the zero flag (ZF), the sign flag (SF), the overflow flag (OF), the parity flag (PF), and the direction flag (DF).
- It has a set of instructions that can perform arithmetic, logical, data transfer, control transfer, and string operations. The instructions can have one or two operands, which can be registers, memory locations, or immediate values. The operands can have different sizes: byte (8 bits), word (16 bits), or double word (32 bits). The size of the operands must match the size of the instruction, which is determined by a prefix or a suffix. For example, the instruction `ADD AL, 10` adds the immediate value 10 to the AL register, while the instruction `ADD AX, 10` adds the immediate value 10 to the AX register. The prefix `BYTE PTR` or the suffix `B` can be used to indicate that the operand is a byte, while the prefix `WORD PTR` or the suffix `W` can be used to indicate that the operand is a word. For example, the instruction `MOV BYTE PTR [BX], 20` moves the immediate value 20 to the byte at the memory location BX, while the instruction `MOV WORD PTR [BX], 20` moves the immediate value 20 to the word at the memory location BX.
- It has a set of directives that can be used to define data, constants, macros, procedures, and segments. The directives are not executed by the processor, but are processed by the assembler. For example, the directive `DB` can be used to define a byte of data, while the directive `DW` can be used to define a word of data. The directive `END` marks the end of the assembly program.

To implement the back end of the compiler, the following steps can be followed:

- Define the data segment, where the global variables and constants are stored. The data segment can be defined by the directive `DATA SEGMENT` and ended by the directive `DATA ENDS`. For example, if the TAC has the statement `a = 10`, the corresponding assembly code can be:

```
DATA SEGMENT
    a DW 10
DATA ENDS
```

- Define the code segment, where the instructions are stored. The code segment can be defined by the directive `CODE SEGMENT` and ended by the directive `CODE ENDS`. For example, if the TAC has the statement `b = a + 5`, the corresponding assembly code can be:

```
CODE SEGMENT
    MOV AX, a ; move the value of a to the AX register
    ADD AX, 5 ; add 5 to the AX register
    MOV b, AX ; move the value of the AX register to b
CODE ENDS
```

- Define the stack segment, where the local variables and parameters are stored. The stack segment can be defined by the directive `STACK SEGMENT` and ended by