### Data Transfer Instructions in 8085 Microprocessor

- Data transfer instructions are the instructions that are used to transfer data between registers, memory and I/O devices in the 8085 microprocessor.
- Data transfer instructions can be classified into the following categories:

  - Register to register transfer: These instructions transfer data between two registers of the microprocessor. For example, MOV A, B transfers the contents of register B to register A.
  - Immediate to register transfer: These instructions transfer an 8-bit immediate data to a register of the microprocessor. For example, MVI A, 05H transfers the hexadecimal value 05 to register A.
  - Memory to register transfer: These instructions transfer data from a memory location to a register of the microprocessor. For example, LDA 2000H transfers the data from the memory location 2000H to register A.
  - Register to memory transfer: These instructions transfer data from a register of the microprocessor to a memory location. For example, STA 3000H transfers the data from register A to the memory location 3000H.
  - I/O to register transfer: These instructions transfer data from an input or output device to a register of the microprocessor. For example, IN 05H transfers the data from the input device with address 05H to register A.
  - Register to I/O transfer: These instructions transfer data from a register of the microprocessor to an input or output device. For example, OUT 06H transfers the data from register A to the output device with address 06H.
  - Register pair to memory transfer: These instructions transfer data from a pair of registers of the microprocessor to a memory location. For example, SHLD 4000H transfers the data from register pair HL to the memory locations 4000H and 4001H.
  - Memory to register pair transfer: These instructions transfer data from a memory location to a pair of registers of the microprocessor. For example, LHLD 5000H transfers the data from the memory locations 5000H and 5001H to register pair HL.
  - Immediate to register pair transfer: These instructions transfer a 16-bit immediate data to a pair of registers of the microprocessor. For example, LXI H, 6000H transfers the hexadecimal value 6000 to register pair HL.
  - Stack to register pair transfer: These instructions transfer data from the top of the stack to a pair of registers of the microprocessor. For example, POP H transfers the data from the stack to register pair HL.
  - Register pair to stack transfer: These instructions transfer data from a pair of registers of the microprocessor to the top of the stack. For example, PUSH H transfers the data from register pair HL to the stack.

- Data transfer instructions do not affect any flags of the microprocessor, except for the IN and OUT instructions, which may affect the parity flag depending on the data transferred.