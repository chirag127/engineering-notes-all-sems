#### Operator in Core Java

- An operator is a symbol that performs a specific operation on one or more operands. An operand is a variable or a value on which the operation is performed.
- Operators are used to manipulate data and variables in Java programs. They can be classified into different categories based on their functionality and precedence.
- The categories of operators in Java are:

  - Arithmetic operators: These operators are used to perform basic mathematical operations such as addition, subtraction, multiplication, division, modulus, increment and decrement. For example, `a + b`, `c - d`, `e * f`, `g / h`, `i % j`, `k++`, `l--`.
  - Relational operators: These operators are used to compare two operands and return a boolean value (true or false) based on the result of the comparison. For example, `a == b`, `c != d`, `e > f`, `g < h`, `i >= j`, `k <= l`.
  - Logical operators: These operators are used to combine two or more boolean expressions and return a boolean value based on the logical rules. For example, `a && b`, `c || d`, `!e`.
  - Bitwise operators: These operators are used to perform operations on individual bits of an operand. They are useful for low-level programming such as encryption, compression, etc. For example, `a & b`, `c | d`, `e ^ f`, `~g`, `h << i`, `j >> k`, `l >>> m`.
  - Assignment operators: These operators are used to assign a value to a variable or to modify the value of a variable based on an operation. For example, `a = b`, `c += d`, `e -= f`, `g *= h`, `i /= j`, `k %= l`, `m &= n`, `o |= p`, `q ^= r`, `s <<= t`, `u >>= v`, `w >>>= x`.
  - Conditional operator: This operator is also known as the ternary operator. It is used to evaluate a boolean expression and return one of two values based on the result. It has the following syntax: `condition ? value1 : value2`. For example, `a > b ? c : d`.
  - instanceof operator: This operator is used to check if an object is an instance of a specific class or interface. It returns a boolean value based on the result. For example, `a instanceof b`.
  - Type cast operator: This operator is used to convert an operand from one data type to another. It has the following syntax: `(type) operand`. For example, `(int) a`, `(double) b`, `(String) c`.

- Some of the operators have higher precedence than others, which means they are evaluated before the others in an expression. The order of precedence of operators in Java is as follows (from highest to lowest):

  - Postfix operators: `a++`, `a--`
  - Prefix operators: `++a`, `--a`, `!a`, `~a`, `(type) a`
  - Multiplicative operators: `a * b`, `a / b`, `a % b`
  - Additive operators: `a + b`, `a - b`
  - Shift operators: `a << b`, `a >> b`, `a >>> b`
  - Relational operators: `a < b`, `a > b`, `a <= b`, `a >= b`, `a instanceof b`
  - Equality operators: `a == b`, `a != b`
  - Bitwise and logical AND operator: `a & b`
  - Bitwise and logical XOR operator: `a ^ b`
  - Bitwise and logical OR operator: `a | b`
  - Conditional AND operator: `a && b`
  - Conditional OR operator: `a || b`
  - Conditional operator: `a ? b : c`
  - Assignment operators: `a = b`, `a += b`, `a -= b`, `a *= b`, `a /= b`, `a %= b`, `a &= b`, `a ^= b`, `a |= b`, `a <<= b`, `a >>= b`, `a >>>= b`

- To change the order of evaluation of operators in an expression, parentheses can be used to group the operands and operators. For example, `(a + b) * c` is different from `a + (b * c)`.
- Some of the operators are overloaded, which means they can perform different operations based on the data type of the operands. For example, the `+` operator can perform addition for numeric