## Implement a simple instruction set computer with a control unit and a data path

- A simple instruction set computer (SISC) is a computer that can execute a limited set of instructions, such as arithmetic, logical, load, store, branch, and jump instructions.
- A control unit (CU) is a component of the SISC that generates the control signals to coordinate the execution of the instructions by the data path.
- A data path (DP) is a component of the SISC that performs the data processing operations, such as fetching, decoding, executing, and writing back the instructions.
- A typical SISC consists of the following components :
  - A program counter (PC) that holds the address of the next instruction to be executed.
  - An instruction memory (IM) that stores the instructions of the program.
  - A register file (RF) that holds the operands and results of the instructions.
  - An arithmetic logic unit (ALU) that performs the arithmetic and logical operations on the data.
  - A data memory (DM) that stores the data values of the program.
  - A multiplexer (MUX) that selects one of the inputs based on the control signal.
  - An adder (ADD) that increments the PC by a constant value.
  - A sign-extend (SE) unit that extends the sign of an immediate value to match the word size.
  - A shifter (SH) that shifts the bits of a value by a certain amount.
  - A control unit (CU) that generates the control signals for the data path components based on the instruction type and opcode.
- A possible data path for a SISC is shown below:

![SISC data path](https://www.researchgate.net/profile/Mohammed-Abdulrazzaq-2/publication/265118005/figure/fig4/AS:667727816466432@1536643701689/The-Simple-Datapath-with-the-Control-Unit.png)

- The data path can be divided into four stages: instruction fetch, instruction decode, execute, and write back.
- In the instruction fetch stage, the PC value is sent to the IM to fetch the instruction, and the PC is incremented by 4 by the ADD unit.
- In the instruction decode stage, the instruction is split into different fields, such as opcode, rs, rt, rd, shamt, funct, and immediate. The rs and rt fields are used to access the RF to read the source operands. The immediate field is sign-extended by the SE unit and shifted by the SH unit if needed.
- In the execute stage, the ALU performs the operation specified by the opcode and funct fields on the source operands, which can be either from the RF or the SE/SH unit. The ALU also sets a zero flag if the result is zero, which can be used for branch instructions. The DM is accessed to read or write data if the instruction is a load or store instruction.
- In the write back stage, the result of the ALU or the DM is written back to the RF if the instruction is a register-type or a load instruction. The write destination is specified by the rd or rt field, depending on the instruction type. The MUX is used to select the write destination based on the control signal.
- The control unit generates the control signals for the data path components based on the instruction type and opcode. The control signals include:
  - RegDst: selects the write destination register (rd or rt).
  - ALUSrc: selects the second ALU operand (rs or SE/SH).
  - MemToReg: selects the write back data (ALU or DM).
  - RegWrite: enables the write back to the RF.
  - MemRead: enables the read from the DM.
  - MemWrite: enables the write to the DM.
  - Branch: enables the branch if the zero flag is set.
  - ALUOp: specifies the ALU operation (add, sub, and, or, slt, etc.).
- A possible control unit for a SISC is shown below:

![SISC control unit](https://www.cise.ufl.edu/~mssz/CompOrg/Figure4.22.jpg)

- The control unit consists of a main decoder that decodes the opcode field of the instruction and generates the main control signals, such as RegDst, ALUSrc, MemToReg, RegWrite, MemRead, MemWrite, and Branch.
- The control unit also consists of