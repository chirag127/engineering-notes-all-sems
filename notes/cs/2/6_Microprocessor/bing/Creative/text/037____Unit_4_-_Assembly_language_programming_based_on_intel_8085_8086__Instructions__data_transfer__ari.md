## Unit 4 - Assembly language programming based on intel 8085/8086. Instructions, data transfer, arithmetic, logic, branch operations, looping, counting, indexing, programming techniques, counters and time delays, stacks and subroutines, conditional call and return instructions

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that can be executed by a microprocessor  .
- Assembly language is specific to a given processor, so the syntax and instruction set may vary depending on the microprocessor .
- Intel 8085 and 8086 are two popular microprocessors that have their own assembly languages and architectures    .
- Intel 8085 is an 8-bit microprocessor that has a 16-bit address bus and a 8-bit data bus  . It can address up to 64 KB of memory and has 74 instructions .
- Intel 8086 is a 16-bit microprocessor that has a 20-bit address bus and a 16-bit data bus . It can address up to 1 MB of memory and has 133 instructions .
- The assembly language instructions of 8085 and 8086 can be classified into the following categories   :
  - Data transfer instructions: These instructions are used to move data between registers, memory locations, input/output devices, etc. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations such as addition, subtraction, multiplication, division, increment, decrement, etc. Examples are ADD, SUB, MUL, DIV, INR, DCR, etc.
  - Logic instructions: These instructions are used to perform logical operations such as AND, OR, XOR, NOT, complement, shift, rotate, etc. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branch instructions: These instructions are used to alter the sequence of execution of the program based on certain conditions or flags. Examples are JMP, JC, JNC, JZ, JNZ, CALL, RET, etc.
  - Looping, counting and indexing instructions: These instructions are used to repeat a block of code for a certain number of times or until a condition is met. They also use index registers to access data in arrays or tables. Examples are LOOP, CX, BX, SI, DI, etc.
  - Programming techniques: These are some of the methods or strategies to write efficient and modular assembly language programs. Examples are using labels, comments, directives, macros, subroutines, etc.
  - Counters and time delays: These are used to generate a specific number of clock cycles or a specific duration of time for the microprocessor to perform certain tasks or wait for certain events. Examples are using register pairs, NOP, HLT, etc.
  - Stacks and subroutines: These are used to store and retrieve data or return addresses in a last-in first-out (LIFO) manner. They also allow the program to call and return from subroutines or functions. Examples are PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions: These are used to call or return from subroutines based on certain conditions or flags. Examples are CC, CNC, CZ, CNZ, etc.