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
    scanf("%d", &n); // read input
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
- The logic behind this program is to use a loop and the modulo (%) and division (/) operators to extract the digits of the input number from right to left and store them in a variable called rev.
- The modulo operator returns the remainder of a division, so n % 10 gives the last digit of n.
- The division operator returns the quotient of a division, so n / 10 gives the number without the last digit.
- The variable rev is initialized to zero and then multiplied by 10 and added with the extracted digit in each iteration of the loop. This way, the digits are appended to rev in reverse order.
- The loop terminates when n becomes zero, which means there are no more digits left to extract.
- The final value of rev is the reverse of the input number, which is printed on the screen.