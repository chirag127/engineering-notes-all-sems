### Micro-operations

- Micro-operations are the basic or atomic operations of a processor that are used to implement complex machine instructions .
- Micro-operations usually perform operations on data stored in one or more registers, such as transferring data, arithmetic or logical operations, and shifting or rotating data  .
- Micro-operations can be classified into four categories :
  - Register transfer micro-operations: These are used to transfer data between registers or between registers and external buses of the CPU. For example, R1 ← R2 transfers the content of register R2 to register R1.
  - Arithmetic micro-operations: These are used to perform arithmetic operations on data stored in registers, such as addition, subtraction, increment, decrement, and complement. For example, R1 ← R1 + R2 adds the content of register R2 to register R1 and stores the result in register R1.
  - Logic micro-operations: These are used to perform bitwise logical operations on data stored in registers, such as AND, OR, XOR, and NOT. For example, R1 ← R1 XOR R2 performs the exclusive OR operation on the bits of register R1 and register R2 and stores the result in register R1.
  - Shift micro-operations: These are used to shift or rotate the bits of a register to the left or the right, either with or without a sign bit. These operations are useful for serial transfer of data and for arithmetic and logic operations. For example, R1 ← shr R1 shifts the bits of register R1 to the right by one position and fills the leftmost bit with zero.