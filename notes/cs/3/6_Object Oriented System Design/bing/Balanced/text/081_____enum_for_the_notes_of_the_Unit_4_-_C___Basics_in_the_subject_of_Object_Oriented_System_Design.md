### enum

- An enum is a user-defined data type that consists of a set of named constants called enumerators.
- An enum declaration defines a new type that can hold one of the enumerators as its value.
- An enum can be declared using the keyword `enum` followed by an optional name and a list of enumerators enclosed in braces.
- Example:

```cpp
enum Color {RED, GREEN, BLUE}; // declare an enum named Color
Color c; // declare a variable of type Color
c = RED; // assign an enumerator to the variable
```

- By default, the enumerators are assigned integer values starting from 0. For example, in the above declaration, RED has the value 0, GREEN has the value 1, and BLUE has the value 2.
- The values of the enumerators can be explicitly specified using the assignment operator. For example:

```cpp
enum Direction {NORTH = 1, SOUTH = 2, EAST = 3, WEST = 4}; // assign values to the enumerators
Direction d; // declare a variable of type Direction
d = EAST; // assign an enumerator to the variable
```

- An enum can also be declared without a name, in which case it is called an anonymous enum. For example:

```cpp
enum {SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY}; // declare an anonymous enum
int day; // declare an integer variable
day = SUNDAY; // assign an enumerator to the variable
```

- An enum can be used to define constants that are related to each other, such as colors, directions, days of the week, etc.
- An enum can improve the readability and maintainability of the code, as it avoids the use of magic numbers and allows the use of meaningful names for the constants.
- An enum can also be used to implement switch statements, as the compiler can check if all the possible cases are covered. For example:

```cpp
switch (c) {
  case RED:
    // do something for red
    break;
  case GREEN:
    // do something for green
    break;
  case BLUE:
    // do something for blue
    break;
  default:
    // do something for invalid color
    break;
}
```