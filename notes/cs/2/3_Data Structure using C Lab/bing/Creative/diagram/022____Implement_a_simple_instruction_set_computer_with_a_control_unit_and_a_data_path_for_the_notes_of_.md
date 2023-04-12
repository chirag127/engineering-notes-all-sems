## Implement a simple instruction set computer with a control unit and a data path for the notes of the Computer Organization Lab in the subject of Computer Organization

- A simple instruction set computer (SISC) is a computer that can execute a limited set of instructions, such as arithmetic, logical, load, store, branch, and jump instructions.
- A control unit (CU) is a component of the SISC that generates the control signals to coordinate the execution of the instructions by the data path.
- A data path (DP) is a component of the SISC that performs the data processing operations, such as fetching, decoding, executing, and writing back the instructions.
- A SISC can be implemented using the following steps:

  - Define the instruction set architecture (ISA) of the SISC, which specifies the format, encoding, and semantics of the instructions, as well as the registers, memory, and addressing modes of the SISC.
  - Design the data path of the SISC, which consists of the following elements:
    - A program counter (PC) that holds the address of the next instruction to be fetched from the instruction memory (IM).
    - An instruction register (IR) that holds the fetched instruction from the IM.
    - A register file (RF) that holds the general-purpose registers of the SISC.
    - An arithmetic logic unit (ALU) that performs the arithmetic and logical operations on the operands from the RF or the immediate field of the IR.
    - A data memory (DM) that holds the data to be loaded or stored by the load or store instructions.
    - A multiplexer (MUX) that selects one of the inputs based on the control signal from the CU.
    - An adder that performs the addition operation on the inputs, such as the PC and the immediate field of the IR, or the ALU output and the PC.
    - A sign-extend unit that extends the sign of the immediate field of the IR to match the word size of the SISC.
    - A shifter that shifts the input by a specified amount, such as the immediate field of the IR, to form the branch target address.
  - Design the control unit of the SISC, which consists of the following elements:
    - A control logic that takes the opcode information from the IR and generates the control signals for the data path, such as the ALU operation, the MUX selection, the register write enable, the memory read or write enable, and the PC update.
    - A branch logic that takes the ALU zero output and the branch opcode information from the IR and generates the branch control signal for the PC update.
  - Connect the data path and the control unit of the SISC, as shown in the following diagram:

```
+-----------------+    +-----------------+
|                 |    |                 |
|  Instruction    |    |  Control Logic  |
|    Memory       |    |                 |
|                 |    |                 |
+-----------------+    +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        v                       v
+-----------------+    +-----------------+
|                 |    |                 |
|  Program        |    |  Branch Logic   |
|  Counter        |    |                 |
|                 |    |                 |
+-----------------+    +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        v                       v
+-----------------+    +-----------------+
|                 |    |                 |
|  Instruction    |    |  Control Unit   |
|  Register       |    |                 |
|                 |    |                 |
+-----------------+    +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        v                       v
+-----------------+    +-----------------+
|                 |    |                 |
|  Register       |    |  Data Path      |
|  File           |    |                 |
|                 |    |                 |
+-----------------+    +-----------------+
        |                       |
        |                       |
        |

```
