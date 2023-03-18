## Unit 2 - Arithmetic Expressions and Precedence : Operators and Expression Using Numeric and Relational Operators, Mixed Operands, Type Conversion, Logical Operators, Bit Operations, Assignment Operator, Operator precedence and Associatively

Arithmetic expressions and precedence are essential concepts in computer programming. They form the foundation for writing programs that can perform complex calculations and algorithms. Here are some key ideas to understand:

### Operators and Expressions Using Numeric and Relational Operators

- Numeric operators are used to perform mathematical operations on values. The most common numeric operators are addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).
- Relational operators are used to compare values. The most common relational operators are less than (<), greater than (>), equal to (==), not equal to (!=), less than or equal to (<=), and greater than or equal to (>=).
- Expressions are combinations of values and operators that can be evaluated to yield a result. For example, 2 + 3 is an expression that evaluates to 5.

### Mixed Operands

- Mixed operands are expressions that contain values of different data types. For example, 2 + 3.5 is a mixed operand expression that contains an integer and a floating-point number.
- When performing operations on mixed operands, the operands are automatically converted to a common data type. This process is called type conversion.

### Type Conversion

- Type conversion is the process of converting a value from one data type to another data type. 
- Implicit type conversion is automatic and occurs when the data types of operands in an expression are different. 
- Explicit type conversion, also known as type casting, requires the programmer to specify the desired data type using a casting operator.

### Logical Operators

- Logical operators are used to combine and manipulate Boolean values (true or false). The most common logical operators are AND (&&), OR (||), and NOT (!).
- The AND operator returns true if both operands are true. The OR operator returns true if either operand is true. The NOT operator returns the opposite of a Boolean value.

### Bit Operations

- Bit operations are used to manipulate individual bits in binary numbers. The most common bit operations are AND (&), OR (|), XOR (^), left shift (<<), and right shift (>>).
- Bitwise AND returns a 1 in each bit position where both corresponding bits are 1. Bitwise OR returns a 1 in each bit position where either corresponding bit is 1. Bitwise XOR returns a 1 in each bit position where only one corresponding bit is 1. Bitwise left shift shifts the bits of a number to the left. Bitwise right shift shifts the bits of a number to the right.

### Assignment Operator

- The assignment operator (=) is used to assign a value to a variable. For example, x = 5 assigns the value 5 to the variable x.
- Compound assignment operators (+=, -=, *=, /=, %=, &=, |=, ^=, <<=, >>=) combine an arithmetic or bit operation with an assignment. For example, x += 5 is equivalent to x = x + 5.

### Operator Precedence and Associativity

- Operator precedence determines the order in which operators are evaluated in an expression. For example, multiplication has a higher precedence than addition, so 2 + 3 * 4 is evaluated as 2 + (3 * 4) = 14.
- Associativity determines the order in which operators of the same precedence are evaluated. Most operators in C++ are left-associative, meaning they are evaluated from left to right. However, some operators, such as the assignment operator, are right-associative, meaning they are evaluated from right to left.