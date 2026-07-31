### Type Conversion

- Type conversion is an operation that takes a data object of one type and creates the equivalent data object of another type.
- The signature of a type conversion operation is given as `conversion_op : type1 → type2`.
- Type conversion can be either implicit or explicit.
  - Implicit conversion is done automatically by the compiler or the interpreter when the types are compatible and no information is lost.
  - Explicit conversion is done by the programmer using a cast operator or a conversion function when the types are incompatible or information may be lost.
- In object-oriented programming languages, objects can also be downcast or upcast.
  - Downcasting is a type of explicit conversion that converts a reference of a base class to one of its derived classes.
  - Upcasting is a type of implicit conversion that converts a reference of a derived class to one of its base classes.
- Type conversion is an important concept in object-oriented system design because it allows the reuse of existing types and the polymorphic behavior of objects.
- Type conversion can be implemented using different design patterns, such as adapter, bridge, facade, or decorator.
  - Adapter pattern converts the interface of one class into another interface that the client expects.
  - Bridge pattern decouples an abstraction from its implementation so that the two can vary independently.
  - Facade pattern provides a unified interface to a set of interfaces in a subsystem.
  - Decorator pattern adds new functionality to an existing object without altering its structure.