### Arithmetic Instructions in 8085 Microprocessor

- Arithmetic instructions are the instructions that perform basic arithmetic operations such as addition, subtraction, increment, and decrement on the data stored in the registers or memory locations.
- The destination operand of these instructions is generally the accumulator, which holds the result of the operation.
- The source operand can be a register, a memory location, or an immediate data.
- The arithmetic instructions affect the flags according to the result of the operation. The flags that are affected are sign, zero, auxiliary carry, parity, and carry flags.
- The arithmetic instructions can be classified into four categories: addition, subtraction, increment, and decrement.

#### Addition Instructions

- The addition instructions perform the addition of two 8-bit or 16-bit operands and store the result in the accumulator or a register pair.
- The addition instructions are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| ADD r | Add the contents of register r to the accumulator | ADD B |
| ADD M | Add the contents of memory location pointed by HL pair to the accumulator | ADD M |
| ADI data | Add the 8-bit immediate data to the accumulator | ADI 25H |
| ADC r | Add the contents of register r and the carry flag to the accumulator | ADC C |
| ADC M | Add the contents of memory location pointed by HL pair and the carry flag to the accumulator | ADC M |
| ACI data | Add the 8-bit immediate data and the carry flag to the accumulator | ACI 12H |
| DAD rp | Add the contents of register pair rp to the HL pair | DAD BC |

#### Subtraction Instructions

- The subtraction instructions perform the subtraction of two 8-bit or 16-bit operands and store the result in the accumulator or a register pair.
- The subtraction instructions are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| SUB r | Subtract the contents of register r from the accumulator | SUB D |
| SUB M | Subtract the contents of memory location pointed by HL pair from the accumulator | SUB M |
| SUI data | Subtract the 8-bit immediate data from the accumulator | SUI 34H |
| SBB r | Subtract the contents of register r and the borrow (complement of carry) from the accumulator | SBB E |
| SBB M | Subtract the contents of memory location pointed by HL pair and the borrow from the accumulator | SBB M |
| SBI data | Subtract the 8-bit immediate data and the borrow from the accumulator | SBI 16H |

#### Increment Instructions

- The increment instructions perform the increment of an 8-bit or a 16-bit operand by one and store the result in the same operand.
- The increment instructions are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| INR r | Increment the contents of register r by one | INR A |
| INR M | Increment the contents of memory location pointed by HL pair by one | INR M |
| INX rp | Increment the contents of register pair rp by one | INX SP |

#### Decrement Instructions

- The decrement instructions perform the decrement of an 8-bit or a 16-bit operand by one and store the result in the same operand.
- The decrement instructions are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| DCR r | Decrement the contents of register r by one | DCR H |
| DCR M | Decrement the contents of memory location pointed by HL pair by one | DCR M |
| DCX rp | Decrement the contents of register pair rp by one | DCX DE |