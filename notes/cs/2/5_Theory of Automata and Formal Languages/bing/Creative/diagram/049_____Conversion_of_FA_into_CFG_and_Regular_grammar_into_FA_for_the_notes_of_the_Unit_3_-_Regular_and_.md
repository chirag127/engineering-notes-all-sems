### Conversion of FA into CFG and Regular grammar into FA

- A finite automaton (FA) is a model of computation that accepts or rejects a string based on its transitions between a finite set of states and a finite alphabet of symbols.
- A context-free grammar (CFG) is a set of rules that generates a language by applying substitutions of variables with terminals or other variables.
- A regular grammar (RG) is a special case of a CFG where each rule has the form A -> aB or A -> a or A -> ε, where A and B are variables, a is a terminal, and ε is the empty string.
- A regular expression (RE) is a notation that describes a regular language using symbols, concatenation, union, and Kleene star.

- To convert a FA into a CFG, we can follow these steps:
  - For each state q of the FA, introduce a new variable Q.
  - The variable corresponding to the starting state will be the starting variable of the new CFG.
  - For each transition q -> r labeled with a symbol a, add a rule Q -> aR to the CFG, where Q and R are the variables corresponding to q and r, respectively.
  - For each final state q of the FA, add a rule Q -> ε to the CFG, where Q is the variable corresponding to q.

- To convert a regular grammar into a FA, we can follow these steps:
  - For each variable A of the RG, create a state q_A in the FA.
  - The state corresponding to the starting variable will be the initial state of the FA.
  - For each rule A -> aB in the RG, add a transition q_A -> q_B labeled with a symbol a in the FA, where q_A and q_B are the states corresponding to A and B, respectively.
  - For each rule A -> a or A -> ε in the RG, add a transition q_A -> q_F labeled with a symbol a or ε in the FA, where q_A is the state corresponding to A and q_F is a new final state of the FA.