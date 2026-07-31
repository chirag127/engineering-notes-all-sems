Hello, I am Sydney, your AI assistant. I can help you with your programming tasks. Here is the content you requested:

### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

- An NFA with ε transition is a nondeterministic finite automaton that can move from one state to another without consuming any input symbol, by using a special transition labeled with ε (the empty string).
- The ε-closure of a state q is the set of all states that can be reached from q by following only ε transitions, including q itself.
- The ε-closure of a set of states Q is the union of the ε-closures of all the states in Q.
- To find the ε-closure of all states of an NFA with ε transition, we can use the following algorithm:

  - Initialize an empty stack S and an empty set E.
  - For each state q in the NFA, do the following steps:
    - Push q onto S and add q to E.
    - While S is not empty, do the following steps:
      - Pop a state p from S.
      - For each state r that has an ε transition from p, do the following steps:
        - If r is not in E, then push r onto S and add r to E.
    - Output E as the ε-closure of q and clear E for the next iteration.

- Here is an example of an NFA with ε transition and its ε-closures:

![NFA with ε transition](https://i.imgur.com/0Q6cZ3w.png)

| State | ε-closure |
| ----- | --------- |
| q0    | {q0, q1}  |
| q1    | {q1, q2}  |
| q2    | {q2}      |
| q3    | {q3}      |
| q4    | {q4}      |