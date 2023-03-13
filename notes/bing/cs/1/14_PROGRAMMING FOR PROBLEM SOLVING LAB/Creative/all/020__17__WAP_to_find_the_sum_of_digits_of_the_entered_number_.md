## 17. WAP to find the sum of digits of the entered number.

- A program to find the sum of digits of the entered number is a common problem that can be solved using a loop and a variable to store the sum.
- The basic idea is to extract each digit of the number using the modulo operator (%) and add it to the sum variable, then divide the number by 10 to remove the last digit. Repeat this process until the number becomes zero.
- Here is an example of a C program that implements this logic:

```c
#include <stdio.h>
int main()
{
    int num, sum = 0, digit; // declare variables
    printf("Enter a number: "); // prompt user for input
    scanf("%d", &num); // read input and store in num
    while (num > 0) // loop until num is zero
    {
        digit = num % 10; // extract last digit using modulo operator
        sum = sum + digit; // add digit to sum
        num = num / 10; // remove last digit by dividing by 10
    }
    printf("The sum of digits is %d\n", sum); // print the result
    return 0;
}
```

- A possible mnemonic to remember the steps of this program is:

  - **M**odulo to get the last digit
  - **A**dd to the sum
  - **D**ivide by 10 to remove the last digit
  - **R**epeat until zero

  - **MADR** for short.