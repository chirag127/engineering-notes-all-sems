# Data Transfer Instructions in 8085 Microprocessor

- Data transfer instructions are the instructions that are used to transfer data between registers, memory and I/O devices in the 8085 microprocessor.
- Data transfer instructions do not affect the flags in the flag register, except for the IN and OUT instructions, which affect the parity flag.
- Data transfer instructions can be classified into the following categories:

  - Register to register transfer: These instructions transfer data from one register to another register within the microprocessor. For example, MOV A, B transfers the contents of register B to register A.
  - Immediate to register transfer: These instructions transfer an 8-bit immediate data to a register. For example, MVI A, 05H transfers the hexadecimal value 05 to register A.
  - Memory to register transfer: These instructions transfer data from a memory location to a register. For example, LDA 2000H transfers the data from the memory location 2000H to register A.
  - Register to memory transfer: These instructions transfer data from a register to a memory location. For example, STA 3000H transfers the data from register A to the memory location 3000H.
  - I/O to register transfer: These instructions transfer data from an input or output device to a register. For example, IN 05H transfers the data from the input port 05H to register A.
  - Register to I/O transfer: These instructions transfer data from a register to an input or output device. For example, OUT 06H transfers the data from register A to the output port 06H.
  - Register pair to register pair transfer: These instructions transfer data from one pair of registers to another pair of registers. For example, XCHG exchanges the contents of register pair HL and DE.
  - Immediate to register pair transfer: These instructions transfer a 16-bit immediate data to a pair of registers. For example, LXI H, 2000H transfers the hexadecimal value 2000 to register pair HL.
  - Memory to register pair transfer: These instructions transfer data from two consecutive memory locations to a pair of registers. For example, LHLD 4000H transfers the data from the memory locations 4000H and 4001H to register pair HL.
  - Register pair to memory transfer: These instructions transfer data from a pair of registers to two consecutive memory locations. For example, SHLD 5000H transfers the data from register pair HL to the memory locations 5000H and 5001H.