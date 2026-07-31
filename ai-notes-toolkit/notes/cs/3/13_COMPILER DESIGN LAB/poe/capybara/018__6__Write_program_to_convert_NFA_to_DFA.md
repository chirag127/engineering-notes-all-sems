### 6. Write program to convert NFA to DFA

#### Introduction
- Nondeterministic Finite Automata (NFA) are finite state machines that can have multiple transitions for a single input.
- Deterministic Finite Automata (DFA) are finite state machines that have only one transition for a single input.
- Converting an NFA to DFA is an important process in automata theory.

#### Steps to Convert NFA to DFA
1. Create a table for the DFA.
2. Identify the initial state of the DFA.
3. Find the closure of the initial state. This is the set of all states that can be reached from the initial state using epsilon transitions.
4. Add the closure of the initial state to the table as the first row.
5. For each input symbol, find the set of states that can be reached from the current state using that input symbol.
6. Find the closure of each state in the set found in step 5.
7. If the set found in step 5 is not already in the table, add it as a new row.
8. Add the transition from the current state to the set found in step 5 for the input symbol.
9. Repeat steps 5-8 for all input symbols and all sets of states that are added to the table.
10. If a set of states contains an accepting state from the original NFA, mark it as an accepting state in the DFA.

#### Code for NFA to DFA Conversion
Here is an example Python code for converting an NFA to a DFA:
```python
def nfa_to_dfa(nfa):
    dfa_table = {}
    queue = []
    start_state = nfa.epsilon_closure(nfa.start_state)
    dfa_table[frozenset(start_state)] = 0
    queue.append(start_state)
    i = 1
    while queue:
        state_set = queue.pop(0)
        for symbol in nfa.alphabet:
            next_state_set = nfa.move(state_set, symbol)
            next_state_set = nfa.epsilon_closure(next_state_set)
            if next_state_set not in dfa_table:
                dfa_table[frozenset(next_state_set)] = i
                i += 1
                queue.append(next_state_set)
            dfa_table[frozenset(state_set)][symbol] = dfa_table[frozenset(next_state_set)]
    dfa = DFA(dfa_table, 0, set([dfa_table[frozenset(state_set)] for state_set in nfa.accept_states]))
    return dfa
```

#### Conclusion
- Converting an NFA to a DFA is an important process in automata theory.
- The above steps and code can be used to convert an NFA to a DFA.