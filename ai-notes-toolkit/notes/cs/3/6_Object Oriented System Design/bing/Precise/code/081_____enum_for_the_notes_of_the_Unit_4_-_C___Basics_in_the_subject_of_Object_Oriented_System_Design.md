### Unit 4 - C++ Basics: Enum

- An enumeration is a user-defined data type that consists of integral constants.
- To define an enumeration, the keyword `enum` is used.
- The syntax for defining an enumeration is as follows:
```
enum enum-name { list of names } var-list;
```
- Here, `enum-name` is the name of the enumeration, `list of names` is a comma-separated list of identifiers for the enumeration constants, and `var-list` is an optional list of variables of the specified enumeration type.
- The first name in the list of names has the value 0, the next has the value 1, and so on. The value of each name can also be explicitly specified using an initializer.
- For example, the following code defines an enumeration called `Day` with seven constants representing the days of the week:
```
enum Day {SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY};
```
- The value of `SUNDAY` is 0, `MONDAY` is 1, and so on.
- Enumerations can be used to improve the readability of the code and to make it easier to work with sets of related constants.
- It is also possible to define an enumeration within a class or a namespace.
- When an enumeration is defined within a class, its constants are members of the class and can be accessed using the scope resolution operator `::`.
- When an enumeration is defined within a namespace, its constants are members of the namespace and can be accessed using the scope resolution operator `::` or by using a `using` declaration.