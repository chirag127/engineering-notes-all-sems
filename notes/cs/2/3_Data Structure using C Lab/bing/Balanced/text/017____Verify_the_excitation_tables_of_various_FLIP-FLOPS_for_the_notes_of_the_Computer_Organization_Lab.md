## Verify the excitation tables of various FLIP-FLOPS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A flip-flop is a sequential logic circuit that can store one bit of information, either 0 or 1. It has two stable states and can switch between them in response to input signals.
- The excitation table of a flip-flop shows the required input to the flip-flop to go from the current state to the next state. It is derived from the truth table of the flip-flop, which shows the output for the given combination of inputs and current state.
- There are different types of flip-flops, such as SR, D, JK and T flip-flops, each with different input and output configurations. The excitation tables of these flip-flops are as follows:

### SR flip-flop

- An SR flip-flop has two inputs, S (set) and R (reset), and one output, Q. It can be set to 1 by applying S = 1 and R = 0, reset to 0 by applying S = 0 and R = 1, or hold its current state by applying S = R = 0. Applying S = R = 1 is an invalid input that should be avoided.
- The excitation table of the SR flip-flop is:

| Q(t) | Q(t+1) | S | R |
|------|--------|---|---|
| 0    | 0      | 0 | 0 |
| 0    | 1      | 1 | 0 |
| 1    | 0      | 0 | 1 |
| 1    | 1      | 0 | 0 |

### D flip-flop

- A D flip-flop has one input, D (data), and one output, Q. It can store the value of D by applying a clock pulse. The output Q is equal to the input D at the rising edge of the clock.
- The excitation table of the D flip-flop is:

| Q(t) | Q(t+1) | D |
|------|--------|---|
| 0    | 0      | 0 |
| 0    | 1      | 1 |
| 1    | 0      | 0 |
| 1    | 1      | 1 |

### JK flip-flop

- A JK flip-flop has two inputs, J and K, and one output, Q. It can be set to 1 by applying J = 1 and K = 0, reset to 0 by applying J = 0 and K = 1, hold its current state by applying J = K = 0, or toggle its state by applying J = K = 1.
- The excitation table of the JK flip-flop is:

| Q(t) | Q(t+1) | J | K |
|------|--------|---|---|
| 0    | 0      | 0 | X |
| 0    | 1      | 1 | X |
| 1    | 0      | X | 1 |
| 1    | 1      | X | 0 |

- Note: X means don't care, meaning either 0 or 1 can be applied.

### T flip-flop

- A T flip-flop has one input, T (toggle), and one output, Q. It can hold its current state by applying T = 0, or toggle its state by applying T = 1.
- The excitation table of the T flip-flop is:

| Q(t) | Q(t+1) | T |
|------|--------|---|
| 0    | 0      | 0 |
| 0    | 1      | 1 |
| 1    | 0      | 1 |
| 1    | 1      | 0 |