## Implementation of 1:4 demultiplexer using logic gates

A demultiplexer is a digital circuit that takes a single input signal and selects one of several possible output signals based on the value of a selection input. In this lab, we will be implementing a 1:4 demultiplexer using logic gates.

### Components Required

To implement a 1:4 demultiplexer using logic gates, we will need the following components:

- One input signal
- Two selection inputs
- Four output signals
- One NOT gate (inverter)
- Two AND gates
- One OR gate

### Circuit Diagram

The circuit diagram for the 1:4 demultiplexer is as follows:

```
        _________
       |         |
--->--|   NOT   |---+
       |         |   |
--->--|_________|   |
                   |
         _______   |
        |       |  |
--->----|  AND  |  |
        |       |  |
--->----|_______|  |   _______
                   +--|       |
                     |  OR   |
--->-----------------|_______|
```

### Implementation Steps

The steps to implement a 1:4 demultiplexer using logic gates are as follows:

1. Connect the input signal to the input of the NOT gate.
2. Connect the output of the NOT gate to one input of each of the two AND gates.
3. Connect one selection input to the other input of the first AND gate, and connect the complement (NOT) of that selection input to the other input of the second AND gate.
4. Connect the outputs of the two AND gates to the two inputs of the OR gate.
5. Connect the output of the OR gate to the four output signals.

### Truth Table

The truth table for the 1:4 demultiplexer is as follows:

| S1 | S0 | Input | Output 0 | Output 1 | Output 2 | Output 3 |
|----|----|-------|----------|----------|----------|----------|
| 0  | 0  | A     | A        | 0        | 0        | 0        |
| 0  | 1  | A     | 0        | A        | 0        | 0        |
| 1  | 0  | A     | 0        | 0        | A        | 0        |
| 1  | 1  | A     | 0        | 0        | 0        | A        |

### Conclusion

In this lab, we have learned how to implement a 1:4 demultiplexer using logic gates. By following the steps outlined above and understanding the truth table, we can successfully build a demultiplexer circuit that will select one of four possible output signals based on the value of two selection inputs.