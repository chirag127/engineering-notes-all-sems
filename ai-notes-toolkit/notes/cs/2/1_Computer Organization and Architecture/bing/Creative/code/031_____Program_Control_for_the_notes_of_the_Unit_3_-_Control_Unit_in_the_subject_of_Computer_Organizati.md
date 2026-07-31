### Program Control

- Program control is the process of directing the execution of instructions in a computer program.
- Program control instructions are the machine code that are used by the processor to perform various tasks, such as branching, looping, subroutine calling, interrupt handling, etc.
- Program control instructions can be classified into two types: conditional and unconditional.
- Conditional program control instructions are those that depend on the status of some flags or registers to determine the next instruction to be executed. For example, `JZ` (jump if zero) and `JNZ` (jump if not zero) are conditional program control instructions that check the zero flag before jumping to a specified address.
- Unconditional program control instructions are those that do not depend on any flags or registers and always change the flow of execution to a specified address. For example, `JMP` (jump) and `CALL` (call subroutine) are unconditional program control instructions that always jump or call to a specified address.
- Program control instructions can also be classified into two types: direct and indirect.
- Direct program control instructions are those that specify the address of the next instruction to be executed in the instruction itself. For example, `JMP 1000H` is a direct program control instruction that jumps to the address 1000H.
- Indirect program control instructions are those that specify the address of the next instruction to be executed in a register or a memory location. For example, `JMP [BX]` is an indirect program control instruction that jumps to the address stored in the register BX.
- Program control is implemented by the control unit of the processor, which is responsible for generating the control signals that activate the appropriate components of the processor and the memory to execute the instructions.
- The control unit can be designed in two ways: hardwired control and microprogrammed control.
- Hardwired control is a control unit that is implemented by using logic gates and flip-flops to generate the control signals. Hardwired control is fast, but complex and inflexible.
- Microprogrammed control is a control unit that is implemented by using a memory that stores the control signals as words, called microinstructions. Microprogrammed control is simple, flexible, and easy to modify, but slow.