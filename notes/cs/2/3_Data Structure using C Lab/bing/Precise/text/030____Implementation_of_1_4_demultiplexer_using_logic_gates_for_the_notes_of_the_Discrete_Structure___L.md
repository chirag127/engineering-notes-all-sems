## Implementation of 1:4 demultiplexer using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A demultiplexer (DEMUX) is a digital circuit that takes a single input and routes it to one of several outputs. A 1:4 demultiplexer has one input, two selection lines, and four outputs. The selection lines determine which output the input will be routed to.

The implementation of a 1:4 demultiplexer using logic gates can be done using AND, NOT, and OR gates. The circuit diagram for a 1:4 demultiplexer using these gates is shown below:

```
       +---+       +---+
Input -|AND|-------|OR |---- Output 0
       +---+       +---+
         |           |
         |         +---+
         |---------|OR |---- Output 1
         |         +---+
         |           |
       +---+       +---+
       |AND|-------|OR |---- Output 2
       +---+       +---+
         |           |
         |         +---+
         |---------|OR |---- Output 3
                   +---+
```

The truth table for a 1:4 demultiplexer is shown below:

| Input | Selection | Output 0 | Output 1 | Output 2 | Output 3 |
|-------|-----------|----------|----------|----------|----------|
|   0   |     00    |     0    |     0    |     0    |     0    |
|   0   |     01    |     0    |     0    |     0    |     0    |
|   0   |     10    |     0    |     0    |     0    |     0    |
|   0   |     11    |     0    |     0    |     0    |     0    |
|   1   |     00    |     1    |     0    |     0    |     0    |
|   1   |     01    |     0    |     1    |     0    |     0    |
|   1   |     10    |     0    |     0    |     1    |     0    |
|   1   |     11    |     0    |     0    |     0    |     1    |

The selection lines determine which output will be active. For example, when the selection lines are 00, output 0 is active, and when the selection lines are 11, output 3 is active. The input is then routed to the active output.

This is a brief overview of the implementation of a 1:4 demultiplexer using logic gates. It is important to understand the circuit diagram and truth table to fully grasp the concept.