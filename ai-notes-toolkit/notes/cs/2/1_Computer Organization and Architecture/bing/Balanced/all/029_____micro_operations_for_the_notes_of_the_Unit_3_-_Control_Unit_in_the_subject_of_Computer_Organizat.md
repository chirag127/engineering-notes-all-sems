# Micro-operations

- Micro-operations are the basic or atomic operations of a processor .
- They are used to implement complex machine instructions.
- They usually perform operations on data stored in one or more registers .
- They can be classified into four categories:
  - Register transfer micro-operations: They transfer data between registers or between registers and external buses.
  - Arithmetic micro-operations: They perform arithmetic operations on numeric data stored in registers.
  - Logic micro-operations: They perform bit-wise logical operations on non-numeric data stored in registers.
  - Shift micro-operations: They perform serial transfer of data and support arithmetic, logic, and data-processing operations .
- Micro-operations can be expressed using symbols and notations :
  - R1 ← R2: Transfer the content of register R2 to register R1.
  - R3 ← R1 + R2: Add the content of registers R1 and R2 and store the result in register R3.
  - R1 ← R1 ^ R2: Perform bitwise XOR operation on the content of registers R1 and R2 and store the result in register R1.
  - R1 ← shl R1: Shift the content of register R1 one bit position to the left.
- Micro-operations are executed by the control unit of the processor.
- Micro-operations are synchronized by a common clock.
- Micro-operations can be performed in parallel or in sequence.
- Micro-operations are the building blocks of instruction execution.