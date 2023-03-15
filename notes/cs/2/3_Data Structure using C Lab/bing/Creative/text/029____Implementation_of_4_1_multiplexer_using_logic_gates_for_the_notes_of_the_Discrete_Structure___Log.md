## Implementation of 4:1 multiplexer using logic gates

- A multiplexer (MUX) is a digital device that selects one of the several input signals and forwards it to the output.
- A 4:1 multiplexer has four data inputs, two select lines, and one output .
- The select lines determine which input is connected to the output.
- The truth table for a 4:1 multiplexer is as follows:

| S1 | S0 | Y  |
|----|----|----|
| 0  | 0  | A0 |
| 0  | 1  | A1 |
| 1  | 0  | A2 |
| 1  | 1  | A3 |

- The output expression for a 4:1 multiplexer can be derived from the truth table as:

Y = A0.S1'.S0' + A1.S1'.S0 + A2.S1.S0' + A3.S1.S0

- To implement a 4:1 multiplexer using logic gates, we need four AND gates, one OR gate, and two NOT gates.
- The circuit diagram for a 4:1 multiplexer using logic gates is as follows :

```
    A0 ──┐
         ├─┬─┐
    A1 ──┘ │ ├─┬─┐
           │ │ │ │
    A2 ──┐ │ │ │ ├─┬─┐
         ├─┘ │ │ │ │ │
    A3 ──┘   │ │ │ │ ├─┐
             │ │ │ │ │ │
    S0 ──────┘ │ │ │ │ │ │
               │ │ │ │ │ │
    S1 ────────┘ │ │ │ │ │ │
                 │ │ │ │ │ │
    S0' ─────────┘ │ │ │ │ │ │
                   │ │ │ │ │ │
    S1' ───────────┘ │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     │ │ │ │ │
                     └─┐ │ │ │
                       └─┐ │ │
                         └─┐ │
                           └─┐
                             └─ Y
```

- The circuit works as follows:

  - The select lines S0 and S1 are inverted by the NOT gates to produce S0' and S1'.
  - The four AND gates produce the product terms A0.S1'.S0', A1.S1'.S0, A2.S1.S0', and A3.S1.S0 respectively.
  - The OR gate produces the sum of the product terms, which is the output expression Y.
  - The output Y is equal to one of the inputs A0, A1, A2, or A3 depending on the values of S0 and S1.