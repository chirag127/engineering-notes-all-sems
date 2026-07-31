## Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- A flip-flop is a bistable device that can store one bit of information. It has two stable states: 0 and 1.
- A flip-flop has two inputs and two outputs. The inputs are used to change the state of the flip-flop, and the outputs reflect the current state of the flip-flop.
- There are different types of flip-flops, such as RS, JK, T and D flip-flops. Each type has a different characteristic equation that defines how the inputs affect the outputs.
- A state table is a tabular representation of the characteristic equation of a flip-flop. It shows the next state of the flip-flop for every possible combination of inputs and present state.
- A state table can be verified by using logic gates to implement the characteristic equation of the flip-flop and comparing the outputs of the logic gates with the state table.
- NAND and NOR gates are universal gates, which means they can be used to implement any logic function. Therefore, they can be used to implement the characteristic equations of any type of flip-flop.
- The following are the state tables and the logic gate implementations of RS, JK, T and D flip-flops using NAND and NOR gates.

### RS flip-flop

- The characteristic equation of an RS flip-flop is: Q<sub>next</sub> = R'Q + SQ'
- The state table of an RS flip-flop is:

| R | S | Q<sub>next</sub> | Q'<sub>next</sub> |
|---|---|------------------|-------------------|
| 0 | 0 | Q<sub>prev</sub>  | Q'<sub>prev</sub>  |
| 0 | 1 | 1                | 0                 |
| 1 | 0 | 0                | 1                 |
| 1 | 1 | X                | X                 |

- X means don't care or indeterminate state.
- The logic gate implementation of an RS flip-flop using NAND gates is:

![RS flip-flop using NAND gates](https://i.imgur.com/9H0Z8XO.png)

- The logic gate implementation of an RS flip-flop using NOR gates is:

![RS flip-flop using NOR gates](https://i.imgur.com/4a6Z4fL.png)

### JK flip-flop

- The characteristic equation of a JK flip-flop is: Q<sub>next</sub> = JQ' + K'Q
- The state table of a JK flip-flop is:

| J | K | Q<sub>next</sub> | Q'<sub>next</sub> |
|---|---|------------------|-------------------|
| 0 | 0 | Q<sub>prev</sub>  | Q'<sub>prev</sub>  |
| 0 | 1 | 0                | 1                 |
| 1 | 0 | 1                | 0                 |
| 1 | 1 | Q'<sub>prev</sub> | Q<sub>prev</sub>  |

- The logic gate implementation of a JK flip-flop using NAND gates is:

![JK flip-flop using NAND gates](https://i.imgur.com/8y1w3qf.png)

- The logic gate implementation of a JK flip-flop using NOR gates is:

![JK flip-flop using NOR gates](https://i.imgur.com/7xZx0Yf.png)

### T flip-flop

- The characteristic equation of a T flip-flop is: Q<sub>next</sub> = TQ' + T'Q
- The state table of a T flip-flop is:

| T | Q<sub>next</sub> | Q'<sub>next</sub> |
|---|------------------|-------------------|
| 0 | Q<sub>prev</sub>  | Q'<sub>prev</sub>  |
| 1 | Q'<sub>prev</sub> | Q<sub>prev</sub>  |

- The logic gate implementation of a T flip-flop using NAND gates is:

![T flip-flop using NAND gates](https://i.imgur.com/0g0aZ9X.png)

- The logic gate implementation of a T flip-flop using NOR gates is:

![T flip-flop using NOR gates](https://i.imgur.com/6Z0n1Z4.png)

### D flip-flop

- The characteristic equation of a D flip-flop is