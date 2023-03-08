 Here is the content in markdown format for the topic ### Array references in arithmetic expressions for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design:

## Array references in arithmetic expressions

1. Array references can appear in arithmetic expressions. For example, the expression a[i] + a[j] consists of two array references and one addition.
2. The code generated for such expressions must evaluate the array references and then perform the arithmetic operation.
3. For example, the code sequence for a[i] + a[j] might be:
    1. Load a[i]
    2. Load a[j]
    3. Add (the two loaded values)
4. The array references are evaluated first, and then the addition is performed.
5. Without this left-to-right evaluation, the addition might be performed before one or both of the array references, leading to incorrect results.
6. Hence, in syntax-directed translation and code generation, the base cases of the translation must handle array references and generate the appropriate code to evaluate them before generating code for any following arithmetic operations.

[Detailed diagrams/codes/examples can be added here if required to help understand the concept better]

The key points to note are:
1. Array references can appear in arithmetic expressions
2. The array references must be evaluated first before performing the arithmetic operation
3. Syntax-directed translation should generate code to evaluate array references first and then perform the arithmetic operation
4. This ensures left-to-right evaluation and correct results