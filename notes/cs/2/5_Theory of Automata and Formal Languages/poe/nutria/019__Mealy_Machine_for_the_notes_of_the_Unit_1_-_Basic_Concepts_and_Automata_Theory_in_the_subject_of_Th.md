
### Mealy Machine

Mealy machines are a type of finite state machine (FSM) which produces an output depending on the current state and the current input. The output of a Mealy machine is a function of both the current state and the current input.

A Mealy machine consists of:
- A set of states
- An input alphabet
- An output alphabet
- A transition function
- An output function

A Mealy machine can be represented as a directed graph, where each node represents a state, and each edge represents a transition from one state to another. The output of the machine is determined by the output function, which is a function of the current state and input.

The transition function of a Mealy machine is defined as follows:

$$\delta(q,x) = (q',y)$$

Where $q$ is the current state, $x$ is the current input, $q'$ is the next state, and $y$ is the output.

The output function of a Mealy machine is defined as follows:

$$\gamma(q,x) = y$$

Where $q$ is the current state, $x$ is the current input, and $y$ is the output.