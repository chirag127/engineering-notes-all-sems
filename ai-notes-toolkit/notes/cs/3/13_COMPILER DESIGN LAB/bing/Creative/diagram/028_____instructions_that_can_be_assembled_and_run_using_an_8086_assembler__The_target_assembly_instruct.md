### Instructions that can be assembled and run using an 8086 assembler

The 8086 microprocessor supports a variety of instructions that can be classified into the following categories:

- Data transfer instructions: These instructions are used to transfer data between registers, memory and I/O ports. Some examples are:

  - MOV: Move data from source to destination. Syntax: MOV destination, source
  - PUSH: Push data onto the stack. Syntax: PUSH source
  - POP: Pop data from the stack. Syntax: POP destination
  - XCHG: Exchange data between two operands. Syntax: XCHG operand1, operand2
  - IN: Input data from an I/O port to a register. Syntax: IN destination, port
  - OUT: Output data from a register to an I/O port. Syntax: OUT port, source

- Arithmetic instructions: These instructions are used to perform arithmetic operations like addition, subtraction, multiplication and division. Some examples are:

  - ADD: Add two operands and store the result in the destination. Syntax: ADD destination, source
  - SUB: Subtract the source operand from the destination operand and store the result in the destination. Syntax: SUB destination, source
  - MUL: Multiply an 8-bit or 16-bit operand by the AL or AX register and store the result in AX or DX:AX. Syntax: MUL source
  - DIV: Divide a 16-bit or 32-bit operand by the AL or AX register and store the quotient in AL or AX and the remainder in AH or DX. Syntax: DIV source
  - INC: Increment an operand by one. Syntax: INC operand
  - DEC: Decrement an operand by one. Syntax: DEC operand

- Logical instructions: These instructions are used to perform bitwise logical operations like AND, OR, XOR and NOT. Some examples are:

  - AND: Perform logical AND operation between two operands and store the result in the destination. Syntax: AND destination, source
  - OR: Perform logical OR operation between two operands and store the result in the destination. Syntax: OR destination, source
  - XOR: Perform logical XOR operation between two operands and store the result in the destination. Syntax: XOR destination, source
  - NOT: Perform logical NOT operation on an operand and store the result in the same operand. Syntax: NOT operand

- Bit manipulation instructions: These instructions are used to test, set, clear or rotate bits in an operand. Some examples are:

  - TEST: Perform logical AND operation between two operands and set the flags according to the result, but do not store the result. Syntax: TEST operand1, operand2
  - SET: Set a bit in an operand to 1. Syntax: SET bit, operand
  - CLR: Clear a bit in an operand to 0. Syntax: CLR bit, operand
  - ROL: Rotate an operand left by a specified number of bits. Syntax: ROL operand, count
  - ROR: Rotate an operand right by a specified number of bits. Syntax: ROR operand, count

- Branch instructions: These instructions are used to alter the flow of execution by jumping to a different location in the program. Some examples are:

  - JMP: Unconditional jump to a specified address or label. Syntax: JMP destination
  - JZ: Jump if zero flag is set. Syntax: JZ destination
  - JNZ: Jump if zero flag is not set. Syntax: JNZ destination
  - JC: Jump if carry flag is set. Syntax: JC destination
  - JNC: Jump if carry flag is not set. Syntax: JNC destination
  - CALL: Call a subroutine at a specified address or label and save the return address on the stack. Syntax: CALL destination
  - RET: Return from a subroutine and pop the return address from the stack. Syntax: RET

- String instructions: These instructions are used to perform operations on strings of bytes or words. They use the SI and DI registers as pointers to the source and destination strings, and the CX register as a counter. Some examples are:

  - MOVSB: Move a byte from the source string to the destination string. Syntax: MOVSB
  - MOVSW: Move a word from the source string to the destination string. Syntax: MOVSW
  - CMPSB: Compare a byte from the source string with a byte from the destination string and set the flags according to the result. Syntax: CMPSB
  - CMPSW: Compare a word from the source string with a