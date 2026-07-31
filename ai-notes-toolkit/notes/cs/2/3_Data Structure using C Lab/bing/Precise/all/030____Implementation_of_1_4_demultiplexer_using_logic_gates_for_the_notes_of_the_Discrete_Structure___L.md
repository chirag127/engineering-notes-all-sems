## Implementation of 1:4 Demultiplexer Using Logic Gates

A demultiplexer is a combinational logic circuit that takes a single input and distributes it over several outputs. A 1:4 demultiplexer has one input, two selection lines, and four outputs. The input is distributed to one of the four outputs based on the binary value of the selection lines.

The implementation of a 1:4 demultiplexer using logic gates can be done using AND, NOT, and OR gates. The circuit diagram for the implementation is shown below:

```
       +---+       +---+
Input -|AND|       |AND|--- Output 0
       +---+       +---+
         |           |
         |       +---+
         |       |NOT|
         |       +---+
         |         |
       +---+       +---+
S1 ----|AND|       |AND|--- Output 1
       +---+       +---+
         |           |
         |       +---+
         |       |NOT|
         |       +---+
         |         |
       +---+       +---+
S0 ----|AND|       |AND|--- Output 2
       +---+       +---+
         |           |
         |       +---+
         |       |NOT|
         |       +---+
         |         |
       +---+       +---+
Input -|AND|       |AND|--- Output 3
       +---+       +---+
```

The truth table for the 1:4 demultiplexer is shown below:

| Input | S1 | S0 | Output 0 | Output 1 | Output 2 | Output 3 |
|-------|----|----|----------|----------|----------|----------|
|   0   | 0  | 0  |     0    |     0    |     0    |     0    |
|   0   | 0  | 1  |     0    |     0    |     0    |     0    |
|   0   | 1  | 0  |     0    |     0    |     0    |     0    |
|   0   | 1  | 1  |     0    |     0    |     0    |     0    |
|   1   | 0  | 0  |     1    |     0    |     0    |     0    |
|   1   | 0  | 1  |     0    |     1    |     0    |     0    |
|   1   | 1  | 0  |     0    |     0    |     1    |     0    |
|   1   | 1  | 1  |     0    |     0    |     0    |     1    |

This is how a 1:4 demultiplexer can be implemented using logic gates. It is an important concept in the subject of Discrete Structure & Logic and can be useful for the Discrete Structure & Logic Lab.