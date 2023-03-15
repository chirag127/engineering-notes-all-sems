# BNF Notation for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- BNF stands for **Backus Naur Form** notation  .
- It is a **formal method** for describing the **syntax** of programming languages and other types of computer input    .
- The syntax means the **structure of strings** in a certain language.
- BNF was introduced by **John Bakus** and **Peter Naur** in 1960 .
- BNF and **CFG** (Context Free Grammar) are nearly identical.
- BNF uses the following symbols and conventions  :
  - **::=** means "is defined as".
  - **< >** enclose **non-terminal** symbols, which are placeholders for syntactic categories.
  - **|** means "or" and separates alternative definitions of a non-terminal.
  - **" "** enclose **terminal** symbols, which are literal strings or characters.
  - **[ ]** enclose optional parts of a definition.
  - **{ }** enclose parts of a definition that can be repeated zero or more times.
  - **( )** are used for grouping parts of a definition.
- For example, the following BNF defines a simple arithmetic expression language:

```
<expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>
<term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
<factor> ::= <number> | "(" <expression> ")"
<number> ::= <digit> | <number> <digit>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

- BNF can be extended with additional symbols and features, such as **comments**, **annotations**, **regular expressions**, **precedence**, and **associativity** .
- Some variants of BNF are **EBNF** (Extended Backus Naur Form), **ABNF** (Augmented Backus Naur Form), and **LBNF** (Labeled Backus Naur Form) .
- BNF is useful for **specifying**, **analyzing**, and **generating** programming languages and other types of computer input  .