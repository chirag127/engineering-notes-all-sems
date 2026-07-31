 Here is the formal notes in Markdown format on the topic "Translation of Assignment Statements" for Unit 3 - Syntax-directed Translation in Compiler Design:

### Translation of Assignment Statements

1. Assignment statements are of the form:

`x = e;`

where x is a variable and e is an expression.

2. The translation of an assignment statement involves the following steps:

- Evaluate the expression e and get its value. Let us call this value `v`.
- Emit code to store `v` in the location corresponding to the variable `x`.

3. For example, the assignment statement:

`a = b + c;`

will be translated to:

- Evaluate `b + c` and get the result `v`
- Store `v` in the location corresponding to variable `a`

4. The exact nature of the code emitted to store the value `v` in the variable `x` will depend on the type of variables and the machine architecture. For example, if variables are stored in registers, the code may move the value to the appropriate register. If variables are stored in memory, the code may involve fetching the memory location of `x`, storing `v` there, etc. The implementation details will be handled by the code generator.

5. The syntax-directed translation of assignment statements is straight-forward. The variable and expression on the two sides can be translated and the code to evaluate the expression and store the value can be emitted.

Does this look okay? Let me know if you would like me to modify or expand the notes in any way.