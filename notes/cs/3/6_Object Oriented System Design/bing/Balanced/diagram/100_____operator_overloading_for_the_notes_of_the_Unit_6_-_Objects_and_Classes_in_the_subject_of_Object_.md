### Operator Overloading

- Operator overloading is a feature of object-oriented programming languages that allows the same operator name or symbol to be used for different operations on different types of operands.
- Operator overloading enables us to define the behavior of operators on user-defined classes or structs. For example, we can overload the `+` operator to perform addition on complex numbers, matrices, strings, etc.
- Operator overloading can improve the readability and expressiveness of the code, as well as the consistency and symmetry of the operators.
- Operator overloading can be implemented by defining a special function that specifies the operation to be performed when the operator is applied to the operands. The name of the function is usually the keyword `operator` followed by the operator symbol or name.
- The syntax of operator overloading function is:

```c++
return_type operator op (argument_list);
```

- The return type is the type of the result of the operation. The operator symbol or name is the operator to be overloaded. The argument list is the list of parameters that represent the operands of the operation.
- The operator overloading function can be either a member function or a non-member function of a class. If the operator overloading function is a member function, then the left operand must be an object of that class. If the operator overloading function is a non-member function, then it must be declared as a friend function of the class if it needs to access the private or protected members of the class.
- Some operators cannot be overloaded, such as `.` (member access), `::` (scope resolution), `?:` (conditional), `sizeof` (size of object), and `typeid` (type information).
- Some operators have predefined meanings for built-in types, such as `=` (assignment), `&` (address-of), `*` (dereference), and `[]` (subscript). These operators can be overloaded for user-defined types, but the default behavior for built-in types cannot be changed.
- Some operators can be overloaded in two forms: unary and binary. For example, `+` can be overloaded to perform unary plus (positive sign) or binary plus (addition). The number of arguments in the operator overloading function determines whether the operator is unary or binary. Unary operators take one argument, while binary operators take two arguments.
- Some operators can be overloaded in multiple ways, such as `<<` and `>>`. These operators are commonly used for bitwise shift operations on integers, but they can also be overloaded for stream input and output operations on objects. The context of the operator determines which overloaded function is called.