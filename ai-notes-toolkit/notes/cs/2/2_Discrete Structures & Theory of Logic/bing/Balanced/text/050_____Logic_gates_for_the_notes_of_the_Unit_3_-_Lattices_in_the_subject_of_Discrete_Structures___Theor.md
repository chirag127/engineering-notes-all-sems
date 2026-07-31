### Logic gates for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- Logic gates are the basic building blocks from which most of the digital systems are built up.
- Logic gates perform logical operations on one or more binary inputs and produce a single binary output.
- The numbers 0 and 1 represent the two possible states of a logic circuit. The two states can also be referred to as 'ON and OFF' or 'HIGH and LOW' or 'TRUE and FALSE'.
- The basic logic gates are 'OR', 'AND' and 'NOT' gates. These three gates can be used to implement any other logic function.
- The OR gate produces a 1 output if at least one of its inputs is 1, otherwise it produces a 0 output.
- The AND gate produces a 1 output if both of its inputs are 1, otherwise it produces a 0 output.
- The NOT gate produces a 1 output if its input is 0, and a 0 output if its input is 1. It is also called an inverter.
- The truth table of a logic gate shows all the possible combinations of inputs and outputs for that gate.
- The symbol and truth table for each basic logic gate are shown below:

| OR gate | AND gate | NOT gate |
|:-------:|:--------:|:--------:|
| ![OR gate symbol](https://www.brainkart.com/media/2016/01/07/1.jpg) | ![AND gate symbol](https://www.brainkart.com/media/2016/01/07/2.jpg) | ![NOT gate symbol](https://www.brainkart.com/media/2016/01/07/3.jpg) |
| | A | B | A OR B |
| | 0 | 0 | 0 |
| | 0 | 1 | 1 |
| | 1 | 0 | 1 |
| | 1 | 1 | 1 | | | A | B | A AND B |
| | 0 | 0 | 0 |
| | 0 | 1 | 0 |
| | 1 | 0 | 0 |
| | 1 | 1 | 1 | | | A | NOT A |
| | 0 | 1 |
| | 1 | 0 |

- Other logic gates that can be derived from the basic ones are 'NOR', 'NAND', 'XOR' and 'XNOR' gates.
- The NOR gate produces a 1 output if both of its inputs are 0, otherwise it produces a 0 output. It is equivalent to an OR gate followed by a NOT gate.
- The NAND gate produces a 0 output if both of its inputs are 1, otherwise it produces a 1 output. It is equivalent to an AND gate followed by a NOT gate.
- The XOR gate produces a 1 output if exactly one of its inputs is 1, otherwise it produces a 0 output. It is also called an exclusive OR gate.
- The XNOR gate produces a 0 output if exactly one of its inputs is 1, otherwise it produces a 1 output. It is also called an exclusive NOR gate.
- The symbol and truth table for each derived logic gate are shown below:

| NOR gate | NAND gate | XOR gate | XNOR gate |
|:--------:|:---------:|:--------:|:---------:|
| ![NOR gate symbol](https://www.brainkart.com/media/2016/01/07/4.jpg) | ![NAND gate symbol](https://www.brainkart.com/media/2016/01/07/5.jpg) | ![XOR gate symbol](https://www.brainkart.com/media/2016/01/07/6.jpg) | ![XNOR gate symbol](https://www.brainkart.com/media/2016/01/07/7.jpg) |
| | A | B | A NOR B |
| | 0 | 0 | 1 |
| | 0 | 1 | 0 |
| | 1 | 0 | 0 |
| | 1 | 1 | 0 | | | A | B | A NAND B |
| |