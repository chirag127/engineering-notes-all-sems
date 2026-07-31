# Introduction of Basic and Universal Gates

- Logic gates are the fundamental building blocks of digital electronics. They perform basic logical operations on binary inputs and produce a binary output.
- There are three basic logic gates: AND, OR, and NOT. They have the following truth tables and symbols:

| A | B | A AND B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 1       |

![AND gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/AND_ANSI_Labelled.svg/1200px-AND_ANSI_Labelled.svg.png)

| A | B | A OR B |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

![OR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/OR_ANSI_Labelled.svg/1200px-OR_ANSI_Labelled.svg.png)

| A | NOT A |
|---|-------|
| 0 | 1     |
| 1 | 0     |

![NOT gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/NOT_ANSI_Labelled.svg/1200px-NOT_ANSI_Labelled.svg.png)

- Universal gates are logic gates that can be used to implement any other logic gate or Boolean function. They are NAND and NOR gates. They have the following truth tables and symbols:

| A | B | A NAND B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 1        |
| 1 | 0 | 1        |
| 1 | 1 | 0        |

![NAND gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/NAND_ANSI_Labelled.svg/1200px-NAND_ANSI_Labelled.svg.png)

| A | B | A NOR B |
|---|---|---------|
| 0 | 0 | 1       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 0       |

![NOR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/NOR_ANSI_Labelled.svg/1200px-NOR_ANSI_Labelled.svg.png)

- The reason why NAND and NOR gates are universal is that they can be combined to produce any other logic gate or Boolean function. For example, the following circuits show how to implement AND, OR, and NOT gates using NAND and NOR gates:

![AND gate using NAND gates](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/AND_from_NAND.svg/1200px-AND_from_NAND.svg.png)

![OR gate using NOR gates](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/OR_from_NOR.svg/1200px-OR_from_NOR.svg.png)

![NOT gate using NAND or NOR gate](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/NOT_from_NAND.svg/1200px-NOT_from_NAND.svg.png)

- Digital logic circuits are integrated into a single IC (integrated circuit) to design several processors and controllers. The IC number of a logic gate indicates its type, number of inputs, and output configuration. For example, the IC number 7400 indicates a quad 2-input NAND gate, which means it has four NAND gates with two inputs each. The IC number 7402 indicates a quad 2-input NOR gate, which means it has four NOR gates with two inputs each. The IC number 7404 indicates a hex inverter, which means it has six NOT gates with one input each. The following table shows some common IC numbers and their corresponding logic gates:

| IC Number | Logic Gate | Number of Inputs | Number of Outputs |
|-----------|------------|------------------|-------------------|
| 7400      | NAND       | 2                | 1                 |
| 7402      | NOR        | 2                | 1                 |
| 7404      | NOT        | 1                | 1                 |
| 7408      |