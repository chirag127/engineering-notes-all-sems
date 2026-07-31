# Design of an 8-bit ARITHMETIC LOGIC UNIT

An 8-bit arithmetic logic unit (ALU) is a combinational circuit that performs arithmetic and logic operations on two 8-bit input operands based on control inputs. The ALU is a fundamental component of any computer system, as it executes the instructions of the processor.

## ALU Functions

The ALU can perform 32 arithmetic functions and 16 logic functions, as shown in the table below. The arithmetic functions include addition, subtraction, increment, decrement, shift, rotate, and compare. The logic functions include AND, OR, XOR, NOT, NAND, NOR, XNOR, and pass. The control inputs are four select lines (S3, S2, S1, S0) and a carry-in (Cin) line. The output is an 8-bit result (R) and a carry-out (Cout) line.

| S3 | S2 | S1 | S0 | Cin | Function | Description |
|----|----|----|----|-----|----------|-------------|
| 0  | 0  | 0  | 0  | 0   | A        | Pass A      |
| 0  | 0  | 0  | 0  | 1   | A + 1    | Increment A |
| 0  | 0  | 0  | 1  | 0   | A + B    | Add A and B |
| 0  | 0  | 0  | 1  | 1   | A + B + 1| Add A, B, and Cin |
| 0  | 0  | 1  | 0  | 0   | A - 1    | Decrement A |
| 0  | 0  | 1  | 0  | 1   | A - B - 1| Subtract B and Cin from A |
| 0  | 0  | 1  | 1  | 0   | A - B    | Subtract B from A |
| 0  | 0  | 1  | 1  | 1   | A - B + 1| Subtract B from A and add Cin |
| 0  | 1  | 0  | 0  | 0   | 0        | Clear       |
| 0  | 1  | 0  | 0  | 1   | A XOR B  | Exclusive OR A and B |
| 0  | 1  | 0  | 1  | 0   | A OR B   | OR A and B  |
| 0  | 1  | 0  | 1  | 1   | A NOR B  | NOR A and B |
| 0  | 1  | 1  | 0  | 0   | NOT A    | Complement A |
| 0  | 1  | 1  | 0  | 1   | A XNOR B | Exclusive NOR A and B |
| 0  | 1  | 1  | 1  | 0   | A AND B  | AND A and B |
| 0  | 1  | 1  | 1  | 1   | A NAND B | NAND A and B |
| 1  | 0  | 0  | 0  | 0   | A        | Pass A      |
| 1  | 0  | 0  | 0  | 1   | A OR NOT B| OR A and complement B |
| 1  | 0  | 0  | 1  | 0   | A + A    | Add A and A |
| 1  | 0  | 0  | 1  | 1   | A + A + 1| Add A, A, and Cin |
| 1  | 0  | 1  | 0  | 0   | A - A    | Subtract A from A |
| 1  | 0  | 1  | 0  | 1   | A - A - 1| Subtract A and Cin from A |
| 1  | 0  | 1  | 1  | 0   | A - A +