### Arithmetic Operations

Arithmetic operations are the instructions that perform basic mathematical operations on the data stored in the registers or memory of the 8085 microprocessor. The 8085 microprocessor supports four types of arithmetic operations: addition, subtraction, increment, and decrement .

#### Addition

Addition is the operation of adding two operands and storing the result in one of the operands. The 8085 microprocessor supports three types of addition instructions: ADD, ADC, and DAD  .

- ADD: This instruction adds the contents of a register or memory to the accumulator and stores the result in the accumulator. The syntax is `ADD r` or `ADD M`, where r is any register and M is the memory location pointed by HL register pair. The flags affected by this instruction are sign, zero, auxiliary carry, parity, and carry.
- ADC: This instruction adds the contents of a register or memory and the carry flag to the accumulator and stores the result in the accumulator. The syntax is `ADC r` or `ADC M`, where r is any register and M is the memory location pointed by HL register pair. The flags affected by this instruction are the same as ADD.
- DAD: This instruction adds the contents of a register pair to the HL register pair and stores the result in the HL register pair. The syntax is `DAD rp`, where rp is any of the three register pairs: BC, DE, or HL. The only flag affected by this instruction is the carry flag.

#### Subtraction

Subtraction is the operation of subtracting one operand from another and storing the result in one of the operands. The 8085 microprocessor supports two types of subtraction instructions: SUB and SBB  .

- SUB: This instruction subtracts the contents of a register or memory from the accumulator and stores the result in the accumulator. The syntax is `SUB r` or `SUB M`, where r is any register and M is the memory location pointed by HL register pair. The flags affected by this instruction are sign, zero, auxiliary carry, parity, and carry.
- SBB: This instruction subtracts the contents of a register or memory and the carry flag from the accumulator and stores the result in the accumulator. The syntax is `SBB r` or `SBB M`, where r is any register and M is the memory location pointed by HL register pair. The flags affected by this instruction are the same as SUB.

#### Increment

Increment is the operation of adding one to an operand and storing the result in the same operand. The 8085 microprocessor supports two types of increment instructions: INR and INX  .

- INR: This instruction increments the contents of a register or memory by one and stores the result in the same register or memory. The syntax is `INR r` or `INR M`, where r is any register and M is the memory location pointed by HL register pair. The flags affected by this instruction are sign, zero, auxiliary carry, and parity.
- INX: This instruction increments the contents of a register pair by one and stores the result in the same register pair. The syntax is `INX rp`, where rp is any of the three register pairs: BC, DE, or HL. The only flag affected by this instruction is the carry flag.

#### Decrement

Decrement is the operation of subtracting one from an operand and storing the result in the same operand. The 8085 microprocessor supports two types of decrement instructions: DCR and DCX  .

- DCR: This instruction decrements the contents of a register or memory by one and stores the result in the same register or memory. The syntax is `DCR r` or `DCR M`, where r is any register and M is the memory location pointed by HL register pair. The flags affected by this instruction are sign, zero, auxiliary carry, and parity.
- DCX: This instruction decrements the contents of a register pair by one and stores the result in the same register pair. The syntax is `DCX rp`, where rp is any of the three register pairs: BC, DE, or HL. The only flag affected by this instruction is the carry flag.