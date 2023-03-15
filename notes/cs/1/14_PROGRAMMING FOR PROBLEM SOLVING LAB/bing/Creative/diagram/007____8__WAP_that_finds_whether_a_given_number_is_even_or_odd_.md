Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program that finds whether a given number is even or odd. Here is the content in markdown format:

## 8. WAP that finds whether a given number is even or odd.

- A number is even if it is divisible by 2 without any remainder. For example, 4, 6, 8, 10 are even numbers.
- A number is odd if it is not divisible by 2 or has a remainder of 1 when divided by 2. For example, 3, 5, 7, 9 are odd numbers.
- To check whether a number is even or odd, we can use the modulo operator (%) which returns the remainder of a division. For example, 5 % 2 = 1, 6 % 2 = 0.
- We can use an if-else statement to compare the remainder with 0 and print the appropriate message. For example, if (num % 2 == 0) { print("The number is even."); } else { print("The number is odd."); }
- Here is the pseudocode for the program:

```
// Declare a variable to store the number
num = input("Enter a number: ")

// Convert the input to an integer
num = int(num)

// Check whether the number is even or odd using modulo operator
if (num % 2 == 0) {
  // If the remainder is 0, the number is even
  print("The number is even.")
} else {
  // If the remainder is not 0, the number is odd
  print("The number is odd.")
}
```

- Here is the program in Python:

```python
# Declare a variable to store the number
num = input("Enter a number: ")

# Convert the input to an integer
num = int(num)

# Check whether the number is even or odd using modulo operator
if (num % 2 == 0):
  # If the remainder is 0, the number is even
  print("The number is even.")
else:
  # If the remainder is not 0, the number is odd
  print("The number is odd.")
```

- Here is the program in C:

```c
// Declare a variable to store the number
int num;

// Prompt the user to enter a number
printf("Enter a number: ");

// Read the input from the user
scanf("%d", &num);

// Check whether the number is even or odd using modulo operator
if (num % 2 == 0) {
  // If the remainder is 0, the number is even
  printf("The number is even.\n");
} else {
  // If the remainder is not 0, the number is odd
  printf("The number is odd.\n");
}
```

- Here is the program in Java:

```java
// Import the Scanner class to read input from the user
import java.util.Scanner;

// Define a class named EvenOdd
public class EvenOdd {

  // Define the main method
  public static void main(String[] args) {

    // Declare a variable to store the number
    int num;

    // Create a Scanner object to read input from the user
    Scanner sc = new Scanner(System.in);

    // Prompt the user to enter a number
    System.out.print("Enter a number: ");

    // Read the input from the user
    num = sc.nextInt();

    // Check whether the number is even or odd using modulo operator
    if (num % 2 == 0) {
      // If the remainder is 0, the number is even
      System.out.println("The number is even.");
    } else {
      // If the remainder is not 0, the number is odd
      System.out.println("The number is odd.");
    }

    // Close the Scanner object
    sc.close();
  }
}
```