### Operators
Operators are symbols that perform some operations on one or more operands. Operands are the values or variables on which the operators act. For example, in the expression `a + b`, `a` and `b` are the operands and `+` is the operator.

C++ supports various types of operators, such as:

- Arithmetic operators: These operators perform basic mathematical operations, such as addition, subtraction, multiplication, division, and modulo. For example, `a + b`, `a - b`, `a * b`, `a / b`, `a % b`.
- Assignment operators: These operators assign the value of the right operand to the left operand. For example, `a = b`, `a += b`, `a -= b`, `a *= b`, `a /= b`, `a %= b`.
- Relational operators: These operators compare the values of the operands and return a boolean value (true or false). For example, `a == b`, `a != b`, `a < b`, `a > b`, `a <= b`, `a >= b`.
- Logical operators: These operators perform logical operations on the operands, such as conjunction, disjunction, and negation. For example, `a && b`, `a || b`, `!a`.
- Bitwise operators: These operators perform bit-level operations on the operands, such as bitwise and, or, xor, complement, left shift, and right shift. For example, `a & b`, `a | b`, `a ^ b`, `~a`, `a << b`, `a >> b`.
- Unary operators: These operators act on a single operand and change its value or state. For example, `++a`, `--a`, `a++`, `a--`, `+a`, `-a`, `sizeof a`, `&a`, `*a`.
- Ternary operator: This operator takes three operands and returns a value based on a condition. For example, `a ? b : c` returns `b` if `a` is true, otherwise returns `c`.
- Comma operator: This operator evaluates the operands from left to right and returns the value of the rightmost operand. For example, `a, b, c` returns `c`.
- Member access operators: These operators access the members (data or functions) of a class or structure. For example, `a.b`, `a->b`, `a.*b`, `a->*b`.
- Scope resolution operator: This operator specifies the scope of a name or a variable. For example, `std::cout`, `::a`.
- Type cast operators: These operators convert the type of an operand to another type. For example, `(int)a`, `static_cast<int>(a)`, `dynamic_cast<Derived*>(a)`.
- New and delete operators: These operators allocate and deallocate memory for objects dynamically. For example, `new int`, `delete a`.
- Operator overloading: This is a feature of C++ that allows the user to define the behavior of an operator for a user-defined type. For example, `a + b` can be defined for a class or structure.