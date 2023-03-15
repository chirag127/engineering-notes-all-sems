# Logic for the notes of the Unit 4 - Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions of a microprocessor.
- Assembly language is specific to a given processor. For example, the assembly language of 8085 is different from that of 8086.
- Assembly language programming involves writing the source code in a text editor, assembling it into an object file, and linking it with other object files to generate an executable file.
- The basic elements of assembly language are:
  - Instructions: The commands that tell the microprocessor what to do. Each instruction consists of an operation code (opcode) and zero or more operands.
  - Operands: The data or addresses that are used by the instructions. Operands can be registers, memory locations, immediate values, or labels.
  - Registers: The internal storage locations of the microprocessor that can hold data or addresses. Each register has a name and a size. For example, the 8085 has eight 8-bit registers: A, B, C, D, E, H, L, and F (flags).
  - Memory: The external storage area that can hold data or instructions. Memory is organized into bytes, each with a unique address. For example, the 8085 can address up to 64 KB of memory, from 0000H to FFFFH.
  - Labels: The symbolic names that are used to identify memory locations or instructions. Labels are defined by the programmer and resolved by the assembler.
  - Directives: The commands that tell the assembler how to process the source code. Directives do not generate any machine code. For example, the ORG directive specifies the starting address of the program.
  - Comments: The remarks that are used to explain the source code. Comments are ignored by the assembler. For example, the ; symbol indicates the start of a comment.

- The 8085 and 8086 microprocessors have different instruction sets, addressing modes, and register sets. Some of the differences are:
  - The 8085 is an 8-bit microprocessor, while the 8086 is a 16-bit microprocessor.
  - The 8085 has a single 16-bit address bus and an 8-bit data bus, while the 8086 has a 20-bit address bus and a 16-bit data bus.
  - The 8085 has five addressing modes: immediate, register, direct, register indirect, and implied, while the 8086 has nine addressing modes: immediate, register, direct, register indirect, based, indexed, based indexed, relative, and segment override.
  - The 8085 has eight 8-bit registers: A, B, C, D, E, H, L, and F, while the 8086 has fourteen 16-bit registers: AX, BX, CX, DX, SP, BP, SI, DI, CS, DS, SS, ES, IP, and FLAGS.
  - The 8085 has 74 instructions, while the 8086 has 133 instructions.

- The assembly language programming of the 8085 and 8086 microprocessors involves the following steps:
  - Write the source code in a text editor, using the appropriate syntax, mnemonics, operands, labels, directives, and comments.
  - Assemble the source code into an object file, using an assembler program. The assembler converts the mnemonics into opcodes, resolves the labels into addresses, and generates an object file that contains the machine code and the relocation information.
  - Link the object file with other object files or libraries, using a linker program. The linker combines the object files into a single executable file, resolves the external references, and assigns the final addresses to the segments and symbols.
  - Load the executable file into the memory of the microprocessor, using a loader program. The loader transfers the executable file from the disk or other device to the memory, and sets the program counter to the starting address of the program.
  - Execute the program, using a monitor program or a debugger program. The monitor or debugger allows the user to control the execution of the program, examine or modify the registers or memory, set breakpoints, or trace the program flow.

- The assembly language programming of the 8085 and 8086 microprocessors requires the knowledge of the following topics:
  - Instructions: The types, formats, opcodes, operands, and effects of the instructions of the 8085 and 8086 microprocessors. The instructions can be classified