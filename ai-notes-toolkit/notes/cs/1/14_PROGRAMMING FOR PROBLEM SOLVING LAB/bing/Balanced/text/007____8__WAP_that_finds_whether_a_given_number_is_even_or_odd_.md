## 8. WAP that finds whether a given number is even or odd.

- A number is even if it is divisible by 2 without any remainder. A number is odd if it is not divisible by 2 or has a remainder of 1 when divided by 2.
- To write a program that finds whether a given number is even or odd, we can use the modulo operator (%) which returns the remainder of a division operation.
- The modulo operator (%) can be used as follows: `number % 2`
- If the result of `number % 2` is 0, then the number is even. If the result of `number % 2` is 1, then the number is odd.
- We can use an if-else statement to check the result of `number % 2` and print the appropriate message.
- The pseudocode for the program is as follows:

```
// Read a number from the user and store it in a variable called number
number = input("Enter a number: ")

// Convert the input to an integer
number = int(number)

// Check if the number is even or odd using the modulo operator
if (number % 2 == 0) {
  // If the number is even, print "The number is even."
  print("The number is even.")
} else {
  // If the number is odd, print "The number is odd."
  print("The number is odd.")
}
```

- The program can be written in different programming languages, such as Python, C, Java, etc. The syntax may vary slightly depending on the language, but the logic is the same.
- Here is an example of the program written in Python:

```python
# Read a number from the user and store it in a variable called number
number = input("Enter a number: ")

# Convert the input to an integer
number = int(number)

# Check if the number is even or odd using the modulo operator
if (number % 2 == 0):
  # If the number is even, print "The number is even."
  print("The number is even.")
else:
  # If the number is odd, print "The number is odd."
  print("The number is odd.")
```

- Here is an example of the program written in C:

```c
#include <stdio.h>

int main() {
  // Declare a variable called number to store the input from the user
  int number;

  // Read a number from the user and store it in the variable number
  printf("Enter a number: ");
  scanf("%d", &number);

  // Check if the number is even or odd using the modulo operator
  if (number % 2 == 0) {
    // If the number is even, print "The number is even."
    printf("The number is even.\n");
  } else {
    // If the number is odd, print "The number is odd."
    printf("The number is odd.\n");
  }

  return 0;
}
```

- Here is an example of the program written in Java:

```java
import java.util.Scanner;

public class EvenOdd {

  public static void main(String[] args) {
    // Create a Scanner object to read input from the user
    Scanner sc = new Scanner(System.in);

    // Declare a variable called number to store the input from the user
    int number;

    // Read a number from the user and store it in the variable number
    System.out.print("Enter a number: ");
    number = sc.nextInt();

    // Check if the number is even or odd using the modulo operator
    if (number % 2 == 0) {
      // If the number is even, print "The number is even."
      System.out.println("The number is even.");
    } else {
      // If the number is odd, print "The number is odd."
      System.out.println("The number is odd.");
    }

    // Close the Scanner object
    sc.close();
  }
}
```