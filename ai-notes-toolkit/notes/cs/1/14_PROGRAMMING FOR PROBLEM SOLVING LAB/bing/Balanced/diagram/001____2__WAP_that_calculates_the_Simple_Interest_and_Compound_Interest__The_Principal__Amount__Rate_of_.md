Hello, I am Sydney, your AI assistant. I can help you with your programming assignments. Here is the content for the topic you requested:

## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- Simple Interest (SI) is the interest earned on a principal amount (P) at a fixed rate of interest (R) per year for a fixed period of time (T). The formula for SI is:

  ```
  SI = (P * R * T) / 100
  ```

- Compound Interest (CI) is the interest earned on a principal amount (P) at a fixed rate of interest (R) per year, compounded annually, for a fixed period of time (T). The formula for CI is:

  ```
  CI = P * (1 + R/100)^T - P
  ```

- To write a program that calculates the SI and CI, we need to:

  - Declare four variables of type float to store the values of P, R, T and A (amount).
  - Use the `scanf` function to read the values of P, R and T from the keyboard.
  - Use the formulas for SI and CI to calculate the values of SI and CI and store them in two more variables of type float.
  - Use the `printf` function to display the values of SI and CI on the screen.
  - End the program with a `return 0` statement.

- Here is an example of the program in C language:

  ```c
  #include <stdio.h>
  #include <math.h>

  int main()
  {
    float P, R, T, A, SI, CI; // declare variables
    printf("Enter the principal amount: "); // prompt for P
    scanf("%f", &P); // read P
    printf("Enter the rate of interest: "); // prompt for R
    scanf("%f", &R); // read R
    printf("Enter the time period: "); // prompt for T
    scanf("%f", &T); // read T
    SI = (P * R * T) / 100; // calculate SI
    CI = P * pow((1 + R/100), T) - P; // calculate CI
    printf("The simple interest is: %.2f\n", SI); // display SI
    printf("The compound interest is: %.2f\n", CI); // display CI
    return 0; // end program
  }
  ```