### Mealy Machine

A Mealy machine is a type of finite-state machine that produces an output based on the current state and the input symbol. It is also known as a **deterministic finite-state transducer**  because it can transform an input sequence into an output sequence.

A Mealy machine can be formally defined by a 6-tuple (Q, q0, ∑, O, δ, λ') where:

- Q is a finite set of states
- q0 is the initial state
- ∑ is a finite input alphabet
- O is a finite output alphabet
- δ: Q × ∑ → Q is the transition function
- λ': Q × ∑ → O is the output function

The output function λ' specifies the output symbol for each state and input symbol pair. The output symbol is written along with the input symbol on the transition arc, separated by a slash (/). For example, a transition from state q1 to state q2 with input symbol a and output symbol b is denoted as a/b.

A Mealy machine can be represented by a state diagram, a state table, or a state equation. Here is an example of a Mealy machine that detects the input sequence 101 and outputs 1 whenever it is detected:

![Mealy machine example](https://media.geeksforgeeks.org/wp-content/uploads/20190829170831/Mealy-Machine-1.png)

The state diagram shows the states, the input symbols, the output symbols, and the transitions. The state table shows the next state and the output symbol for each state and input symbol pair. The state equation shows the output symbol as a function of the current state and the input symbol.

| Current State | Input Symbol | Next State | Output Symbol |
|---------------|--------------|------------|---------------|
| A             | 0            | A          | 0             |
| A             | 1            | B          | 0             |
| B             | 0            | C          | 0             |
| B             | 1            | B          | 0             |
| C             | 0            | A          | 0             |
| C             | 1            | D          | 1             |
| D             | 0            | C          | 0             |
| D             | 1            | B          | 0             |

Output Symbol = A'BC'D + AB'C'D' + ABC'D + A'BCD' + ABCD

Some properties of Mealy machines are :

- They can have fewer states than equivalent Moore machines, because the output depends on both the state and the input.
- They can respond faster than Moore machines, because the output can change as soon as the input changes, without waiting for the next state.
- They can be more difficult to design and implement than Moore machines, because the output function is more complex.