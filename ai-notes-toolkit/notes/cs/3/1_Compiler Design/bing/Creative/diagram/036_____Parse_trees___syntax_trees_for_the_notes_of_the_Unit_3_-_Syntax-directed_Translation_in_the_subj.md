### Parse trees and syntax trees

- Parse trees and syntax trees are data structures that represent the syntactic structure of a source code in compiler design.
- A parse tree is created by a parser, which is a component of a compiler that processes the source code and checks it for syntactic correctness .
- A syntax tree is an abstract or compact representation of a parse tree, which omits some details that are not relevant for semantic analysis . They are also called as abstract syntax trees (ASTs).
- Parse trees and syntax trees are used for different tasks in compiler design. Parse trees are used for syntax checking, error recovery, and code generation. Syntax trees are used for semantic analysis, intermediate code generation, and code optimization.
- Parse trees and syntax trees have different shapes and sizes. Parse trees are usually larger and more detailed than syntax trees, as they include all the terminals and non-terminals of the grammar. Syntax trees are usually smaller and simpler than parse trees, as they only include the essential syntactic information.
- Parse trees and syntax trees can be represented using different notations, such as bracketed notation, tree diagrams, or graphical notation. For example, consider the following arithmetic expression:

```
a + b * c
```

- The parse tree for this expression using bracketed notation is:

```
(E (E (T (F a))) + (T (F b) * (F c)))
```

- The syntax tree for this expression using bracketed notation is:

```
(+ a (* b c))
```

- The parse tree for this expression using tree diagrams is:

```
       E
      / \
     E   T
    / \ / \
   T  + F  F
  /  / \  / \
 F  b  * c  a
/  / \    / \
a b  c    a
```

- The syntax tree for this expression using tree diagrams is:

```
    +
   / \
  a   *
     / \
    b   c
```

- The parse tree for this expression using graphical notation is:

![Parse tree](https://www.geeksforgeeks.org/wp-content/uploads/Parse-Tree-1.png)

- The syntax tree for this expression using graphical notation is:

![Syntax tree](https://www.gatevidyalay.com/wp-content/uploads/2018/11/Syntax-Tree-Example-1.png)