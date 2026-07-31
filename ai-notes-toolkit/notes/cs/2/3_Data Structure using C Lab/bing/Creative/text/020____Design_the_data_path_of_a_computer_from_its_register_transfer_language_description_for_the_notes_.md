## Design the data path of a computer from its register transfer language description for the notes of the Computer Organization Lab in the subject of Computer Organization

- Register transfer language (RTL) is a notation that describes the movement of data between registers and the operations performed on them in a computer.
- A data path is a collection of functional units, such as arithmetic logic units (ALUs), registers, multiplexers, and buses, that perform data processing operations in a computer.
- To design the data path of a computer from its RTL description, the following steps can be followed:

  1. Identify the registers and the data types involved in the RTL description.
  2. Identify the operations and the control signals required for each RTL statement.
  3. Draw the functional units and the connections between them that can perform the operations and transfer the data between the registers.
  4. Use multiplexers to select the inputs and outputs of the functional units based on the control signals.
  5. Use buses to connect the functional units and the registers that share the same data type and width.
  6. Label the data path components and the control signals with meaningful names.

- For example, consider the following RTL description of a simple computer that can perform addition, subtraction, and logical AND operations on 8-bit unsigned integers:

  - R0, R1, R2, R3: 8-bit registers
  - IR: 8-bit instruction register
  - PC: 8-bit program counter
  - MAR: 8-bit memory address register
  - MDR: 8-bit memory data register
  - Mem: 256 x 8-bit memory
  - ALU: 8-bit arithmetic logic unit
  - OP: 2-bit operation code
  - RS: 2-bit source register
  - RD: 2-bit destination register
  - The instruction format is: OP RD RS
  - The instruction set is:

    - 00 RD RS: R<sub>RD</sub> ← R<sub>RD</sub> + R<sub>RS</sub>
    - 01 RD RS: R<sub>RD</sub> ← R<sub>RD</sub> - R<sub>RS</sub>
    - 10 RD RS: R<sub>RD</sub> ← R<sub>RD</sub> AND R<sub>RS</sub>
    - 11 RD RS: R<sub>RD</sub> ← Mem[R<sub>RS</sub>]

  - The RTL description of the instruction cycle is:

    - Fetch: MAR ← PC; PC ← PC + 1; IR ← Mem[MAR]
    - Decode: OP ← IR[7:6]; RD ← IR[5:4]; RS ← IR[3:0]
    - Execute: R<sub>RD</sub> ← ALU(R<sub>RD</sub>, R<sub>RS</sub>, OP) or MDR ← Mem[R<sub>RS</sub>]; R<sub>RD</sub> ← MDR

- The data path of the computer can be designed as follows:

  - Draw four 8-bit registers R0, R1, R2, and R3, and connect their outputs to an 8-bit bus B1.
  - Draw an 8-bit register IR, and connect its output to an 8-bit bus B2.
  - Draw an 8-bit register PC, and connect its output to an 8-bit bus B3.
  - Draw an 8-bit register MAR, and connect its input to B3 and its output to an 8-bit bus B4.
  - Draw an 8-bit register MDR, and connect its input to an 8-bit bus B5 and its output to an 8-bit bus B6.
  - Draw a 256 x 8-bit memory Mem, and connect its address input to B4, its data input to B6, and its data output to B5.
  - Draw an 8-bit ALU, and connect its inputs to two 8-bit buses B7 and B8, and its output to an 8-bit bus B9.
  - Draw two 2-bit registers OP and RD, and connect their inputs to B2.
  - Draw a 2-bit register RS, and connect its input to B2 and its output to a 2-bit bus B10.
  - Draw a 2-to-4 decoder, and connect its input to B10 and its outputs to four control signals S0, S1, S2, and S3.
  - Draw four 8-to-1