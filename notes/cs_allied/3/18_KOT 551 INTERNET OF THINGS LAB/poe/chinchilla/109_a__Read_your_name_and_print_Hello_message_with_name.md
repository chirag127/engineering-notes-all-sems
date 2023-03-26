# Read your name and print Hello message with name

When it comes to programming and software development, it is essential to learn how to read input from users and display output. One common task is to read the user's name and print a personalized message, such as "Hello [name]!" In this guide, we will go through the steps to accomplish this task in various programming languages.

## Python
In Python, we can use the `input()` function to read the user's input and the `print()` function to display the output. Here's an example:

```python
# Read user input
name = input("Enter your name: ")

# Print personalized message
print("Hello " + name + "!")
```

## Java
In Java, we can use the `Scanner` class to read the user's input and the `System.out.println()` method to display the output. Here's an example:

```java
import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] args) {
        // Create a Scanner object
        Scanner input = new Scanner(System.in);

        // Read user input
        System.out.print("Enter your name: ");
        String name = input.nextLine();

        // Print personalized message
        System.out.println("Hello " + name + "!");
    }
}
```

## JavaScript
In JavaScript, we can use the `prompt()` function to read the user's input and the `console.log()` function to display the output. Here's an example:

```javascript
// Read user input
let name = prompt("Enter your name:");

// Print personalized message
console.log("Hello " + name + "!");
```

## C++
In C++, we can use the `cin` object to read the user's input and the `cout` object to display the output. Here's an example:

```cpp
#include <iostream>
using namespace std;

int main() {
    // Read user input
    string name;
    cout << "Enter your name: ";
    cin >> name;

    // Print personalized message
    cout << "Hello " << name << "!" << endl;
    return 0;
}
```

By following these simple steps, you can read the user's name and print a personalized message in your favorite programming language. Good luck with your coding!