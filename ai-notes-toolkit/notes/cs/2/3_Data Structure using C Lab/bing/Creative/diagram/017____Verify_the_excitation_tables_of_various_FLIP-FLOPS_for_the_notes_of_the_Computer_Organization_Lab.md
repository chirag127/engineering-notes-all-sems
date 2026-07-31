## Verify the excitation tables of various FLIP-FLOPS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A flip-flop is a sequential logic circuit that can store one bit of information. It has two stable states, represented by 0 and 1, and can switch between them in response to input signals.
- The excitation table of a flip-flop shows the required input to the flip-flop to go from the current state to the next state. It is derived from the truth table or the characteristic equation of the flip-flop.
- There are different types of flip-flops, such as SR, D, JK and T, each with its own excitation table.

### SR flip-flop

- The SR flip-flop has two inputs, S (set) and R (reset), and one output, Q. It can be set to 1 by applying S = 1 and R = 0, or reset to 0 by applying S = 0 and R = 1. It can also hold its state by applying S = R = 0. However, applying S = R = 1 is an invalid input that leads to an undefined state.
- The excitation table of the SR flip-flop is as follows:

| Q(t) | Q(t+1) | S | R |
| --- | --- | --- | --- |
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | X | 0 |

- Here, Q(t) is the current state, Q(t+1) is the next state, and X means don't care (either 0 or 1).

### D flip-flop

- The D flip-flop has one input, D (data), and one output, Q. It can store the value of D by applying a clock pulse. The output Q is always equal to the input D at the rising edge of the clock.
- The excitation table of the D flip-flop is as follows:

| Q(t) | Q(t+1) | D |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

- Here, Q(t) is the current state, Q(t+1) is the next state, and D is the input.

### JK flip-flop

- The JK flip-flop has two inputs, J and K, and one output, Q. It can be set to 1 by applying J = 1 and K = 0, or reset to 0 by applying J = 0 and K = 1. It can also hold its state by applying J = K = 0. However, applying J = K = 1 makes the output Q toggle, or change to the opposite state, at the rising edge of the clock.
- The excitation table of the JK flip-flop is as follows:

| Q(t) | Q(t+1) | J | K |
| --- | --- | --- | --- |
| 0 | 0 | 0 | X |
| 0 | 1 | 1 | X |
| 1 | 0 | X | 1 |
| 1 | 1 | X | 0 |

- Here, Q(t) is the current state, Q(t+1) is the next state, and X means don't care (either 0 or 1).

### T flip-flop

- The T flip-flop has one input, T (toggle), and one output, Q. It can hold its state by applying T = 0, or toggle its state by applying T = 1, at the rising edge of the clock. The output Q is always equal to the input T XOR the previous state Q(t).
- The excitation table of the T flip-flop is as follows:

| Q(t) | Q(t+1) | T |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

- Here, Q(t) is the current state, Q(t+1) is the next state, and T is the input.