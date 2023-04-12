## Implementing 4x1 and 8x1 MULTIPLEXERS

- A multiplexer (MUX) is a digital device that selects one of the N inputs and directs it to the output.
- A 4x1 MUX has 4 data inputs, 2 selection lines and one output. A 8x1 MUX has 8 data inputs, 3 selection lines and one output.
- A 8x1 MUX can be implemented using two 4x1 MUXes and one 2x1 MUX as follows  :

```
    +---+     +---+     +---+
    | A |-----| I0|     | I0|-----+
    +---+     |   |     |   |     |
    +---+     | I1|     | I1|-----+
    | B |-----|   |     |   |     |
    +---+     | I2|     | I2|-----+
    +---+     |   |     |   |     |
    | C |-----| I3|     | I3|-----+
    +---+     |   |     |   |     |
    +---+     | S0|     | S0|-----+
    | S0|-----|   |     |   |     |
    +---+     | S1|     | S1|-----+
    +---+     |   |     |   |     |
    | S1|-----|   |     |   |     |
    +---+     |   |     |   |     |
              |   |     |   |     |
              | O |     | O |     |
              +---+     +---+     |
                |         |       |
                +----+----+       |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     |            |
                     +------------+
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

```
