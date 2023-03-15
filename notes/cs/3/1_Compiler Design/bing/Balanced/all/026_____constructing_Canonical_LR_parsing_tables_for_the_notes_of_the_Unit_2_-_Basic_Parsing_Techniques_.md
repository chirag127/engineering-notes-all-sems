# Constructing Canonical LR Parsing Tables

Canonical LR parsing is a bottom-up parsing technique that can handle a large class of context-free grammars. It is based on the idea of constructing a deterministic finite automaton (DFA) that recognizes the viable prefixes of the grammar. A viable prefix is a prefix of a right sentential form that does not extend past the right end of the rightmost handle of that sentential form.

To construct a canonical LR parsing table, the following steps are required:

- Write an augmented grammar for the given input grammar by adding a new start symbol and a production of the form S' -> S, where S is the original start symbol.
- Construct the canonical collection of LR(1) items for the augmented grammar. An LR(1) item is a pair of a production and a lookahead symbol, denoted as [A -> α.β, a], where A -> αβ is a production, α and β are strings of grammar symbols, and a is a terminal symbol or $. The dot indicates how much of the right-hand side has been seen so far. The lookahead symbol indicates what terminal symbol can follow the production in a right sentential form.
- Define the goto and action functions for the canonical LR parsing table. The goto function maps a state and a grammar symbol to a new state, and is defined as follows: goto(I, X) = closure(J), where I is a state, X is a grammar symbol, and J is the set of all items [A -> αX.β, a] such that [A -> α.Xβ, a] is in I. The closure function computes the set of all items that are valid for a given state, by adding new items that can be derived from the existing ones using the grammar rules. The action function maps a state and a terminal symbol to a parsing action, and is defined as follows:

  - If [A -> α.aβ, b] is in Ii and goto(Ii, a) = Ij, then set action[i, a] to "shift j". This means that the parser shifts the terminal symbol a onto the stack and goes to state j.
  - If [A -> α., a] is in Ii, then set action[i, a] to "reduce A -> α". This means that the parser reduces the handle α on top of the stack to the nonterminal symbol A, and goes to the state indicated by the top of the stack and the goto function.
  - If [S' -> S., $] is in Ii, then set action[i, $] to "accept". This means that the parser accepts the input as a valid sentence of the grammar.
  - If there is no item in Ii that applies to the terminal symbol a, then set action[i, a] to "error". This means that the parser reports a syntax error.

- Construct the canonical LR parsing table by filling in the entries for the goto and action functions for each state and symbol. If there is a conflict between two actions for the same entry, then the grammar is not LR(1) and the table cannot be constructed.