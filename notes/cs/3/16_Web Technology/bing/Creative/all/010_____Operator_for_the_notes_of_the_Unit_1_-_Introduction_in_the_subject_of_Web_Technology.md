# Operator

An operator is a symbol that represents an action or process on one or more operands. Operands are the values or variables that are manipulated by operators. Operators are used to perform specific mathematical and logical computations on operands. In other words, we can say that an operator operates the operands.

Operators are the backbone of any program and they are used for everything from very simple functions like counting to complex operations like encryption.

## Types of Operators

There are different types of operators in web technology, depending on the language and the purpose. Some of the common types of operators are:

- Arithmetic operators: These operators are used to perform basic mathematical operations like addition, subtraction, multiplication, division, modulus, exponentiation, etc. For example, `+`, `-`, `*`, `/`, `%`, `**`, etc.
- Assignment operators: These operators are used to assign a value to a variable or a property. For example, `=`, `+=`, `-=`, `*=`, `/=`, etc.
- Comparison operators: These operators are used to compare two operands and return a boolean value (true or false) based on the result of the comparison. For example, `==`, `===`, `!=`, `!==`, `<`, `>`, `<=`, `>=`, etc.
- Logical operators: These operators are used to combine two or more boolean expressions and return a boolean value based on the logical operation. For example, `&&`, `||`, `!`, etc.
- Bitwise operators: These operators are used to perform operations on the binary representation of the operands. They are useful for low-level programming and manipulating bits. For example, `&`, `|`, `^`, `~`, `<<`, `>>`, etc.
- String operators: These operators are used to perform operations on strings, such as concatenation, slicing, searching, etc. For example, `+`, `+=`, `[]`, `indexOf()`, `slice()`, etc.
- Conditional operators: These operators are used to evaluate a condition and return one of two possible values based on the result of the condition. For example, `? :`, `??`, etc.
- Unary operators: These operators are used to perform an operation on a single operand. For example, `++`, `--`, `typeof`, `delete`, etc.
- Ternary operators: These operators are used to perform an operation on three operands. For example, `? :`, etc.

## Operator Precedence

Operator precedence determines how operators are parsed concerning each other. Operators with higher precedence become the operands of operators with lower precedence. For example, in the expression `a + b * c`, the multiplication operator (`*`) has higher precedence than the addition operator (`+`), so the expression is evaluated as `a + (b * c)`.

Operator precedence can be overridden by using parentheses to group the operands. For example, in the expression `(a + b) * c`, the parentheses force the addition operator (`+`) to be evaluated before the multiplication operator (`*`), so the expression is evaluated as `(a + b) * c`.

The following table shows the operator precedence in JavaScript, from highest to lowest:

| Precedence | Operator type | Operators |
| --- | --- | --- |
| 21 | Grouping | `( ... )` |
| 20 | Member Access | `... . ...` |
| 20 | Computed Member Access | `... [ ... ]` |
| 20 | new (with argument list) | `new ... ( ... )` |
| 20 | Function Call | `... ( ... )` |
| 20 | Optional chaining | `... ?. ...` |
| 19 | new (without argument list) | `new ...` |
| 18 | Postfix Increment | `... ++` |
| 18 | Postfix Decrement | `... --` |
| 17 | Logical NOT | `! ...` |
| 17 | Bitwise NOT | `~ ...` |
| 17 | Unary Plus | `+ ...` |
| 17 | Unary Negation | `- ...` |
| 17 | Prefix Increment | `++ ...` |
| 17 | Prefix Decrement | `-- ...` |
| 17 | typeof | `typeof ...` |
| 17 | delete | `delete ...` |
| 17 | void | `void ...` |
| 17 | await | `await ...` |
| 16 | Exponentiation | `... **