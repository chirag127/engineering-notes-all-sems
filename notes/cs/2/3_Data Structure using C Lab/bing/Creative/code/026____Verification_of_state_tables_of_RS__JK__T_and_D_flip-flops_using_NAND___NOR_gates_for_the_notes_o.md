# Verification of state tables of RS, JK, T and D flip-flops using NAND & NOR gates

- A flip-flop is an electronic circuit with two stable states that can be used to store binary data. The stored data can be changed by applying varying inputs.
- There are four basic types of flip-flops: RS, JK, T and D. Each type has a different characteristic table that shows the next state of the flip-flop depending on the current state and the inputs.
- RS flip-flop has two inputs: S (set) and R (reset). It can be implemented using NAND or NOR gates. The characteristic table of RS flip-flop is shown below:

| S | R | Q(next) | Q'(next) |
|---|---|---------|----------|
| 0 | 0 | Q       | Q'       |
| 0 | 1 | 0       | 1        |
| 1 | 0 | 1       | 0        |
| 1 | 1 | X       | X        |

- The last row of the table indicates an invalid or indeterminate state, where both outputs are undefined.
- The circuit diagram of RS flip-flop using NAND gates is shown below:

![RS flip-flop using NAND gates](https://www.circuitstoday.com/wp-content/uploads/2010/03/S-R-Flip-Flop-using-NAND-Gate.jpg)

- The circuit diagram of RS flip-flop using NOR gates is shown below:

![RS flip-flop using NOR gates](https://www.circuitstoday.com/wp-content/uploads/2010/03/S-R-Flip-Flop-using-NOR-Gate.jpg)

- JK flip-flop is a modified version of RS flip-flop. It has two inputs: J (set) and K (reset). It can also be implemented using NAND or NOR gates. The characteristic table of JK flip-flop is shown below:

| J | K | Q(next) | Q'(next) |
|---|---|---------|----------|
| 0 | 0 | Q       | Q'       |
| 0 | 1 | 0       | 1        |
| 1 | 0 | 1       | 0        |
| 1 | 1 | Q'      | Q        |

- The last row of the table indicates a toggle state, where the outputs switch to the opposite values.
- The circuit diagram of JK flip-flop using NAND gates is shown below:

![JK flip-flop using NAND gates](https://www.electricaltechnology.org/wp-content/uploads/2018/05/JK-Flip-Flop-using-NAND-Gate.png)

- The circuit diagram of JK flip-flop using NOR gates is shown below:

![JK flip-flop using NOR gates](https://www.electricaltechnology.org/wp-content/uploads/2018/05/JK-Flip-Flop-using-NOR-Gate.png)

- T flip-flop is a special case of JK flip-flop, where the inputs J and K are tied together. It has one input: T (toggle). It can also be implemented using NAND or NOR gates. The characteristic table of T flip-flop is shown below:

| T | Q(next) | Q'(next) |
|---|---------|----------|
| 0 | Q       | Q'       |
| 1 | Q'      | Q        |

- The input T determines whether the flip-flop will toggle or not. If T is 0, the flip-flop will hold its state. If T is 1, the flip-flop will switch its state.
- The circuit diagram of T flip-flop using NAND gates is shown below:

![T flip-flop using NAND gates](https://www.brighthubengineering.com/wp-content/uploads/2010/03/T-Flip-Flop-using-NAND-Gate.jpg)

- The circuit diagram of T flip-flop using NOR gates is shown below:

![T flip-flop using NOR gates](https://www.brighthubengineering.com/wp-content/uploads/2010/03/T-Flip-Flop-using-NOR-Gate.jpg)

- D flip-flop is a simple type of flip-flop that has one input: D (data). It can also be implemented using NAND or NOR gates. The characteristic table of D flip-flop is shown below[^