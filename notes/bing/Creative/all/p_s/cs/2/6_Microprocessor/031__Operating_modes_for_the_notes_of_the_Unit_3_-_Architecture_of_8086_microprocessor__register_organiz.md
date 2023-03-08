### Operating modes of 8086 microprocessor

- The 8086 microprocessor has two operating modes: **minimum mode** and **maximum mode**  .
- The minimum mode is used when the 8086 is the only processor in the system, and it provides all the control signals for memory and I/O interfacing.
- The maximum mode is used when the 8086 is part of a multiprocessor system, and it requires additional hardware to generate the control signals.
- The 8086 can also operate in a **virtual 8086 mode** when it is running in a protected mode operating system, which allows the execution of real mode applications that are incompatible with protected mode .

### Register organization of 8086 microprocessor

- The 8086 microprocessor has 14 registers, each of 16 bits.
- The registers are divided into four groups: **general-purpose registers**, **segment registers**, **pointer and index registers**, and **status and control registers**.
- The general-purpose registers are **AX**, **BX**, **CX**, and **DX**, which can be used for arithmetic, logic, data transfer, and I/O operations. Each of these registers can be accessed as two 8-bit registers: **AH** and **AL** for **AX**, **BH** and **BL** for **BX**, **CH** and **CL** for **CX**, and **DH** and **DL** for **DX**.
- The segment registers are **CS**, **DS**, **SS**, and **ES**, which are used to define the four segments of the memory: **code segment**, **data segment**, **stack segment**, and **extra segment**. Each segment register holds the 16-bit base address of the corresponding segment.
- The pointer and index registers are **SP**, **BP**, **SI**, and **DI**, which are used to store the offsets of the stack, data, and extra segments. **SP** and **BP** are used as stack pointers, while **SI** and **DI** are used as source and destination index registers for string operations.
- The status and control register is **FLAGS**, which contains 16 bits that indicate the status and control information of the processor. The FLAGS register has 9 active bits: **CF** (carry flag), **PF** (parity flag), **AF** (auxiliary carry flag), **ZF** (zero flag), **SF** (sign flag), **TF** (trap flag), **IF** (interrupt enable flag), **DF** (direction flag), and **OF** (overflow flag).

### Bus interface unit of 8086 microprocessor

- The bus interface unit (BIU) of the 8086 microprocessor is responsible for fetching the instructions and data from the memory, and transferring them to the execution unit (EU).
- The BIU consists of the following components: **segment registers**, **instruction pointer**, **instruction queue**, and **bus control logic**.
- The segment registers and the instruction pointer are used to generate the 20-bit physical address of the memory location to be accessed. The physical address is obtained by adding the 16-bit base address from the segment register and the 16-bit offset from the instruction pointer.
- The instruction queue is a 6-byte FIFO buffer that prefetches and stores the instructions from the memory, and feeds them to the EU. The instruction queue allows the BIU to fetch the instructions in parallel with the execution of the previous instructions by the EU, thus increasing the speed of the processor.
- The bus control logic generates the control signals for the memory and I/O interfacing, such as **ALE** (address latch enable), **RD** (read), **WR** (write), **IO/M** (I/O or memory), **DT/R** (data transmit or receive), **DEN** (data enable), **INTA** (interrupt acknowledge), and **HOLD** (hold).

### Execution unit of 8086 microprocessor

- The execution unit (EU) of the 8086 microprocessor is responsible for decoding and executing the instructions and data fetched by the BIU.
- The EU consists of the following components: **general-purpose registers**, **pointer and index registers**, **arithmetic and logic unit (ALU)**, **flags register

Some possible mnemonics and learning tricks for the topic are:

- To remember the names of the general-purpose registers, you can use the acronym **ABCD** for **AX**, **BX**, **CX**, and **DX**.
- To remember the names of the segment registers, you can use the acronym **CDES** for **CS**, **DS**, **ES**, and **SS**.
- To remember the names of the pointer and index registers, you can use the acronym **SBSD** for **SP**, **BP**, **SI**, and **DI**.
- To remember the names of the flags in the FLAGS register, you can use the acronym **CPAZSTIDO** for **CF**, **PF**, **AF**, **ZF**, **SF**, **TF**, **IF**, **DF**, and **OF**.
- To remember the order of the flags in the FLAGS register, you can use the phrase **Carry Parrots And Zebras Safely To India During October**.
- To remember the formula for the physical address, you can use the equation **Physical address = Segment address x 10H + Offset address**. The 10H is a hexadecimal constant that shifts the segment address by 4 bits to the left.