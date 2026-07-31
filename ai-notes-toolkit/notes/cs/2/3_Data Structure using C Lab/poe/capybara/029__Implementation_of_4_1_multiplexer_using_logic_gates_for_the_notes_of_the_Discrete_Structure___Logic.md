## Implementation of 4:1 Multiplexer Using Logic Gates

A Multiplexer is a combinational circuit that selects one input among many input lines to be output based on the select lines. The 4:1 multiplexer is a type of multiplexer circuit that has four inputs and one output. In this lab, we will learn how to implement a 4:1 multiplexer using logic gates.

### Truth Table for 4:1 Multiplexer

Let's first understand the truth table for a 4:1 multiplexer. The following table shows the relationship between the input lines, select line, and output line.

| S | D0 | D1 | D2 | D3 | Y |
| - | -- | -- | -- | -- | - |
| 0 | 0  | 0  | 0  | 0  | 0 |
| 0 | 1  | 0  | 0  | 0  | 1 |
| 0 | 0  | 1  | 0  | 0  | 1 |
| 0 | 0  | 0  | 1  | 0  | 1 |
| 0 | 0  | 0  | 0  | 1  | 1 |
| 1 | 0  | 0  | 0  | 0  | 0 |
| 1 | 0  | 1  | 0  | 0  | 1 |
| 1 | 0  | 0  | 1  | 0  | 1 |
| 1 | 0  | 0  | 0  | 1  | 1 |
| 1 | 1  | 0  | 0  | 0  | 1 |
| 1 | 0  | 1  | 0  | 0  | 1 |
| 1 | 0  | 0  | 1  | 0  | 1 |
| 1 | 0  | 0  | 0  | 1  | 1 |
| 1 | 1  | 1  | 1  | 1  | 1 |

### Implementation of 4:1 Multiplexer Using Logic Gates

To implement a 4:1 multiplexer using logic gates, we need to follow the given steps:

1. We will use four AND gates and one OR gate to implement a 4:1 multiplexer.
2. Connect the select line (S) to the inputs of the AND gates.
3. Connect the data lines (D0, D1, D2, and D3) to one input of each AND gate.
4. Connect the complement of the select line (!S) to the other input of each AND gate.
5. Connect the outputs of the AND gates to the inputs of the OR gate.
6. The output of the OR gate will be the output of the 4:1 multiplexer.

### Circuit Diagram

The following circuit diagram shows the implementation of a 4:1 multiplexer using logic gates.

```
     _____
S --|     |
    | AND |-- Y
D0 --|_____|
      
     _____
S --|     |
    | AND |-- Y
D1 --|_____|
      
     _____
S --|     |
    | AND |-- Y
D2 --|_____|
      
     _____
S --|     |
    | AND |-- Y
D3 --|_____|
      
       _____
(!S) --|     |
       | AND |-- Y
       |_____|
```

### Conclusion

In this lab, we have learned how to implement a 4:1 multiplexer using logic gates. We have also understood the truth table for the 4:1 multiplexer and the circuit diagram for its implementation.