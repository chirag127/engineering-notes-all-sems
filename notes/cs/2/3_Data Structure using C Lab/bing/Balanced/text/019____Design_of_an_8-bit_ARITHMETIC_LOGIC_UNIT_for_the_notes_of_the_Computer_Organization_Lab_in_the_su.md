## Design of an 8-bit ARITHMETIC LOGIC UNIT for the notes of the Computer Organization Lab in the subject of Computer Organization

- An 8-bit arithmetic logic unit (ALU) is a combinational circuit that performs arithmetic and logic operations on two 8-bit input operands based on selection inputs.
- The ALU can perform common arithmetic operations such as addition and subtraction, and common logic operations such as AND, OR, XOR, and NOT.
- The ALU can also perform numerical tests such as checking whether the output is zero or negative.
- The ALU has four main components: an 8-bit adder, a 2-to-1 multiplexer, a 4-to-1 multiplexer, and a logic unit.
- The 8-bit adder is a circuit that adds two 8-bit operands and produces an 8-bit sum and a carry-out bit. The adder can also perform subtraction by using the two's complement method.
- The 2-to-1 multiplexer is a circuit that selects one of the two input bits based on a selection bit. The multiplexer is used to invert the second operand when performing subtraction.
- The 4-to-1 multiplexer is a circuit that selects one of the four input bits based on two selection bits. The multiplexer is used to select the output of the ALU from the four possible operations.
- The logic unit is a circuit that performs logic operations on the two 8-bit operands and produces an 8-bit output. The logic unit can perform AND, OR, XOR, and NOT operations.
- The ALU can be designed using the following steps:
  - Design an 8-bit adder using full adders and a carry-lookahead circuit.
  - Design a 2-to-1 multiplexer using AND, OR, and NOT gates.
  - Design a 4-to-1 multiplexer using AND, OR, and NOT gates.
  - Design a logic unit using AND, OR, XOR, and NOT gates.
  - Connect the components as shown in the figure below.

![ALU design](https://content.instructables.com/ORIG/F0O/0T6O/J0Z0LZ8P/F0O0T6OJ0Z0LZ8P.png?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=9c6f9a6f0a6c3f6a4a4f0f0c0f0f0f0f)

- The ALU has the following inputs and outputs:
  - A and B: two 8-bit input operands
  - S0 and S1: two selection bits for the 4-to-1 multiplexer
  - M: one selection bit for the 2-to-1 multiplexer
  - F: one 8-bit output of the ALU
  - C: one carry-out bit of the adder
  - Z: one zero flag that indicates whether the output is zero or not
  - N: one negative flag that indicates whether the output is negative or not
- The ALU can perform the following operations based on the selection inputs:
  - S1 S0 M | Operation
  - 0  0  0 | F = A + B
  - 0  0  1 | F = A - B
  - 0  1  X | F = A AND B
  - 1  0  X | F = A OR B
  - 1  1  X | F = A XOR B
  - X  X  X | F = NOT A

: 8-Bit Arithmetic Logic Unit (ALU) - University of Illinois Chicago
: 8-bit ALU (Arithmetic Logic Unit) - Instructables
: Arithmetic Logic Unit | Baeldung on Computer Science