## Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- A flip-flop is an electronic circuit with two stable states that can be used to store binary data. The stored data can be changed by applying varying inputs.
- There are four basic types of flip-flops: RS, JK, T and D. Each type has a different characteristic table that shows the next state of the output (Q) depending on the current state (Q) and the inputs (S, R, J, K, T or D).
- RS flip-flop has two inputs: S (set) and R (reset). It can be implemented using NAND or NOR gates. The characteristic table of RS flip-flop is shown below:

| S | R | Q | Q' |
|---|---|---|----|
| 0 | 0 | Q | Q' |
| 0 | 1 | 0 | 1  |
| 1 | 0 | 1 | 0  |
| 1 | 1 | X | X  |

- The state X means undefined or indeterminate. It should be avoided as it may cause unpredictable behavior of the circuit.
- JK flip-flop has two inputs: J and K. It can be derived from RS flip-flop by adding a feedback loop from the outputs to the inputs. The characteristic table of JK flip-flop is shown below:

| J | K | Q | Q' |
|---|---|---|----|
| 0 | 0 | Q | Q' |
| 0 | 1 | 0 | 1  |
| 1 | 0 | 1 | 0  |
| 1 | 1 | Q'| Q  |

- The state Q' means the complement of Q. It means that the output toggles when both inputs are 1. This feature makes JK flip-flop more versatile than RS flip-flop.
- T flip-flop has one input: T (toggle). It can be derived from JK flip-flop by connecting both inputs together. The characteristic table of T flip-flop is shown below:

| T | Q | Q' |
|---|---|----|
| 0 | Q | Q' |
| 1 | Q'| Q  |

- The state Q' means the complement of Q. It means that the output toggles when the input is 1. This feature makes T flip-flop useful for counting applications.
- D flip-flop has one input: D (data). It can be derived from RS flip-flop by adding an inverter between S and R inputs. The characteristic table of D flip-flop is shown below:

| D | Q | Q' |
|---|---|----|
| 0 | 0 | 1  |
| 1 | 1 | 0  |

- The state Q is equal to the input D. It means that the output follows the input. This feature makes D flip-flop useful for data storage applications.
- To verify the state tables of RS, JK, T and D flip-flops using NAND and NOR gates, we need to construct the circuits using the appropriate ICs and LEDs. The circuits are shown below :

![RS flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/RS_NAND.png)

![RS flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/RS_NOR.png)

![JK flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/JK_NAND.png)

![JK flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/JK_NOR.png)

![T flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/T_NAND.png)

![T flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/T_NOR.png)

![D flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/D_N