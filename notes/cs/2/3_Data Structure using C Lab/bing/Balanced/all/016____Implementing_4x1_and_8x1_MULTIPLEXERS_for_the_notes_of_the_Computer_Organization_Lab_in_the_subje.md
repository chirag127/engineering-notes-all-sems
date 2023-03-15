## Implementing 4x1 and 8x1 MULTIPLEXERS

- A multiplexer (MUX) is a digital device that selects one of the several input signals and forwards it to the output.
- A multiplexer has n data inputs, m selection lines, and one output, where 2^m = n.
- A 4x1 multiplexer has 4 data inputs, 2 selection lines, and one output.
- A 8x1 multiplexer has 8 data inputs, 3 selection lines, and one output.
- To implement a 8x1 multiplexer using lower order multiplexers, we can use two 4x1 multiplexers and one 2x1 multiplexer.
- The 2x1 multiplexer has 2 data inputs, 1 selection line, and one output.
- The 8 data inputs of the 8x1 multiplexer are divided into two groups of 4 inputs each, and connected to the data inputs of the two 4x1 multiplexers.
- The output of the two 4x1 multiplexers are connected to the data inputs of the 2x1 multiplexer.
- The selection lines of the 8x1 multiplexer are split into two parts: the most significant bit (MSB) and the least significant bits (LSBs).
- The MSB of the selection lines is connected to the selection line of the 2x1 multiplexer, and the LSBs of the selection lines are connected to the selection lines of the two 4x1 multiplexers.
- The output of the 2x1 multiplexer is the output of the 8x1 multiplexer.
- The following diagram shows the implementation of the 8x1 multiplexer using 4x1 and 2x1 multiplexers:

```
    +-----+       +-----+
    | 4x1 |       | 4x1 |
    | MUX |       | MUX |
    +-----+       +-----+
       |             |
       +-----+ +-----+
             | |
             | +-----------------+
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             |                   |
             +-----------------+ |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |
                               | |