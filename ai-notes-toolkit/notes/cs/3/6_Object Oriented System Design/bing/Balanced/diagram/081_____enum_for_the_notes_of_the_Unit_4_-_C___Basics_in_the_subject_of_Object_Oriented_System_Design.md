### enum

- enum or enumeration is a data type consisting of named values that represent integral constants.
- It provides a way to define and group integral constants. It also makes the code easy to maintain and less complex.
- An enum variable takes only one value out of many possible values.
- The syntax for declaring an enum is:

```cpp
enum enum_name {
  enumerator1 = constant1,
  enumerator2 = constant2,
  ...
} variable_name;
```

- The enum_name is optional and can be omitted if the variable_name is specified.
- The enumerator names are identifiers that are associated with constant values. The constant values can be explicitly specified or implicitly assigned by the compiler.
- The default value for the first enumerator is 0, and the value for each subsequent enumerator is increased by 1.
- The enum variables can be assigned and compared using the enumerator names or the constant values.
- The enum variables can also be used in switch statements as the expression or the case labels.
- The size of an enum variable depends on the compiler and the range of values it can hold. It is usually the same as the size of int.
- Example of using enum:

```cpp
#include <iostream>
using namespace std;

enum suit {
  club = 0,
  diamonds = 10,
  hearts = 20,
  spades = 3
} card;

int main() {
  card = club;
  cout << "Size of enum variable " << sizeof(card) << " bytes." << endl;
  cout << "Value of card: " << card << endl;
  switch (card) {
    case club:
      cout << "Club" << endl;
      break;
    case diamonds:
      cout << "Diamonds" << endl;
      break;
    case hearts:
      cout << "Hearts" << endl;
      break;
    case spades:
      cout << "Spades" << endl;
      break;
    default:
      cout << "Invalid suit" << endl;
  }
  return 0;
}
```

- Output:

```
Size of enum variable 4 bytes.
Value of card: 0
Club
```