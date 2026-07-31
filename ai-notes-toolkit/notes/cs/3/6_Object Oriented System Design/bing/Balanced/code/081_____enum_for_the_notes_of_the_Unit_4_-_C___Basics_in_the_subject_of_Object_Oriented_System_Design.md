### enum

- An enum is a user-defined data type that consists of a set of named constants called enumerators.
- An enum declaration defines a new type that can hold one of the enumerators as its value.
- An enum can be declared using the keyword `enum` followed by an optional name and a list of enumerators enclosed in braces.
- The enumerators are separated by commas and can be assigned integer values explicitly or implicitly.
- By default, the first enumerator has the value 0, and the subsequent enumerators have values incremented by 1 from the previous one.
- An enum can be used to create variables of the enum type, which can store one of the enumerators as their value.
- An enum can also be used to define parameters or return types of functions, or as a part of other data structures such as arrays, structures, or classes.
- An enum can improve the readability and maintainability of the code by using meaningful names instead of numeric constants.
- An enum can also help to avoid errors such as typos or mismatched values by restricting the possible values of a variable to a predefined set.

#### Example of enum declaration and usage in C++

```cpp
// Declare an enum named Color with four enumerators
enum Color {RED, GREEN, BLUE, YELLOW};

// Create a variable of type Color and assign it an enumerator
Color c = RED;

// Use the variable in a switch statement
switch (c) {
  case RED:
    cout << "The color is red." << endl;
    break;
  case GREEN:
    cout << "The color is green." << endl;
    break;
  case BLUE:
    cout << "The color is blue." << endl;
    break;
  case YELLOW:
    cout << "The color is yellow." << endl;
    break;
  default:
    cout << "Invalid color." << endl;
}

// Assign a different enumerator to the variable
c = YELLOW;

// Use the variable in an if statement
if (c == YELLOW) {
  cout << "The color is yellow." << endl;
} else {
  cout << "The color is not yellow." << endl;
}

// Declare an enum with explicit values
enum Direction {NORTH = 1, SOUTH = 2, EAST = 3, WEST = 4};

// Create an array of type Direction and initialize it with enumerators
Direction directions[4] = {NORTH, SOUTH, EAST, WEST};

// Use the array in a for loop
for (int i = 0; i < 4; i++) {
  cout << "The direction is " << directions[i] << endl;
}
```