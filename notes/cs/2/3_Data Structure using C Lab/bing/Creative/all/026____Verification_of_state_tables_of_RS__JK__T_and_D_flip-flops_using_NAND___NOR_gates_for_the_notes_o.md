# Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- A flip-flop is a bistable circuit that can store one bit of information. It has two stable states, represented by 0 and 1, and can switch between them in response to input signals.
- There are four basic types of flip-flops: RS, JK, T and D. Each type has a different characteristic equation that defines the output in terms of the input and the previous state.
- RS flip-flop: The output Q depends on the inputs S (set) and R (reset). If S=1 and R=0, Q is set to 1. If S=0 and R=1, Q is reset to 0. If S=0 and R=0, Q remains unchanged. If S=1 and R=1, the output is undefined.
- JK flip-flop: The output Q depends on the inputs J and K, as well as the clock signal CLK. On the rising edge of CLK, if J=1 and K=0, Q is set to 1. If J=0 and K=1, Q is reset to 0. If J=1 and K=1, Q is toggled (complemented). If J=0 and K=0, Q remains unchanged.
- T flip-flop: The output Q depends on the input T (toggle) and the clock signal CLK. On the rising edge of CLK, if T=1, Q is toggled. If T=0, Q remains unchanged.
- D flip-flop: The output Q depends on the input D (data) and the clock signal CLK. On the rising edge of CLK, Q is set to the value of D.

- To verify the state tables of these flip-flops, we can use NAND or NOR gates to implement them. NAND and NOR gates are universal gates, meaning they can be used to construct any other logic gate or circuit.
- RS flip-flop using NAND gates: The circuit diagram and the truth table are shown below.

![RS flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/rs_nand.png)

| S | R | Q | Q' |
|---|---|---|----|
| 0 | 0 | Q | Q' |
| 0 | 1 | 0 | 1  |
| 1 | 0 | 1 | 0  |
| 1 | 1 | X | X  |

- RS flip-flop using NOR gates: The circuit diagram and the truth table are shown below.

![RS flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/rs_nor.png)

| S | R | Q | Q' |
|---|---|---|----|
| 0 | 0 | Q | Q' |
| 0 | 1 | 1 | 0  |
| 1 | 0 | 0 | 1  |
| 1 | 1 | X | X  |

- JK flip-flop using NAND gates: The circuit diagram and the truth table are shown below.

![JK flip-flop using NAND gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/jk_nand.png)

| J | K | Q(t) | Q(t+1) |
|---|---|------|--------|
| 0 | 0 | 0    | 0      |
| 0 | 0 | 1    | 1      |
| 0 | 1 | 0    | 0      |
| 0 | 1 | 1    | 0      |
| 1 | 0 | 0    | 1      |
| 1 | 0 | 1    | 1      |
| 1 | 1 | 0    | 1      |
| 1 | 1 | 1    | 0      |

- JK flip-flop using NOR gates: The circuit diagram and the truth table are shown below.

![JK flip-flop using NOR gates](https://de-iitr.vlabs.ac.in/exp/truth-tables-flip-flops/images/jk_nor.png)

| J | K | Q(t) | Q(t+1) |
|---|---|------|--------|
| 0 | 0 | 0