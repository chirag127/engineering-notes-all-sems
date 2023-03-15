# Fetch and Execute Cycle

- The fetch and execute cycle is the basic operation cycle of a computer (also known as the fetch decode execute cycle or FDX)  .
- It is the process by which a computer retrieves a program instruction from its memory, determines what actions the instruction requires, and carries out those actions .
- The fetch and execute cycle was first proposed by John von Neumann who is famous for the Von Neumann architecture, the framework which is being followed by most computers today .
- The fetch and execute cycle consists of several stages, which are:

  - **Fetch**: The CPU fetches the instruction from the memory address that is stored in the program counter (PC) and places it in the instruction register (IR). The PC is then incremented to point to the next instruction   .
  - **Decode**: The CPU decodes the instruction in the IR and determines the operation code (opcode) and the operands. The opcode specifies what operation to perform, and the operands specify the data or the memory locations involved in the operation   .
  - **Execute**: The CPU executes the instruction by performing the operation specified by the opcode using the operands. The result of the operation may be stored in a register, a memory location, or sent to an output device   .
- The fetch and execute cycle is repeated until the program is completed or an error occurs   .
- The fetch and execute cycle is the basic operation of a computer, but it can be modified or enhanced by using techniques such as pipelining, parallel processing, caching, and branch prediction to improve the performance and efficiency of the CPU .