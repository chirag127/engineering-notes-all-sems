# Execution Unit

The execution unit (EU) is one of the two functional units of the 8086 microprocessor. The other functional unit is the bus interface unit (BIU). The EU is responsible for the following tasks:

- Decoding and executing the instructions fetched by the BIU from the memory or I/O devices.
- Performing arithmetic and logical operations on the data using the arithmetic and logic unit (ALU).
- Storing the results of the operations in the general registers or flags.
- Communicating with the BIU to transfer data to or from the memory or I/O devices.

The EU consists of the following components:

- Instruction pointer (IP): A 16-bit register that holds the offset address of the next instruction to be executed. It is automatically incremented by the BIU after fetching an instruction.
- Instruction decoder: A circuit that decodes the instruction opcode and generates the appropriate control signals for the ALU and the BIU.
- Arithmetic and logic unit (ALU): A circuit that performs arithmetic and logical operations on the data, such as addition, subtraction, multiplication, division, and, or, xor, etc. It also sets or clears the flags according to the result of the operation.
- General registers: Eight 16-bit registers that can be used to store data or addresses. They are divided into four groups: data registers (AX, BX, CX, DX), pointer registers (SP, BP), index registers (SI, DI), and segment registers (CS, DS, SS, ES).
- Flags register: A 16-bit register that holds the status of the EU after an operation. It consists of nine flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow. Some of these flags can be set or cleared by the programmer using instructions.