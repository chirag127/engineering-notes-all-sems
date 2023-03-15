# Implementation of 1:4 demultiplexer using logic gates

- A demultiplexer is a digital circuit that takes one input signal and distributes it to one of several output signals based on some selection criteria.
- A 1:4 demultiplexer has one input signal (D), two selection lines (S1 and S0) and four output signals (Y0 to Y3).
- The input signal is connected to one of the four output signals depending on the binary value of the selection lines.
- The truth table for a 1:4 demultiplexer is shown below:

| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|
| 0  | 0  | D  | 0  | 0  | 0  |
| 0  | 1  | 0  | D  | 0  | 0  |
| 1  | 0  | 0  | 0  | D  | 0  |
| 1  | 1  | 0  | 0  | 0  | D  |

- A 1:4 demultiplexer can be implemented using logic gates such as AND, NOT and OR gates.
- One possible implementation is shown below:

![1:4 demultiplexer using logic gates](https://circuitverse.org/users/59463/projects/1-4-demultiplexer-using-logic-gates/image)

- In this implementation, the input signal D is ANDed with the complement of S1 and S0 to get Y0, with the complement of S1 and S0 to get Y1, with S1 and the complement of S0 to get Y2, and with S1 and S0 to get Y3.
- The output signals are ORed together to get the output of the demultiplexer.
- The logic equations for the output signals are:

Y0 = D.(S1'.S0')
Y1 = D.(S1'.S0)
Y2 = D.(S1.S0')
Y3 = D.(S1.S0)

- Where ' denotes the complement of a signal.
- A 1:4 demultiplexer can be used for various applications such as data distribution, memory addressing, control signal generation, etc.