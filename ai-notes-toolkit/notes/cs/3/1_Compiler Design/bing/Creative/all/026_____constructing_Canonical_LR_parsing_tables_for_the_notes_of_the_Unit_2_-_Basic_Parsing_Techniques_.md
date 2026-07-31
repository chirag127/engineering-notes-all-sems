# Constructing Canonical LR Parsing Tables

Canonical LR parsing is a bottom-up parsing technique that can handle a large class of context-free grammars. It is based on the idea of constructing a deterministic finite automaton (DFA) that recognizes the viable prefixes of the grammar. A viable prefix is a prefix of a right sentential form that does not extend past the right end of the rightmost handle of that sentential form.

To construct a canonical LR parsing table, the following steps are required:

- Write an augmented grammar for the given input grammar by adding a new start symbol and a production of the form S' -> S, where S is the original start symbol.
- Construct the canonical collection of LR(1) items for the augmented grammar. An LR(1) item is a pair of a production and a lookahead symbol, denoted as [A -> α.β, a], where A -> αβ is a production, α and β are strings of grammar symbols, and a is a terminal symbol or $. The dot indicates how much of the right-hand side has been seen so far. The lookahead symbol indicates what terminal symbols can follow the production in a right sentential form.
- For each set of LR(1) items in the canonical collection, define the GOTO function, which maps a grammar symbol X to the set of LR(1) items that can be reached by shifting X on the input. The GOTO function can be computed by applying the closure operation to the set of items of the form [A -> α.Xβ, a], where X is the symbol to be shifted.
- For each set of LR(1) items in the canonical collection, define the ACTION function, which maps a terminal symbol a to one of the following actions: shift, reduce, accept, or error. The ACTION function can be computed by applying the following rules:

  - If [A -> α.aβ, b] is in the set and GOTO(I, a) = I', then ACTION(I, a) = shift I'. This means that the parser can shift the terminal symbol a and go to the next set of items I'.
  - If [A -> α., a] is in the set, then ACTION(I, a) = reduce A -> α. This means that the parser can reduce by the production A -> α if the next input symbol is a.
  - If [S' -> S., $] is in the set, then ACTION(I, $) = accept. This means that the parser can accept the input if it reaches the end of the input.
  - If none of the above rules apply, then ACTION(I, a) = error. This means that the parser cannot parse the input.

- The canonical LR parsing table consists of two parts: the ACTION table and the GOTO table. The ACTION table is indexed by the sets of LR(1) items and the terminal symbols, and the GOTO table is indexed by the sets of LR(1) items and the nonterminal symbols. The entries of the tables are the values of the ACTION and GOTO functions, respectively.