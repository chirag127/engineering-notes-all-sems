### Instructions that can be assembled and run using an 8086 assembler

The 8086 microprocessor supports a variety of instructions that can be classified into the following categories:

- Data transfer instructions: These instructions are used to move data between registers, memory, and I/O ports. Some examples are MOV, XCHG, PUSH, POP, IN, and OUT.
- Arithmetic instructions: These instructions are used to perform arithmetic operations like addition, subtraction, multiplication, and division on data in registers or memory. Some examples are ADD, SUB, MUL, DIV, INC, and DEC.
- Logical instructions: These instructions are used to perform bitwise logical operations like AND, OR, XOR, and NOT on data in registers or memory. Some examples are AND, OR, XOR, NOT, NEG, and CMP.
- Shift and rotate instructions: These instructions are used to shift or rotate data in registers or memory by a specified number of bits. Some examples are SHL, SHR, SAL, SAR, ROL, ROR, RCL, and RCR.
- Branch instructions: These instructions are used to alter the flow of execution based on some condition or flag. Some examples are JMP, JZ, JNZ, JC, JNC, JO, JNO, etc.
- Loop instructions: These instructions are used to repeat a block of code a specified number of times or until a condition is met. Some examples are LOOP, LOOPE, LOOPNE, and LOOPNZ.
- String instructions: These instructions are used to perform operations on strings of data in memory. Some examples are MOVSB, MOVSW, CMPSB, CMPSW, SCASB, SCASW, LODSB, LODSW, STOSB, and STOSW.
- Flag manipulation instructions: These instructions are used to set, clear, or test the status flags in the 8086 microprocessor. Some examples are STC, CLC, CMC, STD, CLD, STI, CLI, LAHF, SAHF, PUSHF, and POPF.
- Miscellaneous instructions: These instructions are used to perform various other functions like interrupt handling, stack operations, no operation, halt, etc. Some examples are INT, IRET, CALL, RET, NOP, HLT, etc.

The following diagram shows the general format of an 8086 assembly instruction:

![8086 instruction format](https://www.tutorialspoint.com/microprocessor/images/8086_instruction_format.jpg)

The instruction consists of an optional label, a mandatory mnemonic, and optional operands and comments. The operands can be registers, memory addresses, immediate values, or I/O ports. The comments are preceded by a semicolon and are ignored by the assembler.