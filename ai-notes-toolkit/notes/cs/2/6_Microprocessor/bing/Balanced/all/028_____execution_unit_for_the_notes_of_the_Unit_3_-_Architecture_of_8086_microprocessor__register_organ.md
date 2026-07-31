# Execution Unit

- The execution unit (EU) is one of the two functional units of the 8086 microprocessor. The other functional unit is the bus interface unit (BIU).
- The EU receives program instruction codes and data from the BIU, decodes and executes them, and stores the results in the general registers.
- The EU can also store the data in a memory location or send them to an I/O device by passing the data back to the BIU.
- The EU consists of the following main components:

  - Arithmetic and Logic Unit (ALU): It performs arithmetic and logical operations on 8-bit or 16-bit data. It can also perform bit manipulation and shift/rotate operations. The ALU has a 16-bit accumulator, a 16-bit temporary register, and a 16-bit flag register.
  - Instruction Decoder: It decodes the instruction codes fetched by the BIU and generates the appropriate control signals for the ALU and other components of the EU.
  - Control Unit: It coordinates the activities of the EU and the BIU. It also handles the interrupts and exceptions that may occur during the execution of a program.
  - General Registers: The EU has eight 16-bit general registers that can be used for various purposes. They are:

    - AX: Accumulator Register. It is used for arithmetic, logical, and data transfer operations. It can also be divided into two 8-bit registers: AH (high byte) and AL (low byte).
    - BX: Base Register. It is used as a base pointer for memory access. It can also be divided into two 8-bit registers: BH (high byte) and BL (low byte).
    - CX: Count Register. It is used as a loop counter or a shift/rotate count. It can also be divided into two 8-bit registers: CH (high byte) and CL (low byte).
    - DX: Data Register. It is used as an extension of the accumulator for multiplication and division operations. It can also be divided into two 8-bit registers: DH (high byte) and DL (low byte).
    - SI: Source Index Register. It is used as a source pointer for string operations.
    - DI: Destination Index Register. It is used as a destination pointer for string operations.
    - BP: Base Pointer Register. It is used as a base pointer for stack operations.
    - SP: Stack Pointer Register. It is used as a pointer to the top of the stack.

  - Segment Registers: The EU has four 16-bit segment registers that are used to define the memory segments for code, data, stack, and extra data. They are:

    - CS: Code Segment Register. It holds the base address of the code segment.
    - DS: Data Segment Register. It holds the base address of the data segment.
    - SS: Stack Segment Register. It holds the base address of the stack segment.
    - ES: Extra Segment Register. It holds the base address of the extra data segment.

  - Pointer and Index Registers: The EU has two 16-bit pointer registers and two 16-bit index registers that are used to form effective addresses for memory access. They are:

    - IP: Instruction Pointer Register. It holds the offset address of the next instruction to be executed within the code segment.
    - FLAGS: Flag Register. It holds the status flags that indicate the result of the previous operation. The flags are:

      - CF: Carry Flag. It is set if there is a carry or borrow out of the most significant bit of the result.
      - PF: Parity Flag. It is set if the result has an even number of 1 bits.
      - AF: Auxiliary Carry Flag. It is set if there is a carry or borrow out of the least significant nibble (4 bits) of the result.
      - ZF: Zero Flag. It is set if the result is zero.
      - SF: Sign Flag. It is set if the result is negative.
      - TF: Trap Flag. It is set if the single-step mode is enabled for debugging.
      - IF: Interrupt Flag. It is set if the maskable interrupts are enabled.
      - DF: Direction Flag. It is set if the string operations are performed from high address to low address.
      - OF: Overflow Flag. It is set if there is a signed overflow in the result.

    - BP: Base Pointer Register. It is used as a base pointer for stack operations.
    - SP: Stack Pointer Register. It is used as a pointer to the top of the stack