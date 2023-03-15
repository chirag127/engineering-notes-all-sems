## Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- A flip-flop is an electronic circuit with two stable states that can be used to store binary data. The stored data can be changed by applying varying inputs.
- There are four main types of flip-flops: RS, JK, T and D. Each type has a different number of inputs and a different way of changing state.
- The state of a flip-flop is indicated by two outputs, Q and Q', which are complementary. The state can also be represented by a state table, which shows the next state of Q for every possible combination of inputs and present state.
- A flip-flop can be implemented using NAND or NOR gates, which are universal logic gates. The circuit diagram and the truth table of each type of flip-flop using NAND or NOR gates are shown below  .

### RS flip-flop using NAND gates

![RS flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/rs_nand.png)

| S | R | Q | Q' | State |
|---|---|---|----|-------|
| 0 | 0 | Q | Q' | No change |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 0 | 1 | 0 | Set |
| 1 | 1 | 0 | 0 | Invalid |

### RS flip-flop using NOR gates

![RS flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/rs_nor.png)

| S | R | Q | Q' | State |
|---|---|---|----|-------|
| 0 | 0 | Q | Q' | No change |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 0 | 1 | 0 | Set |
| 1 | 1 | 1 | 1 | Invalid |

### JK flip-flop using NAND gates

![JK flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/jk_nand.png)

| J | K | Q | Q' | State |
|---|---|---|----|-------|
| 0 | 0 | Q | Q' | No change |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 0 | 1 | 0 | Set |
| 1 | 1 | Q' | Q | Toggle |

### JK flip-flop using NOR gates

![JK flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/jk_nor.png)

| J | K | Q | Q' | State |
|---|---|---|----|-------|
| 0 | 0 | Q | Q' | No change |
| 0 | 1 | 0 | 1 | Reset |
| 1 | 0 | 1 | 0 | Set |
| 1 | 1 | Q' | Q | Toggle |

### T flip-flop using NAND gates

![T flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/t_nand.png)

| T | Q | Q' | State |
|---|---|----|-------|
| 0 | Q | Q' | No change |
| 1 | Q' | Q | Toggle |

### T flip-flop using NOR gates

![T flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/t_nor.png)

| T | Q | Q' | State |
|---|---|----|-------|
| 0 | Q | Q' | No change |
| 1 | Q' | Q | Toggle |

### D flip-flop using NAND gates

![D flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/d_nand.png)

| D | Q | Q' | State |
|---|---|----|-------|
| 0 | 0 | 1 | Reset |
|