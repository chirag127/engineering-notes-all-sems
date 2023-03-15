### Boolean expressions for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Boolean expressions are expressions that evaluate to either true or false values, such as `x > y`, `a && b`, or `!c`.
- Boolean expressions are used to control the flow of execution of conditional statements, such as `if-else` and `while-do`, and to generate intermediate code for them.
- Syntax-directed translation is a technique to attach semantic actions to the grammar rules of a language and to perform them during parsing.
- Syntax-directed translation can be done by constructing a parse tree or a syntax tree and computing the values of attributes at the nodes of the tree by visiting them in some order, such as depth-first or breadth-first.
- Syntax-directed translation can also be done by embedding the semantic actions within the grammar rules and performing them during parsing, without building an explicit tree. This is called a syntax-directed translation scheme.
- A syntax-directed translation scheme can be used to evaluate the order of semantic rules and to generate intermediate code for boolean expressions and control statements.
- For example, consider the following grammar for boolean expressions:

```
E -> E1 or E2
E -> E1 and E2
E -> not E1
E -> (E1)
E -> true
E -> false
```

- A syntax-directed translation scheme for this grammar can be written as follows, where `||` denotes concatenation, `newlabel()` generates a new label, and `emit()` generates a three-address code:

```
E -> E1 or {E.true = newlabel();
            E.false = E2.false;
            emit('goto' || E.true);
            emit(E1.false || ':');} E2
E -> E1 and {E.true = E2.true;
             E.false = newlabel();
             emit('goto' || E.false);
             emit(E1.true || ':');} E2
E -> not {E.true = E1.false;
          E.false = E1.true;} E1
E -> (E1) {E.true = E1.true;
           E.false = E1.false;}
E -> true {E.true = newlabel();
           E.false = 0;
           emit(E.true || ':');}
E -> false {E.true = 0;
            E.false = newlabel();
            emit(E.false || ':');}
```

- The translation scheme generates intermediate code that uses labels to jump to the true or false branches of the boolean expression, depending on the evaluation of the subexpressions.
- The translation scheme can be extended to handle control statements, such as `if-else` and `while-do`, by using the following grammar rules and semantic actions:

```
S -> if E then S1
S -> if E then S1 else S2
S -> while E do S1

S -> if E then {S.next = newlabel();
                emit('goto' || S.next);
                emit(E.false || ':');} S1
S -> if E then {S.next = newlabel();
                emit('goto' || S.next);
                emit(E.false || ':');} S1 else {emit(E.true || ':');} S2
S -> while {S.begin = newlabel();
            emit(S.begin || ':');} E do {emit('goto' || S.begin);
                                         emit(E.false || ':');
                                         S1.next = S.begin;} S1
```

- The translation scheme generates intermediate code that uses labels to jump to the beginning or the end of the loop, or to the then or else branch of the conditional statement, depending on the evaluation of the boolean expression.