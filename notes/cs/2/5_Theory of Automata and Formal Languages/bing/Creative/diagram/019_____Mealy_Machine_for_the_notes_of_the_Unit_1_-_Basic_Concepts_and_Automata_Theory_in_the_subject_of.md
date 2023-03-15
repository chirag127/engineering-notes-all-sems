### Mealy Machine

A Mealy machine is a type of finite-state machine that produces an output based on the current state and the input symbol. It is also known as a **deterministic finite-state transducer**  because it can transform an input sequence into an output sequence .

Some characteristics of a Mealy machine are:

- It has a finite set of states, denoted by **Q**.
- It has a finite set of input symbols, denoted by **∑**.
- It has a finite set of output symbols, denoted by **O**.
- It has a start state, denoted by **q0**, which belongs to Q.
- It has a state transition function, denoted by **δ**, which maps Q × ∑ to Q.
- It has an output function, denoted by **λ**, which maps Q × ∑ to O.

A Mealy machine can be represented by a **state diagram**, where each state is labeled with its name and each transition is labeled with the input symbol and the output symbol separated by a slash. For example, the following state diagram shows a Mealy machine that detects the sequence 101 and outputs 1 whenever it occurs:

![Mealy machine example](https://media.geeksforgeeks.org/wp-content/uploads/20190813104334/Mealy-Machine-1.png)

A Mealy machine can also be represented by a **state table**, where each row corresponds to a state and each column corresponds to an input symbol. The entries in the table are the next state and the output symbol separated by a slash. For example, the following state table shows the same Mealy machine as above:

| State | 0 | 1 |
|-------|---|---|
| A     | A/0 | B/0 |
| B     | A/0 | C/0 |
| C     | D/1 | B/0 |
| D     | A/0 | B/0 |

A Mealy machine can be used to model various applications that involve sequential logic, such as cipher machines, sequence detectors, vending machines, etc.