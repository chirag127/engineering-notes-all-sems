# Postfix Translation

- Postfix translation is a technique of generating intermediate code for a given source program in a compiler.
- Postfix translation uses a syntax-directed translation scheme (SDT) that has its semantic actions at the end of the production rules in the context-free grammar (CFG) of the source language.
- Postfix translation produces a postfix notation of the source program, which is also known as reverse Polish notation (RPN).
- Postfix notation is a way of writing expressions without using parentheses or precedence rules, where the operator appears after the operands.
- Postfix notation is easier to evaluate by a stack-based machine, as it does not require any backtracking or lookahead.
- Postfix translation can be achieved by factoring the production rules of the CFG to eliminate left recursion and left factoring, and then attaching the semantic actions to the rightmost symbols in the right-hand side (RHS) of the production rules.
- Postfix translation can also be implemented by using a bottom-up parser, such as a shift-reduce parser, that performs the semantic actions whenever a handle is reduced.
- Postfix translation can be illustrated by the following example:

  - Given the source expression: `a * d - (b + c)`
  - The CFG for the expression language is:

    ```
    E -> E - T | T
    T -> T * F | F
    F -> (E) | id
    ```

  - The SDT for postfix translation is:

    ```
    E -> E - T {print('-')} | T
    T -> T * F {print('*')} | F
    F -> (E) | id {print(id.lexeme)}
    ```

  - The postfix notation for the expression is: `a d * b c + -`
  - The derivation of the postfix notation is:

    ```
    E -> E - T {print('-')}
      -> T - T {print('-')}
      -> T * F - T {print('-'); print('*')}
      -> F * F - T {print('-'); print('*')}
      -> id * F - T {print('-'); print('*'); print(id.lexeme)}
      -> a * F - T {print('-'); print('*'); print('a')}
      -> a * F * F - T {print('-'); print('*'); print('*')}
      -> a * (E) * F - T {print('-'); print('*'); print('*')}
      -> a * (E - T) * F - T {print('-'); print('*'); print('*'); print('-')}
      -> a * (T - T) * F - T {print('-'); print('*'); print('*'); print('-')}
      -> a * (T * F - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*')}
      -> a * (F * F - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*')}
      -> a * (id * F - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print(id.lexeme)}
      -> a * (b * F - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b')}
      -> a * (b * id - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print(id.lexeme)}
      -> a * (b * c - T) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c')}
      -> a * (b * c - F) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c')}
      -> a * (b * c - id) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c'); print(id.lexeme)}
      -> a * (b * c - d) * F - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c'); print('d')}
      -> a * (b * c - d) * id - T {print('-'); print('*'); print('*'); print('-'); print('*'); print('b'); print('c'); print('