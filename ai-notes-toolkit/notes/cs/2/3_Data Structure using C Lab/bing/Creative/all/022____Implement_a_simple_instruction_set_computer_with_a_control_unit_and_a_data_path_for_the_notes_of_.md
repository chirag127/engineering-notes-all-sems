## Implement a simple instruction set computer with a control unit and a data path

- A simple instruction set computer (SISC) is a computer that uses a small and simple set of instructions to perform basic operations, such as arithmetic, logic, data transfer, and control flow.
- A control unit (CU) is a component of the SISC that generates the control signals to coordinate the execution of the instructions by the data path.
- A data path (DP) is a component of the SISC that performs the data processing operations, such as fetching, decoding, executing, and storing the instructions and the operands.
- To implement a SISC with a CU and a DP, the following steps are required:

  - Define the instruction set architecture (ISA) of the SISC, which specifies the format, encoding, and semantics of the instructions, as well as the registers, memory, and addressing modes of the SISC .
  - Design the CU of the SISC, which consists of a finite state machine (FSM) that generates the control signals based on the current state and the instruction opcode. The CU can be implemented using combinational logic circuits, such as multiplexers, decoders, and encoders .
  - Design the DP of the SISC, which consists of the following components  :
    - A program counter (PC) that holds the address of the next instruction to be executed.
    - An instruction memory (IM) that stores the instructions of the SISC program.
    - An instruction register (IR) that holds the current instruction to be decoded and executed.
    - An arithmetic logic unit (ALU) that performs the arithmetic and logic operations on the operands.
    - A data memory (DM) that stores the data values of the SISC program.
    - A set of general-purpose registers (GPRs) that hold the operands and the results of the operations.
    - A set of buses and wires that connect the components and transfer the data and the control signals.
  - Connect the CU and the DP of the SISC using the control signals and the data signals. The CU controls the DP by sending the control signals to the components of the DP, such as the PC, the IM, the IR, the ALU, the DM, and the GPRs. The DP sends the data signals to the CU, such as the instruction opcode, the operands, and the results .
  - Test and verify the functionality and the performance of the SISC using simulation tools, such as Logisim, Verilog, or VHDL. The SISC can be simulated using different input programs and test cases, and the output can be compared with the expected output .

- The following diagram shows an example of a SISC with a CU and a DP:

![SISC with CU and DP](https://www.researchgate.net/profile/Mohammed-Alshehri-2/publication/265118005/figure/fig4/AS:669646864424960@1546866914570/The-Simple-Datapath-with-the-Control-Unit.png)

- The SISC in the diagram uses a 16-bit ISA, which has four types of instructions: R-type, I-type, J-type, and H-type. The R-type instructions perform arithmetic and logic operations on two registers and store the result in a third register. The I-type instructions perform arithmetic and logic operations on a register and an immediate value and store the result in a register. The J-type instructions perform unconditional jumps to a specified address. The H-type instructions halt the execution of the program. The SISC has eight 16-bit GPRs, numbered from R0 to R7. The SISC has a 16-bit PC, a 16-bit IR, and a 16-bit ALU. The SISC has a 256-word IM and a 256-word DM, each word being 16 bits. The SISC has a 4-bit opcode field, a 3-bit source register field, a 3-bit destination register field, and a 6-bit immediate field. The SISC has the following control signals: PCEn, IMEn, IRLd, ALUOp, ALUSrc, RegDst, RegWr, DMEn, DMLd, and PCSrc.

- The following table shows the format and the encoding of the instructions of the SISC[^1