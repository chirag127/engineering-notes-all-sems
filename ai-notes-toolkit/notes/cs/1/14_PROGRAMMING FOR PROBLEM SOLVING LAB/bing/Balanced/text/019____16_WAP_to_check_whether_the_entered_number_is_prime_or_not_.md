## 16.WAP to check whether the entered number is prime or not.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- To check whether a given number is prime or not, we can use a simple algorithm that iterates from 2 to the square root of the number and checks if any of the numbers divides the given number without a remainder.
- If any such number is found, the given number is not prime. Otherwise, it is prime.
- Here is an example of a program in C language that implements this algorithm:

```c
#include <stdio.h>
#include <math.h>

// A function to check if a number is prime or not
int isPrime(int n)
{
    // If n is less than 2, it is not prime
    if (n < 2)
        return 0;

    // Check if n is divisible by any number from 2 to sqrt(n)
    for (int i = 2; i <= sqrt(n); i++)
    {
        // If n is divisible by i, it is not prime
        if (n % i == 0)
            return 0;
    }

    // If no divisor is found, n is prime
    return 1;
}

// A main function to test the isPrime function
int main()
{
    // Declare a variable to store the input number
    int num;

    // Prompt the user to enter a number
    printf("Enter a number: ");

    // Read the input number
    scanf("%d", &num);

    // Check if the number is prime or not using the isPrime function
    if (isPrime(num))
        printf("%d is a prime number.\n", num);
    else
        printf("%d is not a prime number.\n", num);

    // Return 0 to indicate successful termination
    return 0;
}
```