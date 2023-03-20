 Here is the formal content in Markdown format without any emotions or external links:

## Unit 3 - Regular and Non-Regular Grammars

1. Regular Grammars: Grammars in which all production rules are of the form:

A → a

A → aB

A → aB | ε

Where A, B are non-terminals and a is a terminal.

These grammars can generate regular languages which can be recognized by finite state automata.

2. Non-regular Grammars: Grammars that contain at least one of the following productions:

A → aAa

A → aB | a

Where A and B are non-terminals and a is a terminal.

These grammars can generate non-regular languages which cannot be recognized by finite state automata. Some examples arepalindrome languages, intersection of languages, complement of a language, etc.

3. Differences between regular and non-regular grammars:

Regular Grammars:

- All rules are of the form: A → a, A → aB, A → a | ε
- Generates regular languages
- Can be recognized by finite state automata

Non-Regular Grammars:

- Contains recursive rules like: A → aAa
- Generates non-regular languages
- Cannot be recognized by finite state automata
- Requires pushdown automata or Turing machines for recognition

4. Applications: Regular grammars and expressions are commonly used to define patterns in text processing and lexical analysis. Non-regular grammars are required to generate programming languages and natural languages which contain self-reference and ambiguity.