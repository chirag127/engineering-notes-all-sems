### Using ambiguous grammars for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- An **ambiguous grammar** is a grammar that can generate more than one **leftmost derivation** or **rightmost derivation** for the same sentence .
- An ambiguous grammar can also produce more than one **parse tree** for the same sentence, implying different meanings or structures.
- Ambiguous grammars are undesirable for programming languages, because they can cause **conflicts** in the parsing process and lead to **undecidability** or **inconsistency** in the semantics.
- Some examples of ambiguous grammars are:

  - The grammar for arithmetic expressions with **left-associative** operators `+` and `*`:

    ```
    E -> E + E
    E -> E * E
    E -> id
    ```

    This grammar is ambiguous because it can generate two different parse trees for the sentence `id + id * id`:

    ```
         E                  E
        /|\                /|\
       / | \              / | \
      E  +  E            E  +  E
     / \    |           /   /|\
    /   \   E          /   / | \
    id  id  id        id  E  *  E
                      / \    / \
                     /   \  id id
                    id  id
    ```

    The left parse tree implies that the expression is evaluated as `(id + id) * id`, while the right parse tree implies that it is evaluated as `id + (id * id)`.

  - The grammar for the `if-then-else` statement:

    ```
    S -> if E then S [else S]
    S -> other
    ```

    This grammar is ambiguous because it can generate two different parse trees for the sentence `if E1 then if E2 then S1 else S2`:

    ```
          S                     S
         / \                   / \
        /   \                 /   \
       if   S                if   S
      /|\   |               /|\   |
     / | \  |              / | \  |
    E1 then S             E1 then S
         / \              / \    / \
        /   \            /   \  /   \
       if   S           if   S else S2
      /|\   |          /|\   |
     / | \  |         / | \  |
    E2 then S1       E2 then S1
    ```

    The left parse tree implies that the `else` clause belongs to the inner `if` statement, while the right parse tree implies that it belongs to the outer `if` statement.

- To handle ambiguous grammars, there are some possible remedies:

  - **Restructuring** the grammar to eliminate the ambiguity, such as adding parentheses or separators to the expressions or statements .
  - **Using precedence and associativity rules** to resolve the conflicts in the parsing table, such as giving higher precedence to `*` than `+` and making them left-associative.
  - **Using semantic actions** to attach additional information or constraints to the grammar rules, such as specifying the scope or binding of the `else` clause.
  - **Using disambiguation algorithms** to select a unique parse tree from the set of possible parse trees, such as the **longest match** or **minimal cost** criteria.