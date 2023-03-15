### Normal Forms for grammar for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing

Grammar is the set of rules that define the structure of a language. In natural language processing, it is essential to analyze and understand the structure of a sentence to perform tasks such as sentiment analysis, machine translation, and text summarization. To achieve this, we need to convert the grammar into a standard form, which is called a normal form. In this section, we will discuss the various normal forms for grammar.

#### Chomsky Normal Form (CNF)

Chomsky Normal Form is a type of grammar normalization in which all the productions of a grammar are in one of the following forms:

1. A → BC
2. A → a
3. S → ε

where A, B, and C are non-terminal symbols, a is a terminal symbol, and S is the start symbol. In CNF, all productions are binary and have only one non-terminal on the right-hand side, except for the production that generates the empty string (ε). CNF is useful for parsing algorithms like the CYK algorithm, which requires a grammar in CNF.

Mnemonic: "Chomsky Normal Form has two rules: Binary and Terminal."

#### Greibach Normal Form (GNF)

Greibach Normal Form is another type of grammar normalization in which all the productions of a grammar are in the following form:

1. A → aα

where A is a non-terminal symbol, a is a terminal symbol, and α is a string of non-terminal symbols. In GNF, all productions are left-recursive, which means the left-hand side of a production is always a non-terminal symbol. GNF is useful for some parsing algorithms, such as the Earley parser.

Mnemonic: "Greibach Normal Form has one rule: Left-Recursive."

#### Proofs

To convert a grammar to CNF, we need to follow the following steps:

1. Remove all ε-productions.
2. Remove all unit productions (A → B).
3. Replace all non-binary productions with binary productions.
4. Replace all terminals with new non-terminals.

To convert a grammar to GNF, we need to follow the following steps:

1. Remove all ε-productions.
2. Remove all unit productions (A → B).
3. Remove all non-left-recursive productions.
4. Replace all non-terminals with new non-terminals.

#### Advantages and Disadvantages

The advantages of normalizing a grammar are that it simplifies the parsing process and makes it more efficient. Normalized grammars also have unique parse trees, which makes it easier to analyze and compare different grammars. However, the disadvantage of normalization is that it can increase the size of the grammar, which can lead to slower parsing times.

#### Example

Consider the following grammar:

```
S → AB | BC | a
A → BA | a
B → CC | b
C → AB | a
```

To convert this grammar to CNF, we need to apply the following steps:

1. Remove ε-productions: None in this grammar.
2. Remove unit productions: None in this grammar.
3. Replace non-binary productions with binary productions:

```
S → DE | FG | a
A → DH | a
B → II | b
C → DE | a
D → A | C
E → B
F → B
G → C
H → D
I → C
```

4. Replace terminals with new non-terminals:

```
S → AA1 | BB1 | a
A → AA2 | a
B → CC1 | b
C → AA3 | a
D → A | C
E → B
F → B
G → C
H → D
I → C
AA1 → DE
AA2 → DH
BB1 → FG
CC1 → II
AA3 → DE
```

The resulting grammar is now in CNF.

#### Applications

Normalized grammars are used in various natural language processing tasks, such as parsing, machine translation, and text-to-speech synthesis. They are also used in computer science and programming language theory, such as in the design and implementation of programming languages.