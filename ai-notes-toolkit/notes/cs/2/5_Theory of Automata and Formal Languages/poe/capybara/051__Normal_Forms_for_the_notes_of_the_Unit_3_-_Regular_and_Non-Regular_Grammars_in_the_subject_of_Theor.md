### Normal Forms for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

In the study of formal languages, normal forms are a set of rules that can be applied to generate grammars that are easier to work with. Normal forms can help in simplifying the grammar, which in turn can help in analyzing the language it describes. In this unit, we will discuss two normal forms - Chomsky Normal Form and Greibach Normal Form, for regular and non-regular grammars.

#### Chomsky Normal Form

Chomsky Normal Form is a way of rewriting a context-free grammar in a specific form. The rules for Chomsky Normal Form are:

- All rules must be of the form A → BC or A → a, where A, B, and C are variables, and a is a terminal symbol.
- There can be no ε-rules (rules of the form A → ε)
- Start symbol can't appear on the right-hand side of any rule except the one that defines the start symbol.

By converting the grammar into Chomsky Normal Form, we can simplify the language it describes, and the parsing algorithms become more efficient.

#### Greibach Normal Form

Greibach Normal Form is another form of context-free grammar. The rules for Greibach Normal Form are:

- All rules must be of the form A → aBw, where A and B are variables, a is a terminal symbol, and w is a string of variables and terminals.
- The first symbol of w must be a variable, except when w is ε.
- There can be no ε-rules.
- The start symbol must appear on the right-hand side of a rule.

By converting the grammar into Greibach Normal Form, we can simplify the language it describes, and the parsing algorithms become more efficient.

In conclusion, normal forms are a set of rules that can be applied to generate grammars that are easier to work with. In this unit, we discussed two normal forms - Chomsky Normal Form and Greibach Normal Form, for regular and non-regular grammars. By converting the grammar into these normal forms, we can simplify the language it describes, and the parsing algorithms become more efficient.