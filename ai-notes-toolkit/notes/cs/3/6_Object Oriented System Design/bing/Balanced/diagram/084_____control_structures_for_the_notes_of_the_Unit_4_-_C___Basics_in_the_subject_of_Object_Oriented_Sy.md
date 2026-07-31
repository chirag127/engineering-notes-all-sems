### Control Structures

Control structures are the statements that determine the flow of execution of a program. They allow the program to perform different actions depending on certain conditions or to repeat a block of code until a certain condition is met. Control structures are essential for creating complex and dynamic programs.

There are three types of control structures in C++:

- **Sequence structure**: This is the simplest and most basic form of a control structure. It is simply the plain logic we write; it only has simple linear instructions, no decision making, and no loop. The statements are executed in the order they appear in the program. For example:

```cpp
// Sequence structure example
#include <iostream>
using namespace std;

int main()
{
  int a, b, c; // Declare three variables
  cout << "Enter two numbers: "; // Prompt the user for input
  cin >> a >> b; // Read the input
  c = a + b; // Add the two numbers and store the result in c
  cout << "The sum is " << c << endl; // Display the result
  return 0; // End the program
}
```

- **Selection structure**: This is the type of control structure that allows the program to make decisions based on certain conditions. There are three types of selection structures in C++:

  - **if statement**: This is the simplest form of selection structure. It executes a block of code only if a condition is true. For example:

  ```cpp
  // if statement example
  #include <iostream>
  using namespace std;

  int main()
  {
    int age; // Declare a variable
    cout << "Enter your age: "; // Prompt the user for input
    cin >> age; // Read the input
    if (age >= 18) // Check the condition
    {
      cout << "You are an adult." << endl; // Execute this block if the condition is true
    }
    return 0; // End the program
  }
  ```

  - **if...else statement**: This is an extension of the if statement. It executes one block of code if a condition is true, and another block of code if the condition is false. For example:

  ```cpp
  // if...else statement example
  #include <iostream>
  using namespace std;

  int main()
  {
    int age; // Declare a variable
    cout << "Enter your age: "; // Prompt the user for input
    cin >> age; // Read the input
    if (age >= 18) // Check the condition
    {
      cout << "You are an adult." << endl; // Execute this block if the condition is true
    }
    else
    {
      cout << "You are a minor." << endl; // Execute this block if the condition is false
    }
    return 0; // End the program
  }
  ```

  - **switch statement**: This is a form of selection structure that allows the program to choose one of several alternatives based on the value of an expression. It is useful when there are many possible cases to handle. For example:

  ```cpp
  // switch statement example
  #include <iostream>
  using namespace std;

  int main()
  {
    int choice; // Declare a variable
    cout << "Enter a number from 1 to 3: "; // Prompt the user for input
    cin >> choice; // Read the input
    switch (choice) // Evaluate the expression
    {
      case 1: // If the expression is equal to 1
        cout << "You chose 1." << endl; // Execute this block
        break; // Exit the switch statement
      case 2: // If the expression is equal to 2
        cout << "You chose 2." << endl; // Execute this block
        break; // Exit the switch statement
      case 3: // If the expression is equal to 3
        cout << "You chose 3." << endl; // Execute this block
        break; // Exit the switch statement
      default: // If the expression is not equal to any of the cases
        cout << "Invalid choice." << endl; // Execute this block
        break; // Exit the switch statement
    }
    return 0; // End the program
  }
  ```

- **Repetition structure**: This is the type of control structure that allows the program to repeat a block of code until a certain condition is met. There are three