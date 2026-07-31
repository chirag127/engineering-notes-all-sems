## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

Simple interest is calculated using the formula `Simple Interest = (Principal * Rate of Interest * Time) / 100`. Compound interest is calculated using the formula `Compound Interest = Principal * (1 + Rate of Interest/100)^(Time) - Principal`.

Here is an example of a program in C language that calculates the Simple Interest and Compound Interest:

```c
#include <stdio.h>
#include <math.h>

int main()
{
    float principal, rate, time, simple_interest, compound_interest;

    printf("Enter the Principal: ");
    scanf("%f", &principal);

    printf("Enter the Rate of Interest: ");
    scanf("%f", &rate);

    printf("Enter the Time: ");
    scanf("%f", &time);

    simple_interest = (principal * rate * time) / 100;
    compound_interest = principal * pow((1 + rate/100), time) - principal;

    printf("Simple Interest: %.2f\n", simple_interest);
    printf("Compound Interest: %.2f\n", compound_interest);

    return 0;
}
```

This program prompts the user to enter the Principal, Rate of Interest and Time. It then calculates the Simple Interest and Compound Interest using the respective formulas and displays the result. The `pow()` function from the `math.h` library is used to calculate the power of a number.