## 18.WAP to find the reverse of a number.

- A program to find the reverse of a number is one that takes a positive integer as input and returns its digits in reverse order.
- For example, if the input is 123, the output should be 321.
- One way to write such a program in C language is as follows:

```c
#include <stdio.h>
int main()
{
    int n, rev = 0, rem; // declare variables
    printf("Enter a positive integer: "); // prompt user for input
    scanf("%d", &n); // read input and store in n
    while (n > 0) // loop until n becomes zero
    {
        rem = n % 10; // get the last digit of n
        rev = rev * 10 + rem; // append the digit to rev
        n = n / 10; // remove the last digit of n
    }
    printf("The reverse of the number is %d\n", rev); // print the result
    return 0;
}
```
- The logic behind this program is to use a loop and modulus operator (%) to extract the digits of the number from right to left and multiply them by powers of 10 to form the reverse number.
- For example, if n = 123, then the loop will perform the following steps:

| n | rem | rev |
|---|-----|-----|
| 123 | 3 | 3 |
| 12 | 2 | 32 |
| 1 | 1 | 321 |
| 0 | - | - |

- The loop terminates when n becomes zero and the final value of rev is the reverse of the input number.
- This program assumes that the input is a positive integer. If the input is negative or non-numeric, the program may not work as expected.