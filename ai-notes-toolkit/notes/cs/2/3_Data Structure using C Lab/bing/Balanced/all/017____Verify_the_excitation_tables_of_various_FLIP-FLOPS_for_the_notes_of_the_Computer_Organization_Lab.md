# Verify the excitation tables of various FLIP-FLOPS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A flip-flop is a sequential logic circuit that can store one bit of information, either 0 or 1.
- The output of a flip-flop depends on its current state and the inputs applied to it.
- The state of a flip-flop can change only at certain times, such as when a clock signal is applied or when a preset or clear signal is activated.
- An excitation table shows the minimum inputs that are necessary to generate a particular next state when the current state is known.
- An excitation table is derived from the truth table of a flip-flop by reversing the columns and rows.
- There are different types of flip-flops, such as SR, D, JK and T flip-flops, each with its own characteristic equation and excitation table.

## SR flip-flop

- An SR flip-flop has two inputs, S (set) and R (reset), and two outputs, Q and Q' (complement of Q).
- The characteristic equation of an SR flip-flop is Q(t+1) = S + R'Q(t), where Q(t) is the current state and Q(t+1) is the next state.
- The truth table and the excitation table of an SR flip-flop are shown below:

| S | R | Q(t+1) | Operation |
|---|---|--------|-----------|
| 0 | 0 | Q(t)   | Hold      |
| 0 | 1 | 0      | Reset     |
| 1 | 0 | 1      | Set       |
| 1 | 1 | X      | Invalid   |

| Q(t) | Q(t+1) | S | R |
|------|--------|---|---|
| 0    | 0      | 0 | X |
| 0    | 1      | 1 | 0 |
| 1    | 0      | 0 | 1 |
| 1    | 1      | X | 0 |

- To verify the excitation table of an SR flip-flop, we can use the following steps:
  - Choose any row from the excitation table and note the values of Q(t), Q(t+1), S and R.
  - Substitute the values of Q(t) and Q(t+1) in the characteristic equation and simplify it.
  - Compare the simplified equation with the values of S and R in the excitation table and check if they are consistent.
  - Repeat the process for all the rows in the excitation table.

- For example, let us verify the second row of the excitation table, where Q(t) = 0, Q(t+1) = 1, S = 1 and R = 0.
  - Substituting Q(t) = 0 and Q(t+1) = 1 in the characteristic equation, we get:
    - 1 = S + R'0
    - 1 = S + 1
    - S = 0
  - Comparing this with the values of S and R in the excitation table, we see that they are not consistent, which means that the excitation table is incorrect.
  - To correct the excitation table, we need to change the value of S from 0 to 1 in the second row, as shown below:

| Q(t) | Q(t+1) | S | R |
|------|--------|---|---|
| 0    | 0      | 0 | X |
| 0    | 1      | **1** | 0 |
| 1    | 0      | 0 | 1 |
| 1    | 1      | X | 0 |

- Similarly, we can verify the other rows of the excitation table and correct any errors if found.

## D flip-flop

- A D flip-flop has one input, D (data), and two outputs, Q and Q'.
- The characteristic equation of a D flip-flop is Q(t+1) = D, which means that the next state is equal to the input.
- The truth table and the excitation table of a D flip-flop are shown below:

| D | Q(t+1) | Operation |
|---|--------|-----------|
| 0 | 0      | Reset     |
| 1 | 1      | Set