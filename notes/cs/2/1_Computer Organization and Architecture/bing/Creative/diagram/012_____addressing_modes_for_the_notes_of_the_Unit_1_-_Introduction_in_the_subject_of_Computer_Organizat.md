### Addressing Modes

- Addressing modes are the different ways of specifying the operand location in an instruction.
- Operand is the data on which the operation specified by the instruction is performed.
- Addressing modes affect the instruction format, execution time, and memory requirements of a program.
- Different types of addressing modes exist, such as immediate, direct, indirect, register, register indirect, displacement, stack, etc   .
- The syntax of addressing mode is the way of representing the addressing mode used.
- The choice of addressing mode depends on the instruction set architecture, the programming language, and the compiler.
- Addressing modes can be classified into three categories: zero-address, one-address, and two-address.
- Zero-address mode: no operand is specified in the instruction, the operands are implied or taken from a stack .
- One-address mode: one operand is specified in the instruction, the other operand is implied or taken from an accumulator .
- Two-address mode: two operands are specified in the instruction, one of them is also the destination of the result .
- Some examples of addressing modes are:

  - Immediate mode: the operand is a constant value given in the instruction, e.g. `ADD #5` means add 5 to the accumulator  .
  - Direct mode: the operand is the address of a memory location given in the instruction, e.g. `ADD 1000` means add the contents of memory location 1000 to the accumulator  .
  - Indirect mode: the operand is the address of a memory location that contains the address of another memory location, e.g. `ADD (1000)` means add the contents of the memory location pointed by the contents of memory location 1000 to the accumulator  .
  - Register mode: the operand is a register name given in the instruction, e.g. `ADD R1` means add the contents of register R1 to the accumulator  .
  - Register indirect mode: the operand is a register name that contains the address of a memory location, e.g. `ADD (R1)` means add the contents of the memory location pointed by the contents of register R1 to the accumulator  .
  - Displacement mode: the operand is a combination of a base register and a displacement value given in the instruction, e.g. `ADD 100(R1)` means add the contents of the memory location obtained by adding 100 to the contents of register R1 to the accumulator  .
  - Stack mode: the operands are taken from the top of a stack, e.g. `ADD` means pop two values from the stack, add them, and push the result back to the stack .