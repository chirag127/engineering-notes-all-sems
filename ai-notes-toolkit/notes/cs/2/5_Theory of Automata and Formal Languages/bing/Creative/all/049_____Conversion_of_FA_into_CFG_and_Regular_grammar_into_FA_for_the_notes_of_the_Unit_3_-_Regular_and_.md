# Conversion of FA into CFG and Regular grammar into FA

## FA to CFG conversion

- A finite automaton (FA) is a model of computation that accepts or rejects strings of symbols.
- A context-free grammar (CFG) is a set of rules that generates strings of symbols.
- A FA can be converted into a CFG that generates the same language as the FA.
- The general idea of the algorithm is as follows :
  - For each state q of the FA, introduce a new variable Q.
  - The variable corresponding to the starting state will be the starting variable of the new CFG.
  - For each transition of the FA q a -> q', add a rule Q -> aQ' to the CFG.
  - For each final state q of the FA, add a rule Q -> epsilon to the CFG, where epsilon is the empty string.

- For example, consider the following FA that accepts strings of a's and b's that end with ab:

![FA example](https://jflap.org/modules/JFLAPWorkshop2014/Upload%20Exercises%20and%20Modules%20here/ArvindB/Exercises/RegularGrammar/Regular2CFG_files/image002.jpg)

- The corresponding CFG is:

S -> aS | bA | epsilon

A -> aB | bA

B -> bS | epsilon

## Regular grammar to FA conversion

- A regular grammar is a special type of CFG that has rules of the form A -> aB or A -> a, where A and B are variables and a is a terminal symbol.
- A regular grammar can be converted into a FA that recognizes the same language as the grammar.
- The general idea of the algorithm is as follows:
  - For each variable A of the grammar, create a state qA in the FA.
  - The state corresponding to the starting variable will be the initial state of the FA.
  - For each rule A -> aB in the grammar, add a transition qA a -> qB to the FA.
  - For each rule A -> a in the grammar, add a transition qA a -> qF to the FA, where qF is a new final state.
  - If the grammar has a rule S -> epsilon, where S is the starting variable, then make the initial state also a final state.

- For example, consider the following regular grammar that generates strings of a's and b's that end with ab:

S -> aS | bA | epsilon

A -> aB | bA

B -> bS

- The corresponding FA is:

![FA example](https://i.ytimg.com/vi/L8BT0PXUVQQ/maxresdefault.jpg)