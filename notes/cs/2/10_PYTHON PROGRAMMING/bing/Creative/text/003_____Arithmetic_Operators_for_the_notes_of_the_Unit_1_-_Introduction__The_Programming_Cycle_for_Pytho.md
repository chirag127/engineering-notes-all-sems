### Arithmetic Operators

- Arithmetic operators are used to perform mathematical operations on numeric values, such as addition, subtraction, multiplication, division, etc.
- Python supports the following arithmetic operators:

| Operator | Symbol | Example | Result |
|----------|--------|---------|--------|
| Addition | +      | 5 + 3   | 8      |
| Subtraction | -   | 5 - 3   | 2      |
| Multiplication | * | 5 * 3  | 15     |
| Division | /      | 5 / 3   | 1.6666666666666667 |
| Floor division | // | 5 // 3 | 1      |
| Modulus | %      | 5 % 3   | 2      |
| Exponentiation | ** | 5 ** 3 | 125    |

- The order of operations follows the PEMDAS rule, which stands for Parentheses, Exponents, Multiplication/Division, Addition/Subtraction. This means that expressions inside parentheses are evaluated first, then exponents, then multiplication and division from left to right, and finally addition and subtraction from left to right.
- For example, the expression 2 + 3 * 4 ** 2 - 1 is evaluated as follows:

| Step | Expression | Explanation |
|------|------------|-------------|
| 1    | 2 + 3 * 4 ** 2 - 1 | Original expression |
| 2    | 2 + 3 * 16 - 1 | Evaluate the exponent 4 ** 2 |
| 3    | 2 + 48 - 1 | Evaluate the multiplication 3 * 16 |
| 4    | 50 - 1 | Evaluate the addition 2 + 48 |
| 5    | 49 | Evaluate the subtraction 50 - 1 |

- The result is 49.