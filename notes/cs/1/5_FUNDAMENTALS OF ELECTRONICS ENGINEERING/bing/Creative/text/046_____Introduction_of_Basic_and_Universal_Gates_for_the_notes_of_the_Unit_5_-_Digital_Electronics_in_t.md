### Introduction of Basic and Universal Gates

- Logic gates are the fundamental building blocks of digital electronics. They perform basic logical operations on binary inputs and produce a single binary output.
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

![OR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/OR_ANSI_Labelled.svg/1200px-OR_ANSI_Labelled.svg.png)

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

![NOR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/NOR_ANSI_Labelled.svg/1200px-NOR_ANSI_Labelled.svg.png)

- The reason why NAND and NOR gates are universal is that they can be used to construct any other logic gate or Boolean function. For example, the following diagrams show how to implement AND, OR, and NOT gates using NAND and NOR gates:

![AND gate using NAND gates](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/AND_from_NAND.svg/1200px-AND_from_NAND.svg.png)

![OR gate using NOR gates](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/OR_from_NOR.svg/1200px-OR_from_NOR.svg.png)

![NOT gate using NAND gate](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/NOT_from_NAND.svg/1200px-NOT_from_NAND.svg.png)

![NOT gate using NOR gate](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/NOT_from_NOR.svg/1200px-NOT_from_NOR.svg.png)

- Digital logic circuits are integrated into a single IC (integrated circuit) to design several processors and controllers. The ICs have a specific number that identifies their type and function. For example, the IC 7400 is a quad 2-input NAND gate, the IC 7402 is a quad 2-input NOR gate, the IC 7408 is a quad 2-input AND gate, and the IC 7432 is a quad 2-input OR gate.