## 7. WAP to find the greatest of three numbers.

- A program to find the greatest of three numbers is a common problem that can be solved using conditional statements, such as if-else or switch-case.
- The basic logic is to compare the three numbers and find the one that is larger than the other two.
- The program can be written in different programming languages, such as C, C++, Java, Python, etc. Here is an example of how to write the program in C:

```c
// include the header file for input/output functions
#include <stdio.h>

// define the main function
int main()
{
    // declare three integer variables to store the numbers
    int a, b, c;

    // prompt the user to enter the numbers and read them using scanf function
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    // declare another integer variable to store the greatest number
    int greatest;

    // compare the three numbers using if-else statements and assign the greatest one to the variable
    if (a > b && a > c)
    {
        greatest = a;
    }
    else if (b > a && b > c)
    {
        greatest = b;
    }
    else
    {
        greatest = c;
    }

    // print the result using printf function
    printf("The greatest number is %d\n", greatest);

    // return 0 to indicate successful execution
    return 0;
}
```
- The program can be tested with different inputs and outputs, such as:

```
Enter three numbers: 10 20 30
The greatest number is 30
```

```
Enter three numbers: 50 40 50
The greatest number is 50
```

```
Enter three numbers: -5 -10 -15
The greatest number is -5
```
- The program can also be written using switch-case statements, which are another way of implementing conditional logic. Here is an example of how to write the program using switch-case in C:

```c
// include the header file for input/output functions
#include <stdio.h>

// define the main function
int main()
{
    // declare three integer variables to store the numbers
    int a, b, c;

    // prompt the user to enter the numbers and read them using scanf function
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    // declare another integer variable to store the greatest number
    int greatest;

    // compare the three numbers using switch-case statements and assign the greatest one to the variable
    switch (a > b)
    {
        case 1: // if a is greater than b, compare a and c
            switch (a > c)
            {
                case 1: // if a is greater than c, a is the greatest
                    greatest = a;
                    break;
                case 0: // if a is not greater than c, c is the greatest
                    greatest = c;
                    break;
            }
            break;
        case 0: // if a is not greater than b, compare b and c
            switch (b > c)
            {
                case 1: // if b is greater than c, b is the greatest
                    greatest = b;
                    break;
                case 0: // if b is not greater than c, c is the greatest
                    greatest = c;
                    break;
            }
            break;
    }

    // print the result using printf function
    printf("The greatest number is %d\n", greatest);

    // return 0 to indicate successful execution
    return 0;
}
```
- The program can be tested with the same inputs and outputs as the previous one.