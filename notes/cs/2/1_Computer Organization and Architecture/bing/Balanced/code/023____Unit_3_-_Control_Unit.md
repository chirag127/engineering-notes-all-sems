## Unit 3 - Control Unit

The control unit is the part of the central processing unit (CPU) that directs the operation of the processor. It generates control signals that activate other parts of the CPU, such as the arithmetic logic unit (ALU), the registers, the memory, and the input/output devices.

The main functions of the control unit are:

- Fetching instructions from memory and decoding them to determine the operation and the operands.
- Generating the necessary control signals to execute the instructions, such as enabling or disabling registers, selecting the ALU operation, and initiating memory or I/O transfers.
- Sequencing the execution of instructions by using a clock signal and a program counter.
- Handling interrupts and exceptions that may occur during the execution of instructions.

The control unit can be implemented in different ways, such as:

- Hardwired control: The control unit is designed as a fixed logic circuit that generates the control signals based on the instruction bits and the current state of the CPU. This method is fast, but inflexible and difficult to modify.
- Microprogrammed control: The control unit is designed as a programmable memory that stores a sequence of microinstructions for each instruction. Each microinstruction specifies the control signals to be generated for one step of the instruction execution. This method is flexible and easy to modify, but slower than hardwired control.