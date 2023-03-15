### Instruction Cycles

- An instruction cycle is the time required by the CPU to execute one single instruction.
- An instruction cycle consists of three basic steps: fetch, decode, and execute .
- Fetch: The CPU fetches the instruction from the memory address pointed by the program counter (PC) and stores it in the instruction register (IR) .
- Decode: The CPU decodes the instruction in the IR and determines the operation code (opcode) and the operands .
- Execute: The CPU performs the operation specified by the opcode and the operands, and updates the PC to point to the next instruction .
- Some instructions may have an indirect address, which means the operand is not the actual data, but the address of the data. In this case, the CPU needs to read the effective address from memory before executing the instruction.
- The instruction cycle may be interrupted by external events, such as input/output devices, timers, or other processors. In this case, the CPU saves the current state of the instruction cycle and switches to handle the interrupt.
- The instruction cycle is the basic operation of the CPU, which repetitively performs fetch, decode, execute cycle to execute one program instruction.