### Operating modes

- The 8086 microprocessor has two operating modes: **minimum mode** and **maximum mode**.
- In minimum mode, the 8086 is the only processor in the system and it generates all the control signals by itself.
- In maximum mode, the 8086 can work with other processors such as 8087, 8089, 8088, etc. and it uses a bus controller chip (8288) to generate the control signals.
- The operating mode is selected by the **MN/MX** pin of the 8086. If it is logic 1, the 8086 is in minimum mode. If it is logic 0, the 8086 is in maximum mode.

### Register organization

- The 8086 has 14 registers, each of 16 bits.
- The registers are divided into four groups: **general purpose registers**, **segment registers**, **pointer and index registers**, and **status and control registers**.
- The general purpose registers are **AX, BX, CX, DX**, which can be used for data manipulation and arithmetic operations.
- The segment registers are **CS, DS, SS, ES**, which are used to define the four segments of the memory: **code segment, data segment, stack segment, and extra segment**.
- The pointer and index registers are **SP, BP, SI, DI**, which are used to store the offsets of the stack, data, and extra segments.
- The status and control register is **FLAGS**, which contains 9 flags that indicate the status of the 8086 after an operation.

### Bus interface unit

- The bus interface unit (BIU) is responsible for fetching the instructions from the memory, generating the physical addresses, and interfacing with the external devices.
- The BIU consists of the segment registers, an instruction pointer (IP), an instruction queue, and an address adder.
- The IP register holds the offset of the next instruction to be executed within the code segment.
- The instruction queue is a 6-byte FIFO buffer that prefetches the instructions from the memory and stores them for faster execution.
- The address adder is used to generate the 20-bit physical address by adding the segment address (from the segment register) and the offset address (from the IP or other registers).

### Execution unit

- The execution unit (EU) is responsible for decoding and executing the instructions, performing arithmetic and logical operations, and updating the flags.
- The EU consists of the general purpose registers, the pointer and index registers, the FLAGS register, an arithmetic logic unit (ALU), and a control circuit.
- The ALU performs the arithmetic and logical operations on the data and sets the flags accordingly.
- The control circuit generates the control signals for the EU and the BIU based on the instruction type and the flags.

### Memory addressing

- The 8086 can address up to 1 MB of memory using 20 address lines.
- The memory is divided into 16 segments, each of 64 KB.
- Each segment has a 16-bit segment address and a 16-bit offset address.
- The segment address is stored in the segment register and the offset address is stored in the IP or other registers.
- The physical address is obtained by shifting the segment address 4 bits to the left and adding the offset address.
- The memory addressing modes are the ways of specifying the offset address of an operand in an instruction.
- The 8086 has 12 addressing modes: **immediate, register, direct, register indirect, based, indexed, based indexed, based indexed with displacement, relative, based relative, intrinsic, and implied**.

### Memory segmentation

- Memory segmentation is the technique of dividing the memory into logical segments for better memory management and protection.
- The 8086 uses four segments: code segment, data segment, stack segment, and extra segment.
- The code segment contains the executable instructions of the program.
- The data segment contains the data variables and constants of the program.
- The stack segment contains the stack data structure for storing the return addresses, parameters, and local variables of the subroutines.
- The