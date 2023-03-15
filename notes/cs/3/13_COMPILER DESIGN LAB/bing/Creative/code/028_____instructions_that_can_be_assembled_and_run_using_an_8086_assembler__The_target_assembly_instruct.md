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

The following is a simple example of an 8086 assembly program that uses some of these instructions:

```assembly
; Program to add two numbers and display the result
ORG 100H ; Set the origin to 100H
MOV AX, 1234H ; Load the first number into AX
MOV BX, 5678H ; Load the second number into BX
ADD AX, BX ; Add AX and BX and store the result in AX
MOV DX, AX ; Move the result to DX
MOV AH, 2 ; Set the function code for displaying a character
MOV DL, '0' ; Set the character to display to '0'
ADD DL, DH ; Add the high byte of DX to DL
INT 21H ; Call the DOS interrupt to display the character
MOV DL, '0' ; Set the character to display to '0'
ADD DL, DL ; Add the low byte of DX to DL
INT 21H ; Call the DOS interrupt to display the character
MOV AH, 4CH ; Set the function code for terminating the program
INT 21H ; Call the DOS interrupt to terminate the program
END ; End of the program
```