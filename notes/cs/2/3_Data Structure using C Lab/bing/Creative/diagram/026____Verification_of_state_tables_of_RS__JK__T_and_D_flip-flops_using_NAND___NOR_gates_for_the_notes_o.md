## Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- A flip-flop is an electronic circuit with two stable states that can be used to store binary data. The stored data can be changed by applying varying inputs.
- There are four basic types of flip-flops: RS, JK, T and D. Each type has a different characteristic table that shows the next state of the output (Q) depending on the current state (Q) and the inputs (S, R, J, K, T or D).
- RS flip-flop has two inputs: S (set) and R (reset). It can be implemented using NAND or NOR gates. The characteristic table of RS flip-flop is shown below:

| S | R | Q(next) | Q'(next) |
|---|---|---------|----------|
| 0 | 0 | Q       | Q'       |
| 0 | 1 | 0       | 1        |
| 1 | 0 | 1       | 0        |
| 1 | 1 | X       | X        |

- The circuit diagram of RS flip-flop using NAND gates is shown below:

![RS flip-flop using NAND gates](https://www.circuitstoday.com/wp-content/uploads/2010/08/S-R-Flip-Flop-using-NAND-Gate.png)

- The circuit diagram of RS flip-flop using NOR gates is shown below:

![RS flip-flop using NOR gates](https://www.circuitstoday.com/wp-content/uploads/2010/08/S-R-Flip-Flop-using-NOR-Gate.png)

- To verify the state table of RS flip-flop using NAND or NOR gates, we need to connect the inputs S and R to switches and the outputs Q and Q' to LEDs. Then we can observe the change in the LED states as we vary the switch positions .

- JK flip-flop has two inputs: J and K. It can be implemented using NAND or NOR gates. The characteristic table of JK flip-flop is shown below:

| J | K | Q(next) | Q'(next) |
|---|---|---------|----------|
| 0 | 0 | Q       | Q'       |
| 0 | 1 | 0       | 1        |
| 1 | 0 | 1       | 0        |
| 1 | 1 | Q'      | Q        |

- The circuit diagram of JK flip-flop using NAND gates is shown below:

![JK flip-flop using NAND gates](https://www.electricaltechnology.org/wp-content/uploads/2018/05/JK-Flip-Flop-Using-NAND-Gate.png)

- The circuit diagram of JK flip-flop using NOR gates is shown below:

![JK flip-flop using NOR gates](https://www.brighthubengineering.com/wp-content/uploads/2010/08/JK-Flip-Flop-using-NOR-Gates.jpg)

- To verify the state table of JK flip-flop using NAND or NOR gates, we need to connect the inputs J and K to switches and the outputs Q and Q' to LEDs. Then we can observe the change in the LED states as we vary the switch positions .

- T flip-flop has one input: T (toggle). It can be implemented using NAND or NOR gates. The characteristic table of T flip-flop is shown below:

| T | Q(next) | Q'(next) |
|---|---------|----------|
| 0 | Q       | Q'       |
| 1 | Q'      | Q        |

- The circuit diagram of T flip-flop using NAND gates is shown below:

![T flip-flop using NAND gates](https://www.electricaltechnology.org/wp-content/uploads/2018/05/T-Flip-Flop-Using-NAND-Gate.png)

- The circuit diagram of T flip-flop using NOR gates is shown below:

![T flip-flop using NOR gates](https://www.brighthubengineering.com/wp-content/uploads/2010/08/T-Flip-Flop-using-NOR-Gates.jpg)

- To verify the state table of T flip-flop using NAND or NOR gates, we need to connect the input T to a switch and the outputs Q and Q' to