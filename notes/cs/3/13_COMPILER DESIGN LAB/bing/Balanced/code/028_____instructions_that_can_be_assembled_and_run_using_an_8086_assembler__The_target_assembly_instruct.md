### Instructions that can be assembled and run using an 8086 assembler

The 8086 microprocessor supports a variety of instructions that can be classified into the following categories:

- Data transfer instructions: These instructions are used to transfer data between registers, memory and I/O ports. Some examples are MOV, PUSH, POP, IN and OUT.
- Arithmetic instructions: These instructions are used to perform arithmetic operations like addition, subtraction, multiplication and division on operands in registers or memory. Some examples are ADD, SUB, MUL, DIV, INC and DEC.
- Logical instructions: These instructions are used to perform bitwise logical operations like AND, OR, XOR and NOT on operands in registers or memory. Some examples are AND, OR, XOR, NOT, NEG and CMP.
- Shift and rotate instructions: These instructions are used to shift or rotate the bits of operands in registers or memory by a specified number of positions. Some examples are SHL, SHR, SAL, SAR, ROL, ROR, RCL and RCR.
- Branch instructions: These instructions are used to alter the normal sequence of execution by transferring control to another location in the program based on some condition. Some examples are JMP, JZ, JNZ, JC, JNC, JA, JNA, CALL and RET.
- Loop instructions: These instructions are used to repeat a block of code for a specified number of times or until a condition is met. Some examples are LOOP, LOOPE, LOOPNE, JCXZ and JECXZ.
- String instructions: These instructions are used to perform operations on strings of bytes or words stored in memory. Some examples are MOVSB, MOVSW, CMPSB, CMPSW, SCASB, SCASW, LODSB, LODSW, STOSB and STOSW.
- Flag manipulation instructions: These instructions are used to set, clear or test the status flags in the flag register. Some examples are STC, CLC, CMC, STD, CLD, LAHF, SAHF, PUSHF and POPF.
- Miscellaneous instructions: These instructions are used to perform various other functions like interrupt handling, stack operations, processor identification, etc. Some examples are INT, IRET, NOP, HLT, XLAT, LEA, LDS, LES and CPUID.

To assemble and run a program using an 8086 assembler, the following steps are required:

- Write the source code in a text editor using the 8086 assembly language syntax and mnemonics.
- Save the source code file with an .asm extension.
- Invoke the assembler with the source code file name as an argument. The assembler will generate an object code file with an .obj extension if there are no errors in the source code.
- Invoke the linker with the object code file name as an argument. The linker will generate an executable file with an .exe extension if there are no errors in the object code.
- Run the executable file using an 8086 emulator or simulator.