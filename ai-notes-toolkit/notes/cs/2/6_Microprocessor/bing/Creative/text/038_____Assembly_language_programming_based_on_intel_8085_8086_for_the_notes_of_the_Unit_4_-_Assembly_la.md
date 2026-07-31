### Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that the microprocessor can execute  .
- Assembly language is specific to a given processor, so the syntax and instruction set of 8085 and 8086 are different .
- 8085 is an 8-bit microprocessor that has 74 instructions and 246 opcodes . It has a 16-bit address bus and an 8-bit data bus .
- 8086 is a 16-bit microprocessor that has 133 instructions and 255 opcodes. It has a 20-bit address bus and a 16-bit data bus.
- The basic format of an assembly language program is:

```
[label] mnemonic [operands] [;comment]
```

- The label is an optional identifier that marks a location in the program  .
- The mnemonic is a symbolic name for an instruction or a directive  .
- The operands are the data or addresses that the instruction operates on  .
- The comment is an optional explanation of the program statement  .

- The assembly language program must be converted into machine code by an assembler before it can be executed by the microprocessor  .
- The assembly language instructions can be classified into the following categories   :

  - Data transfer instructions: These instructions are used to move data between registers, memory locations, or I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations such as addition, subtraction, multiplication, division, increment, and decrement. Examples are ADD, SUB, MUL, DIV, INR, DCR, etc.
  - Logic instructions: These instructions are used to perform logical operations such as AND, OR, XOR, NOT, complement, shift, and rotate. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branch instructions: These instructions are used to alter the sequence of execution of the program based on certain conditions. Examples are JMP, JZ, JNZ, JC, JNC, etc.
  - Looping instructions: These instructions are used to repeat a block of code until a certain condition is met. Examples are LOOP, LOOPE, LOOPNE, etc.
  - Counting instructions: These instructions are used to increment or decrement a register or a memory location by a specified value. Examples are INX, DCX, etc.
  - Indexing instructions: These instructions are used to access data from an array or a table using an index register. Examples are LXI, LDAX, STAX, etc.
  - Programming techniques: These are the methods or strategies to write efficient and modular assembly language programs. Examples are using subroutines, macros, interrupts, etc.
  - Counters and time delays: These are the techniques to generate a specific number of clock cycles or a specific duration of time using assembly language instructions. Examples are using NOP, DJNZ, etc.
  - Stacks and subroutines: These are the techniques to store and retrieve data or return addresses using a special memory area called the stack. Examples are using PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions: These are the instructions that allow calling or returning from a subroutine based on certain conditions. Examples are CC, CNC, CZ, CNZ, etc.