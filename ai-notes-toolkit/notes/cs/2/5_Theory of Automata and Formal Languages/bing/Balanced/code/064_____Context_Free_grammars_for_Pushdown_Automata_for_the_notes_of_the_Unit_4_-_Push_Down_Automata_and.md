### Context Free Grammars for Pushdown Automata

- A context-free grammar (CFG) is a set of rewriting rules that can be used to generate or reproduce patterns/strings recursively.
- A pushdown automaton (PDA) is a finite automaton with an additional stack that can store and manipulate symbols.
- A PDA can recognize a context-free language (CFL) by simulating the derivation of a string in a CFG.
- There is a procedure to convert any CFG into an equivalent PDA, and vice versa .
- The procedure to convert a CFG into a PDA is as follows:
  - Create a PDA with a single state and two stack symbols: $ (bottom of stack marker) and Z (start symbol of the CFG).
  - For each production rule A -> w in the CFG, add a transition that pops A from the stack and pushes w in reverse order.
  - For each terminal symbol a in the CFG, add a transition that pops a from the stack and reads a from the input.
  - Add a transition that pops $ from the stack and moves to the accept state.
- The procedure to convert a PDA into a CFG is as follows:
  - Create a CFG with variables of the form [qXp], where q and p are states of the PDA and X is a stack symbol.
  - For each transition of the PDA that pops X and pushes YZ, add a production rule [qXp] -> [qYr][rZp] for every state r of the PDA.
  - For each transition of the PDA that pops X and pushes Y, add a production rule [qXp] -> [qYp].
  - For each transition of the PDA that pops X and pushes nothing, add a production rule [qXp] -> epsilon.
  - For each transition of the PDA that pops X and reads a, add a production rule [qXp] -> a[pXp].
  - Add a start variable [q0Z0p] for every state p of the PDA that is reachable from the initial state q0 with an empty stack.
  - Add a production rule S -> [q0Z0p] for every accepting state p of the PDA.