# Micro-operations

- Micro-operations are the basic or atomic operations of a processor .
- They are used to implement complex machine instructions.
- They usually perform operations on data stored in one or more registers .
- They can be classified into four categories:
  - Register transfer micro-operations: They transfer data between registers or between registers and external buses of the CPU .
  - Arithmetic micro-operations: They perform arithmetic operations on numeric data stored in registers.
  - Logic micro-operations: They perform bit-wise logical operations on non-numeric data stored in registers.
  - Shift micro-operations: They perform serial transfer of data and support arithmetic, logic, and data-processing operations . They can shift the contents of a register to the left or the right.
- Micro-operations can be expressed using symbolic notation . For example:
  - R1 ← R2: This means transfer the contents of register R2 to register R1.
  - R3 ← R1 + R2: This means add the contents of registers R1 and R2 and store the result in register R3.
  - R4 ← R4 OR R5: This means perform bit-wise OR operation on the contents of registers R4 and R5 and store the result in register R4.
  - R6 ← shl R6: This means shift the contents of register R6 one bit position to the left.