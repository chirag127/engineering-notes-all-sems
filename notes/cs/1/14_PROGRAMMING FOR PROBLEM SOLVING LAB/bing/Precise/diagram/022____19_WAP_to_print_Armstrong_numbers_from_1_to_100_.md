## 19. WAP to print Armstrong numbers from 1 to 100

An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.

Here is a program in C language to print all Armstrong numbers from 1 to 100:

```c
#include <stdio.h>
#include <math.h>

int main() {
    int i, temp, rem, sum, n = 0;

    printf("Armstrong numbers from 1 to 100: ");
    for(i = 1; i <= 100; i++) {
        temp = i;
        sum = 0;
        n = 0;

        while (temp != 0) {
            temp /= 10;
            ++n;
        }

        temp = i;

        while (temp != 0) {
            rem = temp % 10;
            sum += pow(rem, n);
            temp /= 10;
        }

        if (sum == i) {
            printf("%d ", i);
        }
    }
    return 0;
}
```

This program uses a for loop to iterate through the numbers from 1 to 100. For each number, it calculates the sum of its digits raised to the power of the number of digits. If the sum is equal to the number, it is printed as an Armstrong number.

- The `#include <stdio.h>` and `#include <math.h>` are preprocessor directives that include the standard input-output and math libraries, respectively.
- The `int main()` function is the entry point of the program.
- The `printf()` function is used to print the output to the console.
- The `for` loop is used to iterate through the numbers from 1 to 100.
- The `while` loop is used to calculate the number of digits in the number.
- The `pow()` function is used to calculate the power of a number.
- The `if` statement is used to check if the sum is equal to the number.
- The `return 0;` statement indicates the successful termination of the program.

This program can be modified to print Armstrong numbers in any given range by changing the values of the for loop. For example, to print Armstrong numbers from 100 to 200, the for loop can be changed to `for(i = 100; i <= 200; i++)`.