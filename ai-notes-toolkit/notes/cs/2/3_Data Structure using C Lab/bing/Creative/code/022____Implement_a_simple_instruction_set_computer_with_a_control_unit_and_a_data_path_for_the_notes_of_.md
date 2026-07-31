## Implement a simple instruction set computer with a control unit and a data path for the notes of the Computer Organization Lab in the subject of Computer Organization

- A simple instruction set computer (SISC) is a computer that uses a small and fixed set of instructions to perform basic operations, such as arithmetic, logic, data transfer, and control flow.
- A control unit (CU) is a component of the SISC that generates the control signals to coordinate the execution of the instructions by the data path.
- A data path (DP) is a component of the SISC that performs the actual operations on the data, such as fetching, decoding, executing, and storing the instructions and operands.
- To implement a SISC with a CU and a DP, the following steps are required:

  - Define the instruction set architecture (ISA) of the SISC, which specifies the format, encoding, and semantics of the instructions, as well as the registers, memory, and addressing modes of the SISC.
  - Design the CU of the SISC, which consists of a finite state machine (FSM) that generates the control signals based on the current state and the instruction opcode. The CU can be implemented using combinational logic circuits, such as multiplexers, decoders, and encoders.
  - Design the DP of the SISC, which consists of functional units, such as arithmetic logic unit (ALU), registers, memory, and buses, that perform the data operations. The DP can be implemented using sequential logic circuits, such as flip-flops, latches, and counters.
  - Connect the CU and the DP of the SISC, using the control signals and the data signals, to form a complete SISC processor. The CU and the DP can be connected using wires, buses, or interconnection networks.
  - Test and verify the functionality and performance of the SISC processor, using simulation tools, hardware description languages, or physical devices. The SISC processor can be tested and verified using test cases, test benches, or test vectors.

- The following figure shows an example of a SISC processor with a CU and a DP, based on the MIPS ISA:

![SISC processor with CU and DP](https://www.researchgate.net/profile/Mohammed-Al-Mahfoudh/publication/265118005/figure/fig4/AS:667727558557696@1536648418339/The-Simple-Datapath-with-the-Control-Unit.png)

- The CU of the SISC processor consists of a FSM that generates the control signals, such as RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, and ALUOp, based on the instruction opcode and the current state.
- The DP of the SISC processor consists of the following functional units:

  - Instruction memory: stores the instructions of the SISC program and provides the instruction to the CU and the DP.
  - Program counter (PC): stores the address of the current instruction and increments by 4 for each instruction cycle.
  - Register file: stores the 32 general-purpose registers of the MIPS ISA and provides two read ports and one write port for accessing the registers.
  - ALU: performs the arithmetic and logic operations on the operands, such as addition, subtraction, and, or, and slt, and provides the result and the zero flag to the DP and the CU.
  - Data memory: stores the data of the SISC program and provides one read port and one write port for accessing the data.
  - Sign-extend unit: extends the 16-bit immediate operand to 32 bits and provides it to the ALU or the shift-left-2 unit.
  - Shift-left-2 unit: shifts the 32-bit immediate operand left by 2 bits and provides it to the adder for branch address calculation.
  - Adder: adds the PC and the shifted immediate operand to calculate the branch target address and provides it to the multiplexer for PC update.
  - Multiplexers: select one of the inputs based on the control signals and provide the output to the DP or the CU.

- The CU and the DP of the SISC processor are connected using the following signals:

  - Instruction[31:0]: the 32-bit instruction from the instruction memory to the CU and the DP.
  - Instruction[31:26]: the 6-bit opcode of the instruction from the instruction memory to the CU.
  - Instruction[25:21]: the 5-bit rs register of the instruction from the instruction memory to the register file and the AL