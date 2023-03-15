# Instructions that can be assembled and run using an 8086 assembler

The 8086 microprocessor supports a variety of instructions that can be used for different purposes. Some of the common types of instructions are:

- Data transfer instructions: These instructions are used to move data between registers, memory, and I/O ports. Some examples are MOV, PUSH, POP, IN, and OUT.
- Arithmetic instructions: These instructions are used to perform arithmetic operations like addition, subtraction, multiplication, and division. Some examples are ADD, SUB, MUL, DIV, and INC.
- Logical instructions: These instructions are used to perform bitwise logical operations like AND, OR, XOR, and NOT. Some examples are AND, OR, XOR, and NEG.
- Shift and rotate instructions: These instructions are used to shift or rotate the bits of a register or a memory operand. Some examples are SHL, SHR, SAL, SAR, ROL, and ROR.
- Branch instructions: These instructions are used to alter the flow of execution based on some condition. Some examples are JMP, JZ, JNZ, JC, and JNC.
- Loop instructions: These instructions are used to repeat a block of code for a specified number of times or until a condition is met. Some examples are LOOP, LOOPE, LOOPNE, and LOOPNZ.
- String instructions: These instructions are used to manipulate strings of bytes or words in memory. Some examples are MOVSB, MOVSW, CMPSB, CMPSW, SCASB, and SCASW.
- Flag manipulation instructions: These instructions are used to set, clear, or test the status flags of the 8086 microprocessor. Some examples are STC, CLC, CMC, STD, CLD, and LAHF.
- Miscellaneous instructions: These instructions are used for various other purposes like interrupt handling, stack operations, and processor control. Some examples are INT, IRET, HLT, NOP, and LOCK.

Each instruction has a specific format and syntax that must be followed when writing assembly code. The general format of an instruction is:

`mnemonic operand1, operand2`

where mnemonic is the name of the instruction, operand1 is the destination operand, and operand2 is the source operand. The operands can be registers, memory locations, immediate values, or I/O ports. The comma separates the operands and the operands are separated by spaces from the mnemonic.

For example, the instruction:

`MOV AX, 1234h`

moves the hexadecimal value 1234h into the AX register. The instruction:

`ADD BX, [SI]`

adds the value stored at the memory location pointed by the SI register to the BX register and stores the result in BX. The instruction:

`JMP LABEL`

jumps to the instruction labeled as LABEL. The instruction:

`IN AL, 80h`

reads a byte from the I/O port 80h and stores it in the AL register.

To assemble and run an 8086 assembly program, one needs an assembler, a linker, and an emulator. An assembler is a program that converts the assembly code into machine code. A linker is a program that combines the machine code with other libraries and modules. An emulator is a program that simulates the 8086 microprocessor and executes the machine code.

One example of an 8086 assembler is MASM (Microsoft Macro Assembler), which is a widely used assembler for the x86 architecture. MASM has a simple syntax and supports macros, directives, and structures. To assemble a MASM program, one can use the command:

`ML filename.asm`

where filename.asm is the name of the assembly file. This will produce a filename.obj file, which is the object file containing the machine code.

To link the object file with other libraries and modules, one can use the command:

`LINK filename.obj`

where filename.obj is the name of the object file. This will produce a filename.exe file, which is the executable file that can be run on an emulator.

One example of an 8086 emulator is DOSBox, which is a free and open-source emulator that can run DOS programs on various platforms. DOSBox can emulate the 8086 microprocessor and the CGA, EGA, VGA, and Tandy graphics modes. To run an executable file on DOSBox, one can use the command:

`filename.exe`

where filename.exe is the name of the executable file. This will start the execution of the program and display the output on the emulator screen.