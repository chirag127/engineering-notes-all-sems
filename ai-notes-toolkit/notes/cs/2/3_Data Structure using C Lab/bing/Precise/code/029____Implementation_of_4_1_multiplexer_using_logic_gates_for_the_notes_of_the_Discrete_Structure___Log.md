## Implementation of 4:1 multiplexer using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A multiplexer (MUX) is a combinational logic circuit that selects one output from multiple inputs based on the value of its control inputs. A 4:1 multiplexer has 4 input lines, 2 control lines, and 1 output line.

The implementation of a 4:1 multiplexer using logic gates can be done using AND, OR, and NOT gates. The circuit diagram for the implementation is shown below:

```
  +---+   +---+   +---+
  | A |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | B |---|   |---|OR |
  +---+   +---+   |   |
                   |   |
  +---+   +---+   |   |
  | C |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | D |---|   |---|   |
  +---+   +---+   +---+
```

The truth table for the 4:1 multiplexer is shown below:

| A | B | C | D | S1 | S0 | Y |
|---|---|---|---|----|----|---|
| 0 | 0 | 0 | 0 | 0  | 0  | 0 |
| 0 | 0 | 0 | 1 | 0  | 1  | 0 |
| 0 | 0 | 1 | 0 | 1  | 0  | 0 |
| 0 | 0 | 1 | 1 | 1  | 1  | 0 |
| 0 | 1 | 0 | 0 | 0  | 0  | 0 |
| 0 | 1 | 0 | 1 | 0  | 1  | 1 |
| 0 | 1 | 1 | 0 | 1  | 0  | 0 |
| 0 | 1 | 1 | 1 | 1  | 1  | 1 |
| 1 | 0 | 0 | 0 | 0  | 0  | 1 |
| 1 | 0 | 0 | 1 | 0  | 1  | 0 |
| 1 | 0 | 1 | 0 | 1  | 0  | 1 |
| 1 | 0 | 1 | 1 | 1  | 1  | 0 |
| 1 | 1 | 0 | 0 | 0  | 0  | 1 |
| 1 | 1 | 0 | 1 | 0  | 1  | 1 |
| 1 | 1 | 1 | 0 | 1  | 0  | 1 |
| 1 | 1 | 1 | 1 | 1  | 1  | 1 |

From the truth table, we can derive the Boolean expression for the output Y as:

Y = (A AND NOT S1 AND NOT S0) OR (B AND NOT S1 AND S0) OR (C AND S1 AND NOT S0) OR (D AND S1 AND S0)

This expression can be implemented using AND, OR, and NOT gates as shown in the circuit diagram above.

In summary, a 4:1 multiplexer can be implemented using logic gates by deriving the Boolean expression for the output from the truth table and then constructing the circuit using AND, OR, and NOT gates. This is one of the many ways to implement a 4:1 multiplexer using logic gates. Other implementations may use different combinations of gates or different circuit designs.