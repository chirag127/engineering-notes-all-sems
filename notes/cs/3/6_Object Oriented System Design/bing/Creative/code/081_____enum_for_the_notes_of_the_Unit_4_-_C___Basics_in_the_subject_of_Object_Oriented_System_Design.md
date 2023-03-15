Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of enum for the notes of the Unit 4 - C++ Basics in the subject of Object Oriented System Design:

```markdown
### enum
- An enum is a user-defined data type that consists of a set of named constants called enumerators.
- The syntax for declaring an enum is:

```cpp
enum enum_name {enumerator1, enumerator2, ...};
```

- The enum_name is optional and can be omitted if the enum is not used as a type.
- The enumerators are separated by commas and are assigned integer values starting from 0 by default. For example:

```cpp
enum Color {RED, GREEN, BLUE}; // RED = 0, GREEN = 1, BLUE = 2
```

- The integer values of the enumerators can be explicitly specified by using the assignment operator. For example:

```cpp
enum Direction {NORTH = 1, SOUTH = 2, EAST = 3, WEST = 4}; // NORTH = 1, SOUTH = 2, etc.
```

- The enum type can be used to declare variables that can only store one of the enumerators. For example:

```cpp
Color c = RED; // c can only store RED, GREEN, or BLUE
Direction d = EAST; // d can only store NORTH, SOUTH, EAST, or WEST
```

- The enum type can also be used to define parameters, return types, and switch cases. For example:

```cpp
void printColor(Color c) {
  switch (c) {
    case RED: cout << "Red\n"; break;
    case GREEN: cout << "Green\n"; break;
    case BLUE: cout << "Blue\n"; break;
  }
}

Color getColor() {
  return GREEN;
}

int main() {
  Color c = getColor();
  printColor(c);
  return 0;
}
```

- The output of the above program is:

```text
Green
```

- The enum type can be nested inside a class or a struct to create an enumeration that is scoped to that class or struct. For example:

```cpp
class Shape {
  public:
    enum Type {CIRCLE, SQUARE, TRIANGLE}; // Type is scoped to Shape
    Shape(Type t) {
      type = t;
    }
    Type getType() {
      return type;
    }
  private:
    Type type;
};

int main() {
  Shape s1(Shape::CIRCLE); // Shape::CIRCLE is an enumerator of Shape::Type
  Shape s2(Shape::SQUARE); // Shape::SQUARE is an enumerator of Shape::Type
  cout << s1.getType() << "\n"; // prints 0
  cout << s2.getType() << "\n"; // prints 1
  return 0;
}
```

- The enum type can also be declared with the keyword class or struct to create an enum class or an enum struct. These are also called scoped enumerations. For example:

```cpp
enum class Color {RED, GREEN, BLUE}; // Color is an enum class
enum struct Direction {NORTH, SOUTH, EAST, WEST}; // Direction is an enum struct
```

- The enum class and enum struct have the following features:
  - They are strongly typed, which means they cannot be implicitly converted to or from other types.
  - They are scoped, which means they can only be accessed by using the scope resolution operator (::).
  - They have a fixed underlying type, which is int by default, but can be specified by using a colon (:). For example:

```cpp
enum class Color : char {RED, GREEN, BLUE}; // Color has an underlying type of char
```

- The advantages of using enum class and enum struct are:
  - They avoid name collisions and ambiguity, as the enumerators are not visible in the global scope.
  - They provide type safety and prevent accidental conversions or comparisons with other types.
  - They allow specifying the underlying type and controlling the size and representation of the enumeration.
```