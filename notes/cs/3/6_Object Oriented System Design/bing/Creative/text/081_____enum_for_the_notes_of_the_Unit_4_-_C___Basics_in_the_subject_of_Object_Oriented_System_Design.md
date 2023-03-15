### enum

- An `enum` is a user-defined data type that consists of a set of named constants called enumerators.
- An `enum` declaration defines a new type and the possible values that the type can hold.
- An `enum` declaration has the following syntax:

```cpp
enum enum_name {enumerator1, enumerator2, ..., enumeratorN};
```

- The `enum_name` is the name of the new type and the `enumerator1, enumerator2, ..., enumeratorN` are the names of the constants that belong to the type.
- Each enumerator has an integer value associated with it, starting from 0 by default and increasing by 1 for each subsequent enumerator.
- The value of an enumerator can be explicitly specified using the `=` operator, as in:

```cpp
enum color {red = 1, green = 2, blue = 3};
```

- An `enum` variable can be declared and initialized using the `enum_name` and one of the enumerators, as in:

```cpp
enum color c = red;
```

- An `enum` variable can be used in expressions and comparisons as an integer value, as in:

```cpp
if (c == 1) {
  cout << "The color is red" << endl;
}
```

- An `enum` can also be declared inside a class or a namespace, in which case the scope of the enumerators is limited to the class or the namespace.
- An `enum` can be used to define symbolic constants that are related to each other, such as days of the week, months of the year, directions, etc.
- An `enum` can improve the readability and maintainability of the code by avoiding the use of magic numbers and giving meaningful names to the constants.