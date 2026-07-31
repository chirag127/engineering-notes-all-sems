### BNF notation for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- BNF stands for **Backus Naur Form** notation .
- It is a **formal method** for describing the **syntax** of programming languages and other types of computer input  .
- The syntax means the **structure of strings** in a certain language.
- BNF was introduced by **John Bakus** and **Peter Naur** in 1960 .
- BNF is a type of **metasyntax** notation for **context-free grammars**.
- A context-free grammar is a set of **production rules** that generate strings belonging to a language.
- A production rule has the form **A ::= B**, where A is a **non-terminal symbol** and B is a **sequence of terminal and non-terminal symbols** .
- A terminal symbol is a **basic symbol** that cannot be further divided .
- A non-terminal symbol is a **placeholder** for a group of terminal or non-terminal symbols .
- The symbol **::=** means **is defined as** or **can be replaced by** .
- The symbol **|** means **or** and is used to separate **alternatives** in the right-hand side of a production rule .
- The symbol **< >** is used to enclose **non-terminal symbols** .
- The symbol **" "** is used to enclose **terminal symbols** .
- The symbol **ε** means **empty string** and is used to indicate that a non-terminal symbol can be replaced by nothing .
- An example of a BNF grammar for a simple arithmetic expression language is:

```
<expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>
<term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
<factor> ::= <number> | "(" <expression> ")"
<number> ::= <digit> | <number> <digit>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

- This grammar can generate strings such as:

```
2 + 3 * (4 - 5)
(1 + 2) * (3 + 4)
9 / 3 - 1
```

- BNF notation is useful for **specifying** the syntax of programming languages and other types of computer input, as well as for **parsing** and **compiling** them  .
- BNF notation has many **variants** and **extensions**, such as **Extended Backus Naur Form (EBNF)**, **Labeled Backus Naur Form (LBNF)**, and **Augmented Backus Naur Form (ABNF)** .
- These variants and extensions introduce additional symbols and features to make the notation more **expressive**, **concise**, and **readable** .