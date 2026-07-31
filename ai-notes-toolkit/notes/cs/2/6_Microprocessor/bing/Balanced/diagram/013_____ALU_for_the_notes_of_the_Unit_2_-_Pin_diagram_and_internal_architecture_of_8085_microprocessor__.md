### ALU

- ALU stands for Arithmetic and Logic Unit. It is a functional unit of the 8085 microprocessor that performs arithmetic, logical, and bitwise operations on 8-bit data.
- ALU is connected to the internal data bus and the accumulator register. The accumulator is an 8-bit register that stores one of the operands and the result of the operation. The other operand is either another register or memory location.
- ALU can perform the following operations:
  - Addition and subtraction: ALU can add or subtract two 8-bit numbers with or without carry/borrow. It can also perform decimal adjust operation after addition or subtraction to correct the result for binary-coded decimal (BCD) arithmetic.
  - Logical operations: ALU can perform logical AND, OR, XOR, and complement operations on 8-bit data. It can also rotate the accumulator left or right through the carry flag.
  - Bitwise operations: ALU can test, set, reset, or complement any bit of the accumulator or a memory location. It can also perform logical shifts and rotates on 8-bit data.
- ALU also affects the status flags of the microprocessor based on the result of the operation. The status flags are stored in the flag register and indicate the following conditions:
  - Sign flag (S): Set if the result is negative, reset if positive.
  - Zero flag (Z): Set if the result is zero, reset otherwise.
  - Auxiliary carry flag (AC): Set if there is a carry/borrow from the lower nibble (4 bits) of the result, reset otherwise. Used for BCD arithmetic.
  - Parity flag (P): Set if the result has even parity (even number of 1 bits), reset if odd parity.
  - Carry flag (CY): Set if there is a carry/borrow from the most significant bit of the result, reset otherwise. Used for unsigned arithmetic and logical operations.