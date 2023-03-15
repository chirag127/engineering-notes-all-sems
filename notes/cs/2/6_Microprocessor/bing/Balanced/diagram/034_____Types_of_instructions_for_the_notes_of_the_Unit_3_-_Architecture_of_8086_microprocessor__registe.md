# Types of instructions for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

## Architecture of 8086 microprocessor

- The 8086 microprocessor is a 16-bit microprocessor that was designed by Intel in 1976.
- It has 20 address lines and 16 data lines that provide up to 1 MB of memory space.
- It consists of two main units: the bus interface unit (BIU) and the execution unit (EU).
- The BIU is responsible for fetching instructions from memory, generating addresses, and transferring data to and from the EU.
- The EU is responsible for decoding and executing instructions, performing arithmetic and logical operations, and controlling the flags register.
- The 8086 microprocessor has 14 registers, divided into four groups: general-purpose registers, segment registers, pointer and index registers, and flag register.
- The general-purpose registers are AX, BX, CX, and DX, each 16-bit wide and can be used as two 8-bit registers (AH, AL, BH, BL, CH, CL, DH, and DL).
- The segment registers are CS, DS, SS, and ES, each 16-bit wide and used to store the base addresses of the code, data, stack, and extra segments respectively.
- The pointer and index registers are SP, BP, SI, and DI, each 16-bit wide and used to store the offsets of the stack, base, source, and destination respectively.
- The flag register is a 16-bit register that contains 9 flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow.
- The 8086 microprocessor has two operating modes: minimum mode and maximum mode.
- In minimum mode, the 8086 operates as a single processor in a system and uses the MN/MX pin as an output to control the bus.
- In maximum mode, the 8086 operates as a master processor in a multiprocessor system and uses the MN/MX pin as an input to receive the status signals from the bus controller.

## Instruction sets, instruction format, and types of instructions

- The 8086 microprocessor supports a powerful instruction set that provides operations like multiplication and division easily.
- The instruction set consists of 246 instructions, divided into 17 groups.
- The instruction format of the 8086 microprocessor is variable-length, ranging from 1 to 6 bytes.
- The instruction format consists of three fields: prefix, opcode, and operand.
- The prefix field is optional and used to modify the default segment, address size, or operand size of the instruction.
- The opcode field is mandatory and specifies the operation to be performed by the instruction.
- The operand field is optional and specifies the source and/or destination of the data involved in the instruction.
- The operands can be of four types: register, memory, immediate, or implied.
- The register operand refers to one of the registers in the 8086 microprocessor.
- The memory operand refers to a location in the memory space addressed by a segment and an offset.
- The immediate operand refers to a constant value encoded in the instruction itself.
- The implied operand refers to a value that is implicitly assumed by the instruction, such as the accumulator or the stack.
- The types of instructions supported by the 8086 microprocessor are:
  - Data transfer instructions: These instructions are used to move data between registers, memory, and I/O ports, such as MOV, PUSH, POP, IN, and OUT.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations on data, such as ADD, SUB, MUL, DIV, INC, and DEC.
  - Bit manipulation instructions: These instructions are used to perform logical and bitwise operations on data, such as AND, OR, XOR, NOT, SHL, and SHR.
  - String instructions: These instructions are used to perform operations on strings of data, such as REP, MOVS,