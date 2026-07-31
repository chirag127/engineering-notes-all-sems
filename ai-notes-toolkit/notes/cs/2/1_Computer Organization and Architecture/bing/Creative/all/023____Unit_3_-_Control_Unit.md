## Unit 3 - Control Unit

- The control unit (CU) is a component of the central processing unit (CPU) that directs the operation of the processor.
- The control unit generates control signals that enable the execution of instructions by the arithmetic logic unit (ALU), the memory, and the input/output devices.
- The control unit can be classified into two types: hardwired and microprogrammed.
- A hardwired control unit is implemented using logic gates and flip-flops. It is fast, but inflexible and difficult to modify.
- A microprogrammed control unit is implemented using a read-only memory (ROM) that stores a sequence of microinstructions. Each microinstruction specifies a set of control signals for one or more micro-operations. It is flexible and easy to modify, but slower than a hardwired control unit.
- The control unit performs the following steps to execute an instruction:
  - Fetch: The control unit fetches the instruction from the memory and stores it in the instruction register (IR).
  - Decode: The control unit decodes the instruction and determines the operation code (opcode) and the operands.
  - Execute: The control unit generates the appropriate control signals to perform the operation specified by the instruction. This may involve transferring data between registers, performing arithmetic or logical operations, accessing the memory, or interacting with the input/output devices.
  - Store: The control unit stores the result of the operation in the designated register or memory location. It also updates the program counter (PC) to point to the next instruction.