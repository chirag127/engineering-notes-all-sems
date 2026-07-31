### Context Free Grammars for Pushdown Automata

- A context-free grammar (CFG) is a set of rewriting rules that can be used to generate or reproduce patterns/strings recursively.
- A pushdown automaton (PDA) is a finite automaton with an additional stack that can store and manipulate symbols.
- A PDA can recognize a context-free language (CFL) by simulating the derivation of a string using a CFG.
- There is an equivalence between CFGs and PDAs, meaning that for every CFG, there exists a PDA that accepts the same language, and vice versa .
- The conversion from a CFG to a PDA is based on the following idea :
  - The PDA starts with the start symbol of the CFG on the stack.
  - The PDA nondeterministically guesses a production rule to apply to the topmost symbol on the stack and replaces it with the right-hand side of the rule.
  - The PDA matches the input symbols with the terminal symbols on the stack and pops them off.
  - The PDA accepts by empty stack when the input is exhausted and the stack is empty.
- The conversion from a PDA to a CFG is based on the following idea :
  - The CFG generates strings that correspond to the sequences of transitions of the PDA.
  - The CFG has variables of the form [q, X, p], where q and p are states of the PDA and X is a stack symbol.
  - The CFG has production rules that capture the possible moves of the PDA, such as pushing, popping, or skipping symbols on the stack.
  - The CFG has a start variable [q0, Z0, qf], where q0 and qf are the initial and final states of the PDA and Z0 is the initial stack symbol.