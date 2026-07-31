### BNF Notation

- BNF (Backus-Naur Form) notation is a formal mathematical way to describe a language.
- It is used to define the syntax of programming languages, command sets, and document formats.
- BNF notation uses a set of production rules to describe the structure of valid strings in a language.
- Each production rule consists of a non-terminal symbol, followed by the symbol "::=", followed by a sequence of terminal and non-terminal symbols.
- Non-terminal symbols represent syntactic categories, while terminal symbols represent the actual characters or tokens in the language.
- The start symbol is the non-terminal symbol that represents the entire language.
- A valid string in the language can be derived by starting with the start symbol and repeatedly applying production rules until only terminal symbols remain.
- BNF notation is widely used in the design of compilers and interpreters for programming languages.

Example:

```
<expression> ::= <term> | <expression> "+" <term>
<term> ::= <factor> | <term> "*" <factor>
<factor> ::= <number> | "(" <expression> ")"
<number> ::= <digit> | <number> <digit>
<digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

In this example, the start symbol is `<expression>`, and the production rules define the syntax of simple arithmetic expressions consisting of numbers, parentheses, and the operators `+` and `*`. The terminal symbols are the digits `0` through `9`, the parentheses `(` and `)`, and the operators `+` and `*`. The non-terminal symbols are `<expression>`, `<term>`, `<factor>`, `<number>`, and `<digit>`. A valid string in this language could be `"(1+2)*3"`, which can be derived from the start symbol `<expression>` by applying the production rules in the following sequence: `<expression>` -> `<term>` -> `<factor>` -> `"("` `<expression>` `")"` -> `"("` `<expression>` `"+"` `<term>` `")"` -> `"("` `<term>` `"+"` `<term>` `")"` -> `"("` `<factor>` `"+"` `<factor>` `")"` -> `"("` `<number>` `"+"` `<number>` `")"` -> `"("` `<digit>` `"+"` `<digit>` `")"` -> `"("` `"1"` `"+"` `"2"` `")"` -> `"("` `"1"` `"+"` `"2"` `")"` `*` `<factor>` -> `"("` `"1"` `"+"` `"2"` `")"` `*` `<number>` -> `"("` `"1"` `"+"` `"2"` `")"` `*` `<digit>` -> `"("` `"1"` `"+"` `"2"` `")"` `*` `"3"` -> `"(1+2)*3"`.