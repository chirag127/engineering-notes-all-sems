# Logic gates for the notes of the Unit 3 - Lattices in the subject of Discrete Structures & Theory of Logic

- Logic gates are the basic building blocks of digital systems that perform logical operations on binary inputs and outputs.
- The three basic logic gates are OR, AND and NOT, which correspond to the logical connectives ∨, ∧ and ¬ in propositional logic.
- The truth table of a logic gate shows the output value for every possible combination of input values.
- The following table summarizes the truth tables of the three basic logic gates:

| Input A | Input B | Output A OR B | Output A AND B | Output NOT A |
|---------|---------|---------------|----------------|--------------|
| 0       | 0       | 0             | 0              | 1            |
| 0       | 1       | 1             | 0              | 1            |
| 1       | 0       | 1             | 0              | 0            |
| 1       | 1       | 1             | 1              | 0            |

- Logic gates can be implemented using discrete components such as transistors, diodes, resistors, etc. The following diagrams show the schematic symbols and circuit diagrams of the three basic logic gates using transistors:

![OR gate](https://www.brainkart.com/media/attachment/2016/01/22/3001_OR%20gate.jpg)

![AND gate](https://www.brainkart.com/media/attachment/2016/01/22/3001_AND%20gate.jpg)

![NOT gate](https://www.brainkart.com/media/attachment/2016/01/22/3001_NOT%20gate.jpg)

- Logic gates can be combined to form more complex logic circuits that perform various functions such as arithmetic, memory, control, etc. The following diagram shows an example of a logic circuit that implements the XOR (exclusive OR) operation using OR, AND and NOT gates:

![XOR gate](https://math.libretexts.org/@api/deki/files/1287/XOR.png)

- The truth table of the XOR gate is as follows:

| Input A | Input B | Output A XOR B |
|---------|---------|----------------|
| 0       | 0       | 0              |
| 0       | 1       | 1              |
| 1       | 0       | 1              |
| 1       | 1       | 0              |

- The XOR gate can be expressed using the following Boolean expression: A XOR B = (A OR B) AND (NOT (A AND B))
- Logic circuits can be analyzed and simplified using the rules and laws of Boolean algebra, such as commutativity, associativity, distributivity, identity, complement, De Morgan's laws, etc.
- Logic circuits can also be represented using diagrams called logic diagrams, which use rectangular boxes to denote logic gates and lines to denote inputs and outputs. The following diagram shows the logic diagram of the XOR gate:

![XOR logic diagram](https://math.libretexts.org/@api/deki/files/1288/XOR2.png)

- Logic diagrams can be converted to truth tables by assigning values to the inputs and tracing the outputs through the logic gates. Conversely, truth tables can be converted to logic diagrams by finding the Boolean expression that corresponds to the output and drawing the logic gates that implement the expression.