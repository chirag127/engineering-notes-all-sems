### Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that a microprocessor can execute  .
- Assembly language is specific to a given processor, so the syntax and instruction set of 8085 and 8086 are different .
- 8085 is an 8-bit microprocessor that has 74 instructions, 246 opcodes, 5 addressing modes, and a 16-bit address bus  .
- 8086 is a 16-bit microprocessor that has 133 instructions, 255 opcodes, 12 addressing modes, and a 20-bit address bus .
- The instructions of 8085 and 8086 can be classified into the following categories   :
  - Data transfer instructions: These are used to move data between registers, memory, and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These are used to perform arithmetic operations on data such as addition, subtraction, multiplication, division, increment, and decrement. Examples are ADD, SUB, MUL, DIV, INR, DCR, etc.
  - Logic instructions: These are used to perform logical operations on data such as AND, OR, XOR, NOT, complement, shift, and rotate. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branch instructions: These are used to alter the sequence of execution of the program based on certain conditions such as flags, registers, or memory contents. Examples are JMP, JZ, JNZ, JC, JNC, CALL, RET, etc.
  - Looping instructions: These are used to repeat a block of instructions for a specified number of times or until a condition is met. Examples are LOOP, LOOPE, LOOPNE, etc.
  - Counting instructions: These are used to increment or decrement a register or a memory location by a constant value. Examples are INX, DCX, etc.
  - Indexing instructions: These are used to access data from an array or a table using an index register. Examples are LXI, LDAX, STAX, etc.
  - Programming techniques: These are used to implement various algorithms and data structures using the instructions of the microprocessor. Examples are sorting, searching, string manipulation, stack implementation, etc.
  - Counters and time delays: These are used to generate a specific duration of time by executing a loop of instructions for a calculated number of times. Examples are using register pairs as counters, using timer/counter devices, etc.
  - Stacks and subroutines: These are used to store and retrieve data or return addresses from a memory area called stack using push and pop operations. Subroutines are blocks of instructions that can be called from the main program using call and return instructions. Examples are PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions: These are used to call or return from a subroutine based on certain conditions such as flags, registers, or memory contents. Examples are CC, CNC, CZ, CNZ, etc.