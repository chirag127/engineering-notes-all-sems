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
 SO    |10        31| READY
 IO/M  |11        30| HOLD
 S1    |12        29| HLDA
 S0    |13        28| RESET IN
 INTA  |14        27| RESET OUT
 WR    |15        26| SID
 RD    |16        25| SOD
 INTR  |17        24| TRAP
 INT   |18        23| RST 7.5
 RST 5.5|19       22| RST 6.5
 RST 5  |20       21| X1
       +------------+
```

The internal architecture of the 8085 microprocessor consists of the following components:
- Registers: The 8085 microprocessor has six general-purpose registers, one accumulator, and one flag register. The general-purpose registers are B, C, D, E, H, and L. They can be used as 8-bit registers individually or as 16-bit register pairs (BC, DE, HL) to perform 16-bit operations.
- ALU (Arithmetic and Logic Unit): The ALU performs arithmetic and logical operations on the data.
- Control & Status: The control unit generates control signals to control the flow of data between the microprocessor and peripherals. The status signals indicate the status of the microprocessor.
- Interrupt: The 8085 microprocessor has five interrupt signals: TRAP, RST 7.5, RST 6.5, RST 5.5, and INTR. These interrupts have different priorities and can be enabled or disabled using the EI (Enable Interrupt) and DI (Disable Interrupt) instructions.
- Machine Cycle: The 8085 microprocessor has six machine cycles: Opcode Fetch, Memory Read, Memory Write, I/O Read, I/O Write, and Interrupt Acknowledge.

The instruction set of the 8085 microprocessor consists of 74 instructions. These instructions can be classified into the following categories:
- Data transfer: These instructions are used to transfer data between registers, memory, and I/O devices.
- Arithmetic operations: These instructions perform arithmetic operations such as addition, subtraction, increment, and decrement.
- Logical operations: These instructions perform logical operations such as AND, OR, XOR, and complement.
- Branching operations: These instructions are used to change the sequence of program execution based on certain conditions.
- Machine control: These instructions are used to control the operation of the microprocessor.
- Assembler directives: These are not instructions but directives for the assembler to perform certain tasks during the assembly process.

The 8085 microprocessor has five addressing modes:
- Immediate addressing: The operand is specified in the instruction itself.
- Register addressing: The operand is in a register.
- Direct addressing: The address of the operand is specified in the instruction.
- Indirect addressing: The address of the operand is in a register pair.
- Implied addressing: The operand is implied by the instruction.

The instruction format of the 8085 microprocessor can be 1-byte, 2-byte, or 3-byte long. The first byte is the opcode, and the remaining bytes (if any) are the operands.
