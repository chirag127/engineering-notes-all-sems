# Notes for Unit 4 - Assembly Language Programming Based on Intel 8085/8086

## Introduction

- Assembly language is a low-level language that uses mnemonics to represent machine instructions.
- Assembly language is specific to a given processor. For example, assembly language of 8085 is different than that of Motorola 6800 microprocessors .
- Assembly language programs are translated into machine code by an assembler.
- Assembly language programming requires knowledge of the processor architecture, instruction set, addressing modes, registers, flags, memory organization, and input/output devices.

## Instructions

- Instructions are the basic commands that the processor executes.
- Instructions consist of an operation code (opcode) and an operand (or operands).
- The opcode specifies the type of operation to be performed, such as data transfer, arithmetic, logic, branch, etc.
- The operand specifies the data or the address of the data involved in the operation.
- Some instructions have no operands, some have one operand, and some have two operands.
- The format of an instruction depends on the processor and the addressing mode used.

## Data Transfer Instructions

- Data transfer instructions are used to move data between registers, memory locations, and input/output devices.
- Data transfer instructions do not affect the flags, except for the HLT instruction which halts the processor.
- Some examples of data transfer instructions are:

| Instruction | Description |
| --- | --- |
| MOV Rd, Rs | Move the contents of register Rs to register Rd |
| MOV Rd, M | Move the contents of the memory location pointed by HL pair to register Rd |
| MOV M, Rs | Move the contents of register Rs to the memory location pointed by HL pair |
| MVI R, data | Move the immediate data to register R |
| MVI M, data | Move the immediate data to the memory location pointed by HL pair |
| LXI Rp, data 16 | Load the 16-bit immediate data to register pair Rp |
| LDA addr | Load the contents of the memory location specified by the 16-bit address to accumulator |
| STA addr | Store the contents of the accumulator to the memory location specified by the 16-bit address |
| LHLD addr | Load the contents of the memory locations specified by the 16-bit address and its next location to HL pair |
| SHLD addr | Store the contents of HL pair to the memory locations specified by the 16-bit address and its next location |
| LDAX Rp | Load the contents of the memory location pointed by register pair Rp to accumulator |
| STAX Rp | Store the contents of the accumulator to the memory location pointed by register pair Rp |
| XCHG | Exchange the contents of HL pair and DE pair |
| PCHL | Load the contents of HL pair to program counter |
| SPHL | Load the contents of HL pair to stack pointer |
| XTHL | Exchange the contents of HL pair and the top of the stack |
| PUSH Rp | Push the contents of register pair Rp to the stack |
| POP Rp | Pop the contents of the stack to register pair Rp |
| IN port | Input the data from the specified port to accumulator |
| OUT port | Output the data from the accumulator to the specified port |
| HLT | Halt the processor |

## Arithmetic Instructions

- Arithmetic instructions are used to perform arithmetic operations on data, such as addition, subtraction, increment, decrement, etc.
- Arithmetic instructions affect the flags according to the result of the operation.
- Some examples of arithmetic instructions are:

| Instruction | Description |
| --- | --- |
| ADD R | Add the contents of register R to accumulator |
| ADD M | Add the contents of the memory location pointed by HL pair to accumulator |
| ADI data | Add the immediate data to accumulator |
| ADC R | Add the contents of register R and the carry flag to accumulator |
| ADC M | Add the contents of the memory location pointed by HL pair and the carry flag to accumulator |
| ACI data | Add the immediate data and the carry flag to accumulator |
| SUB R | Subtract the contents of register R from accumulator |
| SUB M | Subtract the contents of the memory location pointed by HL pair from accumulator |
| SUI data | Subtract the immediate data from accumulator |
| SBB R | Subtract the contents of register R and the borrow flag from accumulator |
| SBB M | Subtract the contents of the memory location pointed by HL pair and the borrow flag from accumulator |
| SBI data | Subtract the immediate data and the borrow flag from accumulator |
| INR R | Increment the contents of register R