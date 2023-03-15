# Digital Circuits and Boolean Algebra

- Digital circuits are electronic devices that process information in binary form, using only two voltage levels to represent 0 and 1.
- Boolean algebra is a branch of mathematics that deals with binary variables and logical operations, such as AND, OR, and NOT.
- Boolean algebra can be used to model the behavior of digital circuits, and to simplify and analyze them.
- The basic elements of digital circuits are logic gates, which perform Boolean operations on one or more inputs and produce one output.
- The most common logic gates are AND, OR, and NOT gates, which have the following truth tables:

| A | B | A AND B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 1       |

| A | B | A OR B |
|---|---|--------|
| 0 | 0 | 0      |
| 0 | 1 | 1      |
| 1 | 0 | 1      |
| 1 | 1 | 1      |

| A | NOT A |
|---|-------|
| 0 | 1     |
| 1 | 0     |

- Other logic gates, such as NAND, NOR, XOR, and XNOR, can be derived from the basic gates by combining them in different ways.
- The symbols and truth tables for these gates are:

| A | B | A NAND B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 1        |
| 1 | 0 | 1        |
| 1 | 1 | 0        |

| A | B | A NOR B |
|---|---|---------|
| 0 | 0 | 1       |
| 0 | 1 | 0       |
| 1 | 0 | 0       |
| 1 | 1 | 0       |

| A | B | A XOR B |
|---|---|---------|
| 0 | 0 | 0       |
| 0 | 1 | 1       |
| 1 | 0 | 1       |
| 1 | 1 | 0       |

| A | B | A XNOR B |
|---|---|----------|
| 0 | 0 | 1        |
| 0 | 1 | 0        |
| 1 | 0 | 0        |
| 1 | 1 | 1        |

- A logic expression is a combination of variables and operators that represents the output of a logic circuit.
- For example, the expression A AND B OR NOT C represents the output of the following circuit:

![A AND B OR NOT C](https://www.allaboutcircuits.com/uploads/articles/boolean-algebra-logic-circuit-example.jpg)

- A logic expression can be simplified using the rules of Boolean algebra, such as:

| Rule | Name | Example |
|------|------|---------|
| A + 0 = A | Identity | A OR 0 = A |
| A + 1 = 1 | Annihilation | A OR 1 = 1 |
| A + A = A | Idempotence | A OR A = A |
| A + B = B + A | Commutativity | A OR B = B OR A |
| (A + B) + C = A + (B + C) | Associativity | (A OR B) OR C = A OR (B OR C) |
| A + (B * C) = (A + B) * (A + C) | Distributivity | A OR (B AND C) = (A OR B) AND (A OR C) |
| A + A * B = A | Absorption | A OR (A AND B) = A |
| A + A' = 1 | Complement | A OR NOT A = 1 |
| (A + B)' = A' * B' | De Morgan's | NOT (A OR B) = NOT A AND NOT B |
| A * 0 = 0 | Identity | A AND 0 = 0 |
| A * 1 = A | Annihilation | A AND 1 = A |
| A * A = A | Idempotence | A AND A = A |
| A * B =