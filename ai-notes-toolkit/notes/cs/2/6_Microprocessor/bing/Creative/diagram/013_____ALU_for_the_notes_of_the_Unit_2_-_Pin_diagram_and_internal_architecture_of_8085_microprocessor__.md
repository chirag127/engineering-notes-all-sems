### ALU

- ALU stands for Arithmetic and Logic Unit. It is a functional unit of the 8085 microprocessor that performs arithmetic, logical, and bitwise operations on 8-bit data .
- ALU is connected to the internal data bus and the accumulator register. The accumulator is an 8-bit register that stores one of the operands and the result of the ALU operations .
- ALU can perform the following operations  :
  - Addition and subtraction of two 8-bit numbers, with or without carry/borrow.
  - Increment and decrement of an 8-bit number by one.
  - Logical AND, OR, XOR, and NOT of two 8-bit numbers.
  - Bitwise shift and rotate of an 8-bit number, left or right, with or without carry.
  - Compare two 8-bit numbers and set the flags accordingly.
- ALU uses a combination of transistors, resistors, and diodes to implement the logic circuits for the above operations. The ALU circuit is divided into four sections: the adder, the shifter, the logic unit, and the output multiplexer.
- The adder is a full-adder circuit that can add or subtract two 8-bit numbers, depending on the carry-in signal. The adder also generates the carry-out and the auxiliary carry flags.
- The shifter is a barrel shifter circuit that can shift or rotate an 8-bit number, left or right, by one bit. The shifter also generates the carry flag for the rotate operations.
- The logic unit is a set of gates that can perform logical AND, OR, XOR, and NOT operations on two 8-bit numbers. The logic unit also generates the zero, sign, and parity flags.
- The output multiplexer is a 4-to-1 multiplexer that can select one of the four outputs from the adder, the shifter, the logic unit, or the accumulator, depending on the operation code. The output multiplexer also generates the overflow flag for the addition and subtraction operations.
- The ALU is controlled by the instruction decoder, which generates the operation code and the carry-in signals for the ALU, based on the instruction opcode and the flags .