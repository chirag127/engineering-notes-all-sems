Hello, I am Sydney, your AI assistant. I can help you with your topic of normal forms in formal languages. Here are some notes that you can use for your study material:

# Normal Forms for the Unit 3 - Regular and Non-Regular Grammars in the Subject of Theory of Automata and Formal Languages

- A normal form is a standard way of writing a grammar that has certain desirable properties, such as simplicity, efficiency, or uniqueness.
- There are different types of normal forms for different types of grammars, such as regular, context-free, context-sensitive, or unrestricted grammars.
- In this unit, we will focus on two normal forms for context-free grammars: Chomsky normal form and Greibach normal form.

## Chomsky Normal Form

- A context-free grammar is in Chomsky normal form if all of its production rules are of the form:

  - A → BC, where A, B, and C are nonterminal symbols
  - A → a, where A is a nonterminal symbol and a is a terminal symbol
  - S → ε, where S is the start symbol and ε is the empty string

- Any context-free grammar can be converted to an equivalent grammar in Chomsky normal form by applying a series of transformations, such as eliminating ε-rules, unit rules, and useless symbols, and introducing new nonterminal symbols.
- Chomsky normal form is useful for proving properties of context-free languages, such as the pumping lemma, and for designing parsing algorithms, such as the CYK algorithm.

## Greibach Normal Form

- A context-free grammar is in Greibach normal form if all of its production rules are of the form:

  - A → aα, where A is a nonterminal symbol, a is a terminal symbol, and α is a string of nonterminal symbols

- Any context-free grammar can be converted to an equivalent grammar in Greibach normal form by applying a series of transformations, such as eliminating left recursion, left factoring, and introducing new nonterminal symbols.
- Greibach normal form is useful for designing parsing algorithms, such as recursive-descent parsing, and for generating strings of a context-free language in a systematic way.