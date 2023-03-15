## 7. WAP to find the greatest of three numbers.

- A program to find the greatest of three numbers is a common problem that can be solved using conditional statements, such as if-else or switch-case.
- The basic logic is to compare the three numbers and find the one that is larger than the other two.
- The program can be written in different programming languages, such as C, C++, Java, Python, etc. Here is an example of how to write the program in C:

```c
#include <stdio.h>
int main()
{
    // Declare three variables to store the numbers
    int a, b, c;
    // Prompt the user to enter the numbers
    printf("Enter three numbers: ");
    // Read the numbers from the standard input
    scanf("%d %d %d", &a, &b, &c);
    // Compare the numbers and find the greatest one
    if (a > b && a > c) // If a is greater than both b and c
    {
        // Print a as the greatest number
        printf("%d is the greatest number.\n", a);
    }
    else if (b > a && b > c) // If b is greater than both a and c
    {
        // Print b as the greatest number
        printf("%d is the greatest number.\n", b);
    }
    else if (c > a && c > b) // If c is greater than both a and b
    {
        // Print c as the greatest number
        printf("%d is the greatest number.\n", c);
    }
    else // If none of the numbers are greater than the others
    {
        // Print that the numbers are equal
        printf("The numbers are equal.\n");
    }
    // Return 0 to indicate successful termination of the program
    return 0;
}
```
- The program can be tested with different inputs and outputs, such as:

```
Enter three numbers: 10 20 30
30 is the greatest number.

Enter three numbers: 50 50 50
The numbers are equal.

Enter three numbers: -5 -10 -15
-5 is the greatest number.
```
- The program can be modified or improved by using different techniques, such as:

  - Using a loop to read the numbers from an array or a file instead of the standard input.
  - Using a function to find the maximum of three numbers and return it to the main function.
  - Using a ternary operator to simplify the conditional statements.
  - Using a switch-case statement instead of if-else statements.
  - Using logical operators to combine multiple conditions.
  - Using comments to explain the code and its purpose.
  - Using proper indentation and spacing to make the code more readable and maintainable.