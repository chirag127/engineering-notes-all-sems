# Read your name and print Hello message with name

- This is a basic programming task that can be done in different languages, such as Python, Java, C, etc.
- The task involves two steps: reading the user's input and printing the output.
- Reading the user's input means getting a string (a sequence of characters) from the keyboard or the console and storing it in a variable.
- Printing the output means displaying a message on the screen or the console that includes the user's input.
- The message can be formatted using concatenation (joining strings together) or interpolation (inserting values into placeholders).
- Here is an example of how to do this task in Python:

```python
# Read the user's name and store it in a variable called name
name = input("Enter your name: ")

# Print the hello message with the name
print("Hello, " + name + "!") # Using concatenation
print(f"Hello, {name}!") # Using interpolation
```

- Here is an example of how to do this task in Java:

```java
// Import the Scanner class to read the user's input
import java.util.Scanner;

// Create a Scanner object to read from the keyboard
Scanner scanner = new Scanner(System.in);

// Read the user's name and store it in a variable called name
System.out.print("Enter your name: ");
String name = scanner.nextLine();

// Print the hello message with the name
System.out.println("Hello, " + name + "!"); // Using concatenation
System.out.printf("Hello, %s!%n", name); // Using interpolation
```

- Here is an example of how to do this task in C:

```c
// Include the stdio.h library to use input and output functions
#include <stdio.h>

// Define a constant for the maximum length of the name
#define MAX_LENGTH 100

// Declare a char array to store the name
char name[MAX_LENGTH];

// Read the user's name and store it in the array
printf("Enter your name: ");
scanf("%s", name);

// Print the hello message with the name
printf("Hello, %s!\n", name); // Using interpolation
```