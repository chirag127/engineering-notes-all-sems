# Read your name and print Hello message with name

- This is a basic programming task that can be done in different languages such as Python, Java, C++, etc.
- The task involves two steps: reading the user's input and printing the output.
- Reading the user's input means taking a string value from the keyboard or the console and storing it in a variable.
- Printing the output means displaying a message on the screen or the console that includes the user's input.
- The syntax and the functions for reading and printing may vary depending on the language.
- Here are some examples of how to do this task in different languages:

## Python
- In Python, we can use the `input()` function to read the user's input and store it in a variable.
- We can use the `print()` function to print the output and concatenate the user's input with the string `"Hello"` using the `+` operator.
- For example:

```python
# Read the user's name and store it in a variable called name
name = input("Enter your name: ")

# Print the output with the user's name
print("Hello " + name)
```

## Java
- In Java, we can use the `Scanner` class to read the user's input and store it in a variable.
- We need to import the `java.util.Scanner` package and create an object of the `Scanner` class.
- We can use the `nextLine()` method to read the user's input as a string and store it in a variable.
- We can use the `System.out.println()` method to print the output and concatenate the user's input with the string `"Hello"` using the `+` operator.
- For example:

```java
// Import the Scanner class
import java.util.Scanner;

// Create a Scanner object
Scanner sc = new Scanner(System.in);

// Read the user's name and store it in a variable called name
System.out.print("Enter your name: ");
String name = sc.nextLine();

// Print the output with the user's name
System.out.println("Hello " + name);
```

## C++
- In C++, we can use the `cin` object to read the user's input and store it in a variable.
- We need to include the `<iostream>` header file and use the `std` namespace.
- We can use the `getline()` function to read the user's input as a string and store it in a variable.
- We can use the `cout` object to print the output and concatenate the user's input with the string `"Hello"` using the `<<` operator.
- For example:

```cpp
// Include the iostream header file
#include <iostream>

// Use the std namespace
using namespace std;

// Read the user's name and store it in a variable called name
cout << "Enter your name: ";
string name;
getline(cin, name);

// Print the output with the user's name
cout << "Hello " << name << endl;
```