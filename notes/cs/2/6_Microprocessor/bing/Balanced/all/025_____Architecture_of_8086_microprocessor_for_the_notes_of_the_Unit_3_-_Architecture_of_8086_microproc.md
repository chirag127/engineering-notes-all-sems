# Architecture of 8086 Microprocessor

The 8086 microprocessor is a 16-bit processor that can access up to 1 MB of memory using 20 address lines. It has a 16-bit internal and external data bus. It consists of two independent sections or units: the Bus Interface Unit (BIU) and the Execution Unit (EU).

## Bus Interface Unit (BIU)

The BIU provides the interface of 8086 to external memory and I/O devices via the system bus. It handles all the data transfer functions. It consists of the following components:

- **Segment registers**: These are four 16-bit registers that store the base addresses of four memory segments: code, data, stack, and extra. Each segment can be up to 64 KB in size. The BIU uses these registers to generate the physical address of any memory location by adding the segment base address and the offset address.
- **Instruction pointer**: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment. The BIU uses this register to fetch the instruction bytes from the memory and store them in the instruction queue.
- **Instruction queue**: This is a 6-byte FIFO buffer that holds the prefetched instruction bytes from the memory. The BIU fills the queue whenever it is not busy with other data transfers. The EU fetches the instruction bytes from the queue for execution.
- **Address adder**: This is a circuit that performs the addition of the segment base address and the offset address to generate the 20-bit physical address.

## Execution Unit (EU)

The EU performs the arithmetic and logical operations on the data. It consists of the following components:

- **General purpose registers**: These are eight 16-bit registers that can be used for various purposes such as data manipulation, address calculation, and temporary storage. They can be accessed as four 16-bit registers (AX, BX, CX, DX) or eight 8-bit registers (AH, AL, BH, BL, CH, CL, DH, DL).
- **Pointer and index registers**: These are four 16-bit registers that are used for address calculation and indexing. They are: stack pointer (SP), base pointer (BP), source index (SI), and destination index (DI).
- **Arithmetic and logic unit (ALU)**: This is a circuit that performs the arithmetic and logical operations on the data. It can operate on 8-bit or 16-bit operands. It also sets the flags in the flag register according to the result of the operation.
- **Flag register**: This is a 16-bit register that stores the status of the EU. It consists of nine flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow. These flags are used to control the flow of the program and to indicate the outcome of the operations.
- **Control unit**: This is a circuit that controls the operation of the EU. It consists of the following components:
  - **Decode unit**: This unit decodes the instruction bytes fetched from the instruction queue and generates the control signals for the execution of the instruction.
  - **Instruction pointer**: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment. The EU uses this register to update the instruction pointer in the BIU after the execution of the instruction.
  - **Temporary register**: This is a 16-bit register that is used for temporary storage of data during the execution of the instruction.