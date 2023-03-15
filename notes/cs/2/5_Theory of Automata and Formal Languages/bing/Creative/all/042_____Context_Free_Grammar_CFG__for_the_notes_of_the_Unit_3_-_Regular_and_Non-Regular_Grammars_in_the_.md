# Context Free Grammar (CFG) for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

- A context free grammar (CFG) is a formal grammar that can be used to generate all possible strings in a given formal language .
- A formal grammar consists of a set of production rules that can be applied to a symbol or a string of symbols to produce another string of symbols.
- A context free grammar is called so because each production rule can be applied to a nonterminal symbol regardless of its context, i.e., the symbols that surround it.
- A context free grammar can be defined by four tuples as: G = (V, T, P, S) where :
  - V is a finite set of nonterminal symbols, also called variables or syntactic categories.
  - T is a finite set of terminal symbols, also called tokens or lexical categories.
  - P is a finite set of production rules, each of the form A -> α, where A is a nonterminal symbol and α is a string of terminals and/or nonterminals (α can be empty).
  - S is a special nonterminal symbol, called the start symbol, that is used to derive the strings of the language.
- A context free grammar can generate a context free language, which is a set of all strings that can be derived from the start symbol using the production rules.
- A context free grammar can be used to specify the syntax of a language, such as a programming language or a natural language .
- A context free grammar can be used to design parsers, which are programs that analyze the structure and meaning of a string of symbols according to a given grammar.
- A context free grammar can be represented by a parse tree, which is a graphical representation of the derivation of a string from the start symbol using the production rules .
- A context free grammar can be classified into different types, such as regular, deterministic, ambiguous, unambiguous, etc., based on certain properties of the grammar or the language it generates .