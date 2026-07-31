### Operator Overloading

- Operator overloading is a feature of object-oriented programming that allows us to define how operators (such as +, -, *, /, etc.) behave when applied to objects of user-defined classes  .
- Operator overloading can be useful to implement intuitive and natural syntax for custom data types, such as complex numbers, matrices, vectors, etc .
- Operator overloading can be achieved by defining operator functions, which are either non-static member functions or friend functions of a class .
- Operator functions have the following general syntax:

```cpp
return_type operator op (argument_list);
```

- Where `return_type` is the type of the value returned by the operator function, `op` is the operator symbol to be overloaded, and `argument_list` is the list of parameters for the operator function.
- The number and type of parameters depend on the operator and whether it is a member function or a friend function. For example, a binary operator (such as + or -) that is a member function takes one parameter (the right operand), while a binary operator that is a friend function takes two parameters (the left and right operands) .
- Some operators cannot be overloaded, such as `.` (member access), `::` (scope resolution), `?:` (conditional), `sizeof` (size of), and `typeid` (type identification) .
- Some operators should be overloaded with caution, such as `=` (assignment), `[]` (subscript), `()` (function call), and `->` (member access through pointer), because they have special meanings and expectations in C++ .
- Operator overloading should follow the principle of least surprise, which means that the overloaded operator should behave in a way that is consistent with its original meaning and does not confuse or mislead the users .