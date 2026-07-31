### Postfix Translation

- Postfix translation is a technique of generating intermediate code in compiler design that uses a syntax-directed translation scheme with semantic actions at the end of the productions .
- Postfix translation is also known as postfix syntax-directed translation or postfix SDT.
- Postfix translation produces intermediate code in postfix notation, which is a way of writing expressions where the operator appears after the operands.
- Postfix notation is also called reverse Polish notation or RPN.
- Postfix notation has the advantage of being easy to evaluate by a stack machine, as it does not require parentheses or precedence rules.
- Postfix translation can be achieved by factoring the productions to eliminate left recursion and left factoring, and by inserting semantic actions to generate the intermediate code .
- Postfix translation can be implemented by using a bottom-up parser, such as a shift-reduce parser, or by using a top-down parser, such as a recursive-descent parser .
- Postfix translation can be illustrated by the following example :

  - Given the grammar for arithmetic expressions:

    ```
    E → E + T | T
    T → T * F | F
    F → (E) | id
    ```

  - The postfix translation scheme is obtained by factoring the grammar and adding semantic actions:

    ```
    E → TE'
    E' → +TE' {print('+')} | ε
    T → FT'
    T' → *FT' {print('*')} | ε
    F → (E) | id {print(id.lexeme)}
    ```

  - The postfix translation scheme can generate the following intermediate code for the input expression `a * (b + c)`:

    ```
    a
    b
    c
    +
    *
    ```