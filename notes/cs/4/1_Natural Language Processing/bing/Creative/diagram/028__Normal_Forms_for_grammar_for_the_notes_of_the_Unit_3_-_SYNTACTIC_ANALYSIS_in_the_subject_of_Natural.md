Normal Forms for grammar are ways of simplifying the rules of a context-free grammar to make it easier to parse or analyze. There are two common normal forms: Chomsky Normal Form and Greibach Normal Form. 

Chomsky Normal Form (CNF) is a normal form where all the production rules are of the form:

- A -> BC, where A, B, and C are nonterminal symbols
- A -> a, where A is a nonterminal symbol and a is a terminal symbol
- S -> ε, where S is the start symbol and ε is the empty string

Greibach Normal Form (GNF) is a normal form where all the production rules are of the form:

- A -> aβ, where A is a nonterminal symbol, a is a terminal symbol, and β is a string of nonterminal symbols

Every context-free grammar that does not contain the empty string can be transformed into an equivalent grammar in CNF or GNF.

The following diagram illustrates the basic architecture of a context-free grammar and its normal forms using ASCII art:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Context-free    |    | Chomsky Normal  |    | Greibach Normal |
| Grammar         |    | Form            |    | Form            |
|                 |    |                 |    |                 |
| A -> X1 X2 ... Xn|    | A -> BC         |    | A -> aβ         |
| A -> a          |    | A -> a          |    |                 |
| A -> ε          |    | S -> ε          |    |                 |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +---------------------->                      |
       |                      |                      |
       |                      +---------------------->
       |                      |                      |
       |                      |                      |
       +-------------------------------------------->
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Input String    |    | Input String    |    | Input String    |
|                 |    |                 |    |                 |
| w = a1 a2 ... an|    | w = a1 a2 ... an|    | w = a1 a2 ... an|
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```