# Machine Control and Assembler Directives

- Machine control instructions are used to control the operation of the 8085 microprocessor, such as enabling or disabling interrupts, halting the processor, or sending or receiving serial data.
- Assembler directives are commands to the assembler that do not generate any machine code, but help in the assembly process, such as defining data, allocating memory, specifying the starting address, or including other files.

## Machine Control Instructions

- The 8085 microprocessor has four machine control instructions: HLT, NOP, SIM, and RIM.
- HLT (Halt) - Opcode: 76, Operand: None, Length: 1 byte, M-Cycles: 1, T-states: 7, Hex code: 76
  - This instruction stops the execution of the program and puts the processor in the halt state until an interrupt or reset occurs.
- NOP (No Operation) - Opcode: 00, Operand: None, Length: 1 byte, M-Cycles: 1, T-states: 4, Hex code: 00
  - This instruction does nothing and simply advances the program counter by one.
- SIM (Set Interrupt Mask) - Opcode: 30, Operand: None, Length: 1 byte, M-Cycles: 1, T-states: 4, Hex code: 30
  - This instruction is used to enable or disable the maskable interrupts RST 7.5, RST 6.5, and RST 5.5, and to send serial data through the SOD pin. The accumulator contains the bit pattern that specifies the interrupt mask and the serial data bit. The format of the accumulator is as follows:

    | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
    | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
    | M7.5  | M6.5  | M5.5  | SOD   | SID   | R7.5  | R6.5  | R5.5  |

    - M7.5, M6.5, and M5.5 are the mask bits for RST 7.5, RST 6.5, and RST 5.5 interrupts, respectively. If a mask bit is 1, the corresponding interrupt is enabled; if it is 0, the interrupt is disabled.
    - SOD is the serial output data bit, which is copied to the SOD pin after the execution of the SIM instruction.
    - SID is the serial input data bit, which is not affected by the SIM instruction.
    - R7.5, R6.5, and R5.5 are the pending interrupt bits for RST 7.5, RST 6.5, and RST 5.5 interrupts, respectively. These bits are set by the hardware when an interrupt request occurs, and are reset by the SIM instruction after the mask bits are updated.

- RIM (Read Interrupt Mask) - Opcode: 20, Operand: None, Length: 1 byte, M-Cycles: 1, T-states: 4, Hex code: 20
  - This instruction is used to read the status of the maskable interrupts and the serial data. The accumulator receives the bit pattern that indicates the interrupt mask, the pending interrupts, and the serial input data. The format of the accumulator is as follows:

    | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
    | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
    | M7.5  | M6.5  | M5.5  | SOD   | SID   | R7.5  | R6.5  | R5.5  |

    - M7.5, M6.5, and M5.5 are the mask bits for RST 7.5, RST 6.5, and RST 5.5 interrupts, respectively. These bits reflect the current state of the interrupt mask, which can be modified by the SIM instruction or the EI instruction.
    - SOD is the serial output data bit, which is not affected by the RIM instruction.
    - SID is the serial input data bit, which is copied from the SID pin to the