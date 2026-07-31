### BNF notation for the notes of the Unit 1 - Introduction to Compiler in the subject of Compiler Design

- BNF stands for **Backus Naur Form** notation . It is a form of notation used for specifying the **syntax** of programming languages and command sets . The syntax means the structure of strings in a certain language.
- BNF is a type of **metasyntax** notation for **context-free grammars** . A metasyntax is a syntax for defining syntaxes. A context-free grammar is a set of rules that describe how to generate strings from a given alphabet .
- BNF was introduced by **John Bakus** and **Peter Naur** in 1960 . It is also known as **Backus Normal Form** or **Backus Naur Form** .
- BNF uses the following symbols and conventions  :
  - **::=** means "is defined as" or "can be replaced by".
  - **< >** enclose **non-terminal symbols**, which are placeholders for syntactic categories or groups of strings.
  - **|** means "or" and separates alternative expansions of a non-terminal symbol.
  - **" "** enclose **terminal symbols**, which are literal symbols or characters that appear in the language.
  - **[ ]** enclose optional parts of a production rule.
  - **{ }** enclose parts of a production rule that can be repeated zero or more times.
  - **( )** are used for grouping symbols or expressions.
  - **;** is used to terminate a production rule.
- For example, the following BNF notation defines the syntax of a simple arithmetic expression language :

```
<expression> ::= <term> | <expression> "+" <term> | <expression> "-" <term>;
<term> ::= <factor> | <term> "*" <factor> | <term> "/" <factor>;
<factor> ::= <number> | "(" <expression> ")";
<number> ::= <digit> | <number> <digit>;
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";
```

- This means that an expression can be a term, or an expression followed by a plus or minus sign and another term. A term can be a factor, or a term followed by a multiplication or division sign and another factor. A factor can be a number, or an expression enclosed in parentheses. A number can be a digit, or a number followed by another digit. A digit can be any of the symbols from 0 to 9.