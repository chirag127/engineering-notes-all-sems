## Implementing 4x1 and 8x1 MULTIPLEXERS for the notes of the Computer Organization Lab in the subject of Computer Organization

A multiplexer (MUX) is a combinational logic circuit that selects one output from multiple inputs. The selection of the output is determined by a set of selection lines. A 4x1 multiplexer has 4 input lines, 1 output line, and 2 selection lines. An 8x1 multiplexer has 8 input lines, 1 output line, and 3 selection lines.

### Implementing a 4x1 Multiplexer

A 4x1 multiplexer can be implemented using AND, OR, and NOT gates. The circuit diagram for a 4x1 multiplexer is shown below:

```
       +---+       +---+
I0 --- |   |       |   |
       | A |       | O |
I1 --- | N |       | R |
       | D |       |   |
I2 --- |   |       |   |
       |   |       |   |
I3 --- |   |       |   |
       +---+       +---+
         |           |
         +-----------+
         |
         Y
```

The truth table for a 4x1 multiplexer is shown below:

| S1 | S0 | Y  |
|----|----|----|
| 0  | 0  | I0 |
| 0  | 1  | I1 |
| 1  | 0  | I2 |
| 1  | 1  | I3 |

### Implementing an 8x1 Multiplexer

An 8x1 multiplexer can be implemented using two 4x1 multiplexers and one 2x1 multiplexer. The circuit diagram for an 8x1 multiplexer is shown below:

```
       +---+       +---+
I0 --- |   |       |   |
       | 4 |       | 2 |
I1 --- | x |       | x |
       | 1 |       | 1 |
I2 --- |   |       |   |
       | M |       | M |
I3 --- | U |       | U |
       | X |       | X |
       +---+       +---+
         |           |
         +-----------+
         |
         Y
```

The truth table for an 8x1 multiplexer is shown below:

| S2 | S1 | S0 | Y  |
|----|----|----|----|
| 0  | 0  | 0  | I0 |
| 0  | 0  | 1  | I1 |
| 0  | 1  | 0  | I2 |
| 0  | 1  | 1  | I3 |
| 1  | 0  | 0  | I4 |
| 1  | 0  | 1  | I5 |
| 1  | 1  | 0  | I6 |
| 1  | 1  | 1  | I7 |

In summary, a multiplexer is a combinational logic circuit that selects one output from multiple inputs. A 4x1 multiplexer can be implemented using AND, OR, and NOT gates, while an 8x1 multiplexer can be implemented using two 4x1 multiplexers and one 2x1 multiplexer. The selection of the output is determined by a set of selection lines. The truth table for a 4x1 multiplexer and an 8x1 multiplexer are shown above.