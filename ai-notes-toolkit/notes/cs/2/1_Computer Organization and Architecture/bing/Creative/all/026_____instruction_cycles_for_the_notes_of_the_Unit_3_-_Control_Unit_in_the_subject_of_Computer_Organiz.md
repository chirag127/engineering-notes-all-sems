# Instruction Cycles

- Instruction cycles are the steps that a CPU performs to execute a single instruction.
- Instruction cycles are the basic operation of the CPU and consist of three main phases: fetch, decode, and execute.
- The CPU repetitively performs instruction cycles to execute a program that is stored in the memory unit.
- The instruction cycle can be decomposed into a sequence of elementary micro-operations that are performed by the CPU components.
- The instruction cycle can be affected by the presence of indirect addressing, interrupts, and pipelining.

## Fetch Phase

- The fetch phase is the first phase of the instruction cycle, where the CPU fetches the next instruction from the memory unit.
- The fetch phase involves the following micro-operations:
  - The CPU copies the content of the program counter (PC) to the memory address register (MAR), which holds the address of the next instruction to be fetched.
  - The CPU sends a read signal to the memory unit, which reads the instruction from the address specified by the MAR and places it on the data bus.
  - The CPU copies the content of the data bus to the instruction register (IR), which holds the last instruction fetched.
  - The CPU increments the PC by one, so that it points to the next instruction in the program.

## Decode Phase

- The decode phase is the second phase of the instruction cycle, where the CPU decodes the instruction in the IR and determines the operation and the operands involved.
- The decode phase involves the following micro-operations:
  - The CPU examines the opcode (operation code) field of the instruction in the IR and identifies the type and format of the instruction.
  - The CPU extracts the operand field(s) of the instruction in the IR and determines the address and value of the operand(s).
  - The CPU may need to perform an indirect cycle if the instruction uses indirect addressing, which means that the operand field contains the address of another memory location that holds the actual operand.
  - The CPU may need to perform an interrupt cycle if an interrupt request is detected, which means that the CPU has to suspend the current instruction and execute a service routine for the interrupt.

## Execute Phase

- The execute phase is the third phase of the instruction cycle, where the CPU executes the instruction and performs the required operation on the operand(s).
- The execute phase involves the following micro-operations:
  - The CPU transfers the operand(s) from the memory unit or the registers to the arithmetic logic unit (ALU), which performs the arithmetic or logical operation specified by the opcode.
  - The CPU transfers the result of the operation from the ALU to the memory unit or the registers, depending on the instruction format.
  - The CPU may need to update the condition code register (CCR), which holds the status flags that indicate the outcome of the operation, such as zero, negative, overflow, or carry.
  - The CPU may need to update the PC or the stack pointer (SP) if the instruction is a branch or a call, which means that the CPU has to change the sequence of execution or store the return address on the stack.

## Pipelining

- Pipelining is a technique that improves the performance of the CPU by overlapping the execution of multiple instructions.
- Pipelining divides the instruction cycle into smaller stages, such as instruction fetch, instruction decode, operand fetch, execute, and result store.
- Pipelining allows the CPU to fetch the next instruction while decoding the current instruction, and execute the current instruction while fetching the operand(s) for the next instruction, and so on.
- Pipelining increases the throughput (the number of instructions executed per unit time) of the CPU, but it also introduces some challenges, such as data hazards, control hazards, and structural hazards.