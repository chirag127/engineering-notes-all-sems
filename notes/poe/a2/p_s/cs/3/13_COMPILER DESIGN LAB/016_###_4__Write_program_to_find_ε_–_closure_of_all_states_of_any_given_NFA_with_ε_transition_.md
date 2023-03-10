 Here is the content written in markdown format for the given topic:

### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

1. ε-closure of a state 'q' is the set of states reachable from 'q' with zero or more ε transitions.
2. To find ε-closure of a state 'q', do following:
    - Add 'q' to the closure set.
    - Do following for each state 'r' reachable from 'q' with an ε transition:
        - If 'r' is not already in closure set, add 'r' to closure set.
        - Find ε-closure of 'r' and add those states to closure set.
3. Repeat step#2 until no more states can be added to closure set.
4. The final closure set contains ε-closure of the given state 'q'.
5. Pseudocode:
    closure(q)
        closure_set = {q}
        for each r such that (q, ε, r) is a transition
        {
            if r is not in closure_set
            {
                closure_set = closure_set U {r}
                closure_set = closure_set U closure(r)
            }
        }
        return closure_set

**Advantages:** ε-closure is used to simplify NFA by replacing ε-transitions with a single state containing the ε-closure of the states. This helps in converting NFA to DFA.
**Disadvantages:** Finding ε-closure of all states can be computationally expensive for large NFAs with many ε-transitions.
**Applications:** Used in converting NFA to DFA which is useful in various algorithms and computations on automata.

[Detailed ASCII diagrams and examples can be added here if required.]