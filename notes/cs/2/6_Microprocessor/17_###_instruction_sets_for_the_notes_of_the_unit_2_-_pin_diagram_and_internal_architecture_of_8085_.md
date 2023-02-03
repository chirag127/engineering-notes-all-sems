### Instruction sets for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives. in the subject of Microprocessor KCS

Instruction sets of 8085 microprocessor include the following:
- Data transfer instructions: MOV, MVI, LXI, LDA, STA, LHLD, SHLD, XCHG, PUSH, POP, XTHL, SPHL.
- Arithmetic operations: ADD, ADC, SUB, SBB, INR, DCR, INX, DCX, DAD, SUI.
- Logical operations: CMA, CMP, ANA, ORA, XRA, RLC, RRC, RAL, RAR, DAA.
- Branching operations: JMP, JC, JNC, JZ, JNZ, JP, JM, CALL, RET, RST.
- Machine control instructions: HLT, NOP, EI, DI, SIM, RIM.
- Assembler directives: ORG, END.

Addressing modes: Immediate, Direct, Register, Register indirect, and Indexed.

Instruction format: Most instructions in 8085 have 1-byte opcode and 1 or 2-byte operand.

Instruction classification:
- Data transfer instructions transfer data between memory and registers or between registers.
- Arithmetic operations perform arithmetic operations like addition, subtraction, increment, decrement, etc.
- Logical operations perform logical operations like AND, OR, XOR, complement, compare, etc.
- Branching operations change the flow of program execution by jumping to a different memory location.
- Machine control instructions control the operation of the microprocessor.
- Assembler directives are used to give special instructions to the assembler.

Registers: Accumulator (A), B, C, D, E, H, L, Program Counter (PC), Stack Pointer (SP), and Status Register (S).

ALU: Arithmetic and Logic Unit performs arithmetic and logical operations.

Control & status: Control Unit fetches instructions from memory and decodes them, while the Status Register stores information about the result of the operations performed by the ALU.

Interrupt: Interrupts allow external devices to request service from the microprocessor.

Machine cycle: The machine cycle is the basic operation performed by the microprocessor to execute an instruction. It consists of fetch, decode, execute, and writeback phases.
