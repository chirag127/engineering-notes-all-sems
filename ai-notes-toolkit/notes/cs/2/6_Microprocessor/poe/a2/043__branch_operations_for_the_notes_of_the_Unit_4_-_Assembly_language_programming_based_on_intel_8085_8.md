 Here is the content in markdown format:

### Branch Operations

- Branch instructions are used to alter the sequence of instruction execution.
- They are used to implement conditional jumps and looping.
- The 8085/8086 has unconditional, conditional and indirect branch instructions.

Unconditional Branch Instructions:

- JMP (Jump) - Transfers control to a new location unconditionally.
- CALL - Used to invoke subroutines. Saves the return address on the stack and transfers control to the subroutine.

Conditional Branch Instructions:

- JC, JNC (Jump if Carry, Jump if No Carry) - Branch if carry flag is set or reset.
- JZ, JNZ (Jump if Zero, Jump if Not Zero) - Branch if ZF flag is set or reset.
- JO, JNO (Jump if Overflow, Jump if No Overflow) - Branch if OF flag is set or reset.
- JP, JNP (Jump if Parity, Jump if No Parity) - Branch if PF flag is set or reset.

Indirect Branch Instructions:

- JMP @A - Jumps to the address specified by the 16-bit register A.
- CALL @A - Calls a subroutine whose address is specified by the 16-bit register A.

The instructions are explained in a formal manner with points and without any feelings or emojis. The content is written by myself and no external links are included. Let me know if you would like me to modify or add anything.