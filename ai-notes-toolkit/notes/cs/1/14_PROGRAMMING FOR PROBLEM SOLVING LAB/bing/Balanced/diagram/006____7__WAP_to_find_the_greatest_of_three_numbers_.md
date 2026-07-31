Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to find the greatest of three numbers. Here is the content in markdown format:

## 7. WAP to find the greatest of three numbers.

- To find the greatest of three numbers, we need to compare them using some conditional statements, such as `if`, `else if`, and `else`.
- We can use the `>` operator to check if one number is greater than another.
- We can use the `=` operator to check if two numbers are equal.
- We can use the `&&` operator to combine two conditions with a logical AND.
- We can use the `||` operator to combine two conditions with a logical OR.
- We can use the `!` operator to negate a condition with a logical NOT.
- Here is the algorithm to find the greatest of three numbers:

```
Step 1: Start
Step 2: Declare three variables a, b, and c and assign them some values
Step 3: If a > b and a > c, then print a is the greatest
Step 4: Else if b > a and b > c, then print b is the greatest
Step 5: Else if c > a and c > b, then print c is the greatest
Step 6: Else if a = b and a > c, then print a and b are the greatest
Step 7: Else if a = c and a > b, then print a and c are the greatest
Step 8: Else if b = c and b > a, then print b and c are the greatest
Step 9: Else print all three numbers are equal
Step 10: Stop
```

- Here is the pseudocode to find the greatest of three numbers:

```
INPUT a, b, c
IF a > b AND a > c THEN
    OUTPUT a is the greatest
ELSE IF b > a AND b > c THEN
    OUTPUT b is the greatest
ELSE IF c > a AND c > b THEN
    OUTPUT c is the greatest
ELSE IF a = b AND a > c THEN
    OUTPUT a and b are the greatest
ELSE IF a = c AND a > b THEN
    OUTPUT a and c are the greatest
ELSE IF b = c AND b > a THEN
    OUTPUT b and c are the greatest
ELSE
    OUTPUT all three numbers are equal
END IF
```

- Here is the code to find the greatest of three numbers in C language:

```c
#include <stdio.h>
int main()
{
    int a, b, c;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    if (a > b && a > c)
    {
        printf("%d is the greatest\n", a);
    }
    else if (b > a && b > c)
    {
        printf("%d is the greatest\n", b);
    }
    else if (c > a && c > b)
    {
        printf("%d is the greatest\n", c);
    }
    else if (a == b && a > c)
    {
        printf("%d and %d are the greatest\n", a, b);
    }
    else if (a == c && a > b)
    {
        printf("%d and %d are the greatest\n", a, c);
    }
    else if (b == c && b > a)
    {
        printf("%d and %d are the greatest\n", b, c);
    }
    else
    {
        printf("All three numbers are equal\n");
    }
    return 0;
}
```

- Here is the output of the program for some sample inputs:

```
Enter three numbers: 10 20 30
30 is the greatest

Enter three numbers: 50 50 40
50 and 50 are the greatest

Enter three numbers: 60 60 60
All three numbers are equal
```
