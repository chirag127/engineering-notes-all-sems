### Array references in arithmetic expressions for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- An array reference is an expression that refers to an element of an array.
- In an arithmetic expression, an array reference can be used as an operand.
- The value of the array reference is the value of the element it refers to.
- The element is determined by the index expression within the square brackets following the array name.
- The index expression must evaluate to an integer value.
- The value of the index expression determines which element of the array is being referred to.
- For example, if `a` is an array of integers and `i` is an integer variable, the expression `a[i]` refers to the `i`-th element of the array `a`.
- Array references can be used in arithmetic expressions in the same way as any other operand.
- For example, the expression `a[i] + 1` adds 1 to the value of the `i`-th element of the array `a`.
- Array references can also be used on the left side of an assignment statement to assign a value to an element of an array.
- For example, the statement `a[i] = a[i] + 1` increments the value of the `i`-th element of the array `a` by 1.