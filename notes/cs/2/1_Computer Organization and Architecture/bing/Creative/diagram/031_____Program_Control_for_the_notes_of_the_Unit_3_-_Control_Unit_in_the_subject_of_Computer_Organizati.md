### Program Control

- Program control is the process of directing the execution of instructions in a computer program.
- Program control instructions are the machine code that are used by the processor to perform various operations, such as branching, looping, subroutine calling, interrupt handling, etc.
- Program control instructions can be classified into two types: conditional and unconditional.
  - Conditional instructions are those that depend on the status of some flags or registers to determine whether to execute or skip the next instruction. For example, `JZ` (jump if zero) and `JNZ` (jump if not zero) are conditional instructions that check the zero flag before jumping to a specified address.
  - Unconditional instructions are those that do not depend on any flags or registers and always execute the next instruction. For example, `JMP` (jump) and `CALL` (call subroutine) are unconditional instructions that always jump to a specified address.
- Program control instructions can also be classified into two types: direct and indirect.
  - Direct instructions are those that specify the address of the next instruction explicitly in the instruction itself. For example, `JMP 1000H` is a direct instruction that jumps to the address 1000H.
  - Indirect instructions are those that specify the address of the next instruction implicitly in a register or a memory location. For example, `JMP [BX]` is an indirect instruction that jumps to the address stored in the register BX.
- Program control instructions are essential for implementing various control structures in high-level languages, such as if-else, switch-case, for, while, do-while, etc.
- Program control instructions are also used for handling exceptions and interrupts, which are events that occur during the execution of a program and require special attention from the processor. For example, `INT` (interrupt) and `IRET` (interrupt return) are program control instructions that are used for invoking and returning from an interrupt service routine.