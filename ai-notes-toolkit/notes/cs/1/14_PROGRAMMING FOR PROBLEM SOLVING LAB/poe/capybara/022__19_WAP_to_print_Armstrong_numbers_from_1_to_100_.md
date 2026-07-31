## 19. WAP to print Armstrong numbers from 1 to 100.

Here are the key points to keep in mind when writing a program to print Armstrong numbers from 1 to 100:

- An Armstrong number is a number such that the sum of its digits raised to the power of the number of digits is equal to the original number. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

- To check if a number is an Armstrong number, you need to find the number of digits in the number and then raise each digit to the power of the number of digits and add them up. If the result is equal to the original number, then it is an Armstrong number.

- You can use a loop to check all the numbers from 1 to 100 and print out the Armstrong numbers.

- To find the number of digits in a number, you can use the log10 function. This function returns the number of digits in a number when you take the logarithm of the number to base 10 and add 1.

- To raise a number to a power, you can use the pow function. This function takes two arguments: the base and the exponent.

- Here's an example program that prints out all the Armstrong numbers from 1 to 100:

```c
#include <stdio.h>
#include <math.h>

int main() {
  int i, n, num, digit, sum;

  for (i = 1; i <= 100; i++) {
    n = 0;
    num = i;
    while (num != 0) {
      digit = num % 10;
      n++;
      num /= 10;
    }
    num = i;
    sum = 0;
    while (num != 0) {
      digit = num % 10;
      sum += pow(digit, n);
      num /= 10;
    }
    if (sum == i) {
      printf("%d\n", i);
    }
  }

  return 0;
}
```

- In this program, we first declare some variables: i for the loop counter, n for the number of digits, num for the original number, digit for the current digit, and sum for the sum of the digits raised to the power of n.

- We then use a for loop to check all the numbers from 1 to 100. Inside the loop, we first set n to 0 and num to the current number. We then use a while loop to count the number of digits in num and store it in n.

- We then reset num to the current number and use another while loop to calculate the sum of the digits raised to the power of n. We use the pow function to raise each digit to the power of n and add it to the sum.

- Finally, we check if the sum is equal to the original number and print it out if it is.

- To run the program, save it as a .c file and compile it using a C compiler. Then run the executable to see the Armstrong numbers from 1 to 100 printed out.