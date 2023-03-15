## 19.WAP to print Armstrong numbers from 1 to 100.

An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.

Here is a program in C language to print all Armstrong numbers from 1 to 100:

```c
#include <stdio.h>
#include <math.h>

int main()
{
    int i, temp, rem, sum, n = 0;

    printf("Armstrong numbers from 1 to 100: ");
    for (i = 1; i <= 100; i++)
    {
        temp = i;
        sum = 0;
        n = 0;

        while (temp != 0)
        {
            temp /= 10;
            n++;
        }

        temp = i;

        while (temp != 0)
        {
            rem = temp % 10;
            sum += pow(rem, n);
            temp /= 10;
        }

        if (sum == i)
        {
            printf("%d ", i);
        }
    }

    return 0;
}
```

This program uses two nested while loops to calculate the sum of the digits raised to the power of the number of digits. The outer for loop iterates from 1 to 100 and checks if the current number is an Armstrong number. If it is, the number is printed.