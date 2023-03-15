### Program Control

- Program control is the process of directing the execution of instructions in a program by the control unit of the processor.
- Program control instructions are the machine code that are used by the processor or in assembly language by the user to command the processor to act accordingly.
- Program control instructions can be classified into three types:
  - Conditional Branch Instructions: These instructions change the sequence of execution based on some condition, such as a flag or a register value. For example, `BEQ` (branch if equal) or `BNE` (branch if not equal).
  - Unconditional Branch Instructions: These instructions change the sequence of execution without any condition, such as `JMP` (jump) or `CALL` (call a subroutine).
  - Loop Control Instructions: These instructions are used to repeat a block of code for a certain number of times or until a condition is met, such as `LOOP` or `FOR`.
- Program control instructions can be implemented by two methods:
  - Hardwired Control: In this method, the control logic is designed using combinational circuits that generate the control signals for each instruction based on the opcode and the state of the processor. This method is fast, but inflexible and complex.
  - Microprogrammed Control: In this method, the control logic is implemented by using a programming approach. The control signals for each instruction are stored as words in a memory called the control store. A microprogram is a sequence of microinstructions that specify the micro-operations to be performed for each instruction. This method is flexible, but slower and requires more memory.