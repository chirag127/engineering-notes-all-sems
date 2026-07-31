### Conversion of FA into CFG and Regular grammar into FA for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A finite automaton (FA) is a model of computation that accepts or rejects strings of symbols over a finite alphabet.
- A context-free grammar (CFG) is a set of rules that generates strings of symbols over a finite alphabet, using a finite set of variables and terminals.
- A regular grammar is a special case of a CFG that has rules of the form A -> aB or A -> a, where A and B are variables and a is a terminal.
- A FA can be converted into a CFG by the following algorithm :
  - For each state q of the FA, introduce a new variable Q.
  - The variable corresponding to the starting state will be the starting variable of the new CFG.
  - For each transition of the FA q -> a r, where q and r are states and a is a symbol, add a rule Q -> aR, where Q and R are the corresponding variables.
  - For each final state q of the FA, add a rule Q -> epsilon, where Q is the corresponding variable and epsilon is the empty string.
- A regular grammar can be converted into a FA by the following algorithm:
  - Create a new state q0 and make it the starting state of the FA.
  - For each variable A of the grammar, create a new state qA.
  - For each rule of the form A -> aB, where A and B are variables and a is a terminal, add a transition qA -> a qB, where qA and qB are the corresponding states.
  - For each rule of the form A -> a, where A is a variable and a is a terminal, add a transition qA -> a qF, where qA is the corresponding state and qF is a new final state.
  - If the grammar has a rule S -> epsilon, where S is the starting variable and epsilon is the empty string, make q0 a final state as well.