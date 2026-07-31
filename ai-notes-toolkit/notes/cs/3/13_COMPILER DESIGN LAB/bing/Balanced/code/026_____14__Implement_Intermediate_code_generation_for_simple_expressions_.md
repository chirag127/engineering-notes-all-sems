### 14. Implement Intermediate code generation for simple expressions.

Intermediate code generation is the process of translating the source code into an intermediate representation that is easier to manipulate and optimize than the original code. Intermediate code can be in various forms, such as abstract syntax trees, three-address code, quadruples, triples, or stack machine code.

To implement intermediate code generation for simple expressions, we can use the following steps:

- Parse the source code and construct an abstract syntax tree (AST) that represents the structure and meaning of the expression.
- Traverse the AST in a post-order fashion and generate intermediate code for each node. For example, if the node is a binary operator, generate code that evaluates its operands and applies the operator. If the node is a variable or a constant, generate code that loads its value.
- Optionally, apply some optimizations to the intermediate code, such as constant folding, algebraic simplification, or common subexpression elimination.
- Output the intermediate code in the desired format.

Here is an example of intermediate code generation for the simple expression `a + b * c - d / e`:

- The AST for the expression is:

```
    -
   / \
  +   /
 / \ / \
a  * d  e
   / \
  b   c
```

- The intermediate code in three-address code form is:

```
t1 = b * c
t2 = d / e
t3 = a + t1
t4 = t3 - t2
```

- The intermediate code in quadruples form is:

```
( * , b , c , t1 )
( / , d , e , t2 )
( + , a , t1 , t3 )
( - , t3 , t2 , t4 )
```

- The intermediate code in triples form is:

```
( * , b , c )
( / , d , e )
( + , a , (0) )
( - , (2) , (1) )
```

- The intermediate code in stack machine code form is:

```
push b
push c
mul
push d
push e
div
push a
swap
add
sub
```