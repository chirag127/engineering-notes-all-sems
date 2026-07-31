## Unit 3 - Regular and Non-Regular Grammars

- A grammar is a set of rules that defines how a language is generated from a finite alphabet of symbols.
- A grammar consists of four components: a set of terminal symbols, a set of non-terminal symbols, a start symbol, and a set of production rules.
- A production rule is of the form A -> B, where A is a non-terminal symbol and B is a string of terminal and/or non-terminal symbols.
- A grammar is said to be regular if all its production rules are of one of the following forms: A -> a, A -> aB, or A -> ε, where A and B are non-terminal symbols, a is a terminal symbol, and ε is the empty string.
- A grammar is said to be non-regular if it has at least one production rule that is not of the regular form.
- Regular grammars are equivalent to regular expressions and finite automata, and can generate regular languages.
- Non-regular grammars can generate languages that are not regular, such as context-free languages and context-sensitive languages.
- Examples of regular grammars are:

  - The grammar for the language L = {a^n b^n | n >= 0}, where the terminal symbols are a and b, the non-terminal symbols are S and A, the start symbol is S, and the production rules are:

    - S -> ε
    - S -> aA
    - A -> aA
    - A -> b

  - The grammar for the language L = {0, 1}*, where the terminal symbols are 0 and 1, the non-terminal symbol is S, the start symbol is S, and the production rules are:

    - S -> ε
    - S -> 0S
    - S -> 1S

- Examples of non-regular grammars are:

  - The grammar for the language L = {a^n b^n c^n | n >= 0}, where the terminal symbols are a, b, and c, the non-terminal symbols are S, A, and B, the start symbol is S, and the production rules are:

    - S -> ε
    - S -> ABC
    - A -> aA
    - A -> a
    - B -> bB
    - B -> b
    - C -> cC
    - C -> c

  - The grammar for the language L = {ww | w ∈ {0, 1}*}, where the terminal symbols are 0 and 1, the non-terminal symbols are S and A, the start symbol is S, and the production rules are:

    - S -> ε
    - S -> 0A0
    - S -> 1A1
    - A -> ε
    - A -> 0A0
    - A -> 1A1