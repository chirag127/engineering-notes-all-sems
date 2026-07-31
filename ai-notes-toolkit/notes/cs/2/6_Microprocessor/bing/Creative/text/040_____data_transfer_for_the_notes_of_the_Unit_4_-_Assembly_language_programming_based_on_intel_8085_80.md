### Data Transfer Instructions in 8085 Microprocessor

- Data transfer instructions are the instructions that are used to transfer data between registers, memory and I/O devices in the 8085 microprocessor.
- Data transfer instructions can be classified into the following categories:

  - Register to register transfer: These instructions transfer data from one register to another register within the microprocessor. For example, MOV A, B transfers the contents of register B to register A.
  - Immediate to register transfer: These instructions transfer an 8-bit immediate data to a register. For example, MVI A, 05H transfers the hexadecimal value 05 to register A.
  - Memory to register transfer: These instructions transfer data from a memory location to a register. For example, LDA 2000H transfers the data stored at memory address 2000H to register A.
  - Register to memory transfer: These instructions transfer data from a register to a memory location. For example, STA 3000H transfers the contents of register A to memory address 3000H.
  - I/O to register transfer: These instructions transfer data from an input or output device to a register. For example, IN 05H transfers the data from the input device connected to port 05H to register A.
  - Register to I/O transfer: These instructions transfer data from a register to an input or output device. For example, OUT 06H transfers the contents of register A to the output device connected to port 06H.
  - Register pair to memory transfer: These instructions transfer data from a pair of registers to a memory location. For example, SHLD 4000H transfers the contents of register pair HL to memory addresses 4000H and 4001H.
  - Memory to register pair transfer: These instructions transfer data from a memory location to a pair of registers. For example, LHLD 5000H transfers the data stored at memory addresses 5000H and 5001H to register pair HL.
  - Immediate to register pair transfer: These instructions transfer a 16-bit immediate data to a pair of registers. For example, LXI H, 6000H transfers the hexadecimal value 6000 to register pair HL.
  - Stack to register pair transfer: These instructions transfer data from the top of the stack to a pair of registers. For example, POP B transfers the data from the stack to register pair BC.
  - Register pair to stack transfer: These instructions transfer data from a pair of registers to the top of the stack. For example, PUSH D transfers the contents of register pair DE to the stack.