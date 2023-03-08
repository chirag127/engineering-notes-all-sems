### Arithmetic Operations

The 8085 microprocessor performs various arithmetic operations, such as addition, subtraction, increment, and decrement. These arithmetic operations have the following mnemonics  :

- ADD: Add the contents of a register or memory location to the accumulator.
- ADI: Add an immediate 8-bit data to the accumulator.
- ADC: Add the contents of a register or memory location and the carry flag to the accumulator.
- ACI: Add an immediate 8-bit data and the carry flag to the accumulator.
- SUB: Subtract the contents of a register or memory location from the accumulator.
- SUI: Subtract an immediate 8-bit data from the accumulator.
- SBB: Subtract the contents of a register or memory location and the borrow flag from the accumulator.
- SBI: Subtract an immediate 8-bit data and the borrow flag from the accumulator.
- INR: Increment the contents of a register or memory location by one.
- INX: Increment the contents of a register pair by one.
- DCR: Decrement the contents of a register or memory location by one.
- DCX: Decrement the contents of a register pair by one.
- DAD: Add the contents of a register pair to the HL register pair.
- DAA: Adjust the accumulator after a binary coded decimal (BCD) addition.

The arithmetic operations affect the following flags in the flag register :

- Zero (Z): Set if the result is zero, reset otherwise.
- Sign (S): Set if the most significant bit of the result is one, indicating a negative value, reset otherwise.
- Parity (P): Set if the number of ones in the result is even, indicating an even parity, reset otherwise.
- Carry (CY): Set if there is a carry out from the most significant bit of the result, reset otherwise.
- Auxiliary Carry (AC): Set if there is a carry out from the lower nibble (4 bits) of the result, reset otherwise.

The following are some examples of arithmetic instructions in 8085 microprocessor :

- ADD B: Add the contents of register B to the accumulator and store the result in the accumulator.
- ADI 25H: Add the immediate data 25H to the accumulator and store the result in the accumulator.
- ADC M: Add the contents of the memory location pointed by the HL register pair and the carry flag to the accumulator and store the result in the accumulator.
- ACI 0FH: Add the immediate data 0FH and the carry flag to the accumulator and store the result in the accumulator.
- SUB C: Subtract the contents of register C from the accumulator and store the result in the accumulator.
- SUI 12H: Subtract the immediate data 12H from the accumulator and store the result in the accumulator.
- SBB D: Subtract the contents of register D and the borrow flag from the accumulator and store the result in the accumulator.
- SBI 05H: Subtract the immediate data 05H and the borrow flag from the accumulator and store the result in the accumulator.
- INR A: Increment the contents of the accumulator by one and store the result in the accumulator.
- INX BC: Increment the contents of the BC register pair by one and store the result in the BC register pair.
- DCR E: Decrement the contents of register E by one and store the result in register E.
- DCX SP: Decrement the contents of the stack pointer by one and store the result in the stack pointer.
- DAD DE: Add the contents of the DE register pair to the HL register pair and store the result in the HL register pair.
- DAA: Adjust the accumulator after a BCD addition by adding 6 to the lower nibble or the upper nibble if the lower nibble or the upper nibble is greater than 9 or if the AC flag or the CY flag is set, respectively.

I'm not sure what topic you are referring to, but I can try to help you find some good mnemonics and learning tricks if you tell me more. What are you studying or trying to learn?