### Mealy Machine

A Mealy machine is a type of finite-state machine that produces an output based on the current state and the input. It is also known as a deterministic finite-state transducer .

Some characteristics of a Mealy machine are:

- It has a finite set of states, denoted by Q.
- It has a finite set of input symbols, denoted by ∑.
- It has a finite set of output symbols, denoted by O.
- It has a start state, denoted by q0, which belongs to Q.
- It has a state transition function, denoted by δ, which maps Q × ∑ to Q.
- It has an output function, denoted by λ, which maps Q × ∑ to O.

A Mealy machine can be represented by a 6-tuple (Q, q0, ∑, O, δ, λ) .

A Mealy machine can also be represented by a state diagram, where each state is labeled with its name and each transition is labeled with the input symbol and the output symbol separated by a slash  .

For example, the following state diagram shows a Mealy machine that detects the input sequence 101 and outputs 1 whenever it is detected, otherwise outputs 0 .

![Mealy machine example](https://media.geeksforgeeks.org/wp-content/uploads/20190702123651/Mealy-Machine-1.png)

Some applications of Mealy machines are:

- Cipher machines: A Mealy machine can be used to encrypt or decrypt a string of letters by mapping each input symbol and state to an output symbol .
- Sequence detectors: A Mealy machine can be used to detect a specific pattern of bits in a stream of input symbols and generate an output accordingly .
- Protocol analyzers: A Mealy machine can be used to verify the correctness of a communication protocol by checking the sequence of messages exchanged between two parties .