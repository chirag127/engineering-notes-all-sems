### Branching operations

Branching operations are a type of instructions that allow the microprocessor to change the sequence of the program execution, either unconditionally or under certain conditions. They are useful for implementing loops, subroutines, conditional statements, and interrupts in the program.

The 8085 microprocessor supports the following branching instructions:

- **JMP** (Jump): This instruction unconditionally transfers the program control to the specified 16-bit address. The syntax is `JMP addr`, where `addr` is the destination address. For example, `JMP 2000H` will jump to the location 2000H.
- **JC** (Jump if Carry): This instruction conditionally transfers the program control to the specified 16-bit address if the carry flag (CY) is set. The syntax is `JC addr`, where `addr` is the destination address. For example, `JC 3000H` will jump to the location 3000H only if CY = 1.
- **JNC** (Jump if No Carry): This instruction conditionally transfers the program control to the specified 16-bit address if the carry flag (CY) is reset. The syntax is `JNC addr`, where `addr` is the destination address. For example, `JNC 4000H` will jump to the location 4000H only if CY = 0.
- **JZ** (Jump if Zero): This instruction conditionally transfers the program control to the specified 16-bit address if the zero flag (Z) is set. The syntax is `JZ addr`, where `addr` is the destination address. For example, `JZ 5000H` will jump to the location 5000H only if Z = 1.
- **JNZ** (Jump if Not Zero): This instruction conditionally transfers the program control to the specified 16-bit address if the zero flag (Z) is reset. The syntax is `JNZ addr`, where `addr` is the destination address. For example, `JNZ 6000H` will jump to the location 6000H only if Z = 0.
- **JP** (Jump if Positive): This instruction conditionally transfers the program control to the specified 16-bit address if the sign flag (S) is reset. The syntax is `JP addr`, where `addr` is the destination address. For example, `JP 7000H` will jump to the location 7000H only if S = 0.
- **JM** (Jump if Minus): This instruction conditionally transfers the program control to the specified 16-bit address if the sign flag (S) is set. The syntax is `JM addr`, where `addr` is the destination address. For example, `JM 8000H` will jump to the location 8000H only if S = 1.
- **JPE** (Jump if Parity Even): This instruction conditionally transfers the program control to the specified 16-bit address if the parity flag (P) is set. The syntax is `JPE addr`, where `addr` is the destination address. For example, `JPE 9000H` will jump to the location 9000H only if P = 1.
- **JPO** (Jump if Parity Odd): This instruction conditionally transfers the program control to the specified 16-bit address if the parity flag (P) is reset. The syntax is `JPO addr`, where `addr` is the destination address. For example, `JPO A000H` will jump to the location A000H only if P = 0.
- **CALL** (Call): This instruction unconditionally transfers the program control to the specified 16-bit address after saving the return address on the stack. The syntax is `CALL addr`, where `addr` is the destination address. For example, `CALL B000H` will push the address of the next instruction on the stack and jump to the location B000H.
- **RET** (Return): This instruction unconditionally transfers the program control back to the return address stored on the stack. The syntax is `RET`. For example, `RET` will pop the address from the stack and jump to that location.
- **RST** (Restart): This instruction unconditionally transfers the program control to one of the eight predefined addresses depending on the operand. The syntax is `RST n`, where `n` is a number from 0 to 7. For example, `RST 5` will jump to the location

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of the flags in the flag register, use the acronym **SPAZ** (Sign, Parity, Auxiliary carry, Zero).
- To remember the names of the branching instructions, use the acronym **JCRZPMSPEPO** (Jump, Call, Return, Restart, Zero, Positive, Minus, Parity Even, Parity Odd).
- To remember the addresses of the restart instructions, use the formula **8n**, where n is the operand. For example, `RST 3` will jump to the address 8*3 = 24 = 18H.