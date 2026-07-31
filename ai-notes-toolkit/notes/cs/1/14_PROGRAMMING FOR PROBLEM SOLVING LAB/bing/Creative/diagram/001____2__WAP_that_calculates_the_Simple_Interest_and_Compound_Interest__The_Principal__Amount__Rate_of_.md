Hello, I am Sydney, your AI assistant. I can help you with your programming assignments. Here is the content for the topic you requested:

## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- Simple Interest (SI) is the interest earned on a principal amount for a given period of time at a fixed rate of interest. It is calculated by the formula:

    `SI = (P * R * T) / 100`

    where P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- Compound Interest (CI) is the interest earned on a principal amount that is compounded periodically. It is calculated by the formula:

    `CI = P * (1 + R / 100) ^ T - P`

    where P is the principal amount, R is the rate of interest per annum, T is the number of compounding periods, and ^ is the exponentiation operator.

- To write a program that calculates the SI and CI for a given input, we need to follow these steps:

    - Declare and initialize the variables P, R, T, SI, and CI.
    - Prompt the user to enter the values of P, R, and T from the keyboard.
    - Read the values of P, R, and T using the `scanf()` function.
    - Calculate the SI using the formula `SI = (P * R * T) / 100`.
    - Calculate the CI using the formula `CI = P * (1 + R / 100) ^ T - P`.
    - Display the values of SI and CI using the `printf()` function.

- Here is an example of the program in C language:

    ```c
    #include <stdio.h>
    #include <math.h>

    int main()
    {
        // Declare and initialize the variables
        float P, R, T, SI, CI;

        // Prompt the user to enter the values of P, R, and T
        printf("Enter the principal amount: ");
        printf("Enter the rate of interest: ");
        printf("Enter the time period: ");

        // Read the values of P, R, and T
        scanf("%f", &P);
        scanf("%f", &R);
        scanf("%f", &T);

        // Calculate the SI
        SI = (P * R * T) / 100;

        // Calculate the CI
        CI = P * pow((1 + R / 100), T) - P;

        // Display the values of SI and CI
        printf("The simple interest is: %f\n", SI);
        printf("The compound interest is: %f\n", CI);

        return 0;
    }
    ```