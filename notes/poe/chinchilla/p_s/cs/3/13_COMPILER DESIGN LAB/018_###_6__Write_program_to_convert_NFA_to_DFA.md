### 6. Write program to convert NFA to DFA

Converting a Non-Deterministic Finite Automata (NFA) to a Deterministic Finite Automata (DFA) is a significant concept in automata theory. The conversion process involves creating a DFA equivalent to a given NFA. Here are the steps involved in the conversion of NFA to DFA.

#### Steps to Convert NFA to DFA
1. Create a state table for the NFA.
2. Define the set of states in the DFA.
3. Define the initial state of the DFA.
4. Define the final states of the DFA.
5. Define the transition function of the DFA.
6. Simulate the NFA to find the set of states that can be reached from the initial state using the ε-closure function.
7. For each input symbol, calculate the set of states that can be reached from the set of states obtained in step 6 using the move function.
8. Repeat step 7 until no new states can be added to the DFA.
9. The set of states in the DFA is the power set of the set of states in the NFA.

#### Advantages of Converting NFA to DFA
- DFA is easier to understand and implement as compared to NFA.
- DFA recognizes the languages faster than NFA.
- DFA can be easily implemented in hardware.

#### Disadvantages of Converting NFA to DFA
- The number of states in the DFA can be exponentially larger than in the NFA.
- The conversion process can be time-consuming for large NFAs.

#### Example
Consider the following NFA:
```
     a        b
--►(q0)---ε--►(q1)
  │ │        │ │
ε│ │ε      ε│ │ε
  │ ▼        ▼ │
--►(q2)---ε--►(q3)
     a        b
```
The set of states in the NFA is {q0, q1, q2, q3}, and the input symbols are {a, b}. The initial state is q0, and the final state is q3.

The DFA equivalent of the NFA is as follows:
```
       a       b
→ {q0} → {q1, q2} → {q3}
```
The set of states in the DFA is {{q0}, {q1, q2}, {q3}}. The initial state is {q0}, and the final state is {q3}. The transition function is as follows:
```
    |   a   |   b   |
----|-------|-------|
{q0}|{q1,q2}|   ∅   |
{q1,q2}|{q1,q2}|{q3}|
{q3}|   ∅   |   ∅   |
```

#### Applications of Converting NFA to DFA
- DFA is widely used in lexical analysis, where it is used to recognize tokens in a computer program.
- DFA is used in network routing algorithms to find the shortest path between two nodes in a network.

In conclusion, converting NFA to DFA is an important concept in automata theory. By following the above-mentioned steps, we can convert an NFA to an equivalent DFA. DFA is easier to understand and implement as compared to NFA, and it recognizes the languages faster than NFA. However, the conversion process can be time-consuming for large NFAs, and the number of states in the DFA can be exponentially larger than in the NFA.