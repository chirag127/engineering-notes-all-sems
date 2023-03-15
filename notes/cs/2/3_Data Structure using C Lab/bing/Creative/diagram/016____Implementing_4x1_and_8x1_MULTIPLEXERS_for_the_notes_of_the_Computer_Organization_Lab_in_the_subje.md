## Implementing 4x1 and 8x1 MULTIPLEXERS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A multiplexer or mux is a combinational circuit that selects one of several input signals and forwards it to a single output line.
- A multiplexer has n selection lines and 2^n input lines. The selection lines determine which input line is connected to the output.
- A 4x1 multiplexer has four data inputs, two selection lines and one output. The block diagram of a 4x1 multiplexer is shown below.

![4x1 multiplexer block diagram](https://www.tutorialspoint.com/digital_circuits/images/multiplexer_4x1.jpg)

- The truth table of a 4x1 multiplexer is given below.

| S1 | S0 | Y  |
|----|----|----|
| 0  | 0  | I0 |
| 0  | 1  | I1 |
| 1  | 0  | I2 |
| 1  | 1  | I3 |

- The logical expression for the output Y of a 4x1 multiplexer is:

Y = (I0.S1'.S0') + (I1.S1'.S0) + (I2.S1.S0') + (I3.S1.S0)

- A 4x1 multiplexer can be implemented using logic gates as shown below.

![4x1 multiplexer logic gates](https://technobyte.org/wp-content/uploads/2020/01/4x1-multiplexer-using-logic-gates.png)

- A 4x1 multiplexer can also be implemented using Verilog code as shown below.

```verilog
module m41(out, a, b, c, d, s1, s0);
  output out;
  input a, b, c, d, s1, s0;
  assign out = (a & ~s1 & ~s0) | (b & ~s1 & s0) | (c & s1 & ~s0) | (d & s1 & s0);
endmodule
```

- An 8x1 multiplexer has eight data inputs, three selection lines and one output. The block diagram of an 8x1 multiplexer is shown below.

![8x1 multiplexer block diagram](https://static.javatpoint.com/digital-electronics/images/multiplexer-8x1.png)

- The truth table of an 8x1 multiplexer is given below.

| S2 | S1 | S0 | Y  |
|----|----|----|----|
| 0  | 0  | 0  | A0 |
| 0  | 0  | 1  | A1 |
| 0  | 1  | 0  | A2 |
| 0  | 1  | 1  | A3 |
| 1  | 0  | 0  | A4 |
| 1  | 0  | 1  | A5 |
| 1  | 1  | 0  | A6 |
| 1  | 1  | 1  | A7 |

- The logical expression for the output Y of an 8x1 multiplexer is:

Y = (A0.S2'.S1'.S0') + (A1.S2'.S1'.S0) + (A2.S2'.S1.S0') + (A3.S2'.S1.S0) + (A4.S2.S1'.S0') + (A5.S2.S1'.S0) + (A6.S2.S1.S0') + (A7.S2.S1.S0)

- An 8x1 multiplexer can be implemented using logic gates as shown below.

![8x1 multiplexer logic gates](https://static.javatpoint.com/digital-electronics/images/multiplexer-8x1-logic-gate.png)

- An 8x1 multiplexer can also be implemented using Verilog code as shown below.

```verilog
module m81(out, a, b, c, d, e, f, g, h, s2, s1, s0);
  output out;
  input a