## Implementing 4x1 and 8x1 MULTIPLEXERS for the notes of the Computer Organization Lab in the subject of Computer Organization

- A multiplexer or mux is a combinational circuit that selects one of several input signals and forwards it to a single output line.
- A 4x1 multiplexer has four data inputs, two selection lines and one output. The output is determined by the combination of the selection lines.
- A 8x1 multiplexer has eight data inputs, three selection lines and one output. The output is determined by the combination of the selection lines.
- A multiplexer can be implemented using logic gates, such as AND, OR and NOT gates.
- A multiplexer can also be implemented using Verilog, a hardware description language that can describe the structure and behavior of digital circuits.
- A multiplexer can be used for various applications, such as data routing, data compression, encryption, signal processing, etc.

### 4x1 Multiplexer

- The block diagram of a 4x1 multiplexer is shown below:

```
    I0  I1  I2  I3
     |   |   |   |
     |   |   |   |
     +---+---+---+
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
         |   |
         |   |
         |   |
         |   |
         |   |
         |   |
         |   |
         |   |
         |   |
         +---+
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           Y
```

- The truth table of a 4x1 multiplexer is shown below:

| S1 | S0 | Y  |
|----|----|----|
| 0  | 0  | I0 |
| 0  | 1  | I1 |
| 1  | 0  | I2 |
| 1  | 1  | I3 |

- The logical expression of the output Y is:

```
Y = (I0.S1'.S0') + (I1.S1'.S0) + (I2.S1.S0') + (I3.S1.S0)
```

- The circuit diagram of a 4x1 multiplexer using logic gates is shown below:

```
    I0  I1  I2  I3
     |   |   |   |
     |   |   |   |
     +---+---+---+
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
         |   |
         |   |
         |   |
         |   |
         +---+
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           Y
     +---+---+---+
     |   |   |   |
     |   |   |   |
     +---+---+---+
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
         +---+
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           |
           +---+
               |
               |
               |
               |
               |