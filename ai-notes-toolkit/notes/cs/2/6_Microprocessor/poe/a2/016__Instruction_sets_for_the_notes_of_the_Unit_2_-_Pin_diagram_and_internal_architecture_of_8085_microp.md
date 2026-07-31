 Here is the content in Markdown format:

### Instruction sets for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle.

1. Instruction sets: The 8085 microprocessor has 78 instructions. These instructions are used to perform various operations on the data. The instructions are classified into the following categories:
- Data transfer instructions: Used to transfer data between the memory and registers. e.g. `MOV`, `MVI`, `LDA`, `STA` etc.
- Arithmetic instructions: Used to perform arithmetic operations like addition, subtraction, comparison etc. on the data. e.g. `ADD`, `SUB`, `CMP` etc.
- Logical instructions: Used to perform logical operations like AND, OR, Exclusive-OR, complement etc. on the data. e.g. `ANA`, `ORA`, `XRA`, `CMA` etc.
- Branching instructions: Used to alter the sequence of program execution. e.g. `JMP`, `CALL`, `RET`, `RST` etc.
- Machine control instructions: Used to control the microprocessor. e.g. `halt`, `NOP`, `RM`, `SIM` etc.

2. Addressing modes: The 8085 microprocessor supports five addressing modes to access (read/write) the memory location:
- Register addressing: Operand is present in the register. e.g. `MOV A,B`
- Direct addressing: Operand address is present in the instruction. e.g. `MVI A,20H`
- Indirect addressing: Contents of the register specify the address of the operand. e.g. `Mov A,M`
- Immediate addressing: Operand is embedded in the instruction. e.g. `MOV A,#20H`
- Implicit addressing: No memory location is specified. e.g. `INR A`

[The content continues in the same format with points on Instruction formats, Instruction Classification, Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle.]