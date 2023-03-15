### Introduction of Basic and Universal Gates

- Logic gates are the fundamental building blocks of digital electronics. They perform basic logical operations on binary inputs and produce a binary output.
- There are three basic logic gates: AND, OR, and NOT. They have the following truth tables and symbols:

| A | B | A AND B |
|---|---|---------|
| 0 | 0 |    0    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    1    |

![AND gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/AND_ANSI_Labelled.svg/1200px-AND_ANSI_Labelled.svg.png)

| A | B | A OR B |
|---|---|--------|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   1    |

![OR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/OR_ANSI_Labelled.svg/1200px-OR_ANSI_Labelled.svg.png)

| A | NOT A |
|---|-------|
| 0 |   1   |
| 1 |   0   |

![NOT gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/NOT_ANSI_Labelled.svg/1200px-NOT_ANSI_Labelled.svg.png)

- Universal gates are logic gates that can be used to implement any other logic gate or Boolean function. They are NAND and NOR gates. They have the following truth tables and symbols:

| A | B | A NAND B |
|---|---|----------|
| 0 | 0 |    1     |
| 0 | 1 |    1     |
| 1 | 0 |    1     |
| 1 | 1 |    0     |

![NAND gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/NAND_ANSI_Labelled.svg/1200px-NAND_ANSI_Labelled.svg.png)

| A | B | A NOR B |
|---|---|---------|
| 0 | 0 |    1    |
| 0 | 1 |    0    |
| 1 | 0 |    0    |
| 1 | 1 |    0    |

![NOR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/NOR_ANSI_Labelled.svg/1200px-NOR_ANSI_Labelled.svg.png)

- The reason why NAND and NOR gates are universal is that they can be combined to produce any other logic gate or Boolean function. For example, the following diagrams show how to construct an AND gate, an OR gate, and a NOT gate using only NAND gates:

![AND gate using NAND gates](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/NAND_from_NAND.svg/1200px-NAND_from_NAND.svg.png)

![OR gate using NAND gates](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/OR_from_NAND.svg/1200px-OR_from_NAND.svg.png)

![NOT gate using NAND gate](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/NOT_from_NAND.svg/1200px-NOT_from_NAND.svg.png)

- Similarly, the following diagrams show how to construct an AND gate, an OR gate, and a NOT gate using only NOR gates:

![AND gate using NOR gates](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/AND_from_NOR.svg/1200px-AND_from_NOR.svg.png)

![OR gate using NOR gates](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/OR_from_NOR.svg/1200px-OR_from_NOR.svg.png)

![NOT gate using NOR gate](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/NOT_from_NOR.svg/1200px-NOT_from_NOR.svg.png)

- Digital logic circuits are integrated into a single IC to design several processors and controllers. The IC number of a logic gate indicates the type and number of gates in the IC. For example, the IC number 7400 indicates a quad 2-input NAND gate, which