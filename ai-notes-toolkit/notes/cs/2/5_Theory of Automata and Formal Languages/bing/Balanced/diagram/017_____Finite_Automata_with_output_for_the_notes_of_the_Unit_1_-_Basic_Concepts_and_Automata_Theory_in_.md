### Finite Automata with Output

- A finite automata with output is a mathematical model of computation that can be in one of a finite number of states and can produce output symbols depending on the current state and the input symbol .
- A finite automata with output is also known as a finite state machine (FSM) or a transducer .
- There are two types of finite automata with output: Moore machines and Mealy machines  .
- A Moore machine is a finite automata with output where the output depends only on the current state  .
- A Mealy machine is a finite automata with output where the output depends on both the current state and the input symbol  .
- A finite automata with output can be represented by a five-tuple (Q, Σ, δ, λ, q0) where  :
  - Q is a finite set of states
  - Σ is a finite set of input symbols (alphabet)
  - δ is a transition function that maps Q × Σ to Q
  - λ is an output function that maps Q × Σ to a finite set of output symbols (for Mealy machines) or Q to a finite set of output symbols (for Moore machines)
  - q0 is the initial state
- A finite automata with output can be represented by a state diagram, where each state is a circle labeled with the state name and the output symbol (for Moore machines) or a transition is an arrow labeled with the input symbol and the output symbol (for Mealy machines)  .
- A finite automata with output can be used to perform various tasks, such as encoding, decoding, pattern matching, arithmetic operations, etc.  .

Here is an example of a Moore machine that takes a binary number as input and produces its 1's complement as output:

![Moore machine example](https://media.geeksforgeeks.org/wp-content/uploads/20201221155305/Untitled-Diagram-2020-12-21T155254.421.png)

Here is an example of a Mealy machine that takes a binary number as input and produces its 1's complement as output:

![Mealy machine example](https://media.geeksforgeeks.org/wp-content/uploads/20201221155305/Untitled-Diagram-2020-12-21T155254.421-1.png)