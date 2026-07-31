### Sub cycles of Control Unit

- The control unit is the part of the CPU that coordinates and controls the execution of instructions by the processor.
- The control unit performs the following functions:
  - It fetches the instruction from the memory and decodes it.
  - It generates the control signals that activate the appropriate components of the CPU and the memory to carry out the instruction.
  - It monitors the status of the CPU and the memory and handles any interrupts or exceptions that may occur during the execution.
  - It advances the program counter to the next instruction address.
- The execution of an instruction involves a sequence of substeps, generally called cycles. Each cycle consists of one or more micro-operations, which are the basic operations performed by the CPU on the data.
- The number and type of cycles depend on the instruction and the CPU architecture, but some common cycles are:
  - Fetch cycle: The control unit fetches the instruction from the memory and stores it in the instruction register. It also increments the program counter to point to the next instruction.
  - Decode cycle: The control unit decodes the instruction and determines the opcode, the operands, and the addressing mode. It also generates the effective address of the operands if needed.
  - Execute cycle: The control unit executes the instruction by activating the appropriate components of the CPU, such as the ALU, the registers, and the buses. It also performs any data transfers between the CPU and the memory or the I/O devices.
  - Interrupt cycle: The control unit checks for any external or internal interrupts that may have occurred during the execution and handles them accordingly. It may save the current state of the CPU and jump to an interrupt service routine.
- The control unit can be implemented in two ways: hardwired or microprogrammed. A hardwired control unit uses logic circuits to generate the control signals, while a microprogrammed control unit uses a sequence of microinstructions stored in a control memory to generate the control signals.