## Implementation of 1:4 demultiplexer using logic gates

- A demultiplexer is a device that takes a single input and distributes it to one of several outputs depending on the values of some control signals.
- A 1:4 demultiplexer has one input, four outputs, and two control signals.
- The input is denoted by D, the outputs are denoted by Y0, Y1, Y2, and Y3, and the control signals are denoted by S0 and S1.
- The truth table of a 1:4 demultiplexer is shown below:

| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|
| 0  | 0  | D  | 0  | 0  | 0  |
| 0  | 1  | 0  | D  | 0  | 0  |
| 1  | 0  | 0  | 0  | D  | 0  |
| 1  | 1  | 0  | 0  | 0  | D  |

- The output equations of a 1:4 demultiplexer are given by:

  - Y0 = D.S0'.S1'
  - Y1 = D.S0.S1'
  - Y2 = D.S0'.S1
  - Y3 = D.S0.S1

- Where S0' and S1' are the complements of S0 and S1 respectively.
- A 1:4 demultiplexer can be implemented using logic gates as shown in the following circuit diagram:

```
    D
    |
    |     S0
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |   +---+
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    |   |   |
    +---+   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   |
        |   +---+
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        |       |
        +-------+
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                |
                +-----------------+
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                +-----------------+
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |                 |
                |