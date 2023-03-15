# Array references in arithmetic expressions

Array references in arithmetic expressions are used to access the elements of an array in an expression. Here are some key points to remember when using array references in arithmetic expressions:

1. An array reference is made up of the array name followed by an index expression enclosed in square brackets. For example, `a[i]` refers to the `i`-th element of the array `a`.
2. The index expression must evaluate to an integer value. This value is used to determine which element of the array is being accessed.
3. The index expression can be any valid arithmetic expression that evaluates to an integer value. For example, `a[i+1]` and `a[i-1]` are both valid array references.
4. Array references can be used on both the left and right sides of an assignment statement. For example, `a[i] = b[i] + c[i]` is a valid assignment statement that adds the `i`-th elements of arrays `b` and `c` and stores the result in the `i`-th element of array `a`.
5. Array references can also be used in more complex arithmetic expressions. For example, `a[i] + b[i] * c[i]` is a valid arithmetic expression that adds the `i`-th element of array `a` to the product of the `i`-th elements of arrays `b` and `c`.
6. When using array references in arithmetic expressions, it is important to ensure that the index value is within the bounds of the array. Accessing an element outside the bounds of the array can result in undefined behavior.
