### Instruction Cycles

- Instruction cycles are the basic operations of the CPU that consist of three steps: fetch, decode, and execute.
- Fetch: The CPU retrieves an instruction from the memory unit and stores it in the instruction register (IR). The program counter (PC) is incremented to point to the next instruction.
- Decode: The CPU analyzes the instruction in the IR and determines what actions are required. The instruction may specify operands in the memory or in the registers. The CPU may need to fetch the operands from the memory or use the ones in the registers.
- Execute: The CPU performs the operation specified by the instruction. The result may be stored in the memory or in a register. The CPU may also update the condition code flags or branch to another location based on the instruction.

- The instruction cycle may vary depending on the type and format of the instruction. Some instructions may require more than one cycle to complete. Some instructions may involve additional steps such as interrupt, indirect, and interrupt cycles.
- Interrupt cycle: The CPU suspends the execution of the current instruction and transfers control to an interrupt service routine (ISR) that handles the interrupt. The CPU saves the current state of the PC and the IR before branching to the ISR. After the ISR is completed, the CPU restores the PC and the IR and resumes the execution of the interrupted instruction.
- Indirect cycle: The CPU fetches an instruction that contains an indirect address, which is a memory location that holds the actual address of the operand. The CPU fetches the operand from the indirect address and stores it in the memory buffer register (MBR). The CPU then proceeds to the execute cycle.
- I/O cycle: The CPU communicates with an input/output (I/O) device to transfer data between the memory and the device. The CPU may use programmed I/O, interrupt-driven I/O, or direct memory access (DMA) to perform the I/O operation. The CPU may need to wait for the I/O device to be ready before transferring the data.

- The instruction cycle is the fundamental operation of the CPU that enables it to execute programs. The instruction cycle is influenced by the instruction set architecture, the memory organization, and the I/O system of the computer. The instruction cycle is measured by the clock rate and the CPI (cycles per instruction) of the CPU.