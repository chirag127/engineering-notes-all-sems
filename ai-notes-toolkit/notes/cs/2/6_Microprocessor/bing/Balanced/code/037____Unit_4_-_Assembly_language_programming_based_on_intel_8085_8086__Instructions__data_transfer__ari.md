## Unit 4 - Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that a microprocessor can execute  .
- Assembly language is specific to a given processor, so the syntax and instruction set of 8085 and 8086 are different .
- 8085 is an 8-bit microprocessor that can address 64 KB of memory and has 74 instructions  .
- 8086 is a 16-bit microprocessor that can address 1 MB of memory and has 133 instructions .
- The instructions of 8085 and 8086 can be classified into the following categories   :
  - Data transfer instructions: These are used to move data between registers, memory and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These are used to perform arithmetic operations on data such as addition, subtraction, increment, decrement, etc. Examples are ADD, SUB, INR, DCR, ADC, SBB, etc.
  - Logic instructions: These are used to perform logical operations on data such as AND, OR, XOR, NOT, etc. Examples are ANA, ORA, XRA, CMA, etc.
  - Branch instructions: These are used to alter the sequence of execution of the program based on some conditions. Examples are JMP, JC, JNC, JZ, JNZ, etc.
  - Looping instructions: These are used to repeat a block of instructions until a condition is met. Examples are LOOP, LOOPE, LOOPNE, etc.
  - Counting instructions: These are used to manipulate the contents of the counter register. Examples are CX, CLC, STC, CMC, etc.
  - Indexing instructions: These are used to access data in memory using an index register. Examples are SI, DI, BX, etc.
  - Programming techniques: These are used to implement various algorithms and data structures using assembly language. Examples are sorting, searching, string manipulation, stack, queue, etc.
  - Counters and time delays: These are used to generate a specific amount of time delay or count the number of events using assembly language. Examples are using loops, timers, interrupts, etc.
  - Stacks and subroutines: These are used to store and retrieve data from a stack, and to call and return from a subroutine. Examples are PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions: These are used to call and return from a subroutine based on some conditions. Examples are CC, CNC, CZ, CNZ, etc.