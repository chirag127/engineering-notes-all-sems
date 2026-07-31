# Fetch and Execute Cycle

- The fetch and execute cycle is the basic operation or instruction cycle of a computer  .
- It is the process by which a computer retrieves a program instruction from its memory, determines what actions the instruction requires, and carries out those actions.
- The cycle consists of several stages, which are usually divided into two phases: fetch and execute  .
- The fetch phase involves the following steps:
  - The address of the next instruction to be executed is stored in the program counter (PC) register.
  - The address in the PC is moved to the memory address register (MAR), which is connected to the address lines of the system bus.
  - The PC is incremented by one to point to the next instruction.
  - The instruction stored at the address in the MAR is fetched from the memory and placed in the memory data register (MDR), which is connected to the data lines of the system bus.
  - The instruction in the MDR is moved to the instruction register (IR), where it is decoded and interpreted by the control unit.
- The execute phase involves the following steps:
  - The control unit generates the appropriate control signals to direct the data movement and processing required by the instruction.
  - The operands (data) needed by the instruction are fetched from the registers or memory and placed in the arithmetic logic unit (ALU) or other functional units.
  - The ALU or other functional units perform the operation specified by the instruction and store the result in a register or memory.
  - The cycle repeats for the next instruction until the program is completed or interrupted.
- The fetch and execute cycle is also known as the fetch-decode-execute cycle or FDX.