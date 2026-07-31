## Unit 4 - Assembly language programming based on intel 8085/8086

Assembly language is a low-level programming language used to write programs for microprocessors and microcontrollers. It is a symbolic representation of the machine code, which is the native language of the processor. Assembly language programming is based on the architecture of the microprocessor, and in this unit, we will focus on the Intel 8085/8086 microprocessors.

### Instructions
The Intel 8085/8086 microprocessors have a set of instructions that can be used to perform various operations. These instructions are classified into the following categories:
- Data transfer instructions
- Arithmetic instructions
- Logic instructions
- Branch instructions
- Stack and subroutine instructions

### Data Transfer
Data transfer instructions are used to move data between registers, memory, and I/O devices. Some common data transfer instructions are:
- MOV: Move data from one register to another
- MVI: Move immediate data to a register
- LXI: Load register pair with immediate data
- LDA: Load accumulator with data from memory
- STA: Store accumulator data to memory

### Arithmetic
Arithmetic instructions are used to perform mathematical operations such as addition, subtraction, multiplication, and division. Some common arithmetic instructions are:
- ADD: Add data to the accumulator
- ADI: Add immediate data to the accumulator
- SUB: Subtract data from the accumulator
- SUI: Subtract immediate data from the accumulator
- INR: Increment a register
- DCR: Decrement a register

### Logic
Logic instructions are used to perform logical operations such as AND, OR, XOR, and NOT. Some common logic instructions are:
- ANA: AND data with the accumulator
- ANI: AND immediate data with the accumulator
- ORA: OR data with the accumulator
- ORI: OR immediate data with the accumulator
- XRA: XOR data with the accumulator
- XRI: XOR immediate data with the accumulator

### Branch Operations
Branch instructions are used to change the sequence of program execution. Some common branch instructions are:
- JMP: Unconditional jump to a memory location
- JZ: Jump if zero
- JNZ: Jump if not zero
- JC: Jump if carry
- JNC: Jump if no carry

### Looping, Counting, and Indexing
Looping, counting, and indexing are common programming techniques used in assembly language programming. Looping is used to repeat a set of instructions a certain number of times. Counting is used to keep track of the number of times a loop has been executed. Indexing is used to access elements of an array.

### Programming Techniques
There are several programming techniques that can be used to write efficient and effective assembly language programs. These include:
- Using registers effectively
- Minimizing memory access
- Using subroutines
- Using conditional instructions

### Counters and Time Delays
Counters and time delays are used to control the timing of events in a program. Counters are used to count the number of times an event has occurred, while time delays are used to introduce a delay between events.

### Stacks and Subroutines
Stacks and subroutines are used to organize and structure programs. A stack is a data structure used to store data in a last-in, first-out (LIFO) manner. Subroutines are self-contained blocks of code that can be called from the main program.

### Conditional Call and Return Instructions
Conditional call and return instructions are used to call and return from subroutines based on certain conditions. Some common conditional call and return instructions are:
- CC: Call if carry
- CNC: Call if no carry
- CZ: Call if zero
- CNZ: Call if not zero
- RC: Return if carry
- RNC: Return if no carry
- RZ: Return if zero
- RNZ: Return if not zero