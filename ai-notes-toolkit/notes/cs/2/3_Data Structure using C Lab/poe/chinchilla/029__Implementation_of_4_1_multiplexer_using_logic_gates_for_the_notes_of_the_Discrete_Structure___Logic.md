## Implementation of 4:1 multiplexer using logic gates

In this lab, we will learn how to implement a 4:1 multiplexer using logic gates. A multiplexer is a device that selects one of several input signals and forwards the selected input to a single output line. A 4:1 multiplexer has four input lines and one output line. We will use logic gates to design a 4:1 multiplexer.

### Required Components

- 4 AND gates
- 2 NOT gates
- 1 OR gate

### Circuit Diagram

![Circuit Diagram for 4:1 Multiplexer](https://i.imgur.com/npvB6U9.png)

### Explanation

1. The four input lines A, B, C, and D are connected to the AND gates along with the select lines S1 and S0.
2. The select lines S1 and S0 are connected to NOT gates to invert the values of the select lines.
3. The output of the four AND gates are connected to the OR gate.
4. The output of the OR gate is the output of the 4:1 multiplexer.

### Truth Table

| S1 | S0 | A | B | C | D | Output |
|--- |--- |---|---|---|---|--------|
| 0  | 0  | I0| 0 | 0 | 0 | I0     |
| 0  | 1  | 0 | I1| 0 | 0 | I1     |
| 1  | 0  | 0 | 0 | I2| 0 | I2     |
| 1  | 1  | 0 | 0 | 0 | I3| I3     |

### Conclusion

In this lab, we learned how to implement a 4:1 multiplexer using logic gates. We used AND gates, NOT gates, and an OR gate to design the circuit. The select lines are used to choose the input signal to be forwarded to the output line. The truth table shows the output of the multiplexer for different combinations of input signals and select lines.