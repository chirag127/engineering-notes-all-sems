### Context Free Grammar (CFG) for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A context free grammar (CFG) is a formal grammar that can generate all possible strings in a given formal language .
- A formal grammar consists of a set of production rules that can be applied to a symbol or a string of symbols to produce another string of symbols.
- A context free grammar is called so because the production rules can be applied to a nonterminal symbol regardless of its context, i.e., the symbols that surround it.
- A context free grammar can be defined by four tuples as: G = (V, T, P, S) where :
  - V is a finite set of nonterminal symbols, also called variables or syntactic categories.
  - T is a finite set of terminal symbols, also called tokens or lexical categories. V and T are disjoint sets, i.e., V ∩ T = ∅.
  - P is a finite set of production rules, each of the form A → α, where A ∈ V and α ∈ (V ∪ T)*. The symbol * denotes the Kleene star, which means zero or more repetitions of the symbols in the parentheses.
  - S ∈ V is the start symbol, from which the derivation of strings begins.
- A context free grammar can be used to specify the syntax of a language, such as a programming language or a natural language .
- A context free grammar can also be used to describe the nested structures in a language, such as parentheses, brackets, or tags .
- A context free grammar can generate a context free language, which is the set of all strings that can be derived from the start symbol using the production rules .
- A context free language can be recognized by a pushdown automaton, which is a finite state machine with a stack .
- A context free grammar can be represented by a parse tree, which is a graphical representation of the derivation of a string from the start symbol .
- A context free grammar can be classified into different types, such as ambiguous, unambiguous, left-recursive, right-recursive, left-linear, right-linear, etc., based on the properties of the production rules and the generated language .