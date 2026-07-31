 Here is the content in markdown format:

### Architecture of 8086 microprocessor

- Register organization: 8086 has 8 general purpose 16-bit registers (BX,CX,DX,SP,BP,SI,DI,AL). It also has 8 segment registers (CS, DS, SS, ES, FS, GS).
- Bus interface unit: It is used to interface the internal data bus and address bus to the external system bus. It controls all the data transfer between the microprocessor and memory or I/O devices.
- Execution unit: It fetches, decodes and executes the instructions. It includes circuits to perform arithmetic, logical, shifting and branching operations.
- Memory addressing: 8086 has four addressing modes: register addressing, immediate addressing, direct addressing and indirect addressing.
- Memory segmentation: 8086 has a segmented memory architecture. The logical address space is divided into segments of 64KB each. Each segment has its own base address.
- Operating modes: 8086 has two operating modes - Minimun mode and Maximum mode. In minimum mode, it can address only 1MB of memory and I/O bus is multiplexed. In maximum mode, it can address up to 1GB of memory and has separate address and data buses.
- Instruction sets: 8086 has 246 instructions including data transfer, arithmetic, logical, shift, rotate, branch, string, processor control, flag control and interrupt instructions.
- Instruction format: 8086 instructions are either 1 byte, 2 bytes or variable length. The maximum instruction length is 6 bytes.
- Types of instructions: Data transfer (MOV), Arithmetic (ADD, SUB), Logical (AND, OR, XOR), Shift and rotate (SHL, SHR, ROL, ROR), Branch (JMP, JZ), String (MOVS), Processor control (HLT, IN, OUT), Flag control (CMC, CLC, STC), Interrupts (INT n).
- Interrupts: Hardware interrupts (INTR, NMI) and Software interrupts (INT n). They are used to get the attention of the processor on the occurrence of an external event or error condition.