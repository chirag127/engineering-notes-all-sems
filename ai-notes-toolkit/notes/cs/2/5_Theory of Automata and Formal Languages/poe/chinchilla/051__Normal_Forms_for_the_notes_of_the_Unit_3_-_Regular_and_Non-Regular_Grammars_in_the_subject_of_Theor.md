### Normal Forms for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

In the study of formal languages and automata theory, it is essential to understand the concept of normal forms for grammars. Normal forms for grammars are a set of rules that transform a grammar into a standard form, making it easier to analyze and work with. In this unit, we will cover the following normal forms for regular and non-regular grammars:

#### Normal forms for Regular Grammars

1. Right-Linear Grammar Normal Form (RLGNF): A right-linear grammar is a regular grammar in which all production rules are of the form A → aB or A → a, where A and B are non-terminals and a is a terminal symbol. The RLGNF is a normal form for regular grammars that ensures all production rules are in this form.

2. Left-Linear Grammar Normal Form (LLGNF): A left-linear grammar is a regular grammar in which all production rules are of the form A → Ba or A → a, where A and B are non-terminals and a is a terminal symbol. The LLGNF is a normal form for regular grammars that ensures all production rules are in this form.

3. Regular Grammar Normal Form (RGNF): A regular grammar in RGNF has the following properties:
   - All productions are of the form A → aB or A → a, where A and B are non-terminals and a is a terminal symbol.
   - The start variable S only appears in productions of the form S → ε or S → aB, where a is a terminal symbol and B is a non-terminal.

#### Normal forms for Non-Regular Grammars

1. Chomsky Normal Form (CNF): In CNF, each production rule is in one of the two forms:
   - A → BC, where A, B, and C are non-terminals
   - A → a, where A is a non-terminal and a is a terminal symbol
   The CNF ensures that every non-terminal can generate a string of either two non-terminals or a single terminal symbol.

2. Greibach Normal Form (GNF): In GNF, each production rule is of the form A → aα, where A is a non-terminal, a is a terminal symbol, and α is a string of non-terminals and/or terminals. The GNF ensures that every production starts with a terminal symbol.

Understanding and applying these normal forms can help in simplifying the analysis and manipulation of grammars. It can also aid in the conversion of grammars to automata or vice versa.