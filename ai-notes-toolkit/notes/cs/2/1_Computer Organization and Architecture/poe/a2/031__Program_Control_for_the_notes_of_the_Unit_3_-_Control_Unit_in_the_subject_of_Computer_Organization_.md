 Here is the content in markdown format without any emojis or external links in a formal tone:

### Program Control

1. Program counter (PC): It is a register that contains the address of either the first instruction of a program or the next instruction to be executed. It is incremented automatically after each instruction execution to point to the next instruction.
2. Instruction fetch: The control unit fetches the instruction pointed to by the PC. The PC is then incremented to point to the next instruction.
3. Instruction decode and execute: The control unit decodes and executes the instruction. It may read and write data from/to the registers or memory.
4. Branching: It is a control flow mechanism. The PC can be modified to branch to a different part of the program. This allows conditional execution of instructions.
5. Subroutine call: It is a mechanism to call a subroutine (function) and return back to the calling location. The return address is saved and the PC is loaded with the address of the subroutine. After execution returns to the calling address.
6. Interrupt: An interrupt is a mechanism by which an external device can get the attention of the CPU. The CPU then handles the interrupt by suspending the running program and executing an interrupt service routine. After handling the interrupt, the CPU resumes the original program.

The above points cover the key aspects of program control in a CPU. The program counter and the control unit work in coordination to execute the instructions in a program in the intended order including mechanisms like branching and subroutine calls to enable non-linear program execution.