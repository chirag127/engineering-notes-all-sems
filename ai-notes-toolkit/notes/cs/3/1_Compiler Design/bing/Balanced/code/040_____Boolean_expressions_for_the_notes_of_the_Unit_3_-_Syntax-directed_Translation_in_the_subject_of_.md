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

- A syntax-directed translation scheme for this grammar can be written as follows, where `||` denotes concatenation, `newlabel()` generates a new label, and `emit()` outputs a line of intermediate code:

```
E -> E1 or {E.true = newlabel();
            E.false = E2.false;
            emit(E1.false || ': ' || E.true);}
     E2
E -> E1 and {E.true = E2.true;
             E.false = newlabel();
             emit(E1.true || ': ' || E.false);}
      E2
E -> not {E.true = E1.false;
          E.false = E1.true;}
     E1
E -> (E1) {E.true = E1.true;
           E.false = E1.false;}
E -> true {E.true = newlabel();
           E.false = 'fall';
           emit(E.true || ':');}
E -> false {E.true = 'fall';
            E.false = newlabel();
            emit(E.false || ':');}
```

- The translation scheme generates intermediate code in three-address form, where each instruction has at most three operands and one operator.
- The translation scheme uses labels to mark the entry and exit points of the code blocks for each boolean expression.
- The translation scheme uses short-circuit evaluation, where the evaluation of a boolean expression stops as soon as its value is determined. For example, `E1 or E2` is true if `E1` is true, and `E1 and E2` is false if `E1` is false.
- The translation scheme also uses the fall-through technique, where the control falls through to the next instruction if a condition is not satisfied. For example, `E.true = 'fall'` means that if `E` is true, the control goes to the next instruction without a jump. This reduces the number of jumps and labels in the intermediate code.