# 8. Develop an operator precedence parser for a given language.

- An operator precedence parser is a bottom-up parser that can parse a subset of context-free grammars, namely those that are operator precedence grammars.
- An operator precedence grammar is a grammar that has the following properties:
  - Every production is of the form `A -> w`, where `A` is a non-terminal and `w` is a string of terminals and/or non-terminals.
  - No production has an empty right-hand side, i.e., `w` is not empty.
  - There are no two distinct productions with the same non-terminal on the left-hand side and the same terminal on the right-hand side, i.e., if `A -> w` and `A -> x` are two productions, then `w` and `x` do not start with the same terminal.
  - For every pair of terminals `a` and `b`, there is a precedence relation between them, denoted by `a < b`, `a = b`, or `a > b`, which is consistent and transitive. The precedence relation determines the order of evaluation of the operators represented by the terminals.
- An operator precedence parser works as follows:
  - It uses a stack to store symbols (terminals and non-terminals) and an input buffer to store the remaining input string.
  - It scans the input from left to right and performs one of the following actions at each step:
    - Shift: If the top of the stack is `$` (the end-of-input marker) or has lower precedence than the next input symbol, push the next input symbol onto the stack and advance the input pointer.
    - Reduce: If the top of the stack has higher precedence than the next input symbol, pop symbols from the stack until a handle is found. A handle is a substring of the stack that matches the right-hand side of a production. Replace the handle by the corresponding left-hand side non-terminal and push it onto the stack.
    - Accept: If the stack contains only the start symbol and the input buffer contains only `$`, the parsing is successful and the parser halts.
    - Error: If none of the above actions can be performed, the parser reports an error and halts.
- An example of an operator precedence parser for a simple arithmetic language is given below:

  - The grammar of the language is:

    ```
    E -> E + E | E * E | (E) | id
    ```

  - The precedence relation of the terminals is:

    ```
    $ < id, (, +, *
    id > $, +, *, )
    ( < id, (, +, *
    ) > id, (, +, *, $
    + < id, (, +
    + > +, *, ), $
    * < id, (, *
    * > +, *, ), $
    ```

  - The parsing table for the grammar is:

    | Stack | Input | Action |
    | ----- | ----- | ------ |
    | $     | id + id * id $ | Shift |
    | $ id  | + id * id $ | Reduce by E -> id |
    | $ E   | + id * id $ | Shift |
    | $ E + | id * id $ | Shift |
    | $ E + id | * id $ | Reduce by E -> id |
    | $ E + E | * id $ | Reduce by E -> E + E |
    | $ E   | * id $ | Shift |
    | $ E * | id $ | Shift |
    | $ E * id | $ | Reduce by E -> id |
    | $ E * E | $ | Reduce by E -> E * E |
    | $ E   | $ | Accept |