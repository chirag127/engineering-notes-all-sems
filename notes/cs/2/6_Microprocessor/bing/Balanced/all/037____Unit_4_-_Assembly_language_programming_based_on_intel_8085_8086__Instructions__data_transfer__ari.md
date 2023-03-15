# Unit 4 - Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that the microprocessor can execute  .
- Assembly language is specific to a given processor, so the syntax and instruction set of 8085 and 8086 are different .
- 8085 is an 8-bit microprocessor that has 74 instructions and 246 opcodes  .
- 8086 is a 16-bit microprocessor that has 133 instructions and 255 opcodes .
- The instructions of 8085 and 8086 can be classified into the following categories   :
  - Data transfer instructions: These instructions are used to move data between registers, memory and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations such as addition, subtraction, multiplication, division, increment and decrement. Examples are ADD, SUB, MUL, DIV, INR, DCR, etc.
  - Logic instructions: These instructions are used to perform logical operations such as AND, OR, XOR, NOT, complement, shift and rotate. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branch instructions: These instructions are used to alter the sequence of execution based on certain conditions. Examples are JMP, JZ, JNZ, JC, JNC, CALL, RET, etc.
  - Looping, counting and indexing instructions: These instructions are used to repeat a block of code for a specified number of times or until a condition is met. They also use index registers to access data in memory. Examples are LOOP, CX, SI, DI, etc.
  - Programming techniques: These are the methods and strategies to write efficient and modular assembly programs. They include using labels, comments, directives, macros, subroutines, etc.
  - Counters and time delays: These are the techniques to generate a specific duration of time by using loops or timers. They are useful for interfacing with devices that require precise timing. Examples are DELAY, TIMER, etc.
  - Stacks and subroutines: These are the techniques to store and retrieve data or return addresses using a special memory area called stack. They are useful for implementing nested or recursive calls, parameter passing, etc. Examples are PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions: These are the instructions that perform a subroutine call or return only if a certain condition is met. They are useful for reducing the number of branch instructions and simplifying the program flow. Examples are CC, CNC, RC, RNC, etc.