## Implementing 4x1 and 8x1 MULTIPLEXERS for the notes of the Computer Organization Lab in the subject of Computer Organization

Multiplexers are important components in digital circuits that allow the selection of one out of multiple input signals based on a control signal. In this lab, we will focus on implementing 4x1 and 8x1 multiplexers using logic gates.

### 4x1 Multiplexer

A 4x1 multiplexer has four input signals and one output signal. The output signal is selected based on a two-bit control signal. The truth table for a 4x1 multiplexer is as follows:

| S1 | S0 | Output |
|----|----|--------|
| 0  | 0  | I0     |
| 0  | 1  | I1     |
| 1  | 0  | I2     |
| 1  | 1  | I3     |

To implement a 4x1 multiplexer, we can use four AND gates, two OR gates, and two NOT gates. The circuit diagram is shown below:

![4x1 Multiplexer Circuit Diagram](multiplexer-4x1.png)

### 8x1 Multiplexer

An 8x1 multiplexer has eight input signals and one output signal. The output signal is selected based on a three-bit control signal. The truth table for an 8x1 multiplexer is as follows:

| S2 | S1 | S0 | Output |
|----|----|----|--------|
| 0  | 0  | 0  | I0     |
| 0  | 0  | 1  | I1     |
| 0  | 1  | 0  | I2     |
| 0  | 1  | 1  | I3     |
| 1  | 0  | 0  | I4     |
| 1  | 0  | 1  | I5     |
| 1  | 1  | 0  | I6     |
| 1  | 1  | 1  | I7     |

To implement an 8x1 multiplexer, we can use eight AND gates, three OR gates, and three NOT gates. The circuit diagram is shown below:

![8x1 Multiplexer Circuit Diagram](multiplexer-8x1.png)

In conclusion, implementing 4x1 and 8x1 multiplexers using logic gates is an important concept in digital circuits. By understanding the truth tables and circuit diagrams, we can effectively select one out of multiple input signals based on a control signal.