### Fetch and Execute Cycle

- The fetch and execute cycle is the basic operation or instruction cycle of a computer  .
- It is the process by which a computer retrieves a program instruction from its memory, determines what actions the instruction requires, and carries out those actions.
- The cycle consists of several stages, which are usually divided into two phases: fetch phase and execute phase  .
- In the fetch phase, the computer performs the following steps:
  - The address of the next instruction to be executed is stored in the program counter (PC) register.
  - The address in the PC is moved to the memory address register (MAR), which is connected to the address lines of the system bus.
  - The PC is incremented by one to point to the next instruction.
  - The instruction stored at the address in the MAR is fetched from the memory and placed in the memory data register (MDR), which is connected to the data lines of the system bus.
  - The instruction in the MDR is moved to the instruction register (IR), where it is decoded and interpreted by the control unit.
- In the execute phase, the computer performs the following steps:
  - The control unit generates the appropriate control signals to execute the instruction in the IR.
  - The instruction may involve one or more of the following operations:
    - Data transfer: moving data between registers, memory, and input/output devices.
    - Arithmetic: performing arithmetic operations on data, such as addition, subtraction, multiplication, and division.
    - Logic: performing logical operations on data, such as AND, OR, NOT, and XOR.
    - Control: changing the sequence of execution, such as branching, looping, and subroutine calls.
  - The result of the execution may be stored in a register, memory, or output device, depending on the instruction.
- The cycle repeats until the program is terminated or an error occurs.