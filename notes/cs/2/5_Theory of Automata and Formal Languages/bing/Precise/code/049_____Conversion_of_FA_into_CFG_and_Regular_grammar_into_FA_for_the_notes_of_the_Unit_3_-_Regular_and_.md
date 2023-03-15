### Conversion of FA into CFG and Regular grammar into FA for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

1. **Conversion of Finite Automata (FA) into Context-Free Grammar (CFG):**
    - A finite automaton can be converted into an equivalent context-free grammar by using the following steps:
        1. For each state `q` in the FA, create a non-terminal symbol `Aq` in the CFG.
        2. For each transition `q1 -> q2` labeled with input symbol `a` in the FA, create a production rule `Aq1 -> aAq2` in the CFG.
        3. For each final state `qf` in the FA, create a production rule `Aqf -> ε` in the CFG, where `ε` represents the empty string.
        4. The start symbol of the CFG is the non-terminal symbol corresponding to the initial state of the FA.
    - This conversion process generates a context-free grammar that generates the same language as the finite automaton.

2. **Conversion of Regular Grammar into Finite Automata (FA):**
    - A regular grammar can be converted into an equivalent finite automaton by using the following steps:
        1. For each non-terminal symbol `A` in the regular grammar, create a state `qA` in the FA.
        2. For each production rule `A -> aB` in the regular grammar, create a transition `qA -> qB` labeled with input symbol `a` in the FA.
        3. For each production rule `A -> a` in the regular grammar, create a transition `qA -> qf` labeled with input symbol `a` in the FA, where `qf` is a new final state.
        4. The initial state of the FA is the state corresponding to the start symbol of the regular grammar.
        5. If the regular grammar contains a production rule `S -> ε`, where `S` is the start symbol and `ε` represents the empty string, then the initial state of the FA is also a final state.
    - This conversion process generates a finite automaton that recognizes the same language as the regular grammar.