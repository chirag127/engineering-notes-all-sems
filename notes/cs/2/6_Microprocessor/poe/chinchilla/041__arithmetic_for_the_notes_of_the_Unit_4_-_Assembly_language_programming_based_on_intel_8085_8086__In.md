### Arithmetic

Assembly language programming based on Intel 8085/8086 involves various instructions for arithmetic operations. In this unit, we will learn about the arithmetic instructions in detail.

#### Add Instruction

The `ADD` instruction is used to add two numbers and store the result in the accumulator. The syntax of the `ADD` instruction is:

```
ADD source
```

Where `source` can be a register or a memory location. The `ADD` instruction affects the flags as follows:

- **Carry Flag** (CY): Set if the result of the addition exceeds 8 bits.
- **Auxiliary Carry Flag** (AC): Set if there is a carry from bit 3 to bit 4 of the accumulator.
- **Zero Flag** (Z): Set if the result is zero.
- **Sign Flag** (S): Set if the result is negative.
- **Parity Flag** (P): Set if the number of 1's in the result is even.

#### Subtract Instruction

The `SUB` instruction is used to subtract two numbers and store the result in the accumulator. The syntax of the `SUB` instruction is:

```
SUB source
```

Where `source` can be a register or a memory location. The `SUB` instruction affects the flags as follows:

- **Carry Flag** (CY): Set if there is a borrow from bit 8 of the accumulator.
- **Auxiliary Carry Flag** (AC): Set if there is a borrow from bit 4 to bit 3 of the accumulator.
- **Zero Flag** (Z): Set if the result is zero.
- **Sign Flag** (S): Set if the result is negative.
- **Parity Flag** (P): Set if the number of 1's in the result is even.

#### Increment Instruction

The `INR` instruction is used to increment a register or a memory location by 1. The syntax of the `INR` instruction is:

```
INR destination
```

Where `destination` can be a register or a memory location. The `INR` instruction affects the flags as follows:

- **Zero Flag** (Z): Set if the result is zero.
- **Sign Flag** (S): Set if the result is negative.
- **Auxiliary Carry Flag** (AC): Set if there is a carry from bit 3 to bit 4 of the destination.
- **Parity Flag** (P): Set if the number of 1's in the result is even.

#### Decrement Instruction

The `DCR` instruction is used to decrement a register or a memory location by 1. The syntax of the `DCR` instruction is:

```
DCR destination
```

Where `destination` can be a register or a memory location. The `DCR` instruction affects the flags as follows:

- **Zero Flag** (Z): Set if the result is zero.
- **Sign Flag** (S): Set if the result is negative.
- **Auxiliary Carry Flag** (AC): Set if there is a borrow from bit 4 to bit 3 of the destination.
- **Parity Flag** (P): Set if the number of 1's in the result is even.

#### Increment and Decrement Instructions for Accumulator

The `INX` instruction is used to increment the contents of the HL register pair by 1. The syntax of the `INX` instruction is:

```
INX HL
```

The `DCX` instruction is used to decrement the contents of the HL register pair by 1. The syntax of the `DCX` instruction is:

```
DCX HL
```

#### Complement Accumulator Instruction

The `CMA` instruction is used to take the 1's complement of the contents of the accumulator. The syntax of the `CMA` instruction is:

```
CMA
```

#### Decimal Adjust Accumulator Instruction

The `DAA` instruction is used to adjust the contents of the accumulator to form two 4-bit Binary Coded Decimal (BCD) digits. The syntax of the `DAA` instruction is:

```
DAA
```

#### Add with Carry Instruction

The `ADC` instruction is used to add two numbers along with the carry and store the result in the accumulator. The syntax of the `ADC` instruction is:

```
ADC source
```

Where `source` can be a register or a memory location. The `ADC` instruction affects the flags as follows:

- **Carry Flag** (CY): Set if the result of the addition exceeds 8 bits.
- **Auxiliary Carry Flag** (AC): Set if there is a carry from bit 3 to bit 4 of the accumulator.
- **Zero Flag** (Z): Set if the result is zero.
- **Sign Flag** (S): Set if the result is negative.
- **Parity Flag** (P): Set if the number