## Verify the excitation tables of various FLIP-FLOPS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A flip-flop is a sequential logic circuit that can store one bit of information, either 0 or 1. It has two stable states and can switch between them in response to input signals.
- The excitation table of a flip-flop shows the required input to the flip-flop to go from the current state to the next state. It is derived from the truth table or the characteristic equation of the flip-flop.
- There are different types of flip-flops, such as SR, D, JK and T flip-flops, each with its own excitation table.

### SR flip-flop

- An SR flip-flop has two inputs, S (set) and R (reset), and one output, Q. It can be set to 1 by applying S = 1 and R = 0, or reset to 0 by applying S = 0 and R = 1. If both S and R are 0, the output remains unchanged. If both S and R are 1, the output is undefined.
- The excitation table of the SR flip-flop is:

| Q(t) | Q(t+1) | S | R |
|------|--------|---|---|
| 0    | 0      | 0 | X |
| 0    | 1      | 1 | 0 |
| 1    | 0      | 0 | 1 |
| 1    | 1      | X | 0 |

- X means don't care, meaning either 0 or 1 can be applied.

### D flip-flop

- A D flip-flop has one input, D (data), and one output, Q. It transfers the input to the output at the edge of a clock signal. It can be seen as a memory element that stores one bit of data.
- The excitation table of the D flip-flop is:

| Q(t) | Q(t+1) | D |
|------|--------|---|
| 0    | 0      | 0 |
| 0    | 1      | 1 |
| 1    | 0      | 0 |
| 1    | 1      | 1 |

- The input D is the same as the next state Q(t+1).

### JK flip-flop

- A JK flip-flop has two inputs, J and K, and one output, Q. It can be set to 1 by applying J = 1 and K = 0, or reset to 0 by applying J = 0 and K = 1. If both J and K are 0, the output remains unchanged. If both J and K are 1, the output toggles, meaning it changes to the opposite state.
- The excitation table of the JK flip-flop is:

| Q(t) | Q(t+1) | J | K |
|------|--------|---|---|
| 0    | 0      | 0 | X |
| 0    | 1      | 1 | X |
| 1    | 0      | X | 1 |
| 1    | 1      | X | 0 |

- X means don't care, meaning either 0 or 1 can be applied.

### T flip-flop

- A T flip-flop has one input, T (toggle), and one output, Q. It toggles the output when T = 1, and holds the output when T = 0. It can be seen as a counter that increments by one at every clock edge when T = 1.
- The excitation table of the T flip-flop is:

| Q(t) | Q(t+1) | T |
|------|--------|---|
| 0    | 0      | 0 |
| 0    | 1      | 1 |
| 1    | 0      | 1 |
| 1    | 1      | 0 |

- The input T is the same as the exclusive OR of the current state Q(t) and the next state Q(t+1).