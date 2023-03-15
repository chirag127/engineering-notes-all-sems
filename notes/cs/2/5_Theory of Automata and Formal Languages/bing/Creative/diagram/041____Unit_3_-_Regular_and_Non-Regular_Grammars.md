## Unit 3 - Regular and Non-Regular Grammars

- A grammar is a set of rules that defines how a language is generated from a finite alphabet of symbols.
- A grammar consists of four components: a set of terminal symbols, a set of non-terminal symbols, a start symbol, and a set of production rules.
- A production rule is of the form A -> B, where A is a non-terminal symbol and B is a string of terminal and/or non-terminal symbols.
- A grammar can be used to derive strings of the language by starting from the start symbol and applying production rules until only terminal symbols are left.
- A grammar is said to be regular if it has only production rules of the form A -> a, A -> aB, or A -> ε, where A and B are non-terminal symbols, a is a terminal symbol, and ε is the empty string.
- A regular grammar can generate a regular language, which is a language that can be recognized by a finite automaton.
- A grammar is said to be non-regular if it has production rules that do not conform to the regular grammar form.
- A non-regular grammar can generate a non-regular language, which is a language that cannot be recognized by a finite automaton.
- An example of a regular grammar is G = ({a, b}, {S, A, B}, S, {S -> aA, S -> bB, A -> a, A -> bB, B -> b, B -> aA}), which generates the language L(G) = {w | w contains an equal number of a's and b's}.
- An example of a non-regular grammar is G = ({a, b}, {S, A, B}, S, {S -> aA, S -> bB, A -> aS, A -> a, B -> bS, B -> b}), which generates the language L(G) = {w | w is a palindrome}.