### Normal Forms for Grammar for the Notes of the Unit 3 - Syntactic Analysis in the Subject of Natural Language Processing

In Natural Language Processing, one of the primary tasks is to analyze the grammatical structure of a sentence. It is crucial to represent the structure of sentences in a systematic and organized way for further processing. Normal Forms for Grammar is a set of rules that helps in transforming the sentence structure into a standard form.

There are four types of Normal Forms for Grammar:

1. Chomsky Normal Form (CNF)
2. Greibach Normal Form (GNF)
3. Binary Normal Form (BNF)
4. Extended Backus-Naur Form (EBNF)

Let's discuss each of them in detail:

#### 1. Chomsky Normal Form (CNF)

Chomsky Normal Form is a type of grammar in which all the production rules are in one of the two forms:

1. A -> BC
2. A -> a

Where A, B, and C are non-terminal symbols, and 'a' is a terminal symbol.

Mnemonic: CNF can be remembered as "Chomsky's Nice Form," where every production rule has either one non-terminal symbol or two non-terminal symbols.

#### 2. Greibach Normal Form (GNF)

Greibach Normal Form is a type of grammar in which all the production rules are in the form:

1. A -> aB1B2...Bn

Where A is a non-terminal symbol, a is a terminal symbol, and B1B2...Bn are non-terminal symbols.

Mnemonic: GNF can be remembered as "Greibach's Neat Form," where every production rule has a terminal symbol at the beginning.

#### 3. Binary Normal Form (BNF)

Binary Normal Form is a type of grammar in which all the production rules are in one of the two forms:

1. A -> BC
2. A -> a

Where A, B, and C are non-terminal symbols, and 'a' is a terminal symbol. In addition, all the production rules have at most two non-terminal symbols.

Mnemonic: BNF can be remembered as "Binary's Nice Form," where every production rule has at most two non-terminal symbols.

#### 4. Extended Backus-Naur Form (EBNF)

Extended Backus-Naur Form is a type of grammar that extends the Backus-Naur Form (BNF) by adding some additional features like repetition, optionality, grouping, etc. It is used to represent complex grammars.

Mnemonic: EBNF can be remembered as "Extended's Best Notation Form," where it is used to represent complex grammars.

Advantages of Normal Forms for Grammar:

1. It helps in reducing the ambiguity in the sentence structure.
2. It simplifies the processes of parsing and generating sentences.
3. It makes the grammatical structure of sentences more understandable and organized.

Disadvantages of Normal Forms for Grammar:

1. It is time-consuming to transform the sentence structure into a standard form.
2. It may lead to the loss of information in some cases.

Examples:

1. Chomsky Normal Form: S -> AB, A -> a, B -> b
2. Greibach Normal Form: S -> aB, B -> bC, C -> cD, D -> d
3. Binary Normal Form: S -> AB, A -> CD, B -> EF, C -> a, D -> b, E -> c, F -> d
4. Extended Backus-Naur Form: <expression> ::= <term> {('+'|'-') <term>}*

Applications:

1. Natural Language Processing
2. Compiler Design
3. Syntax Analysis in Computer Science

In conclusion, Normal Forms for Grammar is a set of rules that helps in transforming the sentence structure into a standard form. It is crucial in Natural Language Processing and other fields of computer science, where analyzing the grammatical structure of sentences is required.