# Unit 4 - C++ Basics in the subject of Object Oriented System Design

### Enum

- An enumeration is a user-defined data type that consists of integral constants.
- To define an enumeration, the keyword `enum` is used.
- Enumerations are used to represent a collection of related values as a single entity.
- The values of an enumeration are known as enumerators.
- Enumerators are defined within curly braces `{}` and are separated by commas.
- By default, the first enumerator has the value 0, and the value of each subsequent enumerator is increased by 1.
- It is possible to assign specific values to enumerators.
- Enumerations can be used to improve the readability of the code and to make it easier to maintain.
- Enumerations can be used in switch statements, as well as in if-else statements.
- Enumerations can be used to define arrays, where the enumerators represent the indices of the array.

Example:

```c++
enum Day {SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY};
Day today;
today = WEDNESDAY;
```

In this example, an enumeration `Day` is defined with seven enumerators representing the days of the week. The variable `today` is declared as type `Day` and is assigned the value `WEDNESDAY`.