## Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- A flip-flop is an electronic circuit with two stable states that can be used to store binary data. The stored data can be changed by applying varying inputs.
- There are four basic types of flip-flops: RS, JK, T and D. Each type has a characteristic table that shows the next state of the flip-flop depending on the current state and the inputs.
- RS flip-flop has two inputs: S (set) and R (reset). It can be implemented using NAND or NOR gates. The characteristic table of RS flip-flop is:

| S | R | Q(next) | Q'(next) |
|---|---|---------|----------|
| 0 | 0 | Q       | Q'       |
| 0 | 1 | 0       | 1        |
| 1 | 0 | 1       | 0        |
| 1 | 1 | X       | X        |

- The last row of the table indicates an invalid or indeterminate state, where X means "don't care".
- JK flip-flop has two inputs: J and K. It is a modified version of RS flip-flop that avoids the invalid state. It can be implemented using NAND or NOR gates. The characteristic table of JK flip-flop is:

| J | K | Q(next) | Q'(next) |
|---|---|---------|----------|
| 0 | 0 | Q       | Q'       |
| 0 | 1 | 0       | 1        |
| 1 | 0 | 1       | 0        |
| 1 | 1 | Q'      | Q        |

- The last row of the table indicates a toggle state, where the flip-flop changes its state to the complement of the previous state.
- T flip-flop has one input: T (toggle). It is a simplified version of JK flip-flop that toggles the state when T is 1. It can be implemented using NAND or NOR gates. The characteristic table of T flip-flop is:

| T | Q(next) | Q'(next) |
|---|---------|----------|
| 0 | Q       | Q'       |
| 1 | Q'      | Q        |

- D flip-flop has one input: D (data). It is a modified version of RS flip-flop that transfers the input to the output. It can be implemented using NAND or NOR gates. The characteristic table of D flip-flop is:

| D | Q(next) | Q'(next) |
|---|---------|----------|
| 0 | 0       | 1        |
| 1 | 1       | 0        |

- To verify the state tables of the flip-flops using NAND or NOR gates, we need to construct the circuit diagrams of the flip-flops using the respective gates and observe the output LEDs display. The circuit diagrams are shown below:

- RS flip-flop using NAND gates:

![RS flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/RS_NAND.png)

- RS flip-flop using NOR gates:

![RS flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/RS_NOR.png)

- JK flip-flop using NAND gates:

![JK flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/JK_NAND.png)

- JK flip-flop using NOR gates:

![JK flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/JK_NOR.png)

- T flip-flop using NAND gates:

![T flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/T_NAND.png)

- T flip-flop using NOR gates:

![T flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/T_NOR.png)

- D flip-flop using NAND gates:

![D flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/D_NAND.png)

- D flip-flop using NOR gates:

![D flip-flop using