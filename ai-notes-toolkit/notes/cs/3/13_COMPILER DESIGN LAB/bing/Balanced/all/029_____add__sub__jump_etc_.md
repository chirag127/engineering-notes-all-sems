# Add, Sub, Jump etc.

- These are some of the basic instructions that can be executed by a computer processor.
- They are part of the instruction set architecture (ISA) of the processor, which defines the format, syntax, and semantics of the instructions.
- Add, sub, and jump are examples of arithmetic, logical, and control instructions, respectively.
- Add and sub instructions perform addition and subtraction operations on the operands, which can be registers, memory locations, or immediate values.
- Jump instructions transfer the control of the program execution to a different address, which can be specified by a register, a memory location, or an immediate value.
- The jump instruction can be conditional or unconditional, depending on whether it is executed based on the result of a previous instruction or not.
- For example, a conditional jump instruction can be used to implement a loop or an if-else statement in a program.
- The syntax and format of these instructions vary depending on the ISA of the processor, but they usually consist of an opcode (operation code) and one or more operands.
- For example, in the MIPS ISA, the add instruction has the following syntax:

`add $rd, $rs, $rt`

where $rd, $rs, and $rt are registers, and the instruction adds the values of $rs and $rt and stores the result in $rd.

- In the x86 ISA, the add instruction has the following syntax:

`add dest, src`

where dest and src can be registers, memory locations, or immediate values, and the instruction adds the value of src to dest and stores the result in dest.

- In the MIPS ISA, the jump instruction has the following syntax:

`j target`

where target is an immediate value that specifies the address to jump to.

- In the x86 ISA, the jump instruction has the following syntax:

`jmp target`

where target can be a register, a memory location, or an immediate value that specifies the address to jump to.