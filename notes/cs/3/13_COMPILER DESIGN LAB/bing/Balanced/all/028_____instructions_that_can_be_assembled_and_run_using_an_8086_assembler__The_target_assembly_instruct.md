# Instructions that can be assembled and run using an 8086 assembler

- The 8086 microprocessor supports a set of instructions that can be used to perform various operations on data, such as data transfer, arithmetic, logical, bit manipulation, string, control transfer, and processor control.
- The instructions are classified into different groups based on their functionality and operand types. The groups are:

  - Data Transfer Instructions: These instructions are used to transfer the data from the source operand to the destination operand. The source and destination operands can be registers, memory locations, or immediate values. Some examples of data transfer instructions are:

    - MOV: It copies the data from the source operand to the destination operand without affecting the source. For example, `MOV AX, 1234H` copies the hexadecimal value 1234 to the AX register.
    - PUSH: It decrements the stack pointer (SP) by two and copies the data from the source operand to the top of the stack. For example, `PUSH BX` pushes the value of BX register to the stack.
    - POP: It copies the data from the top of the stack to the destination operand and increments the SP by two. For example, `POP CX` pops the value from the stack to the CX register.
    - XCHG: It exchanges the data between the source and destination operands. For example, `XCHG AX, BX` swaps the values of AX and BX registers.
    - IN: It reads the data from the input port specified by the source operand and stores it in the AL or AX register. For example, `IN AL, 20H` reads the data from the port 20H and stores it in AL register.
    - OUT: It writes the data from the AL or AX register to the output port specified by the destination operand. For example, `OUT 21H, AL` writes the data from the AL register to the port 21H.

  - Arithmetic Instructions: These instructions are used to perform arithmetic operations like addition, subtraction, multiplication, division, increment, and decrement on the operands. The operands can be registers, memory locations, or immediate values. Some examples of arithmetic instructions are:

    - ADD: It adds the source operand to the destination operand and stores the result in the destination operand. It also sets the flags according to the result. For example, `ADD AX, BX` adds the values of AX and BX registers and stores the sum in AX register.
    - SUB: It subtracts the source operand from the destination operand and stores the result in the destination operand. It also sets the flags according to the result. For example, `SUB AX, BX` subtracts the value of BX register from the value of AX register and stores the difference in AX register.
    - MUL: It multiplies the source operand with the AL or AX register and stores the result in the AX or DX:AX registers. The source operand can be a byte or a word. It also sets the flags according to the result. For example, `MUL BL` multiplies the value of BL register with the value of AL register and stores the product in AX register.
    - DIV: It divides the AX or DX:AX registers by the source operand and stores the quotient in the AL or AX register and the remainder in the AH or DX register. The source operand can be a byte or a word. It also sets the flags according to the result. For example, `DIV BL` divides the value of AX register by the value of BL register and stores the quotient in AL register and the remainder in AH register.
    - INC: It increments the operand by one and sets the flags according to the result. The operand can be a register or a memory location. For example, `INC CX` increments the value of CX register by one.
    - DEC: It decrements the operand by one and sets the flags according to the result. The operand can be a register or a memory location. For example, `DEC CX` decrements the value of CX register by one.

  - Logical Instructions: These instructions are used to perform logical operations like AND, OR, XOR, NOT, and complement on the operands. The operands can be registers, memory locations, or immediate values. Some examples of logical instructions are:

    - AND: It performs the logical AND operation between the source and destination operands and stores the result in the destination operand. It also sets the flags according to the result. For example, `AND AX, BX` performs the logical AND operation between the values of AX and BX registers and stores the result in