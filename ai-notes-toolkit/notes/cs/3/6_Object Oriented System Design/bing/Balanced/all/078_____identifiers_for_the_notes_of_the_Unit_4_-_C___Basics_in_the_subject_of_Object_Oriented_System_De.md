# Identifiers in C++

- Identifiers are the names given to various elements in a C++ program, such as variables, functions, classes, etc.
- Identifiers help to identify and distinguish different elements in the code and make it more readable and maintainable.
- Identifiers must follow certain rules and conventions in C++, such as:
  - They can only consist of letters, digits, and underscores (_).
  - They cannot start with a digit or a reserved keyword, such as int, float, void, etc.
  - They are case-sensitive, meaning that x and X are different identifiers.
  - They cannot contain spaces or special characters, such as @, #, $, etc.
  - They should be meaningful and descriptive, but not too long.
- Some examples of valid and invalid identifiers in C++ are:

| Valid Identifiers | Invalid Identifiers |
| ----------------- | ------------------- |
| x                 | 1x                  |
| sum               | sum#                |
| age               | int                 |
| totalVolume       | total volume        |
| _temp             | temp@               |
| myClass           | class               |
| MAX_VALUE         | MAX-VALUE           |

- There are different types of identifiers in C++, depending on their usage and scope, such as:
  - Constants: identifiers that represent fixed values that cannot be changed, such as PI, MAX, etc.
  - Variables: identifiers that represent memory locations that store data, such as x, y, name, etc.
  - Functions: identifiers that represent blocks of code that perform a specific task, such as main, sqrt, print, etc.
  - Classes: identifiers that represent user-defined data types that contain data and functions, such as string, vector, student, etc.
  - Structures: identifiers that represent user-defined data types that contain data only, such as point, date, employee, etc.
  - Unions: identifiers that represent user-defined data types that share the same memory space, such as variant, color, shape, etc.
  - Enumerations: identifiers that represent user-defined data types that consist of a set of named constants, such as season, direction, gender, etc.
  - Typedefs: identifiers that represent aliases for existing data types, such as byte, size_t, string, etc.
  - Labels: identifiers that represent the destination of a goto statement, such as start, end, loop, etc.