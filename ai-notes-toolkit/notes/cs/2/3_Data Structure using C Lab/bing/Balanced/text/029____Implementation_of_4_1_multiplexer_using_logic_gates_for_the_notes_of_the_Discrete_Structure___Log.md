## Implementation of 4:1 multiplexer using logic gates

- A multiplexer is a combinational circuit that takes multiple inputs and delivers only a single output .
- A 4:1 multiplexer has 4 input lines, 2 selection lines and 1 output line .
- The output of the multiplexer depends on the values of the selection lines and the input lines.
- The truth table for a 4:1 multiplexer is as follows :

| S1 | S0 | Y  |
|----|----|----|
| 0  | 0  | A0 |
| 0  | 1  | A1 |
| 1  | 0  | A2 |
| 1  | 1  | A3 |

- The Boolean expression for the output Y is:

Y = A0.S1'.S0' + A1.S1'.S0 + A2.S1.S0' + A3.S1.S0

- The logic diagram for a 4:1 multiplexer using logic gates is as follows :

```
    A0  A1  A2  A3
     |   |   |   |
     |   |   |   |
    AND AND AND AND
     |   |   |   |
S1---|   |   |   |
     |   |   |   |
S0---|---|   |   |
     |   |   |   |
S1'--|---|---|---|
     |   |   |   |
S0'--|---|---|---|
     |   |   |   |
     |   |   |   |
     OR  OR  OR  OR
      \   |   |   /
       \  |   |  /
        \ |   | /
         \|   |/
          \   /
           \ /
            |
            Y
```

- The 4:1 multiplexer can be used to implement any logic function of two variables by connecting the input lines to the appropriate logic values and using the selection lines as the variables.
- The 4:1 multiplexer can also be used to implement other logic gates, such as NOT, AND, OR, XOR, etc. by connecting the input lines and the selection lines in different ways.