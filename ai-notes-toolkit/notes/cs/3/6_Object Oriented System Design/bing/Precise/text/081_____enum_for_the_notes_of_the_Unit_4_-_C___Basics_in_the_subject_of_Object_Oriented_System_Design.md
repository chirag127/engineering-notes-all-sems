### Enum in C++ Basics - Unit 4 of Object Oriented System Design

- Enum, short for enumeration, is a user-defined data type in C++.
- It is used to assign names to integral constants, making the code more readable and maintainable.
- The syntax for defining an enum is as follows:
```
enum enum_name {const1, const2, ..., constN};
```
- By default, the first enumerator has the value 0, and the value of each subsequent enumerator is increased by 1.
- It is possible to specify the value of an enumerator explicitly by using an initializer, for example:
```
enum Season {Spring = 1, Summer, Autumn, Winter};
```
- In this example, Spring has the value 1, Summer has the value 2, Autumn has the value 3, and Winter has the value 4.
- Enumerators can be used in expressions and can be converted to integers.
- It is also possible to define an enum within a class or a namespace.
- Enum classes, introduced in C++11, provide stronger type checking and scoping for enum types.
