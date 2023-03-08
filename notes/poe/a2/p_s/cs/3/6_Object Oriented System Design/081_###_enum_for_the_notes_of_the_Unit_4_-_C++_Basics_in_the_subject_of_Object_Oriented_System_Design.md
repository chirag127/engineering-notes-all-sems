 Here are the notes for enum in markdown format for Unit 4 - C++ Basics in Object Oriented System Design:

### enum

Enumerations (enums) are a user-defined data type consisting of a set of named constants (enumerators).

- Enums are a way to give meaningful names to integral constants, which can make code more readable and understandable.
- Enums are strongly typed constants. The underlying type of an enum is int by default.
- Enums can be defined using the enum keyword followed by a distinct name/identifier.
- Enumerators are defined using identifiers within the enum scope.
- Enums can be defined with or without an underlying type. If not specified, int is assumed.

**Syntax:**
enum enum_name {
    enumerator1,
    enumerator2,
    ...
};

**Example:**
enum Color {Red, Green, Blue};

Color c = Green; // c holds value 1

**Advantages:**
- Increased readability of code.
- Type safety.
- Avoid magic numbers.

**Disadvantages:**
- The enum values are arbitrary unless explicitly defined.
- The enum type is limited by the underlying type (typically int).

**Applications:**
- Defining a finite set of constants(days of week, color codes etc.)
- Replacing integer constants with named constants to make the code more readable.

[Detailed diagrams and examples can be added here for more clarity]