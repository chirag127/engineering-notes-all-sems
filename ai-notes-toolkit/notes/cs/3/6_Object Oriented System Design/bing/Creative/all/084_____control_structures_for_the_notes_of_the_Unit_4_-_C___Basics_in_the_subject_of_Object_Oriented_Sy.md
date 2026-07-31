# Control Structures

Control structures are the statements that determine the flow of execution of a program. They allow the program to perform different actions depending on certain conditions or to repeat a set of actions until a certain condition is met. Control structures are essential for creating complex and dynamic programs.

There are three types of control structures in C++:

- Sequence structure: This is the simplest and most basic form of a control structure. It is simply the plain logic we write; it only has simple linear instructions, no decision making, and no loop. The statements are executed in the order they appear in the program. For example:

```cpp
// Sequence structure example
#include <iostream>
using namespace std;

int main()
{
  int a, b, c; // Declare three variables
  a = 10; // Assign a value to a
  b = 20; // Assign a value to b
  c = a + b; // Assign the sum of a and b to c
  cout << "The sum is " << c << endl; // Print the value of c
  return 0; // End the program
}
```

- Selection structure: This is a form of a control structure that allows the program to choose between two or more alternative paths based on some condition. The condition is usually a logical expression that evaluates to either true or false. There are three types of selection structures in C++:

  - if statement: This is the simplest form of a selection structure. It executes a block of statements if the condition is true, and skips it otherwise. For example:

  ```cpp
  // if statement example
  #include <iostream>
  using namespace std;

  int main()
  {
    int age; // Declare a variable
    cout << "Enter your age: "; // Prompt the user
    cin >> age; // Read the user input
    if (age >= 18) // Check the condition
    {
      cout << "You are an adult." << endl; // Execute this block if true
    }
    return 0; // End the program
  }
  ```

  - if...else statement: This is an extension of the if statement. It executes one block of statements if the condition is true, and another block of statements if the condition is false. For example:

  ```cpp
  // if...else statement example
  #include <iostream>
  using namespace std;

  int main()
  {
    int age; // Declare a variable
    cout << "Enter your age: "; // Prompt the user
    cin >> age; // Read the user input
    if (age >= 18) // Check the condition
    {
      cout << "You are an adult." << endl; // Execute this block if true
    }
    else
    {
      cout << "You are a minor." << endl; // Execute this block if false
    }
    return 0; // End the program
  }
  ```

  - switch statement: This is a form of a selection structure that allows the program to choose among multiple cases based on the value of a variable or an expression. Each case is associated with a constant value and a block of statements. The program executes the block of statements that matches the value of the variable or the expression. If no case matches, the program executes the default case, if any. For example:

  ```cpp
  // switch statement example
  #include <iostream>
  using namespace std;

  int main()
  {
    int day; // Declare a variable
    cout << "Enter a day number (1-7): "; // Prompt the user
    cin >> day; // Read the user input
    switch (day) // Check the value of the variable
    {
      case 1: // Case 1
        cout << "Monday" << endl; // Execute this block if day is 1
        break; // Exit the switch statement
      case 2: // Case 2
        cout << "Tuesday" << endl; // Execute this block if day is 2
        break; // Exit the switch statement
      case 3: // Case 3
        cout << "Wednesday" << endl; // Execute this block if day is 3
        break; // Exit the switch statement
      case 4: // Case 4
        cout << "Thursday" << endl; // Execute this block if day is 4
        break; // Exit the switch statement
      case 5: // Case 5
        cout <<

```
