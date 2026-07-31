### Machine Control and Assembler Directives

- Machine control instructions are used to control the operation of the 8085 microprocessor, such as enabling or disabling interrupts, halting the processor, or sending or receiving serial data.
- Assembler directives are commands to the assembler that do not generate machine codes, but help in the assembly process, such as defining data, allocating memory, or specifying the starting address of the program.
- Some of the machine control instructions are:
  - EI: Enable Interrupts. This instruction sets the interrupt enable flip-flop, which allows the processor to accept maskable interrupts. Opcode: 11111011, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex code: FB.
  - DI: Disable Interrupts. This instruction resets the interrupt enable flip-flop, which prevents the processor from accepting maskable interrupts. Opcode: 11110011, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex code: F3.
  - HLT: Halt. This instruction stops the execution of the program and puts the processor in the idle state. The processor can be restarted by a reset or an interrupt. Opcode: 01110110, Length: 1 byte, M-Cycles: 1, T-States: 7, Hex code: 76.
  - SIM: Set Interrupt Mask. This instruction is used to implement different interrupts of 8085 microprocessor like RST 7.5, 6.5 and 5.5 and also serial data output. It does not affect TRAP interrupt. Opcode: 00110000, Operand: None, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex code: 30.
  - RIM: Reset Interrupt Mask. This instruction is used to read the status of the interrupts and the serial data input. It does not affect TRAP interrupt. Opcode: 00100000, Operand: None, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex code: 20.
- Some of the assembler directives are:
  - DB: Define Byte. This directive is used for the purpose of allocating and initializing single or multiple data bytes. For example, AREA DB 30H, 52H, 35H allocates three consecutive locations where 30H, 52H and 35H are to be stored .
  - DW: Define Word. This directive is used for the purpose of allocating and initializing single or multiple data words. For example, DATA DW 1234H, 5678H allocates two consecutive words where 1234H and 5678H are to be stored .
  - DS: Define Storage. This directive is used for the purpose of reserving a specified number of bytes or words without initializing them. For example, TEMP DS 10 reserves 10 bytes of memory with the label TEMP .
  - EQU: Equate. This directive is used for the purpose of assigning a value or an expression to a symbol. For example, COUNT EQU 10 assigns the value 10 to the symbol COUNT .
  - ORG: Origin. This directive is used for the purpose of specifying the starting address of the program or a segment. For example, ORG 2000H sets the program counter to 2000H .
  - END: End. This directive is used for the purpose of indicating the end of the source program. For example, END marks the end of the program and optionally specifies the starting address of the program .