# Conversion of FA into CFG and Regular grammar into FA

## FA into CFG

- A finite automaton (FA) is a model of computation that accepts or rejects a string based on its transitions between a finite set of states and a finite alphabet of symbols.
- A context-free grammar (CFG) is a set of production rules that generate a language by applying substitutions to a start symbol.
- To convert a FA into a CFG, we can follow these steps:
  - For each state q of the FA, introduce a new variable Q in the CFG.
  - The variable corresponding to the starting state of the FA will be the starting variable of the CFG.
  - For each transition q -> r labeled by a symbol a in the FA, add a production rule Q -> aR in the CFG, where Q and R are the variables corresponding to q and r, respectively.
  - For each final state q of the FA, add a production rule Q -> epsilon in the CFG, where Q is the variable corresponding to q and epsilon is the empty string.
- Example: Consider the following FA that accepts the language of all strings over {0,1} that end with 1.

![FA](https://i.stack.imgur.com/4x0hR.png)

- By applying the above algorithm, we get the following CFG with the starting variable S and the following rules:

```
S -> 0E | 1D
E -> 0E | 1D
D -> 0E | 1D | epsilon
```

- To derive a word in the CFG, we can follow the transitions of the FA and apply the corresponding rules. For example, to derive the word 011, we can do:

```
S -> 0E -> 01D -> 011
```

## Regular grammar into FA

- A regular grammar is a special type of CFG that has the following restrictions on its production rules:
  - The left-hand side must be a single variable.
  - The right-hand side must be either a single terminal, a single terminal followed by a single variable, or epsilon.
- To convert a regular grammar into a FA, we can follow these steps:
  - For each variable A in the grammar, create a state q_A in the FA.
  - The state corresponding to the starting variable of the grammar will be the starting state of the FA.
  - For each production rule A -> aB in the grammar, where a is a terminal and B is a variable, create a transition q_A -> q_B labeled by a in the FA.
  - For each production rule A -> a in the grammar, where a is a terminal, create a transition q_A -> q_F labeled by a in the FA, where q_F is a new final state.
  - For each production rule A -> epsilon in the grammar, where epsilon is the empty string, make q_A a final state in the FA.
- Example: Consider the following regular grammar that generates the language of all strings over {a,b} that contain at least one a.

```
S -> aA | bS
A -> aA | bA | epsilon
```

- By applying the above algorithm, we get the following FA with the starting state q_S and the final states q_A and q_F.

![FA](https://i.stack.imgur.com/0f0X9.png)

- To accept a word in the FA, we can follow the transitions of the FA and match the symbols of the word. For example, to accept the word bab, we can do:

```
q_S -> b -> q_S -> a -> q_A -> b -> q_A
```