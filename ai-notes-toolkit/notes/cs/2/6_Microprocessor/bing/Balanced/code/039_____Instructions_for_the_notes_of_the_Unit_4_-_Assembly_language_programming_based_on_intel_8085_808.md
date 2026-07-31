# Notes for Unit 4 - Assembly Language Programming Based on Intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent machine instructions .
- Assembly language is specific to a given processor, so the assembly language of 8085 is different from that of 8086 .
- An assembler is a program that converts an assembly language program to machine language.
- The 8085 microprocessor is an 8-bit microprocessor that has 8 bits of data bus and 16 bits of address bus.
- The 8086 microprocessor is a 16-bit microprocessor that has 16 bits of data bus and 20 bits of address bus.
- The 8086 microprocessor can operate in two modes: minimum mode and maximum mode.
- The 8086 microprocessor has 14 registers: 4 general purpose registers (AX, BX, CX, DX), 4 segment registers (CS, DS, SS, ES), 4 index registers (SI, DI, BP, SP), and 2 instruction pointer registers (IP, FLAG) .
- The assembly language program of 8086 consists of four sections: data section, code section, stack section, and extra section.
- The data section contains the data declarations and initializations.
- The code section contains the executable instructions and labels.
- The stack section contains the stack pointer initialization and stack operations.
- The extra section contains the extra data or code that does not fit in the other sections.
- The assembly language instructions of 8086 can be classified into four types: data transfer instructions, arithmetic instructions, logic instructions, and branch instructions.
- Data transfer instructions are used to move data between registers, memory, and I/O ports.
- Arithmetic instructions are used to perform arithmetic operations such as addition, subtraction, multiplication, and division.
- Logic instructions are used to perform logical operations such as AND, OR, XOR, NOT, and compare.
- Branch instructions are used to alter the sequence of execution based on certain conditions.
- Looping, counting, and indexing are programming techniques that are used to repeat a set of instructions for a certain number of times or until a certain condition is met .
- Looping can be done using the LOOP instruction or the conditional jump instructions .
- Counting can be done using the register CX as a counter or using a memory location as a counter .
- Indexing can be done using the index registers SI and DI to access data in an array or a table .
- Programming techniques can be used to implement counters and time delays in assembly language .
- Counters are used to count the number of events or pulses that occur in a given time interval .
- Time delays are used to create a pause or a wait in the program execution .
- Counters and time delays can be implemented using loops, arithmetic instructions, and branch instructions .
- Stacks and subroutines are programming techniques that are used to store and retrieve data or return addresses in a last-in first-out (LIFO) order .
- Stacks are used to store data temporarily in a memory area pointed by the stack pointer SP .
- Subroutines are used to execute a set of instructions that are repeated or called from different parts of the program .
- Stacks and subroutines can be implemented using the PUSH, POP, CALL, and RET instructions .
- Conditional call and return instructions are used to execute a subroutine or return from a subroutine based on certain conditions .
- Conditional call and return instructions can be implemented using the conditional jump instructions and the flags register .

: Assembly language programming with 8085 microprocessor
: Know Assembly Language Programming of 8086 - ElProCus
: Differences between 8085 and 8086 microprocessor -