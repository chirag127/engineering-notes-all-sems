# Introduction of Basic and Universal Gates

- Logic gates are the fundamental building blocks of digital electronics. They perform basic logical operations on binary inputs and produce binary outputs.
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

- The reason why NAND and NOR gates are universal is that they can be combined to construct any other logic gate or Boolean function. For example, the following diagrams show how to implement AND, OR, and NOT gates using NAND and NOR gates:

![AND gate using NAND gates](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/AND_from_NAND.svg/1200px-AND_from_NAND.svg.png)

![OR gate using NOR gates](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/OR_from_NOR.svg/1200px-OR_from_NOR.svg.png)

![NOT gate using NAND gate](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/NOT_from_NAND.svg/1200px-NOT_from_NAND.svg.png)

![NOT gate using NOR gate](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/NOT_from_NOR.svg/1200px-NOT_from_NOR.svg.png)

- Digital logic circuits are integrated into a single IC (integrated circuit) to design several processors and controllers. The ICs have a specific number that identifies their type and function. For example, the IC 7400 is a quad 2-input NAND gate, which means it has four NAND gates with two inputs each. The IC 7402 is a quad 2-input NOR gate, which means it has four NOR gates with two inputs each. The following diagrams show the pin configurations of these ICs:

![IC 7400 pin configuration](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/7400_pinout.svg/1200px-7400_pinout.svg.png)

![IC 7402 pin configuration](https://upload.wikimedia.org/wikipedia/commons/thumb/5