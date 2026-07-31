# Notes for Unit 4 - Assembly Language Programming Based on Intel 8085/8086

## Introduction

- Assembly language is a low-level language that uses mnemonics to represent machine instructions.
- Assembly language is specific to a given processor. For example, the assembly language of 8085 is different from that of 8086.
- The microprocessor cannot understand a program written in assembly language. A program known as an assembler is used to convert an assembly language program to machine code.
- Assembly language programming requires a good knowledge of the internal architecture and instruction set of the microprocessor.

## Instructions

- An instruction is a binary pattern that tells the microprocessor to perform a specific operation.
- An instruction consists of two parts: an opcode and an operand.
- The opcode specifies the operation to be performed, such as add, subtract, move, etc.
- The operand specifies the data or the address of the data on which the operation is to be performed.
- An instruction can have zero, one, or two operands, depending on the type of operation.
- An instruction can be classified into three types: data transfer, arithmetic/logic, and branch/loop.

## Data Transfer Instructions

- Data transfer instructions are used to move data between registers, memory, and I/O devices.
- Data transfer instructions do not affect the flags in the flag register.
- Some examples of data transfer instructions are:

  - MOV: moves data from source to destination without affecting the source.
  - MVI: moves immediate data (8-bit or 16-bit) to a register or a memory location.
  - LXI: loads a 16-bit immediate data to a register pair.
  - LDA: loads data from a memory location (specified by a 16-bit address) to the accumulator.
  - STA: stores data from the accumulator to a memory location (specified by a 16-bit address).
  - LDAX: loads data from a memory location (specified by the contents of a register pair) to the accumulator.
  - STAX: stores data from the accumulator to a memory location (specified by the contents of a register pair).
  - LHLD: loads data from two consecutive memory locations (specified by a 16-bit address) to a register pair.
  - SHLD: stores data from a register pair to two consecutive memory locations (specified by a 16-bit address).
  - XCHG: exchanges data between two register pairs.
  - PUSH: pushes data from a register pair to the stack.
  - POP: pops data from the stack to a register pair.
  - IN: reads data from an I/O device (specified by an 8-bit address) to the accumulator.
  - OUT: writes data from the accumulator to an I/O device (specified by an 8-bit address).

## Arithmetic Instructions

- Arithmetic instructions are used to perform arithmetic operations on data, such as addition, subtraction, increment, decrement, etc.
- Arithmetic instructions affect the flags in the flag register, such as carry, sign, zero, parity, and auxiliary carry.
- Some examples of arithmetic instructions are:

  - ADD: adds data from a register or a memory location to the accumulator and stores the result in the accumulator.
  - ADC: adds data from a register or a memory location and the carry flag to the accumulator and stores the result in the accumulator.
  - SUB: subtracts data from a register or a memory location from the accumulator and stores the result in the accumulator.
  - SBB: subtracts data from a register or a memory location and the borrow (complement of carry) from the accumulator and stores the result in the accumulator.
  - INR: increments data in a register or a memory location by one and affects the flags except the carry flag.
  - DCR: decrements data in a register or a memory location by one and affects the flags except the carry flag.
  - INX: increments data in a register pair by one and does not affect the flags.
  - DCX: decrements data in a register pair by one and does not affect the flags.
  - DAD: adds data from a register pair to the HL register pair and stores the result in the HL register pair. The carry flag is affected.
  - DAA: adjusts the result in the accumulator after a binary coded decimal (BCD) addition operation and affects the flags.

## Logic Instructions

- Logic instructions are used to perform logical operations on data, such as AND, OR, XOR, NOT, etc.
- Logic instructions affect the flags in the flag register, such as sign, zero, parity,