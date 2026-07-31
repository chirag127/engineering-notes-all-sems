### Logic gates

- A logic gate is an idealized or physical device that performs a Boolean function, a logical operation performed on one or more binary inputs that produces a single binary output.
- Logic gates can be made using various types of devices, such as pneumatic, mechanical, molecular, optical, or electronic.
- There are three basic types of logic gates: AND, OR, and NOT. Each type of gate has a truth table that shows the output for every possible combination of inputs.
- AND gate: The output is 1 only if both inputs are 1. Otherwise, the output is 0.
- OR gate: The output is 1 if at least one of the inputs is 1. Otherwise, the output is 0.
- NOT gate: The output is the opposite of the input. If the input is 1, the output is 0. If the input is 0, the output is 1.
- The symbols and truth tables for these gates are shown below:

| AND gate | OR gate | NOT gate |
|:--------:|:-------:|:--------:|
| ![AND gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/AND_ANSI_Labelled.svg/1200px-AND_ANSI_Labelled.svg.png) | ![OR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/OR_ANSI_Labelled.svg/1200px-OR_ANSI_Labelled.svg.png) | ![NOT gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/NOT_ANSI_Labelled.svg/1200px-NOT_ANSI_Labelled.svg.png) |
| |A|B|Output|
| |0|0|0|
| |0|1|0|
| |1|0|0|
| |1|1|1| | |A|B|Output|
| |0|0|0|
| |0|1|1|
| |1|0|1|
| |1|1|1| | |A|Output|
| |0|1|
| |1|0|

- There are also other types of logic gates that are derived from the basic ones, such as NAND, NOR, XOR, and XNOR. These gates can be constructed by combining the basic gates in various ways.
- NAND gate: The output is 0 only if both inputs are 1. Otherwise, the output is 1. It is equivalent to an AND gate followed by a NOT gate.
- NOR gate: The output is 0 if at least one of the inputs is 1. Otherwise, the output is 1. It is equivalent to an OR gate followed by a NOT gate.
- XOR gate: The output is 1 if the inputs are different. Otherwise, the output is 0. It is also known as the exclusive OR gate.
- XNOR gate: The output is 0 if the inputs are different. Otherwise, the output is 1. It is also known as the exclusive NOR gate.
- The symbols and truth tables for these gates are shown below:

| NAND gate | NOR gate | XOR gate | XNOR gate |
|:---------:|:--------:|:--------:|:---------:|
| ![NAND gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/NAND_ANSI_Labelled.svg/1200px-NAND_ANSI_Labelled.svg.png) | ![NOR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/NOR_ANSI_Labelled.svg/1200px-NOR_ANSI_Labelled.svg.png) | ![XOR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/XOR_ANSI_Labelled.svg/1200px-XOR_ANSI_Labelled.svg.png) | ![XNOR gate symbol](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/XNOR_ANSI_Labelled.svg/1200px-XNOR_ANSI_Labelled.svg.png) |
| |A|B|Output|
| |0|0|1|
| |0|1|1|
| |1|0|1|
| |1|1|0| | |A|B|Output|
| |0|0|1|
| |0|1|0|
| |1|0|0|
| |1|1|0| | |A|