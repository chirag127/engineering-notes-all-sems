### BNF notation for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- BNF stands for **Backus Naur Form** notation . It is a form of notation used for specifying the **syntax** of programming languages and command sets . The syntax means the structure of strings in a certain language.
- BNF is a type of **metasyntax** notation, which means it is a syntax for describing syntax. It is also a type of **context-free grammar** (CFG), which means it can generate strings that are not dependent on the previous symbols.
- BNF uses the following symbols and conventions:
  - **::=** means "is defined as" or "can be replaced by".
  - **< >** enclose **non-terminal symbols**, which are placeholders for other symbols or sequences of symbols.
  - **|** means "or" and separates alternative choices for a non-terminal symbol.
  - **" "** enclose **terminal symbols**, which are the basic symbols of the language and cannot be further replaced.
  - **[ ]** enclose optional symbols or sequences of symbols.
  - **{ }** enclose symbols or sequences of symbols that can be repeated zero or more times.
  - **( )** group symbols or sequences of symbols together.
- For example, the following BNF notation defines the syntax of a simple arithmetic expression:

```
<expression> ::= <term> | <term> "+" <expression> | <term> "-" <expression>
<term> ::= <factor> | <factor> "*" <term> | <factor> "/" <term>
<factor> ::= <number> | "(" <expression> ")"
<number> ::= <digit> | <digit> <number>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

- This BNF notation can be used to generate valid strings such as "3+4", "(2*5)-1", or "6/(3+3)".
- BNF notation is useful for describing the syntax of programming languages in a precise and unambiguous way. It can also be used to create parsers, which are programs that check if a given string conforms to the syntax of a language and convert it into a meaningful structure .