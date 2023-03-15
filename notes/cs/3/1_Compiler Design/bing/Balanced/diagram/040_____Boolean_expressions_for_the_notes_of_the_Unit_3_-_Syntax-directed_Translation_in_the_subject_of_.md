### Boolean expressions for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Boolean expressions are expressions that evaluate to either true or false values, such as `x > y`, `a && b`, `!c`, etc.
- Boolean expressions are used to control the flow of execution of conditional statements, such as `if-else` and `while-do`, and to generate intermediate code for them.
- Syntax-directed translation is a technique to associate semantic actions with the grammar rules of a language and to execute them during parsing.
- Syntax-directed translation can be done by constructing a parse tree or a syntax tree and computing the values of attributes at the nodes of the tree by visiting them in some order, such as depth-first or breadth-first.
- Syntax-directed translation can also be done by embedding the semantic actions within the grammar rules and executing them during parsing, without building an explicit tree. This is called a syntax-directed translation scheme.
- A syntax-directed translation scheme can be represented by augmenting the grammar rules with semantic actions enclosed in curly braces, such as `S -> if E then S1 { action1 } | if E then S1 else S2 { action2 } | while E do S1 { action3 }`.
- The semantic actions can be used to generate intermediate code, such as three-address code, for the boolean expressions and the control statements, by using temporary variables, labels, and jumps.
- For example, the following grammar rule and semantic action can be used to generate three-address code for a boolean expression involving the `&&` operator:

```
E -> E1 && E2 { E.true = newlabel();
                E.false = E2.false;
                E.code = E1.code || label(E1.true) || E2.code;
              }
```

- The semantic action creates a new label for the true branch of the boolean expression, assigns it to the attribute `E.true`, and copies the attribute `E2.false` to the attribute `E.false`.
- The semantic action also concatenates the code segments of `E1` and `E2`, and inserts a label statement for the true branch of `E1` in between.
- The resulting code segment for `E` will look something like this:

```
E1.code
if E1.addr == false goto E.false
label(E1.true)
E2.code
if E2.addr == false goto E.false
E.true: ...
```

- The code segment evaluates the subexpressions `E1` and `E2` and jumps to the false branch of `E` if either of them is false, otherwise it continues to the true branch of `E`.
- Similarly, other grammar rules and semantic actions can be defined for other boolean operators and control statements, such as `||`, `!`, `if-else`, and `while-do`.