## Implementation of 1:4 demultiplexer using logic gates

A demultiplexer is a combinational logic circuit that takes a single input and routes it to one of several outputs. A 1:4 demultiplexer has one input, four outputs, and two control lines. The control lines determine which output the input will be routed to.

The implementation of a 1:4 demultiplexer using logic gates can be done using AND, NOT, and OR gates. The circuit diagram for the implementation is shown below:

```
       +----+----+
       | A0 | A1 |
       +----+----+
          |    |
          v    v
       +----+----+
       | NOT| NOT|
       +----+----+
          |    |
          v    v
       +----+----+
       | AND| AND|
       +----+----+
          |    |
          v    v
       +----+----+
       | OR | OR |
       +----+----+
          |    |
          v    v
       +----+----+
       | Y0 | Y1 |
       +----+----+
```

The input is connected to all four AND gates. The control lines A0 and A1 are connected to the AND gates as shown in the diagram. The NOT gates are used to invert the control lines. The outputs of the AND gates are connected to the OR gates, which produce the final outputs Y0 and Y1.

The truth table for the 1:4 demultiplexer is shown below:

| A1 | A0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|
| 0  | 0  | 1  | 0  | 0  | 0  |
| 0  | 1  | 0  | 1  | 0  | 0  |
| 1  | 0  | 0  | 0  | 1  | 0  |
| 1  | 1  | 0  | 0  | 0  | 1  |

This implementation of a 1:4 demultiplexer using logic gates can be used in the Discrete Structure & Logic Lab for the subject of Discrete Structure & Logic. It provides a practical example of how combinational logic circuits can be used to route a single input to one of several outputs based on the values of the control lines.