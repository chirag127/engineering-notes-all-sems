# Branching Operations

- Branching operations are instructions that allow the microprocessor to change the sequence of the program, either unconditionally or under certain conditions  .
- Branching operations can be classified into three types: jump, call and return, and restart .
- Jump instructions are used to transfer the program control to a specified memory location unconditionally or based on a flag condition .
- Call and return instructions are used to implement subroutines, which are a set of instructions that perform a specific task and return to the main program .
- Restart instructions are used to invoke one of the eight predefined subroutines that are stored in the memory locations 0000H to 0038H .

## Jump Instructions

- The jump instructions are of two types: unconditional and conditional .
- Unconditional jump instructions are JMP and PCHL .
- JMP instruction transfers the program control to the memory location specified by the 16-bit address in the instruction .
- PCHL instruction transfers the program control to the memory location specified by the contents of the HL register pair .
- Conditional jump instructions are JC, JNC, JZ, JNZ, JP, JM, JPE, and JPO .
- JC instruction transfers the program control to the memory location specified by the 16-bit address in the instruction if the carry flag is set .
- JNC instruction transfers the program control to the memory location specified by the 16-bit address in the instruction if the carry flag is reset .
- JZ instruction transfers the program control to the memory location specified by the 16-bit address in the instruction if the zero flag is set .
- JNZ instruction transfers the program control to the memory location specified by the 16-bit address in the instruction if the zero flag is reset .
- JP instruction transfers the program control to the memory location specified by the 16-bit address in the instruction if the sign flag is reset .
- JM instruction transfers the program control to the memory location specified by the 16-bit address in the instruction if the sign flag is set .
- JPE instruction transfers the program control to the memory location specified by the 16-bit address in the instruction if the parity flag is set .
- JPO instruction transfers the program control to the memory location specified by the 16-bit address in the instruction if the parity flag is reset .

## Call and Return Instructions

- The call and return instructions are of two types: unconditional and conditional .
- Unconditional call and return instructions are CALL and RET .
- CALL instruction pushes the address of the next instruction onto the stack and transfers the program control to the memory location specified by the 16-bit address in the instruction .
- RET instruction pops the address from the stack and transfers the program control to that address .
- Conditional call and return instructions are CC, CNC, CZ, CNZ, CP, CM, CPE, and CPO .
- CC instruction performs the same operation as CALL instruction if the carry flag is set .
- CNC instruction performs the same operation as CALL instruction if the carry flag is reset .
- CZ instruction performs the same operation as CALL instruction if the zero flag is set .
- CNZ instruction performs the same operation as CALL instruction if the zero flag is reset .
- CP instruction performs the same operation as CALL instruction if the sign flag is reset .
- CM instruction performs the same operation as CALL instruction if the sign flag is set .
- CPE instruction performs the same operation as CALL instruction if the parity flag is set .
-