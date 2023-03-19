## 19. WAP to print Armstrong numbers from 1 to 100.

Armstrong numbers are the numbers whose sum of cubes of all the digits is equal to the number itself. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

In this program, we will write a C program to print all the Armstrong numbers from 1 to 100.

### Steps to print Armstrong numbers from 1 to 100

1. Create a for loop to iterate through all the numbers from 1 to 100.
2. For each number, calculate the sum of cubes of all its digits.
3. If the sum of cubes of all its digits is equal to the number itself, print the number.
4. Continue the loop until all the numbers from 1 to 100 have been checked.

### Code snippet

Here is the code snippet to print Armstrong numbers from 1 to 100.

```c
#include <stdio.h>

int main()
{
    int num, originalNum, remainder, result = 0;

    printf("Armstrong numbers from 1 to 100:\n");

    for (num = 1; num <= 100; num++)
    {
        originalNum = num;

        while (originalNum != 0)
        {
            remainder = originalNum % 10;
            result += remainder * remainder * remainder;
            originalNum /= 10;
        }

        if (result == num)
        {
            printf("%d\n", num);
        }

        result = 0;
    }

    return 0;
}
```

### Explanation of the code

1. We start by including the standard input/output library in our program using `#include <stdio.h>`.
2. We define the main function of our program using `int main()`.
3. We declare the necessary variables `num`, `originalNum`, `remainder`, and `result` as integers.
4. We start a for loop to iterate through all the numbers from 1 to 100.
5. For each number, we initialize the `originalNum` variable with the value of the number.
6. We then start a while loop to calculate the sum of cubes of all the digits of the number.
7. Inside the while loop, we calculate the remainder of the number when divided by 10 using `remainder = originalNum % 10`.
8. We then calculate the cube of the remainder and add it to the `result` variable using `result += remainder * remainder * remainder`.
9. We update the `originalNum` variable by dividing it by 10 using `originalNum /= 10`.
10. We continue the while loop until all the digits of the number have been processed.
11. We check if the `result` variable is equal to the number itself using `if (result == num)`.
12. If the `result` variable is equal to the number itself, we print the number using `printf("%d\n", num)`.
13. We reset the `result` variable to 0 for the next iteration of the loop.
14. We continue the loop until all the numbers from 1 to 100 have been checked.
15. We return 0 to indicate that the program has executed successfully.

By following these steps, we can write a C program to print all the Armstrong numbers from 1 to 100.