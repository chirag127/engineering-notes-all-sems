### Operators

Operators are symbols that perform some operations on one or more operands. Operands are the values or variables on which the operators act. For example, in the expression `a + b`, `a` and `b` are operands and `+` is the operator.

C++ supports various types of operators, such as:

- Arithmetic operators: These operators perform basic mathematical operations, such as addition, subtraction, multiplication, division, and modulus. For example, `a + b`, `a - b`, `a * b`, `a / b`, `a % b`.
- Assignment operators: These operators assign the value of the right operand to the left operand. For example, `a = b`, `a += b`, `a -= b`, `a *= b`, `a /= b`, `a %= b`.
- Relational operators: These operators compare the values of the operands and return a boolean value (true or false). For example, `a == b`, `a != b`, `a > b`, `a < b`, `a >= b`, `a <= b`.
- Logical operators: These operators perform logical operations on the operands, such as conjunction, disjunction, and negation. For example, `a && b`, `a || b`, `!a`.
- Bitwise operators: These operators perform bit-level operations on the operands, such as bitwise and, or, xor, complement, left shift, and right shift. For example, `a & b`, `a | b`, `a ^ b`, `~a`, `a << b`, `a >> b`.
- Unary operators: These operators act on a single operand and change its value or state. For example, `++a`, `--a`, `a++`, `a--`, `+a`, `-a`, `sizeof a`, `&a`, `*a`, `!a`, `~a`.
- Ternary operator: This operator takes three operands and returns a value based on a condition. For example, `a ? b : c` returns `b` if `a` is true, otherwise returns `c`.
- Member access operators: These operators access the members (data or functions) of a class or a structure. For example, `a.b`, `a->b`, `a.*b`, `a->*b`.
- Scope resolution operator: This operator specifies the scope of a name, such as a class, a namespace, or a global variable. For example, `std::cout`, `::a`.
- Type cast operators: These operators convert the type of an operand to another type. For example, `static_cast<int>(a)`, `dynamic_cast<B*>(a)`, `reinterpret_cast<char*>(a)`, `const_cast<int*>(a)`.
- Comma operator: This operator evaluates the operands from left to right and returns the value of the rightmost operand. For example, `a = (b, c)` assigns the value of `c` to `a`.
- New and delete operators: These operators allocate and deallocate memory for objects dynamically. For example, `a = new int[10]`, `delete[] a`.

C++ also allows user-defined types (such as classes and structures) to overload operators, which means to define how the operators behave when applied to the user-defined types. For example, one can define how the `+` operator works for a class that represents a complex number. However, not all operators can be overloaded, such as the scope resolution operator, the member access operators, and the ternary operator.