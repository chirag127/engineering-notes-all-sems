 Here is the content in markdown format:

### Normal Forms for grammar for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

The normal forms for grammar are:

1. Chomsky Normal Form (CNF):
- Every rule must be of the type: A → B C or A → a
- All rules must be in the form of either:
    - A → B C (where B and C are non-terminals)
    - A → a (where a is a terminal)
- Advantage: Useful for compiler design. Simplifies grammars and makes parsing easier.
- Disadvantage: Not all grammars can be converted to CNF.

2. Greibach Normal Form (GNF):
- Every rule must be of the type: A → a B C or A → a
- All rules must be in the form of either:
    - A → a B C (where B and C are non-terminals and a is a terminal)
    - A → a (where a is a terminal)
- Advantage: Any grammar can be converted to GNF. Useful for compiler design.
- Disadvantage: May result in exponential increase in number of rules.

3. Chomsky Normal Form without ε-rules (CNF−ε):
- Same as Chomsky Normal Form but without any ε-rules (rules of the type A → ε where ε represents empty string).
- Advantage: ε-removal simplifies grammars and parsing.
- Disadvantage: Not all grammars can be converted to CNF−ε (those with ε-rules cannot be converted).

[Detailed descriptions, examples, diagrams, codes, pros and cons, applications, etc. can be added if required.]