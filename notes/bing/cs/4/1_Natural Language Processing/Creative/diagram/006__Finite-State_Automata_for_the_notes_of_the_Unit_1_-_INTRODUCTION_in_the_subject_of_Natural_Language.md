A finite-state automaton (FSA) is a mathematical model of computation that can accept or reject a string of symbols based on a set of states and transitions. An FSA can be used to model various natural language processing (NLP) tasks, such as morphological analysis, tokenization, spelling correction, text segmentation, and speech recognition.

A finite-state automaton consists of the following components:

- A finite set of states, denoted by Q
- A finite set of input symbols, denoted by Σ
- A transition function, denoted by δ, that maps a state and an input symbol to a state or a set of states
- An initial state, denoted by q0, that belongs to Q
- A set of final or accepting states, denoted by F, that is a subset of Q

A finite-state automaton can be represented by a diagram, where the states are depicted by circles, the transitions are depicted by arrows labeled with input symbols, the initial state is marked by an incoming arrow, and the final states are marked by double circles.

The following diagram illustrates the basic architecture of a finite-state automaton:

```
    +----+     a     +----+
    | q0 | ---->---- | q1 |
    +----+           +----+
      |               |  ^
      |               |  |
      |               |  | b
      |               |  |
      |               |  |
      |               v  |
      +---->---->----+----+
               c     | q2 |
                     +----+
```

In this example, Q = {q0, q1, q2}, Σ = {a, b, c}, q0 is the initial state, F = {q2}, and the transition function is defined as follows:

- δ(q0, a) = q1
- δ(q0, b) = q0
- δ(q0, c) = q2
- δ(q1, a) = q1
- δ(q1, b) = q2
- δ(q1, c) = q1
- δ(q2, a) = q1
- δ(q2, b) = q2
- δ(q2, c) = q2

This FSA accepts strings that end with c or contain the substring ab, such as abc, c, ab, abab, cab, etc. It rejects strings that do not satisfy these conditions, such as a, b, ba, ac, etc.