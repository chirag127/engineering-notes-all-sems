## 8. WAP that finds whether a given number is even or odd.

A WAP (Write a Program) that finds whether a given number is even or odd can be written in many programming languages. Here is an example of how this can be done in Python:

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
```

In this program, the user is prompted to enter a number. The number is then stored in the variable `num`. The `if` statement checks if the remainder of the number when divided by 2 is equal to 0. If it is, the number is even and the program prints that the number is even. If the remainder is not equal to 0, the number is odd and the program prints that the number is odd.

This program can be modified to work with different programming languages by changing the syntax accordingly. For example, in C++, the program would look like this:

```c++
#include <iostream>
using namespace std;

int main() {
    int num;
    cout << "Enter a number: ";
    cin >> num;

    if (num % 2 == 0)
        cout << num << " is even";
    else
        cout << num << " is odd";

    return 0;
}
```

In both examples, the logic of the program remains the same. The program checks if the number is divisible by 2 without a remainder to determine if it is even or odd. The syntax, however, changes to match the requirements of the specific programming language.