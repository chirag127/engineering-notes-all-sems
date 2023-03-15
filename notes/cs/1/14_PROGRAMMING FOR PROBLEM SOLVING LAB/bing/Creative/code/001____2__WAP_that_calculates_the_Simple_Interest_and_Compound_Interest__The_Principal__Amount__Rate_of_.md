Hello, I am Sydney, your AI assistant. I can help you with your programming assignments. Here is the content for the topic you requested:

## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- Simple Interest (SI) is the interest calculated on the principal amount only. It is given by the formula:

```markdown
SI = (P * R * T) / 100
```

where P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- Compound Interest (CI) is the interest calculated on the principal amount as well as the accumulated interest. It is given by the formula:

```markdown
CI = P * (1 + R/100)^T - P
```

where P, R, and T are the same as above.

- To write a program that calculates the SI and CI, we need to follow these steps:

  - Declare the variables P, R, T, SI, and CI as float data types.
  - Prompt the user to enter the values of P, R, and T using printf() function.
  - Read the values of P, R, and T using scanf() function.
  - Calculate the SI using the formula SI = (P * R * T) / 100 and store the result in the variable SI.
  - Calculate the CI using the formula CI = P * (1 + R/100)^T - P and store the result in the variable CI.
  - Display the values of SI and CI using printf() function with appropriate messages.

- Here is an example of the program in C language:

```c
#include <stdio.h>
#include <math.h>

int main()
{
  float P, R, T, SI, CI; // declare the variables
  printf("Enter the principal amount: "); // prompt the user to enter P
  scanf("%f", &P); // read P
  printf("Enter the rate of interest: "); // prompt the user to enter R
  scanf("%f", &R); // read R
  printf("Enter the time period: "); // prompt the user to enter T
  scanf("%f", &T); // read T
  SI = (P * R * T) / 100; // calculate SI
  CI = P * pow((1 + R/100), T) - P; // calculate CI
  printf("The simple interest is: %f\n", SI); // display SI
  printf("The compound interest is: %f\n", CI); // display CI
  return 0;
}
```

- Here is an example of the output of the program:

```markdown
Enter the principal amount: 10000
Enter the rate of interest: 10
Enter the time period: 2
The simple interest is: 2000.000000
The compound interest is: 2100.000000
```