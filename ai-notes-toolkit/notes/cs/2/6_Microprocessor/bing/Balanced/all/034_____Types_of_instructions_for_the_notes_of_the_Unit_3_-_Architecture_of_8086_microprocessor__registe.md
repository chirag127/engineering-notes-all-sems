# Types of instructions for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

## Architecture of 8086 microprocessor

- The 8086 microprocessor is a 16-bit microprocessor that was designed by Intel in 1976.
- It has 20 address lines and 16 data lines that provide up to 1 MB of memory space.
- It consists of two main components: the bus interface unit (BIU) and the execution unit (EU).
- The BIU is responsible for fetching instructions from memory, generating memory addresses, and transferring data to and from memory and I/O devices.
- The EU is responsible for decoding and executing instructions, performing arithmetic and logical operations, and controlling the flags and registers.
- The 8086 microprocessor has 14 registers, divided into four groups: general-purpose registers, segment registers, pointer and index registers, and flag register.
- The general-purpose registers are AX, BX, CX, and DX, each 16-bit wide and can be used as two 8-bit registers (AH, AL, BH, BL, CH, CL, DH, DL).
- The segment registers are CS, DS, SS, and ES, each 16-bit wide and used to store the base addresses of the code, data, stack, and extra segments respectively.
- The pointer and index registers are SP, BP, SI, and DI, each 16-bit wide and used to store the offsets of the stack, base, source, and destination respectively.
- The flag register is a 16-bit register that contains 9 flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow.
- The 8086 microprocessor has two operating modes: minimum mode and maximum mode.
- In minimum mode, the 8086 operates as a single processor in a system and uses the pins MN/MX, S0, S1, and S2 for bus control.
- In maximum mode, the 8086 operates as a master processor in a multiprocessor system and uses the pins MN/MX, RQ/GT0, RQ/GT1, and LOCK for bus control.

## Instruction sets, instruction format, and types of instructions

- The 8086 microprocessor supports a powerful instruction set that provides operations like multiplication, division, string manipulation, and interrupts.
- The instruction set consists of 246 instructions, divided into 17 groups.
- The instruction format of the 8086 microprocessor consists of one or more bytes, each byte containing an opcode, an operand, or a prefix.
- The opcode is a 6-bit or 8-bit field that specifies the operation to be performed.
- The operand is a 4-bit, 8-bit, or 16-bit field that specifies the source or destination of the data.
- The prefix is an optional 8-bit field that modifies the operation of the instruction, such as segment override, repeat, lock, or address size.
- The types of instructions supported by the 8086 microprocessor are:
  - Data transfer instructions: These instructions are used to move data between registers, memory, and I/O devices. Examples are MOV, PUSH, POP, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations on data, such as addition, subtraction, multiplication, division, increment, decrement, etc. Examples are ADD, SUB, MUL, DIV, INC, DEC, etc.
  - Bit manipulation instructions: These instructions are used to perform logical operations on data, such as AND, OR, XOR, NOT, etc. Examples are AND, OR, XOR, NOT, TEST, etc.
  - String instructions: These instructions are used to perform operations on strings of data, such as compare, move, scan, load, store, etc. Examples are CMPS, MOVS, SCAS, LODS, STOS, etc.
  - Program execution transfer instructions: These instructions are used to change the sequence of execution of instructions, such as branch, loop, call, return, etc. Examples are JMP, JZ, J