### Mealy Machine

A Mealy machine is a type of finite-state machine that produces an output based on the current state and the input. It is also known as a **deterministic finite-state transducer** because it can transform an input sequence into an output sequence.

Some characteristics of a Mealy machine are:

- It has a finite set of states, denoted by **Q**.
- It has a finite set of input symbols, denoted by **∑**.
- It has a finite set of output symbols, denoted by **O**.
- It has a start state, denoted by **q0**, which belongs to **Q**.
- It has a state transition function, denoted by **δ**, which maps a state and an input symbol to a next state: **δ: Q × ∑ → Q**.
- It has an output function, denoted by **λ**, which maps a state and an input symbol to an output symbol: **λ: Q × ∑ → O**.

A Mealy machine can be represented by a **transition table** or a **transition diagram**. In a transition table, each row corresponds to a state, each column corresponds to an input symbol, and each entry contains the next state and the output symbol separated by a slash. In a transition diagram, each state is represented by a circle, each input symbol is represented by an edge, and each output symbol is represented by a label on the edge.

For example, consider a Mealy machine that detects whether the input sequence contains an even number of 0s and 1s. The machine has two states: **q0**, which indicates that the number of 0s and 1s is even, and **q1**, which indicates that the number of 0s and 1s is odd. The machine has two input symbols: **0** and **1**. The machine has two output symbols: **E**, which indicates that the number of 0s and 1s is even, and **O**, which indicates that the number of 0s and 1s is odd. The machine can be described by the following transition table and diagram:

| State | 0 | 1 |
| ----- | - | - |
| q0    | q1/O | q1/O |
| q1    | q0/E | q0/E |

![Mealy machine example](https://i.imgur.com/0Q8zZmX.png)

Some advantages of a Mealy machine are:

- It can produce an output as soon as an input is received, without waiting for the next state.
- It can have fewer states than a Moore machine, which is another type of finite-state machine that produces an output based on the current state only.
- It can be easily converted to a Moore machine by adding intermediate states and output symbols.

Some disadvantages of a Mealy machine are:

- It can have more complex logic than a Moore machine, as the output depends on both the state and the input.
- It can have more transitions than a Moore machine, as each state can have multiple outputs for different inputs.
- It can have more glitches than a Moore machine, as the output can change rapidly with the input.