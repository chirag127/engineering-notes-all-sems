## Design of an 8-bit ARITHMETIC LOGIC UNIT for the notes of the Computer Organization Lab in the subject of Computer Organization

- An 8-bit arithmetic logic unit (ALU) is a combinational circuit that performs arithmetic and logic operations on two 8-bit input operands based on control inputs.
- The ALU can perform common arithmetic operations such as addition and subtraction, and common logic operations such as AND, OR, XOR, and NOT.
- The ALU can also perform numerical tests such as checking if the result is zero or negative.
- The ALU has three main components: an 8-bit adder, a logic unit, and a multiplexer .
- The 8-bit adder is a circuit that can add or subtract two 8-bit numbers using a carry-in and a carry-out signal. The adder can be implemented using full adders, which are circuits that can add two 1-bit numbers and a carry-in and produce a 1-bit sum and a carry-out.
- The logic unit is a circuit that can perform bitwise logic operations on two 8-bit numbers. The logic unit can be implemented using logic gates, which are circuits that can perform basic logic operations on two 1-bit inputs and produce a 1-bit output.
- The multiplexer is a circuit that can select one of several inputs based on a control signal and output it to a single line. The multiplexer can be implemented using transmission gates, which are circuits that can pass or block a signal based on a control signal.
- The ALU can be designed as follows :

  - The two 8-bit input operands are denoted as A and B, and the 8-bit output is denoted as F.
  - The control inputs are denoted as S0, S1, and S2, and they determine the operation to be performed by the ALU.
  - The carry-in input is denoted as Cin, and the carry-out output is denoted as Cout.
  - The zero output is denoted as Z, and it is 1 if the output F is zero, and 0 otherwise.
  - The negative output is denoted as N, and it is 1 if the output F is negative (the most significant bit is 1), and 0 otherwise.
  - The ALU has four main blocks: an 8-bit adder, a logic unit, a 4-to-1 multiplexer, and a 1-bit multiplexer.
  - The 8-bit adder takes A and B as inputs, and produces a sum S and a carry-out Cout. The adder also has a carry-in Cin, which can be used to perform subtraction by setting Cin to 1 and complementing B.
  - The logic unit takes A and B as inputs, and produces four outputs: A AND B, A OR B, A XOR B, and NOT A.
  - The 4-to-1 multiplexer takes the four outputs of the logic unit as inputs, and selects one of them based on the control inputs S0 and S1. The output of the multiplexer is denoted as L.
  - The 1-bit multiplexer takes the sum S and the output L as inputs, and selects one of them based on the control input S2. The output of the multiplexer is the final output F of the ALU.
  - The zero output Z is obtained by connecting the output F to an 8-input NOR gate, which produces 1 if all its inputs are 0, and 0 otherwise.
  - The negative output N is obtained by connecting the most significant bit of the output F to a buffer, which produces the same value as its input.

- The ALU can perform the following operations based on the control inputs S0, S1, and S2:

  - S0 S1 S2 | Operation | F | Cout | Z | N
  - 0 0 0 | A + B | A + B | Carry-out of adder | 1 if A + B = 0, 0 otherwise | 1 if A + B < 0, 0 otherwise
  - 0 0 1 | A - B | A + (NOT B) + 1 | Carry-out of adder | 1 if A - B = 0, 0 otherwise | 1 if A - B < 0,