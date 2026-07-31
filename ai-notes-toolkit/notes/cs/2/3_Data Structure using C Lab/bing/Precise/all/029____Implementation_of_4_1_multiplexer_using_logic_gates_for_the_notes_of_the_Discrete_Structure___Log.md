## Implementation of 4:1 multiplexer using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A multiplexer, also known as a data selector, is a combinational logic circuit that selects one of several input signals and forwards the selected input to a single output line. A 4:1 multiplexer has four input lines, two select lines, and one output line.

The implementation of a 4:1 multiplexer using logic gates can be done using AND, OR, and NOT gates. The circuit diagram for the implementation is shown below:

```
       +---+       +---+
I0 ---|   |       |   |
       | A |       |   |
I1 ---| N |       |   |
       | D |       | O |
I2 ---|   |       | R |
       |   |       |   |
I3 ---|   |       |   |
       +---+       +---+
         |           |
         |           |
         +-----------+
                   |
                   |
                   O
```

The truth table for the 4:1 multiplexer is shown below:

| I0 | I1 | I2 | I3 | S1 | S0 | O |
|----|----|----|----|----|----|---|
| 0  | 0  | 0  | 0  | 0  | 0  | 0 |
| 0  | 0  | 0  | 1  | 0  | 1  | 0 |
| 0  | 0  | 1  | 0  | 1  | 0  | 0 |
| 0  | 0  | 1  | 1  | 1  | 1  | 1 |
| 0  | 1  | 0  | 0  | 0  | 0  | 0 |
| 0  | 1  | 0  | 1  | 0  | 1  | 1 |
| 0  | 1  | 1  | 0  | 1  | 0  | 0 |
| 0  | 1  | 1  | 1  | 1  | 1  | 1 |
| 1  | 0  | 0  | 0  | 0  | 0  | 1 |
| 1  | 0  | 0  | 1  | 0  | 1  | 1 |
| 1  | 0  | 1  | 0  | 1  | 0  | 1 |
| 1  | 0  | 1  | 1  | 1  | 1  | 1 |
| 1  | 1  | 0  | 0  | 0  | 0  | 1 |
| 1  | 1  | 0  | 1  | 0  | 1  | 1 |
| 1  | 1  | 1  | 0  | 1  | 0  | 1 |
| 1  | 1  | 1  | 1  | 1  | 1  | 1 |

From the truth table, we can derive the Boolean expression for the output as:

O = (I3 AND S1 AND S0) OR (I2 AND S1 AND NOT S0) OR (I1 AND NOT S1 AND S0) OR (I0 AND NOT S1 AND NOT S0)

This expression can be implemented using AND, OR, and NOT gates as shown in the circuit diagram above.

In summary, a 4:1 multiplexer can be implemented using logic gates by deriving the Boolean expression for the output from the truth table and then implementing the expression using AND, OR, and NOT gates. This is a useful technique for designing combinational logic circuits.