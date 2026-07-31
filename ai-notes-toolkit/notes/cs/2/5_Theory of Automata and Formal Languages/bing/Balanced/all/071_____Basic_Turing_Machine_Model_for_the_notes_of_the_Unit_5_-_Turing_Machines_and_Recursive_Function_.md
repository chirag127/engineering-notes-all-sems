# Basic Turing Machine Model

A Turing machine is a mathematical model of computation that can perform any algorithmic task. It was proposed by Alan Turing in 1936 as a way of studying the limits of computability .

A basic Turing machine consists of the following components :

- An infinite tape divided into cells, each cell containing a symbol from a finite alphabet. The tape serves as the input and output of the machine, as well as its memory.
- A tape head that can read and write symbols on the tape, and move one cell to the left or right at a time.
- A finite set of states, one of which is designated as the initial state, and some of which are designated as accepting or rejecting states. The state of the machine determines its behavior at each step.
- A transition function that specifies, for each state and tape symbol, what the machine should do next: write a new symbol on the tape, move the head left or right, and change to a new state.

The machine starts in the initial state with the input string on the tape, and the head positioned on the leftmost cell. It then follows the transition function until it reaches an accepting or rejecting state, or loops indefinitely. The output of the machine is the final configuration of the tape, or undefined if the machine does not halt.

A Turing machine can be represented by a diagram, a table, or a formal notation. Here is an example of a Turing machine that decides whether a binary string is a palindrome (a string that is the same when reversed):

![Turing machine diagram](https://plato.stanford.edu/entries/turing-machine/fig1.png)

The diagram shows the states as circles, the tape symbols as letters, and the transitions as arrows. The transition function is written as (write symbol, move direction, new state) on each arrow. For example, the transition from state q0 to q1 on symbol 0 is (0, R, q1), which means write 0, move right, and change to state q1. The initial state is marked with an arrow, and the accepting state is marked with a double circle.

The table shows the same information in a tabular form, with the rows corresponding to the states, and the columns corresponding to the tape symbols. The blank symbol is denoted by B. For example, the entry in row q0 and column 0 is (0, R, q1), which means the same as above.

| State | 0 | 1 | B |
| ----- | - | - | - |
| q0 | (0, R, q1) | (1, R, q2) | (B, R, qa) |
| q1 | (0, R, q1) | (1, R, q2) | (B, L, q3) |
| q2 | (0, R, q1) | (1, R, q2) | (B, L, q4) |
| q3 | (0, L, q3) | (1, L, q5) | (B, R, q6) |
| q4 | (0, L, q5) | (1, L, q4) | (B, R, q6) |
| q5 | (B, L, q5) | (B, L, q5) | (B, R, q0) |
| q6 | (B, R, q6) | (B, R, q6) | (B, R, qa) |
| qa | (0, R, qr) | (1, R, qr) | (B, R, qa) |
| qr | (0, R, qr) | (1, R, qr) | (B, R, qr) |

The formal notation shows the same information in a compact form, using a semicolon to separate the transitions for each state, and a comma to separate the transitions for each symbol. For example, the notation for state q0 is q0: 0->0, R, q1; 1->1, R, q2; B->B, R, qa, which means the same as the diagram and the table.

q0: 0->0, R, q1; 1->1, R, q2; B->B, R, qa
q1: 0->0, R, q1; 1->1