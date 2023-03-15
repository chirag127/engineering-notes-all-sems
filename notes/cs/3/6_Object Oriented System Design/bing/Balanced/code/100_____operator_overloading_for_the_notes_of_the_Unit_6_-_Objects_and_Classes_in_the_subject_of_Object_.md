### Operator Overloading

- Operator overloading is a feature of object oriented programming that allows the same operator symbol or name to be used for different operations on different types of operands.
- Operator overloading can be used to define custom behavior for operators when they are applied to user-defined types, such as classes or structs.
- Operator overloading can improve the readability and expressiveness of the code, as well as the consistency and symmetry of the operators.
- Operator overloading can be implemented by either member functions or friend functions of a class, depending on the type and number of operands involved.
- Operator overloading function must have at least one operand of user-defined type. The other operand can be of user-defined or built-in type.
- Operator overloading function must have the same number and order of operands as the original operator, except for the assignment operator (=), which can have only one operand of user-defined type.
- Operator overloading function must have the same precedence and associativity as the original operator, which cannot be changed by the programmer.
- Operator overloading function must return a value of the same type as the original operator, except for the stream insertion (<<) and extraction (>>) operators, which can return a reference to the stream object.
- Operator overloading function must not change the meaning or behavior of the original operator, which should be consistent and intuitive for the user.
- Operator overloading function must not overload operators that have a special meaning or function in the language, such as the scope resolution (::), member access (.), member pointer access (->), sizeof, typeid, or new and delete operators.