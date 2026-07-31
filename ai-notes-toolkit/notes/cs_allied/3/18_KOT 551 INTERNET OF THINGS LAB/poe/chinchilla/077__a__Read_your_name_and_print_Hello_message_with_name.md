#### a) Read your name and print Hello message with name

In programming, it is common to ask the user for their name and then use it to personalize messages. In this topic, we will learn how to read a user's name and print a "Hello" message with their name using various programming languages.

Here are the steps to achieve this in different programming languages:

##### Python

1. Ask the user to enter their name using the `input()` function.
2. Store the name in a variable, say `name`.
3. Print the greeting message using the `print()` function, with the format string `f"Hello, {name}!"`.

Here's the code:

```python
name = input("Please enter your name: ")
print(f"Hello, {name}!")
```

##### Java

1. Import the `java.util.Scanner` class to read input from the user.
2. Create a new `Scanner` object to read input from the standard input stream, `System.in`.
3. Ask the user to enter their name using the `Scanner` object's `nextLine()` method, and store it in a variable, say `name`.
4. Print the greeting message using the `System.out.println()` method, with the concatenation operator `+`.

Here's the code:

```java
import java.util.Scanner;

public class HelloName {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Please enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");
    }
}
```

##### JavaScript

1. Ask the user to enter their name using the `prompt()` method.
2. Store the name in a variable, say `name`.
3. Print the greeting message using the `alert()` method, with the concatenation operator `+`.

Here's the code:

```javascript
let name = prompt("Please enter your name:");
alert("Hello, " + name + "!");
```

##### C++

1. Import the `iostream` library to read input from the user and write output to the console.
2. Ask the user to enter their name using the `std::cin` object.
3. Store the name in a variable, say `name`.
4. Print the greeting message using the `std::cout` object, with the insertion operator `<<`.

Here's the code:

```cpp
#include <iostream>
using namespace std;

int main() {
    string name;
    cout << "Please enter your name: ";
    getline(cin, name);
    cout << "Hello, " << name << "!" << endl;
    return 0;
}
```

By following the above steps, you can easily read a user's name and print a personalized greeting message.