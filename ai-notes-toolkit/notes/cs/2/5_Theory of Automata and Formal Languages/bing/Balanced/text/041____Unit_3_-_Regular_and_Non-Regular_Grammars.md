## Unit 3 - Regular and Non-Regular Grammars

- A grammar is a set of rules that define how a language is generated from a finite alphabet of symbols.
- A grammar consists of four components: a set of terminal symbols, a set of non-terminal symbols, a start symbol, and a set of production rules.
- A production rule is of the form A -> B, where A is a non-terminal symbol and B is a string of terminal and/or non-terminal symbols.
- A grammar can be used to derive strings of the language by starting from the start symbol and applying production rules until only terminal symbols are left.
- A grammar is said to be regular if all its production rules are of one of the following forms: A -> a, A -> aB, or A -> ε, where A and B are non-terminal symbols, a is a terminal symbol, and ε is the empty string.
- A regular grammar can generate a regular language, which is a language that can be recognized by a finite automaton.
- A grammar is said to be non-regular if it has at least one production rule that is not of the forms mentioned above.
- A non-regular grammar can generate a non-regular language, which is a language that cannot be recognized by a finite automaton.
- Examples of non-regular languages are {a^n b^n | n >= 0}, {w w^R | w is any string}, and {a^p | p is a prime number}.
- Non-regular languages can be recognized by more powerful models of computation, such as pushdown automata or Turing machines.