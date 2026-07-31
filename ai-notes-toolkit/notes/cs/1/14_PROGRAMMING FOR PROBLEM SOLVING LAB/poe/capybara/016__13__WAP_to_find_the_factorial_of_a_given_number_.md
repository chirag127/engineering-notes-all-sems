## 13. WAP to find the factorial of a given number.

Factorial is a mathematical operation that is used to calculate the product of a given number and all the positive integers below it. For example, the factorial of 5 is calculated as 5 x 4 x 3 x 2 x 1 = 120. In this program, we will write a code to find the factorial of a given number.

Here are the steps to write a program to find the factorial of a given number:

1. Start the program by defining the main function.

2. Declare a variable to store the input number and ask the user to enter a number.

3. Read the input number using the scanf() function.

4. Declare another variable to store the factorial value and initialize it to 1.

5. Use a for loop to calculate the factorial of the input number.

6. In the for loop, start the loop from 1 and iterate till the input number.

7. Multiply the factorial variable with the loop variable in each iteration.

8. After the loop is completed, display the factorial value using printf() function.

9. End the program.

Here is the code to find the factorial of a given number:

```c
#include<stdio.h>
int main()
{
    int n, i;
    unsigned long long factorial = 1;

    printf("Enter an integer: ");
    scanf("%d",&n);

    // Error message if the input number is negative
    if (n < 0)
        printf("Error! Factorial of a negative number doesn't exist.");

    else
    {
        for(i=1; i<=n; ++i)
        {
            factorial *= i;             // factorial = factorial*i;
        }
        printf("Factorial of %d = %llu", n, factorial);
    }

    return 0;
}
```

In this program, we have used an if-else statement to handle negative input numbers. If the input number is negative, the program displays an error message. Otherwise, the program calculates the factorial using a for loop and displays the result.

To summarize, the program to find the factorial of a given number is a simple program that uses a for loop to calculate the factorial value. It is important to handle negative input numbers separately to avoid errors in the program.