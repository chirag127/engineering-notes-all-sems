## Implement a simple instruction set computer with a control unit and a data path

- A simple instruction set computer (SISC) is a computer that can execute a limited number of instructions, usually in one or a few clock cycles per instruction.
- A control unit (CU) is a component of the SISC that generates the control signals to coordinate the execution of instructions by the data path.
- A data path (DP) is a component of the SISC that performs the arithmetic and logic operations on the data, as well as the data transfer between registers, memory, and input/output devices.
- To implement a SISC with a CU and a DP, the following steps are required:

  - Define the instruction set architecture (ISA) of the SISC, which specifies the format, encoding, and semantics of the instructions, as well as the registers, memory, and input/output devices available to the SISC .
  - Design the DP of the SISC, which consists of functional units such as arithmetic logic unit (ALU), registers, multiplexers, and buses, and their interconnections .
  - Design the CU of the SISC, which consists of a finite state machine (FSM) that generates the control signals for the DP based on the current instruction and the state of the SISC .
  - Implement the top level of the SISC by connecting the DP and the CU to the instruction memory and the data memory, as well as the input/output devices if any .
  - Test and verify the functionality and performance of the SISC using simulation tools or hardware prototyping .

- The following diagram shows an example of a simple datapath with the control unit for a SISC that can execute four instructions: add, subtract, load, and store.

![Simple Datapath with the Control Unit](https://www.researchgate.net/profile/Mohammed-Alshehri-2/publication/265118005/figure/fig4/AS:669784412016640@1536645389179/The-Simple-Datapath-with-the-Control-Unit.png)

- The instruction memory (IM) stores the instructions to be executed by the SISC. The program counter (PC) stores the address of the current instruction. The instruction register (IR) stores the current instruction. The instruction decoder (ID) decodes the current instruction and sends the opcode and the operands to the CU and the DP. The CU generates the control signals for the DP based on the opcode and the state of the SISC. The DP performs the arithmetic and logic operations on the operands using the ALU and the registers, and transfers the data between the registers, the data memory (DM), and the input/output devices. The DM stores the data to be used by the SISC. The input/output devices provide the interface between the SISC and the external world. The buses are the wires that carry the data and the addresses between the components of the SISC. The multiplexers are the switches that select the input or output of a component based on the control signals. The registers are the storage elements that hold the data temporarily. The ALU is the functional unit that performs the arithmetic and logic operations on the data.