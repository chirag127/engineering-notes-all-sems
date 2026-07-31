### Fetch and Execute Cycle

- The fetch and execute cycle is the basic operation or instruction cycle of a computer  .
- It is the process by which a computer retrieves a program instruction from its memory, determines what actions the instruction requires, and carries out those actions.
- The cycle consists of several stages, which are explained below  .

#### Fetch Stage

- At the beginning of the fetch stage, the address of the next instruction to be executed is in the Program Counter (PC).
- The PC is a register that holds the address of the current instruction or the next instruction.
- The address in the PC is moved to the Memory Address Register (MAR), as this is the only register that is connected to the address lines of the system bus.
- The system bus is a set of wires that connects the CPU, memory, and input/output devices.
- The MAR holds the address of the memory location from which data or instruction is to be accessed.
- The control unit sends a signal to the memory to fetch the instruction from the address specified by the MAR.
- The instruction is transferred from the memory to the Memory Data Register (MDR), which is connected to the data lines of the system bus.
- The MDR holds the data or instruction that is to be written to or read from the memory.
- The instruction in the MDR is copied to the Instruction Register (IR), which holds the instruction that is currently being executed.
- The PC is incremented by one to point to the next instruction.

#### Decode Stage

- In the decode stage, the control unit decodes the instruction in the IR and determines what operation and operands are required.
- The operation code (opcode) is the part of the instruction that specifies what operation to perform, such as add, subtract, load, store, etc.
- The operands are the data or addresses that are involved in the operation, such as registers, memory locations, or immediate values.
- The control unit may need to access the registers or the memory to fetch the operands, depending on the addressing mode of the instruction.
- The addressing mode is the way of specifying how to access the operands, such as direct, indirect, immediate, register, etc.
- The control unit generates the appropriate control signals to coordinate the execution of the instruction.

#### Execute Stage

- In the execute stage, the control unit executes the instruction by performing the specified operation on the operands.
- The operation may involve the arithmetic logic unit (ALU), which is a part of the CPU that performs arithmetic and logical operations, such as addition, subtraction, multiplication, division, and, or, etc.
- The result of the operation may be stored in a register or in the memory, depending on the instruction.
- The flags register may be updated to reflect the status of the operation, such as zero, carry, overflow, etc.
- The flags register is a register that holds one-bit values that indicate certain conditions that occur after an operation.
- The cycle is repeated until the program is completed or an error occurs.