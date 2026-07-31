### Add, Sub, Jump etc.

These are some of the basic instructions in assembly language, which is a low-level programming language that directly controls the hardware of a computer.

- Add: This instruction adds two operands and stores the result in the destination operand. For example, `add eax, ebx` adds the values of the registers eax and ebx and stores the sum in eax.
- Sub: This instruction subtracts the second operand from the first operand and stores the result in the destination operand. For example, `sub eax, ebx` subtracts the value of ebx from eax and stores the difference in eax.
- Jump: This instruction transfers the control flow of the program to another location specified by a label or an address. For example, `jmp loop` jumps to the instruction labeled as loop. There are different types of jumps, such as conditional jumps, which depend on the status of some flags in the processor. For example, `jz loop` jumps to loop only if the zero flag is set, which means the previous arithmetic or logical operation resulted in zero.