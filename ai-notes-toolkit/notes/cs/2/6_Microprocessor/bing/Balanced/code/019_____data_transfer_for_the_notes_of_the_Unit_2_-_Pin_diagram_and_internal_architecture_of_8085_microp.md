### Data Transfer for the Notes of the Unit 2

- Data transfer is the process of moving data from one location to another in the microprocessor system.
- Data transfer can be done in different ways, such as parallel, serial, or direct memory access (DMA).
- Data transfer instructions are the instructions that transfer data in the 8085 microprocessor without any modification of data.
- Data transfer instructions are classified into the following types:

  - **MOV**: This instruction copies the contents of the source register into the destination register without any alteration. The 8-bit data is stored in the destination register or memory. The syntax is `MOV destination, source`.
  - **MVI**: This instruction loads an 8-bit immediate data into the specified register or memory location. The syntax is `MVI destination, data`.
  - **LDA**: This instruction loads the accumulator with the 8-bit data from the specified memory address. The syntax is `LDA address`.
  - **STA**: This instruction stores the contents of the accumulator into the specified memory address. The syntax is `STA address`.
  - **LHLD**: This instruction loads the 16-bit data from the specified memory address into the H and L registers. The syntax is `LHLD address`.
  - **SHLD**: This instruction stores the 16-bit data from the H and L registers into the specified memory address. The syntax is `SHLD address`.
  - **LXI**: This instruction loads a 16-bit immediate data into the specified register pair. The syntax is `LXI register pair, data`.
  - **LDAX**: This instruction loads the accumulator with the 8-bit data from the memory location specified by the register pair. The syntax is `LDAX register pair`.
  - **STAX**: This instruction stores the contents of the accumulator into the memory location specified by the register pair. The syntax is `STAX register pair`.
  - **XCHG**: This instruction exchanges the contents of the H and L registers with the contents of the D and E registers. The syntax is `XCHG`.
  - **PUSH**: This instruction pushes the contents of the specified register pair onto the stack. The syntax is `PUSH register pair`.
  - **POP**: This instruction pops the contents of the stack into the specified register pair. The syntax is `POP register pair`.
  - **IN**: This instruction reads an 8-bit data from the specified input port and stores it in the accumulator. The syntax is `IN port number`.
  - **OUT**: This instruction writes an 8-bit data from the accumulator to the specified output port. The syntax is `OUT port number`.
  - **XTHL**: This instruction exchanges the contents of the H and L registers with the contents of the top two bytes of the stack. The syntax is `XTHL`.
  - **SPHL**: This instruction loads the stack pointer with the 16-bit data from the H and L registers. The syntax is `SPHL`.
  - **PCHL**: This instruction loads the program counter with the 16-bit data from the H and L registers. The syntax is `PCHL`.

- Data transfer instructions can be used with different addressing modes, such as register, immediate, direct, register indirect, or implied.
- Data transfer instructions have different formats, such as one-byte, two-byte, or three-byte, depending on the operands involved.
- Data transfer instructions are one of the five instruction classifications in the 8085 microprocessor, along with arithmetic, logical, branching, and machine control instructions.
- Data transfer instructions are also known as copy instructions.