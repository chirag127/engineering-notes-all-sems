### Machine Control and Assembler Directives

- Machine control instructions are used to control the operation of the 8085 microprocessor, such as enabling or disabling interrupts, halting the processor, or sending or receiving serial data.
- Assembler directives are commands to the assembler that do not generate machine codes, but help in the assembly process, such as defining data, allocating memory, specifying the origin, or including other files.
- Some of the machine control instructions are:
  - EI (Enable Interrupts) - This instruction enables the maskable interrupts RST 7.5, 6.5, and 5.5 by setting the interrupt enable flip-flop. It does not affect the non-maskable TRAP interrupt. It has an opcode of FB, a length of 1 byte, and a hex code of FB.
  - DI (Disable Interrupts) - This instruction disables the maskable interrupts by resetting the interrupt enable flip-flop. It does not affect the TRAP interrupt. It has an opcode of F3, a length of 1 byte, and a hex code of F3.
  - HLT (Halt) - This instruction stops the execution of the program and puts the processor in the halt state. The processor can be restarted by a reset or an interrupt signal. It has an opcode of 76, a length of 1 byte, and a hex code of 76.
  - SIM (Set Interrupt Mask) - This instruction is used to implement the different interrupts of 8085 microprocessor, such as RST 7.5, 6.5, and 5.5, and also serial data output. It does not affect the TRAP interrupt. It has an opcode of 30, a length of 1 byte, and a hex code of 30.
  - RIM (Reset Interrupt Mask) - This instruction is used to read the status of the interrupts and the serial data input. It has an opcode of 20, a length of 1 byte, and a hex code of 20.
- Some of the assembler directives are:
  - DB (Define Byte) - This directive is used to allocate and initialize single or multiple data bytes in the memory. For example, `NAME DB 30H, 52H, 35H` allocates three consecutive locations where 30H, 52H, and 35H are stored .
  - DW (Define Word) - This directive is used to allocate and initialize single or multiple data words (16 bits) in the memory. For example, `NUM DW 1234H, 5678H` allocates four consecutive locations where 34H, 12H, 78H, and 56H are stored .
  - DS (Define Storage) - This directive is used to reserve a specified number of bytes in the memory without initializing them. For example, `ARRAY DS 10` reserves 10 bytes of memory for the array .
  - EQU (Equation) - This directive is used to assign a value to a symbol or a label. For example, `COUNT EQU 05H` assigns the value 05H to the symbol COUNT .
  - ORG (Origin) - This directive is used to specify the starting address of the program or a segment. For example, `ORG 2000H` tells the assembler to start assembling the program from the address 2000H .
  - END (End) - This directive is used to indicate the end of the source program. It also specifies the address of the first instruction to be executed. For example, `END START` tells the assembler to end the program and start the execution from the label START .
  - INCLUDE (Include) - This directive is used to include another source file in the current program. For example, `INCLUDE SUBROUTINES.ASM` tells the assembler to include the file SUBROUTINES.ASM in the program.