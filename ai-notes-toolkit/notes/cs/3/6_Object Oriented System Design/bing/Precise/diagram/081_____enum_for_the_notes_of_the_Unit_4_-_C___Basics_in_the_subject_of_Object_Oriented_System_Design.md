### Unit 4 - C++ Basics: Enum

- An `enum` is a user-defined data type that consists of a set of named values called enumerators.
- The `enum` keyword is used to define an enumeration.
- The values of the enumerators are automatically assigned by the compiler if not explicitly specified.
- The first enumerator is assigned the value 0, and the value of each subsequent enumerator is increased by 1.
- The enumerators can be used in expressions and can be compared with each other.
- The `enum` type is useful for defining a set of related values that can be used in a readable and type-safe manner.

Here is an example of how to define and use an `enum` in C++:

```c++
#include <iostream>
using namespace std;

enum Day {SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY};

int main() {
    Day today = WEDNESDAY;
    cout << "Today is day number " << today << endl;
    return 0;
}
```

In this example, we define an `enum` called `Day` with seven enumerators representing the days of the week. We then use the `enum` to declare a variable `today` of type `Day` and assign it the value `WEDNESDAY`. Finally, we output the value of `today` using the `cout` statement. The output of this program is `Today is day number 3`, since `WEDNESDAY` is the fourth enumerator and its value is 3 (0-based indexing).
