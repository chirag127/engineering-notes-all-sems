# Mealy Machine

A Mealy machine is a type of finite-state machine that produces an output based on the current state and the input. It is also known as a **deterministic finite-state transducer**  because it can transform an input sequence into an output sequence.

Some characteristics of a Mealy machine are:

- It has a finite set of states, denoted by **Q**.
- It has a finite set of input symbols, denoted by **∑**.
- It has a finite set of output symbols, denoted by **O**.
- It has a start state, denoted by **q0**, which belongs to **Q**.
- It has a state transition function, denoted by **δ**, which maps a state and an input symbol to a next state: **δ: Q × ∑ → Q**.
- It has an output function, denoted by **λ**, which maps a state and an input symbol to an output symbol: **λ: Q × ∑ → O**.

A Mealy machine can be represented by a **state diagram**, where each state is labeled with its name and each transition is labeled with the input symbol and the output symbol separated by a slash (/). For example, the following state diagram shows a Mealy machine that detects the sequence 101 in the input and outputs 1 when the sequence is complete:

![Mealy machine example](https://media.geeksforgeeks.org/wp-content/uploads/20191029152204/Mealy-Machine-1.png)

A Mealy machine can also be represented by a **transition table**, where each row corresponds to a state and each column corresponds to an input symbol. The entries in the table show the next state and the output symbol for each state and input symbol. For example, the following transition table shows the same Mealy machine as the state diagram above:

| State | 0 | 1 |
|-------|---|---|
| A     | A/0 | B/0 |
| B     | A/0 | C/0 |
| C     | D/1 | B/0 |
| D     | A/0 | B/0 |

Some advantages of a Mealy machine are:

- It can have fewer states than a Moore machine (another type of finite-state machine) for the same functionality .
- It can respond faster to the input changes because the output depends on the input as well as the state .

Some disadvantages of a Mealy machine are:

- It can have more complex logic than a Moore machine because the output depends on the input as well as the state .
- It can have glitches (unwanted changes) in the output because the output can change asynchronously with the state .