## Implementation of 1:4 demultiplexer using logic gates for the notes of the Discrete Structure & Logic Lab in the subject of Discrete Structure & Logic

A demultiplexer (DEMUX) is a digital circuit that takes a single input line and routes it to one of several output lines. A 1:4 demultiplexer has one input, two selection lines, and four outputs. The selection lines determine which output line the input will be routed to.

The implementation of a 1:4 demultiplexer using logic gates can be done using AND, NOT, and OR gates. The circuit diagram for the implementation is shown below:

```
       +---+       +---+
Input -|AND|-------|OR |---- Output 0
       +---+       +---+
         |           |
         |         +---+
         |---------|OR |---- Output 1
         |         +---+
       +---+       +---+
         |---------|AND|-------|OR |---- Output 2
       +---+       +---+       +---+
         |           |
         |         +---+
         |---------|OR |---- Output 3
                   +---+
```

The truth table for the 1:4 demultiplexer is shown below:

| Input | Selection | Output 0 | Output 1 | Output 2 | Output 3 |
|-------|-----------|----------|----------|----------|----------|
|   0   |    00     |    0     |    0     |    0     |    0     |
|   1   |    00     |    1     |    0     |    0     |    0     |
|   0   |    01     |    0     |    0     |    0     |    0     |
|   1   |    01     |    0     |    1     |    0     |    0     |
|   0   |    10     |    0     |    0     |    0     |    0     |
|   1   |    10     |    0     |    0     |    1     |    0     |
|   0   |    11     |    0     |    0     |    0     |    0     |
|   1   |    11     |    0     |    0     |    0     |    1     |

The above truth table shows how the input is routed to one of the four outputs based on the values of the selection lines. For example, when the input is 1 and the selection lines are 10, the input is routed to output 2.
