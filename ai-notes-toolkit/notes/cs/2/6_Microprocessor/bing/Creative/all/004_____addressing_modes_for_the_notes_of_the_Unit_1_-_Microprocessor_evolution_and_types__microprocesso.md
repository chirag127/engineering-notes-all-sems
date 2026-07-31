# Addressing Modes

- Addressing modes are an aspect of the instruction set architecture in most central processing unit (CPU) designs.
- Addressing modes define how the machine language instructions in that architecture identify the operand(s) of each instruction.
- Operand is the data or the address of the data on which the instruction operates.
- Addressing modes provide different ways in which the instruction specifies the address of the operand or the operand itself.
- Different addressing modes may have different advantages and disadvantages, such as speed, flexibility, code size, etc.
- Different microprocessors may have different sets of addressing modes, depending on their design and functionality.
- Some of the common types of addressing modes are:

  - Immediate addressing mode: The instruction includes the operand along with the operation. For example, `ADD #5` means add 5 to the accumulator.
  - Register addressing mode: The instruction specifies the register that contains the operand. For example, `ADD R1` means add the contents of register R1 to the accumulator.
  - Register indirect addressing mode: The instruction specifies the register that contains the address of the operand. For example, `ADD (R1)` means add the contents of the memory location pointed by register R1 to the accumulator.
  - Direct addressing mode: The instruction specifies the address of the operand in the memory. For example, `ADD 1000H` means add the contents of the memory location 1000H to the accumulator.
  - Implicit addressing mode: The instruction does not specify the operand, but it is implied by the operation. For example, `INR A` means increment the accumulator by 1.
  - Program memory addressing mode: The instruction specifies the address of the operand in the program memory. For example, `CALL 2000H` means jump to the subroutine at the memory location 2000H.
  - Port addressing mode: The instruction specifies the address of the input/output port. For example, `IN 10H` means read the data from the input port 10H and store it in the accumulator.

- The 8085 microprocessor uses five addressing modes: Immediate, Register, Register indirect, Direct, and Implicit.
- The 8086 microprocessor uses nine addressing modes: Immediate, Register, Register indirect, Direct, Displacement, Base, Base plus index, Base plus displacement, and Base plus index plus displacement.