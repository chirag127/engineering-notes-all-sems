# Type Conversion

- Type conversion is an operation that takes a data object of one type and creates the equivalent data object of another type.
- The signature of a type conversion operation is given as `conversion_op : type1 → type2`.
- Type conversion can be either implicit or explicit.
  - Implicit conversion is done automatically by the compiler or the interpreter when the types are compatible and no information is lost.
  - Explicit conversion is done by the programmer using a cast operator or a conversion function when the types are incompatible or information may be lost.
- In object-oriented programming languages, objects can also be downcast or upcast.
  - Downcasting is a type of explicit conversion that converts a reference of a base class to one of its derived classes.
  - Upcasting is a type of implicit conversion that converts a reference of a derived class to one of its base classes.
- Type conversion is an important aspect of object-oriented design, as it allows the reuse of existing classes and the polymorphic behavior of objects .
  - Reuse of existing classes means that a class can be used as a type for another class without modifying its implementation.
  - Polymorphic behavior of objects means that an object can behave differently depending on its actual type at run time.
- Some examples of type conversion in object-oriented programming languages are:
  - In C#, type conversion can be made in a safe or unsafe manner, the former called checked type cast and the latter called unchecked type cast.
  - In Java, type conversion can be done using the `instanceof` operator, the `cast` operator, or the `getClass` method.
  - In Python, type conversion can be done using the built-in functions `int`, `float`, `str`, `bool`, etc. or the special methods `__int__`, `__float__`, `__str__`, `__bool__`, etc. defined in a class.