### Execution Unit for the notes of the Unit 3 - Architecture of 8086 microprocessor

- The execution unit (EU) is one of the two functional units of the 8086 microprocessor, along with the bus interface unit (BIU).
- The EU receives program instruction codes and data from the BIU, decodes and executes them, and stores the results in the general registers .
- The EU can also store the data in a memory location or send them to an I/O device by passing the data back to the BIU.
- The EU consists of the following main components:
  - Arithmetic and Logic Unit (ALU): It performs arithmetic and logical operations on 8-bit or 16-bit data, such as addition, subtraction, multiplication, division, and, or, xor, etc.
  - Control Unit (CU): It controls the flow of instructions and data within the EU and between the EU and the BIU. It also generates control signals for the BIU and the external devices.
  - Instruction Pointer (IP): It holds the offset address of the next instruction to be fetched from the code segment.
  - Flags Register: It holds the status flags that reflect the outcome of the previous operation. It also holds the control flags that affect the operation of the EU.
  - General Registers: They are used to store data and operands during the execution of instructions. They can be accessed as 8-bit or 16-bit registers. They are divided into two groups: data registers and pointer/index registers.
    - Data Registers: They are AX, BX, CX, and DX. They can be used for arithmetic, logical, and data transfer operations. They can also be used as segment registers in some cases.
    - Pointer/Index Registers: They are SP, BP, SI, and DI. They are used to store the offset addresses of the stack segment, the data segment, and the source and destination operands in string operations.
- The EU communicates with the BIU through an internal 16-bit bidirectional bus, called the EU-BIU interface.
- The EU operates independently of the BIU, as long as the BIU has fetched enough instructions and data for the EU to execute.
- The EU can execute instructions faster than the BIU can fetch them, resulting in an instruction queue in the BIU.
- The EU can also execute some instructions in parallel with the BIU, such as jump, call, and return instructions.