# Mealy Machine

A Mealy machine is a type of finite-state machine that produces an output based on the current state and the input symbol. It is also known as a **deterministic finite-state transducer**  because it can transform an input sequence into an output sequence.

A Mealy machine can be formally defined by a 6-tuple (Q, q0, ∑, O, δ, λ') where:

- Q is a finite set of states
- q0 is the initial state
- ∑ is a finite input alphabet
- O is a finite output alphabet
- δ: Q × ∑ → Q is the transition function
- λ': Q × ∑ → O is the output function

A Mealy machine can be represented by a state diagram, where each state is labeled with its name and each transition is labeled with the input symbol and the output symbol separated by a slash. For example, the following state diagram shows a Mealy machine that detects the sequence 101 in the input and outputs 1 whenever it is detected:

![Mealy machine example](https://media.geeksforgeeks.org/wp-content/uploads/20190802110913/Mealy-Machine-1.png)

Some properties of Mealy machines are :

- They are more efficient than Moore machines, as they require fewer states to implement the same functionality.
- They are more expressive than Moore machines, as they can produce different outputs for the same state depending on the input symbol.
- They are equivalent to Moore machines in terms of computational power, as any Mealy machine can be converted into a Moore machine and vice versa.