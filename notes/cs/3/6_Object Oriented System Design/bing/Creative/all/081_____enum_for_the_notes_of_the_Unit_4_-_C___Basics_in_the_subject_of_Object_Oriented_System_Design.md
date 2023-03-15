Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of enum for the notes of the Unit 4 - C++ Basics in the subject of Object Oriented System Design.

# Enum

- Enum is a user-defined data type that consists of a set of named constants called enumerators.
- Enum is used to create symbolic names for a set of related values, such as days of the week, colors, directions, etc.
- Enum can improve the readability and maintainability of the code by avoiding the use of magic numbers or hard-coded values.
- Enum can also be used to define bit flags, which are a set of binary values that can be combined using bitwise operators.

## Syntax of enum

- The syntax of enum is as follows:

```cpp
enum enum_name {
    enumerator1 = value1,
    enumerator2 = value2,
    ...
    enumeratorN = valueN
};
```

- The enum_name is the name of the enum type, which can be used to declare variables of that type.
- The enumerator1, enumerator2, ..., enumeratorN are the names of the enumerators, which are the constants that belong to the enum type.
- The value1, value2, ..., valueN are the integer values assigned to the enumerators. If the values are not specified, they are assigned automatically starting from 0.
- The values of the enumerators must be unique within the same enum type.
- The enumerators can be accessed using the scope resolution operator (::) as enum_name::enumerator.

## Example of enum

- Here is an example of enum that defines the days of the week:

```cpp
enum Weekday {
    Monday,    // 0
    Tuesday,   // 1
    Wednesday, // 2
    Thursday,  // 3
    Friday,    // 4
    Saturday,  // 5
    Sunday     // 6
};
```

- Here is an example of enum that defines the colors of the rainbow:

```cpp
enum Rainbow {
    Red = 1,    // 1
    Orange = 2, // 2
    Yellow = 4, // 4
    Green = 8,  // 8
    Blue = 16,  // 16
    Indigo = 32,// 32
    Violet = 64 // 64
};
```

- Here is an example of enum that defines the directions of a compass:

```cpp
enum Direction {
    North = 0,  // 0
    East = 90,  // 90
    South = 180,// 180
    West = 270  // 270
};
```

## Usage of enum

- Enum can be used to declare variables of the enum type, which can store one of the enumerators as their value.
- Enum can also be used to compare variables or constants using relational operators, such as ==, !=, <, >, etc.
- Enum can also be used to switch between different cases using the switch statement, which can match the value of an enum variable or constant with the enumerators.
- Enum can also be used to define bit flags, which are a set of binary values that can be combined using bitwise operators, such as |, &, ^, ~, etc.

## Example of usage of enum

- Here is an example of using enum to declare variables and compare them:

```cpp
// Declare an enum variable
Weekday today = Weekday::Friday;

// Declare another enum variable
Weekday tomorrow = Weekday::Saturday;

// Compare the enum variables
if (today == tomorrow) {
    cout << "Today and tomorrow are the same day." << endl;
} else {
    cout << "Today and tomorrow are different days." << endl;
}

// Compare the enum variable with an enumerator
if (today == Weekday::Friday) {
    cout << "Today is Friday." << endl;
} else {
    cout << "Today is not Friday." << endl;
}
```

- Here is an example of using enum to switch between different cases:

```cpp
// Declare an enum variable
Rainbow color = Rainbow::Green;

// Switch on the enum variable
switch (color) {
    case Rainbow::Red:
        cout << "The color is red." << endl;
        break;
    case Rainbow::Orange:
        cout << "The color is orange." << endl;
        break;
    case Rainbow::Yellow:
        cout << "The color is yellow." << endl;
        break;
    case Rainbow::Green:
        cout << "The color is green." << endl;
        break;
    case Rainbow::Blue: