### Boolean expressions for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Boolean expressions are expressions that evaluate to either true or false values, such as `x > y`, `a && b`, or `!c`.
- Boolean expressions are used as conditions for control statements, such as `if`, `else`, `while`, or `do-while`, that change the flow of execution of statements.
- The translation of boolean expressions is associated with the translation of control statements, which can be done using syntax-directed translation .
- Syntax-directed translation is a method of translating the source code into intermediate code or target code by using the syntax and semantic information of the source language.
- Syntax-directed translation can be done by constructing a parse tree or a syntax tree and computing the values of attributes at the nodes of the tree by visiting them in some order.
- A syntax-directed translation scheme is a context-free grammar with semantic actions embedded within production bodies. The semantic actions are executed when the corresponding production is used during parsing.
- A syntax-directed translation scheme can be used to evaluate the order of semantic rules for boolean expressions and control statements.
- An example of a syntax-directed translation scheme for boolean expressions and control statements is given below:

```
S -> if E then S1 | if E then S1 else S2 | while E do S1
E -> E1 or E2 { E.true = newlabel(); E.false = E2.false;
                gen(E1.true 'goto' E.true);
                gen('goto' E1.false);
                gen(E.true ':'); }
  | E1 and E2 { E.true = E2.true; E.false = newlabel();
                gen('goto' E1.true);
                gen(E1.false ':');
                gen('goto' E.false); }
  | not E1 { E.true = E1.false; E.false = E1.true; }
  | ( E1 ) { E.true = E1.true; E.false = E1.false; }
  | id relop id { E.true = newlabel(); E.false = newlabel();
                  gen('if' id1.lexval relop.lexval id2.lexval 'goto' E.true);
                  gen('goto' E.false); }
```