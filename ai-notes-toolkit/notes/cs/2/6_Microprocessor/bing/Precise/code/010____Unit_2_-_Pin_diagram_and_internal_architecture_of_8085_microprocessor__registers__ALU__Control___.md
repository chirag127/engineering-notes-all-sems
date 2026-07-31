## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

The 8085 microprocessor is an 8-bit microprocessor with a 40-pin DIP (Dual In-line Package). The pin diagram of the 8085 microprocessor is as follows:

```
       +----+--+----+
 AD7   |1   +--+   40| Vcc
 AD6   |2         39| AD8
 AD5   |3         38| AD9
 AD4   |4         37| AD10
 AD3   |5         36| AD11
 AD2   |6         35| AD12
 AD1   |7         34| AD13
 AD0   |8         33| AD14
 ALE   |9         32| AD15
 RD    |10        31| WR
 IO/M  |11        30| HOLD
 S0    |12        29| HLDA
 S1    |13        28| READY
 RESET |14        27| INTR
 CLK   |15        26| INTA
 Vss   |16        25| TRAP
 SID   |17        24| RST 7.5
 SOD   |18        23| RST 6.5
 RESET |19        22| RST 5.5
 X1    |20        21| X2
       +------------+
```

The internal architecture of the 8085 microprocessor consists of the following components:

- Registers: The 8085 microprocessor has six general-purpose registers, one accumulator, and one flag register. The general-purpose registers are B, C, D, E, H, and L. They can be used as 8-bit registers individually or as 16-bit register pairs (BC, DE, HL) to perform 16-bit operations.

- ALU (Arithmetic and Logic Unit): The ALU performs arithmetic and logical operations on the data. It can perform operations such as addition, subtraction, AND, OR, XOR, and complement.

- Control & Status: The control unit generates control signals to control the flow of data between the microprocessor and the peripherals. The status signals indicate the status of the microprocessor.

- Interrupt: The 8085 microprocessor has five interrupt signals: TRAP, RST 7.5, RST 6.5, RST 5.5, and INTR. These interrupts have different priorities and can be used to interrupt the normal execution of the program.

- Machine Cycle: A machine cycle is the time taken by the microprocessor to complete one operation of accessing memory or I/O devices.

The instruction set of the 8085 microprocessor consists of various instructions to perform different operations. These instructions can be classified into the following categories:

- Data transfer: These instructions are used to transfer data between registers, memory, and I/O devices.

- Arithmetic operations: These instructions are used to perform arithmetic operations such as addition, subtraction, increment, and decrement.

- Logical operations: These instructions are used to perform logical operations such as AND, OR, XOR, and complement.

- Branching operations: These instructions are used to change the sequence of execution of the program.

- Machine control: These instructions are used to control the operation of the microprocessor.

- Assembler directives: These are not instructions but are directives for the assembler to perform specific tasks during the assembly process.

The 8085 microprocessor has various addressing modes to access data from memory or I/O devices. These addressing modes are:

- Immediate addressing: The operand is specified in the instruction itself.

- Direct addressing: The address of the operand is specified in the instruction.

- Register addressing: The operand is in a register.

- Register indirect addressing: The address of the operand is in a register pair.

- Implied addressing: The operand is implied by the instruction.

The instruction format of the 8085 microprocessor consists of an opcode and an operand. The opcode specifies the operation to be performed and the operand specifies the data on which the operation is to be performed.