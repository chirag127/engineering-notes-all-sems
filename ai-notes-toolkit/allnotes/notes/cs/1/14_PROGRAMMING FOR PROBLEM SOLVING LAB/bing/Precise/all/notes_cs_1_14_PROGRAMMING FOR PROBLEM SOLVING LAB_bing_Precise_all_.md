

## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

A WAP (Write a Program) is a common term used in computer science and programming to refer to the task of writing a computer program to solve a specific problem or perform a specific task.

In this case, the WAP is to write a program that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student. Here are the steps to solve this problem:

1. Define a variable to store the marks of each subject.
2. Accept the marks of 5 subjects from the user and store them in the respective variables.
3. Calculate the sum of the marks by adding the marks of all 5 subjects.
4. Calculate the percentage marks by dividing the sum of the marks by the total marks and multiplying by 100.
5. Display the sum and percentage marks obtained by the student.

Here is an example of a program written in Python that solves this problem:

```python
# Define variables to store the marks of each subject
subject1 = 0
subject2 = 0
subject3 = 0
subject4 = 0
subject5 = 0

# Accept the marks of 5 subjects from the user
subject1 = int(input("Enter the marks of subject 1: "))
subject2 = int(input("Enter the marks of subject 2: "))
subject3 = int(input("Enter the marks of subject 3: "))
subject4 = int(input("Enter the marks of subject 4: "))
subject5 = int(input("Enter the marks of subject 5: "))

# Calculate the sum of the marks
sum_of_marks = subject1 + subject2 + subject3 + subject4 + subject5

# Calculate the percentage marks
percentage_marks = (sum_of_marks / 500) * 100

# Display the sum and percentage marks obtained by the student
print("Sum of marks: ", sum_of_marks)
print("Percentage marks: ", percentage_marks)
```

This program accepts the marks of 5 subjects from the user, calculates the sum and percentage marks, and displays the result. The user can run this program and enter the marks of the 5 subjects to find the sum and percentage marks obtained by the student.



## 2. WAP that calculates the Simple Interest and Compound Interest

Simple Interest and Compound Interest are two methods of calculating the interest on a principal amount over a period of time. The main difference between the two is the frequency of interest calculation.

Simple Interest is calculated only on the initial principal amount, whereas Compound Interest is calculated on the initial principal and also on the accumulated interest of previous periods.

Here is an example of a program that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest, and Time are entered through the keyboard.

```python
# Python program to calculate Simple Interest and Compound Interest

# Taking input from the user
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of Interest: "))
T = float(input("Enter the Time in years: "))

# Calculating Simple Interest
SI = (P * R * T) / 100
print("Simple Interest: ", SI)

# Calculating Compound Interest
CI = P * (pow((1 + R / 100), T))
print("Compound Interest: ", CI)
```

In the above program, the user is prompted to enter the Principal amount, Rate of Interest, and Time in years. The program then calculates the Simple Interest and Compound Interest using the respective formulas and displays the result.

Simple Interest is calculated using the formula `SI = (P * R * T) / 100`, where `P` is the Principal amount, `R` is the Rate of Interest, and `T` is the Time in years.

Compound Interest is calculated using the formula `CI = P * (pow((1 + R / 100), T))`, where `P` is the Principal amount, `R` is the Rate of Interest, and `T` is the Time in years.

This program can be modified to include additional features such as the ability to choose the frequency of compounding (e.g. annually, semi-annually, quarterly, etc.) and the ability to calculate the final amount after the interest has been applied.



## 3. WAP to calculate the area and circumference of a circle.

The area of a circle is calculated using the formula `A = πr^2`, where `A` is the area, `π` is approximately equal to 3.14, and `r` is the radius of the circle.

The circumference of a circle is calculated using the formula `C = 2πr`, where `C` is the circumference, `π` is approximately equal to 3.14, and `r` is the radius of the circle.

Here is an example of a program that calculates the area and circumference of a circle with a given radius:

```python
import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
```

This program prompts the user to enter the radius of the circle, then calculates the area and circumference using the formulas above and displays the results.



## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

Here is a program that accepts the temperature in Centigrade and converts it into Fahrenheit using the formula C/5=(F-32)/9:

```python
# Accept the temperature in Centigrade
C = float(input("Enter the temperature in Centigrade: "))

# Convert the temperature into Fahrenheit using the formula C/5=(F-32)/9
F = (C * 9/5) + 32

# Print the temperature in Fahrenheit
print("The temperature in Fahrenheit is:", F)
```

This program prompts the user to enter the temperature in Centigrade. It then converts the temperature into Fahrenheit using the formula C/5=(F-32)/9 and prints the result.

To use this program, the user needs to enter the temperature in Centigrade when prompted. The program will then calculate and display the temperature in Fahrenheit.

For example, if the user enters 25 as the temperature in Centigrade, the program will calculate the temperature in Fahrenheit as (25 * 9/5) + 32 = 77.0 and display the result as "The temperature in Fahrenheit is: 77.0".



## 5. WAP that swaps values of two variables using a third variable.

Swapping the values of two variables means exchanging their values. For example, if variable `a` has the value `5` and variable `b` has the value `10`, after swapping, variable `a` will have the value `10` and variable `b` will have the value `5`.

Here is an example of a program that swaps the values of two variables using a third variable in the C programming language:

```c
#include <stdio.h>

int main()
{
    int a = 5, b = 10, temp;

    printf("Before swapping: a = %d, b = %d\n", a, b);

    temp = a;
    a = b;
    b = temp;

    printf("After swapping: a = %d, b = %d\n", a, b);

    return 0;
}
```

In this program, we first declare three integer variables `a`, `b`, and `temp`. We assign the values `5` and `10` to `a` and `b` respectively. We then print the values of `a` and `b` before swapping.

Next, we use the `temp` variable to temporarily store the value of `a`. We then assign the value of `b` to `a` and the value of `temp` (which is the original value of `a`) to `b`. This effectively swaps the values of `a` and `b`.

Finally, we print the values of `a` and `b` after swapping.

This is one way to swap the values of two variables using a third variable. There are other ways to achieve the same result, such as using arithmetic operations or bitwise operations, but using a third variable is a simple and straightforward method.



## 6. WAP that checks whether the two numbers entered by the user are equal or not.

A WAP (Write a Program) is a common term used to describe the task of writing a computer program to solve a specific problem or perform a specific task. In this case, the task is to write a program that checks whether two numbers entered by the user are equal or not.

Here is one way to write such a program in the Python programming language:

```python
# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the numbers are equal
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
```

This program takes two numbers as input from the user and stores them in the variables `num1` and `num2`. It then uses an `if` statement to check if the two numbers are equal. If they are equal, it prints a message saying that the numbers are equal. Otherwise, it prints a message saying that the numbers are not equal.

This is just one way to write a program that checks whether two numbers entered by the user are equal or not. There are many other ways to write such a program, and the specific details of the program may vary depending on the programming language used and the specific requirements of the task.



## 7. WAP to find the greatest of three numbers.

To find the greatest of three numbers, we can use the following algorithm:

1. Take three numbers as input from the user.
2. Compare the first two numbers and store the greater number in a variable.
3. Compare the third number with the variable and update the variable if the third number is greater.
4. The variable now contains the greatest of the three numbers.

Here is an example of a program in Python that implements this algorithm:

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2:
    greatest = num1
else:
    greatest = num2

if num3 > greatest:
    greatest = num3

print("The greatest of the three numbers is:", greatest)
```

This program takes three numbers as input from the user and compares them to find the greatest number. The result is then printed to the screen. This program can be easily modified to find the greatest of any number of numbers.



## 8. WAP that finds whether a given number is even or odd.

A WAP (Write a Program) that finds whether a given number is even or odd can be written in many programming languages. Here is an example of how it can be done in Python:

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
```

In this program, the user is prompted to enter a number. The number is then stored in the variable `num`. The `if` statement checks if the remainder of the number when divided by 2 is equal to 0. If it is, the number is even and the program prints that the number is even. If the remainder is not equal to 0, the number is odd and the program prints that the number is odd.

This program can be modified to work with different programming languages and can be expanded to include additional functionality. For example, the program could be modified to check if the number is positive or negative, or if it is a prime number. The possibilities are endless.



## 9. WAP that tells whether a given year is a leap year or not.

A leap year is a year that is divisible by 4, except for end-of-century years which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

Here is an example of a program that checks whether a given year is a leap year or not:

```python
year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))
```

This program takes a year as input from the user and checks whether it is a leap year or not using the conditions mentioned above. If the year is a leap year, it prints a message stating that the year is a leap year, otherwise, it prints a message stating that the year is not a leap year.



## 10. WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

1. First, the program should accept the marks of five subjects as input from the user.
2. Then, the program should calculate the total marks obtained by the user by adding the marks of all five subjects.
3. Next, the program should calculate the percentage of marks obtained by the user by dividing the total marks by the maximum possible marks and multiplying the result by 100.
4. Finally, the program should print the grade of the user according to the following criteria:
    - If the percentage is greater than or equal to 90, the grade is 'A'.
    - If the percentage is greater than or equal to 80 and less than 90, the grade is 'B'.
    - If the percentage is greater than or equal to 70 and less than 80, the grade is 'C'.
    - If the percentage is greater than or equal to 60 and less than 70, the grade is 'D'.
    - If the percentage is less than 60, the grade is 'F'.



## Between 90-100%-----Print ‘A’

- This statement is often used in the context of grading systems, where a percentage score between 90 and 100 corresponds to a grade of 'A'.
- The percentage score represents the proportion of total points earned out of the total possible points.
- A score between 90 and 100 percent indicates that the student has achieved a high level of mastery of the material and has demonstrated exceptional performance.
- The grade of 'A' is typically the highest grade that can be awarded, and is often associated with excellence and outstanding achievement.
- Different institutions may have slightly different grading scales, but a score between 90 and 100 percent is generally considered to be within the 'A' range.



## 80-90% - Print 'B'

- The given topic appears to be related to a grading system where a score between 80-90% is represented by the letter 'B'.
- In many educational systems, grades are represented by letters, with 'A' being the highest and 'F' being the lowest.
- A score of 80-90% would typically be considered above average and would indicate a good understanding of the material being tested.
- The exact meaning and value of a 'B' grade can vary depending on the specific grading system and the context in which it is used.
- It is important to understand the grading system being used in order to accurately interpret the meaning of a 'B' grade.



## 60-80%-----------------Print ‘C’

- The percentage range of 60-80% is often used as a threshold for determining a passing grade or satisfactory performance in many academic or professional settings.
- In this context, the instruction to "Print 'C'" could refer to the output of a program or script that evaluates a student or employee's performance and assigns a letter grade based on their score falling within the 60-80% range.
- The letter grade 'C' is generally considered to represent average or satisfactory performance, and is often used as a baseline for determining whether a student or employee has met the minimum requirements for passing a course or evaluation.
- It is important to note that grading scales and performance standards can vary widely between different institutions and organizations, and the specific meaning and implications of a 'C' grade may differ depending on the context in which it is used.



## Below 60%-------------Print ‘D’

- This statement appears to be a conditional statement that specifies an action to be taken when a certain condition is met.
- In this case, the condition is that a certain value or variable is below 60%.
- If this condition is met, the specified action is to print the letter 'D'.
- This type of statement is commonly used in programming languages to control the flow of a program based on certain conditions.
- The exact syntax and usage of this statement may vary depending on the specific programming language being used.



## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

A switch statement is a control structure that allows us to choose which statement to execute next. It is an alternative to the if-else-if ladder statement. The switch statement evaluates an expression and executes the corresponding case that matches the expression's value.

Here is an example of a program that takes two operands and one operator from the user, performs the operation, and prints the result by using a switch statement:

```c
#include <stdio.h>

int main()
{
    double num1, num2;
    char operator;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);

    printf("Enter two operands: ");
    scanf("%lf %lf", &num1, &num2);

    switch(operator)
    {
        case '+':
            printf("%.1lf + %.1lf = %.1lf", num1, num2, num1 + num2);
            break;

        case '-':
            printf("%.1lf - %.1lf = %.1lf", num1, num2, num1 - num2);
            break;

        case '*':
            printf("%.1lf * %.1lf = %.1lf", num1, num2, num1 * num2);
            break;

        case '/':
            printf("%.1lf / %.1lf = %.1lf", num1, num2, num1 / num2);
            break;

        default:
            printf("Error! operator is not correct");
    }

    return 0;
}
```

In this program, the user is prompted to enter an operator and two operands. The operator is stored in the `operator` variable and the operands are stored in the `num1` and `num2` variables.

The switch statement then evaluates the `operator` variable and executes the corresponding case that matches the value of the `operator` variable. If the `operator` variable is `'+'`, the case `case '+'` is executed and the result of the addition of `num1` and `num2` is printed. Similarly, if the `operator` variable is `'-'`, the case `case '-'` is executed and the result of the subtraction of `num1` and `num2` is printed.

If the `operator` variable does not match any of the cases, the `default` case is executed and an error message is printed.

This is how you can use a switch statement to take two operands and one operator from the user, perform the operation, and print the result. You can modify the code to add more cases and operators as per your requirements.



## 12. WAP to print the sum of all numbers up to a given number.

Here is a program that can be used to print the sum of all numbers up to a given number:

```python
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of all numbers up to", n, "is", sum)
```

- The program starts by taking an input from the user and storing it in the variable `n`.
- The variable `sum` is initialized to 0.
- A `for` loop is used to iterate over the range of numbers from 1 to `n+1`.
- In each iteration, the value of `i` is added to the `sum` variable.
- After the loop is completed, the final value of `sum` is printed, which is the sum of all numbers up to `n`.

This program can be used to calculate the sum of all numbers up to any given number. It is a simple and efficient way to solve this problem.



## 13. WAP to find the factorial of a given number.

Factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, the factorial of 5 is 120, or 5! = 5 × 4 × 3 × 2 × 1 = 120.

Here is an example of a program that calculates the factorial of a given number:

```python
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"The factorial of {n} is {factorial}")
```

This program prompts the user to enter a number, then checks if the number is negative, zero, or positive. If the number is negative, the program prints an error message. If the number is zero, the program prints that the factorial of 0 is 1. If the number is positive, the program calculates the factorial by multiplying all the numbers from 1 to the entered number, then prints the result.



## 14. WAP to print sum of even and odd numbers from 1 to N numbers.

Here is a program that calculates the sum of even and odd numbers from 1 to N numbers:

```python
N = int(input("Enter the value of N: "))

even_sum = 0
odd_sum = 0

for i in range(1, N+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
```

- The program prompts the user to enter the value of N.
- Two variables, `even_sum` and `odd_sum`, are initialized to 0 to store the sum of even and odd numbers, respectively.
- A for loop is used to iterate over the range of numbers from 1 to N.
- Inside the loop, an if-else statement is used to check if the current number is even or odd.
- If the number is even, it is added to the `even_sum` variable. Otherwise, it is added to the `odd_sum` variable.
- After the loop, the sum of even and odd numbers is printed.

This program can be used to calculate the sum of even and odd numbers from 1 to any given value of N. It can be modified to perform other calculations as well.



## 15. WAP to print the Fibonacci series

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding numbers. The simplest Fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

Here is an example of a program that prints the Fibonacci series:

```python
n = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence upto", n, ":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
```

This program prompts the user to enter the number of terms in the Fibonacci series to be printed. It then uses a while loop to calculate and print the Fibonacci series up to the specified number of terms.

The program initializes two variables, `n1` and `n2`, to 0 and 1, respectively. These variables represent the first two terms of the Fibonacci series. The program also initializes a variable `count` to 0 to keep track of the number of terms printed.

The program then checks if the number of terms entered by the user is less than or equal to 0. If it is, the program prints an error message asking the user to enter a positive integer.

If the number of terms entered by the user is 1, the program prints the first term of the Fibonacci series, which is 0.

If the number of terms entered by the user is greater than 1, the program enters a while loop that continues until the specified number of terms have been printed. In each iteration of the loop, the program prints the value of `n1`, calculates the next term in the series by adding `n1` and `n2`, and updates the values of `n1` and `n2`. The program also increments the `count` variable to keep track of the number of terms printed.

This program can be modified to print the Fibonacci series in different ways, such as using a for loop or using recursion. It can also be modified to perform other operations on the Fibonacci series, such as finding the sum of the first n terms or finding the nth term in the series.



## 16. WAP to check whether the entered number is prime or not.

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. To check if a number is prime or not, we can follow these steps:

1. Take input from the user and store it in a variable.
2. Initialize a flag variable to 0.
3. Run a loop from 2 to the square root of the entered number.
4. Check if the entered number is divisible by the loop variable.
5. If it is divisible, set the flag variable to 1 and break the loop.
6. After the loop, check the value of the flag variable.
7. If the flag variable is 0, the entered number is prime. Otherwise, it is not prime.

Here is an example code in C language that implements the above algorithm:

```c
#include <stdio.h>
#include <math.h>

int main()
{
    int n, i, flag = 0;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    for(i = 2; i <= sqrt(n); i++)
    {
        if(n % i == 0)
        {
            flag = 1;
            break;
        }
    }

    if (n <= 1)
        printf("%d is not a prime number.", n);
    else
    {
        if (flag == 0)
            printf("%d is a prime number.", n);
        else
            printf("%d is not a prime number.", n);
    }

    return 0;
}
```



## 17. WAP to find the sum of digits of the entered number.

1. To find the sum of digits of a number, we can use a while loop to iterate through each digit of the number.
2. First, initialize a variable to store the sum of the digits, for example `sum = 0`.
3. Then, use a while loop to iterate through each digit of the number. In each iteration, use the modulo operator `%` to obtain the last digit of the number, add it to the sum, and then remove the last digit from the number by dividing it by 10.
4. Continue this process until the number becomes 0.
5. The final value of the `sum` variable will be the sum of the digits of the entered number.

Here is an example of the code in Python:

```python
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10
print("The sum of the digits is:", sum)
```

This code prompts the user to enter a number, and then uses a while loop to calculate the sum of its digits. The result is then printed to the screen.



## 18. WAP to find the reverse of a number

Here is an algorithm to find the reverse of a number:

1. Initialize a variable `rev` to 0, which will store the reverse of the number.
2. While the number is greater than 0, repeat the following steps:
    1. Multiply `rev` by 10 and add the last digit of the number to it.
    2. Remove the last digit from the number by dividing it by 10.
3. `rev` now contains the reverse of the original number.

Here is an example of a program in C language that implements the above algorithm:

```c
#include <stdio.h>

int main()
{
    int n, rev = 0, remainder;
    printf("Enter an integer: ");
    scanf("%d", &n);
    while (n != 0)
    {
        remainder = n % 10;
        rev = rev * 10 + remainder;
        n /= 10;
    }
    printf("Reversed number = %d", rev);
    return 0;
}
```

This program takes an integer as input from the user and stores it in the variable `n`. The `while` loop runs until `n` is not equal to 0. In each iteration of the loop, the last digit of `n` is obtained using the modulus operator (`%`) and added to `rev` after multiplying `rev` by 10. Then, the last digit is removed from `n` by dividing it by 10. Finally, the reversed number is printed using the `printf` function.



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



## 20. WAP to convert binary number into decimal number and vice versa.

Converting a binary number into a decimal number involves taking the binary digits (bits) and calculating their respective place values. Here is an example of how to convert the binary number `1011` into a decimal number:

1. Start with the rightmost digit (in this case, `1`). This digit has a place value of 2^0, or 1. So, the value of this digit is 1 * 1 = 1.
2. Move to the next digit to the left (in this case, `1`). This digit has a place value of 2^1, or 2. So, the value of this digit is 1 * 2 = 2.
3. Move to the next digit to the left (in this case, `0`). This digit has a place value of 2^2, or 4. So, the value of this digit is 0 * 4 = 0.
4. Move to the next digit to the left (in this case, `1`). This digit has a place value of 2^3, or 8. So, the value of this digit is 1 * 8 = 8.
5. Add up all the values calculated for each digit: 1 + 2 + 0 + 8 = 11. So, the binary number `1011` is equivalent to the decimal number `11`.

Converting a decimal number into a binary number involves repeatedly dividing the decimal number by 2 and keeping track of the remainders. Here is an example of how to convert the decimal number `11` into a binary number:

1. Divide 11 by 2. The quotient is 5 and the remainder is 1. Write down the remainder (1).
2. Divide 5 by 2. The quotient is 2 and the remainder is 1. Write down the remainder (1).
3. Divide 2 by 2. The quotient is 1 and the remainder is 0. Write down the remainder (0).
4. Divide 1 by 2. The quotient is 0 and the remainder is 1. Write down the remainder (1).
5. Since the quotient is now 0, the process is complete. The remainders, read from bottom to top, form the binary number `1011`. So, the decimal number `11` is equivalent to the binary number `1011`.



## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

Here is a program that takes elements of an array from the user and finds the sum of these elements:

```python
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)
sum = 0
for i in arr:
    sum += i
print("The sum of the elements in the array is:", sum)
```

This program first takes the number of elements in the array as input from the user. Then, it takes the elements of the array one by one from the user and stores them in a list. After that, it initializes a variable `sum` to 0 and iterates over the elements of the list, adding each element to the `sum` variable. Finally, it prints the sum of the elements in the array.



## 22. WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

Here is an example of a program that inputs two arrays and saves the sum of corresponding elements of these arrays in a third array and prints them:

```python
# Input the length of the arrays
n = int(input("Enter the length of the arrays: "))

# Initialize the arrays
arr1 = [0] * n
arr2 = [0] * n
arr3 = [0] * n

# Input the elements of the first array
print("Enter the elements of the first array: ")
for i in range(n):
    arr1[i] = int(input())

# Input the elements of the second array
print("Enter the elements of the second array: ")
for i in range(n):
    arr2[i] = int(input())

# Calculate the sum of corresponding elements and store in the third array
for i in range(n):
    arr3[i] = arr1[i] + arr2[i]

# Print the third array
print("The third array is: ")
for i in range(n):
    print(arr3[i])
```

This program first inputs the length of the arrays and initializes them. Then, it inputs the elements of the first and second arrays. After that, it calculates the sum of corresponding elements of the first and second arrays and stores the result in the third array. Finally, it prints the third array.



## 23. WAP to find the minimum and maximum element of the array

Here is an example of a program that finds the minimum and maximum element of an array:

```c
#include <stdio.h>

int main() {
    int n, i;
    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements of the array: ");
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    int min = arr[0], max = arr[0];
    for (i = 1; i < n; i++) {
        if (arr[i] < min) {
            min = arr[i];
        }
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    printf("The minimum element of the array is %d\n", min);
    printf("The maximum element of the array is %d\n", max);
    return 0;
}
```

This program first prompts the user to enter the number of elements in the array, and then the elements of the array. It then initializes the `min` and `max` variables to the first element of the array. The program then iterates through the rest of the elements in the array, updating the `min` and `max` variables if a smaller or larger element is found, respectively. Finally, the program prints the minimum and maximum elements of the array.



## 24. WAP to search an element in an array using Linear Search

Linear search is a simple search algorithm that can be used to find an element in an array. Here is an example of how to implement linear search in C:

```c
#include <stdio.h>

int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x) {
            return i;
        }
    }
    return -1;
}

int main() {
    int arr[] = {1, 3, 5, 7, 9};
    int n = sizeof(arr) / sizeof(arr[0]);
    int x = 5;
    int result = linearSearch(arr, n, x);
    if (result == -1) {
        printf("Element is not present in array");
    } else {
        printf("Element is present at index %d", result);
    }
    return 0;
}
```

This code defines a function `linearSearch` that takes an array `arr`, the size of the array `n`, and the element to search for `x` as input. The function then iterates over the array and returns the index of the first occurrence of `x` in the array. If `x` is not found in the array, the function returns `-1`.

In the `main` function, we define an array `arr` and its size `n`, and the element to search for `x`. We then call the `linearSearch` function and store the result in the variable `result`. If `result` is `-1`, we print that the element is not present in the array. Otherwise, we print the index at which the element is present.

This is a simple example of how to implement linear search in C. You can modify the code to suit your needs.



## 25. WAP to sort the elements of the array in ascending order using Bubble Sort technique.

Bubble sort is a simple sorting algorithm that compares adjacent elements in an array and swaps them if they are in the wrong order. The algorithm continues to do this until the entire array is sorted in ascending order. Here is an example of how to implement bubble sort in C:

```c
#include <stdio.h>

void bubbleSort(int arr[], int n)
{
    int i, j, temp;
    for (i = 0; i < n-1; i++)
    {
        for (j = 0; j < n-i-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    printf("Sorted array: \n");
    for (int i=0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
```

This code defines a function `bubbleSort` that takes an array of integers and its size as arguments. The function uses two nested loops to iterate over the array. In each iteration, the function compares adjacent elements and swaps them if the first element is greater than the second. This process continues until the entire array is sorted.

The `main` function initializes an array of integers and calls the `bubbleSort` function to sort the array. The sorted array is then printed to the standard output.



## 26. WAP to add and multiply two matrices of order nxn.

### Matrix Addition
To add two matrices of order nxn, we follow these steps:
1. Create a new matrix of order nxn to store the result.
2. Loop through each element of both matrices using nested loops.
3. For each element, add the corresponding elements of both matrices and store the result in the new matrix.
4. Return the resulting matrix.

### Matrix Multiplication
To multiply two matrices of order nxn, we follow these steps:
1. Create a new matrix of order nxn to store the result.
2. Loop through each row of the first matrix using the outer loop.
3. Loop through each column of the second matrix using the second loop.
4. Loop through each element of the current row of the first matrix and the current column of the second matrix using the innermost loop.
5. Multiply the corresponding elements and add the result to a variable.
6. Store the final result in the current element of the resulting matrix.
7. Return the resulting matrix.

Here is an example code in Python that adds and multiplies two matrices of order nxn:

```python
def add_matrices(mat1, mat2, n):
    result = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = mat1[i][j] + mat2[i][j]
    return result

def multiply_matrices(mat1, mat2, n):
    result = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
```

This code defines two functions, `add_matrices` and `multiply_matrices`, that take as input two matrices of order nxn and the order n, and return the resulting matrix after performing the respective operation. The functions use nested loops to iterate over the elements of the matrices and perform the required operations. The resulting matrix is then returned.



## 27. WAP that finds the sum of diagonal elements of a mxn matrix

A matrix is a two-dimensional array of numbers. A diagonal of a matrix is a set of elements that run from one corner of the matrix to the opposite corner. In a square matrix, there are two diagonals: the main diagonal and the secondary diagonal. The main diagonal runs from the top-left corner to the bottom-right corner, while the secondary diagonal runs from the top-right corner to the bottom-left corner.

Here is an example of a program that finds the sum of the diagonal elements of a mxn matrix:

```python
def diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum += matrix[i][j]
    return sum
```

This program defines a function called `diagonal_sum` that takes a matrix as an input. The function first determines the number of rows and columns in the matrix. Then, it initializes a variable called `sum` to 0. The function then uses two nested for loops to iterate over the elements of the matrix. If the row index and the column index are the same, the element is on the main diagonal, and its value is added to the `sum`. Finally, the function returns the value of `sum`.

Here is an example of how to use this function:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = diagonal_sum(matrix)
print(result) # 15
```

In this example, we define a 3x3 matrix and pass it to the `diagonal_sum` function. The function returns the sum of the diagonal elements, which is 15. This value is then printed to the screen.



## 28. WAP to implement strlen(), strcat(), strcpy() using the concept of Functions

`strlen()`, `strcat()`, and `strcpy()` are all functions in the C programming language that operate on strings. Here is an example of how to implement these functions using the concept of functions:

1. `strlen()` function: This function returns the length of a string. Here is an example of how to implement this function:

```c
#include <stdio.h>

int strlen(char *str) {
    int length = 0;
    while (*str != '\0') {
        length++;
        str++;
    }
    return length;
}
```

2. `strcat()` function: This function concatenates two strings. Here is an example of how to implement this function:

```c
#include <stdio.h>

void strcat(char *dest, char *src) {
    while (*dest != '\0') {
        dest++;
    }
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
}
```

3. `strcpy()` function: This function copies a string from one location to another. Here is an example of how to implement this function:

```c
#include <stdio.h>

void strcpy(char *dest, char *src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
}
```

These are the basic implementations of the `strlen()`, `strcat()`, and `strcpy()` functions using the concept of functions in C programming language. These functions can be further optimized and improved based on specific requirements.



## TRAIN_INFO Structure Data Type

A structure data type `TRAIN_INFO` can be defined to store information about a train. The structure can contain the following members:

1. `Train No.`: An integer type member to store the train number.
2. `Train name`: A string type member to store the train name.
3. `Departure Time`: An aggregate type `TIME` to store the departure time of the train.
4. `Arrival Time`: An aggregate type `TIME` to store the arrival time of the train.
5. `Start station`: A string type member to store the name of the start station.
6. `End station`: A string type member to store the name of the end station.

The structure type `TIME` contains two integer members: `hour` and `minute` to represent the time in hours and minutes.

A train timetable can be maintained using an array of `TRAIN_INFO` structures. The following operations can be implemented on the train timetable:

1. **Add a train**: A new train can be added to the timetable by creating a new `TRAIN_INFO` structure and adding it to the array of `TRAIN_INFO` structures.
2. **Search for a train**: A train can be searched in the timetable by its train number or train name.
3. **Update train information**: The information of a train can be updated by modifying the corresponding `TRAIN_INFO` structure in the array of `TRAIN_INFO` structures.
4. **Delete a train**: A train can be deleted from the timetable by removing the corresponding `TRAIN_INFO` structure from the array of `TRAIN_INFO` structures.
5. **Display train information**: The information of all the trains or a specific train can be displayed by accessing the corresponding `TRAIN_INFO` structures in the array of `TRAIN_INFO` structures.



## a. List all the trains (sorted according to train number) that depart from a particular section.

1. To list all the trains that depart from a particular section, one must first identify the section in question.
2. Once the section is identified, one can access the train schedule database to retrieve information about the trains that depart from that section.
3. The retrieved information can then be sorted according to the train number in ascending or descending order.
4. The sorted list of trains can then be presented to the user.

It is important to note that the train schedule database must be up-to-date and accurate in order to provide reliable information to the user. Additionally, the sorting of the train numbers can be done using various sorting algorithms, depending on the specific requirements and constraints of the system.



## b. List all the trains that depart from a particular station at a particular time.

To list all the trains that depart from a particular station at a particular time, you can follow these steps:

1. Navigate to the website or application that provides information about trains between stations.
2. Enter the station name, journey date, and time.
3. Tap on the option to check trains.
4. You will get a list of trains running on a particular route with details of the arrival and departure time .

Alternatively, you can also use a loop to check both the start station and departure time to list all the trains that depart from a particular station at a particular time .



## c. List all the trains that depart from a particular station within the next one hour of a given time.

1. To list all the trains that depart from a particular station within the next one hour of a given time, you can use the railway's official website or app.
2. Enter the station name or code in the search bar and select the station from the drop-down list.
3. Select the date and time for which you want to see the train departures.
4. The website or app will display a list of all the trains that are scheduled to depart from the selected station within the next one hour of the given time.
5. The list will include the train name, number, departure time, and destination.
6. You can also check the availability of seats and book tickets for the desired train from the same platform.



## d. List all the trains between a pair of start station and end station.

To list all the trains between a pair of start and end stations, you can follow these steps:

1. Visit the official website of the railway company or use a third-party train ticket booking website.
2. Enter the start station and end station in the search fields.
3. Select the date of travel.
4. Click on the search button to view the list of trains available between the start and end stations.
5. The list of trains will include information such as train name, train number, departure time, arrival time, travel time, and availability of seats.
6. You can also filter the search results by train type, departure time, arrival time, and travel time to find the most suitable train for your journey.

Note that the availability of trains and the information provided may vary depending on the railway company and the country you are traveling in. It is always a good idea to check the official website of the railway company for the most accurate and up-to-date information.



## 30. WAP to swap two elements using the concept of pointers.

Here is a C program that demonstrates how to swap two elements using the concept of pointers:

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    printf("Before swapping: x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("After swapping: x = %d, y = %d\n", x, y);
    return 0;
}
```

In this program, the `swap` function takes two pointers to integers as arguments. The function uses a temporary variable `temp` to store the value of the first integer, then assigns the value of the second integer to the first integer, and finally assigns the value of `temp` to the second integer. This effectively swaps the values of the two integers.

In the `main` function, we define two integers `x` and `y` and print their values before swapping. Then we call the `swap` function, passing the addresses of `x` and `y` as arguments. This allows the `swap` function to modify the values of `x` and `y` directly. Finally, we print the values of `x` and `y` after swapping.

This program demonstrates how pointers can be used to pass the addresses of variables to a function, allowing the function to modify the values of those variables directly. This is a powerful feature of the C language that allows for more efficient and flexible code.



## 31. WAP to compare the contents of two files and determine whether they are same or not.

Here is a program that compares the contents of two files and determines whether they are the same or not:

```python
def compare_files(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        content1 = f1.read()
        content2 = f2.read()
        if content1 == content2:
            print("The contents of the two files are the same.")
        else:
            print("The contents of the two files are different.")
```

This program defines a function `compare_files` that takes two arguments: `file1` and `file2`, which are the names of the two files to be compared. The function opens both files in read mode using the `with` statement and the `open` function. The contents of the files are read using the `read` method and stored in the variables `content1` and `content2`. The `if` statement is used to compare the contents of the two files. If the contents are the same, a message is printed indicating that the contents of the two files are the same. Otherwise, a message is printed indicating that the contents of the two files are different.

To use this function, you can call it and pass the names of the two files you want to compare as arguments. For example:

```python
compare_files('file1.txt', 'file2.txt')
```

This will compare the contents of the files `file1.txt` and `file2.txt` and print a message indicating whether the contents of the two files are the same or different.



## 32. WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

Here is a Python program that checks whether a given word exists in a file or not. If the word exists, the program also finds the number of times it occurs:

```python
def check_word_in_file(file_name, word):
    with open(file_name, 'r') as file:
        data = file.read()
        words = data.split()
        count = words.count(word)
        if count > 0:
            print(f"The word '{word}' exists in the file '{file_name}' and it occurs {count} times.")
        else:
            print(f"The word '{word}' does not exist in the file '{file_name}'.")
```

To use this function, you need to provide the name of the file and the word you want to search for as arguments. For example, if you want to check if the word "example" exists in a file named "test.txt", you can call the function like this:

```python
check_word_in_file('test.txt', 'example')
```

This program reads the content of the file, splits it into a list of words, and then counts the number of times the given word occurs in the list. If the count is greater than 0, it means the word exists in the file and the program prints the number of times it occurs. Otherwise, it prints that the word does not exist in the file.



## Note:
- A note is a brief record of something that has been written down to assist the memory or for future reference.
- Notes can be written on various mediums, including paper, electronic devices, or even on walls or other surfaces.
- Notes can be used for a variety of purposes, including recording important information, making lists, or jotting down ideas or thoughts.
- Taking notes can be an effective way to retain information and improve memory.
- There are various methods for taking notes, including the Cornell Method, the Outline Method, and the Mapping Method.
- It is important to develop a note-taking system that works for the individual, as everyone has different learning styles and preferences.
- Effective note-taking can improve comprehension, retention, and recall of information.
- Notes can be reviewed and revised to improve understanding and retention of information.



## a) The Instructor may add/delete/modify/tune experiments, wherever he/she feels in a justified manner

- The instructor has the authority to make changes to the experiments in the course.
- These changes can include adding new experiments, deleting existing experiments, modifying the procedure or objectives of the experiments, or tuning the experiments to better fit the course objectives.
- The instructor should make these changes in a justified manner, meaning that the changes should be made for a valid reason and should be beneficial to the students' learning experience.
- The instructor should communicate any changes to the experiments to the students in a timely and clear manner, so that the students are aware of the changes and can prepare accordingly.
- The instructor should also be open to feedback from the students regarding the changes to the experiments, and should take the students' feedback into consideration when making future changes to the experiments.



## b) The subject teachers are suggested to use the concept of project-based learning. The subject teacher may give certain use cases/case studies where the student is able to apply multiple concepts in one single program.

Project-based learning is a teaching method in which students gain knowledge and skills by working for an extended period of time to investigate and respond to an authentic, engaging, and complex question, problem, or challenge. This approach can be particularly effective in helping students apply multiple concepts in one single program.

Here are some benefits of project-based learning:
1. It promotes student engagement and motivation by providing a real-world context for learning.
2. It encourages collaboration and teamwork, as students often work in groups to complete projects.
3. It helps students develop critical thinking and problem-solving skills as they work to find solutions to complex problems.
4. It allows for the integration of multiple subjects and concepts, as students apply knowledge from different areas to complete their projects.

In summary, project-based learning can be a powerful tool for subject teachers to help their students apply multiple concepts in one single program. By providing real-world use cases and case studies, teachers can engage and motivate their students while helping them develop important skills.



## c) It is also suggested that open source tools should be preferred to conduct the lab. Some open source online compiler to conduct the C lab are as follows:

1. **GCC**: The GNU Compiler Collection (GCC) is a compiler system produced by the GNU Project supporting various programming languages. GCC is a key component of the GNU toolchain and the standard compiler for most projects related to GNU and Linux.

2. **Code::Blocks**: Code::Blocks is a free, open-source, cross-platform C, C++ and Fortran IDE built to meet the most demanding needs of its users. It is designed to be very extensible and fully configurable.

3. **Eclipse CDT**: The Eclipse CDT (C/C++ Development Tooling) Project provides a fully functional C and C++ Integrated Development Environment based on the Eclipse platform.

4. **NetBeans**: NetBeans is an open-source integrated development environment (IDE) for developing with Java, JavaScript, PHP, Python, and other languages. It also has a C/C++ plugin that allows users to develop, build, and debug C/C++ applications.

5. **Clang**: Clang is a C, C++, Objective-C, and Objective-C++ compiler that is part of the LLVM project. It is designed to be highly compatible with GCC and to provide improved diagnostics and faster compilation times.

These are some of the open-source tools that can be used to conduct the C lab. They are widely used and have a large community of developers and users who can provide support and assistance. It is important to choose a tool that is suitable for the specific needs and requirements of the lab.



## JDoodle Online C Compiler

JDoodle is an online compiler and editor for various programming languages, including C. It allows users to write, compile, and execute C code directly in their web browser without the need for installing any software or setting up a development environment.

Some of the features of JDoodle's online C compiler include:
- Support for multiple C standards, including C99 and C11.
- The ability to save and share code snippets with others.
- The option to provide command line arguments to the program.
- The ability to include external libraries in the code.

JDoodle's online C compiler is a useful tool for quickly testing and debugging C code, as well as for sharing code snippets with others. It is also a convenient way for beginners to learn and practice C programming without the need for setting up a development environment. However, for more complex projects, a local development environment is still recommended.



## Tutorialspoint Online C Compiler

- Tutorialspoint provides an online C compiler that allows users to write, compile, and execute C programs directly from their web browser.
- The online compiler is easy to use and does not require any installation or setup.
- Users can write their C code in the text editor provided on the website and then click the "Compile and Execute" button to run their program.
- The output of the program is displayed in the output window below the text editor.
- The online compiler also provides options for users to save their code, load previously saved code, and share their code with others.
- This online compiler is a useful tool for students, teachers, and professionals who want to quickly test and run C programs without the need for a local development environment.




## Online C Compiler

An online C compiler is a tool that allows you to write, compile, and execute C code directly from your web browser. One such online C compiler is available at Programiz.com.

Here are some key features of the online C compiler at Programiz.com:

1. It allows you to write, compile, and execute C code directly from your web browser, without the need to install any software on your computer.
2. It provides a simple and user-friendly interface, making it easy for beginners to get started with C programming.
3. It supports the latest C standards, ensuring that your code is up-to-date and compatible with modern C compilers.
4. It provides helpful error messages and suggestions, helping you to quickly identify and fix any issues with your code.
5. It allows you to save and share your code with others, making it easy to collaborate on projects or get help from others.

Overall, the online C compiler at Programiz.com is a convenient and powerful tool for anyone looking to learn or practice C programming. It provides a simple and accessible way to write, compile, and execute C code, making it an excellent resource for both beginners and experienced programmers alike.



## HackerRank

HackerRank is a technology company that focuses on competitive programming challenges for both consumers and businesses. It is a platform where software developers can practice their coding skills, prepare for interviews, and compete in coding challenges.

- HackerRank offers a variety of skills-based assessments, including coding challenges, multiple-choice questions, and project-based assessments.
- The platform supports over 35 programming languages, including popular languages such as Java, Python, and C++.
- HackerRank for Work is the company's business offering, which enables companies to use the platform for technical recruiting and skills-based hiring.
- HackerRank has a large community of developers, with over 11 million developers in its community as of 2021.
- The company was founded in 2012 by Vivek Ravisankar and Harishankaran Karunanidhi, and is headquartered in Mountain View, California.



## Mapping with Virtual Lab

Mapping is the process of creating a visual representation of a geographical area or a spatial relationship between objects. Virtual labs are computer-based simulations that allow users to interact with and manipulate virtual objects in a simulated environment.

Here are some points to consider when using virtual labs for mapping:

1. Virtual labs provide a safe and controlled environment for users to experiment with mapping techniques and tools.
2. Virtual labs can simulate a wide range of mapping scenarios, from simple topographical maps to complex 3D models.
3. Virtual labs can provide users with immediate feedback on their mapping techniques, allowing them to quickly learn and improve their skills.
4. Virtual labs can be used to teach mapping concepts and techniques to students in a classroom setting.
5. Virtual labs can be used to test and evaluate new mapping technologies and methods before they are deployed in the field.

Overall, virtual labs provide a powerful tool for learning and experimenting with mapping techniques and technologies. They offer a safe and controlled environment for users to develop their skills and knowledge in this field.



# Name of the Lab Name of the Experiment

- The name of the lab is not specified.
- The name of the experiment is not specified.




## Problem Solving Lab

1. **Introduction:** Problem solving is the process of finding a solution to a problem or issue. It involves identifying the problem, analyzing it, and developing and implementing a solution.

2. **Identifying the problem:** The first step in problem solving is to identify the problem. This involves defining the problem and understanding its causes and effects.

3. **Analyzing the problem:** Once the problem has been identified, it is important to analyze it in order to understand its complexity and to identify potential solutions. This can involve breaking the problem down into smaller parts, identifying patterns, and gathering information.

4. **Developing a solution:** After analyzing the problem, the next step is to develop a solution. This can involve brainstorming, evaluating potential solutions, and selecting the best solution.

5. **Implementing the solution:** Once a solution has been developed, it is important to implement it. This can involve creating a plan, assigning tasks, and monitoring progress.

6. **Evaluating the solution:** After the solution has been implemented, it is important to evaluate its effectiveness. This can involve gathering feedback, assessing the results, and making any necessary adjustments.

7. **Conclusion:** Problem solving is an important skill that involves identifying and analyzing problems, developing and implementing solutions, and evaluating their effectiveness. By following a structured approach to problem solving, individuals and organizations can effectively address challenges and achieve their goals.



## Numerical Representation

Numerical representation refers to the different ways in which numbers can be represented and manipulated in a computer system. There are several different numerical representation systems, including:

1. **Binary:** This is the most basic numerical representation system, where numbers are represented using only two symbols, 0 and 1. This system is used by computers to store and manipulate data.

2. **Decimal:** This is the most commonly used numerical representation system, where numbers are represented using ten symbols, 0 to 9. This system is used in everyday life for counting and measuring.

3. **Hexadecimal:** This is a numerical representation system where numbers are represented using sixteen symbols, 0 to 9 and A to F. This system is often used in computer programming and data storage.

4. **Octal:** This is a numerical representation system where numbers are represented using eight symbols, 0 to 7. This system is less commonly used, but can be useful in certain applications.

Each of these numerical representation systems has its own advantages and disadvantages, and the choice of which system to use depends on the specific application and requirements. For example, binary is the most efficient system for computers to use, while decimal is the most intuitive for humans to use.



## Beauty of Numbers

Numbers are an essential part of our daily lives. They are used to count, measure, and quantify the world around us. But beyond their practical uses, numbers also possess a beauty and elegance that can be appreciated by anyone.

1. **Patterns and Symmetry:** One of the most fascinating aspects of numbers is the patterns and symmetry that can be found within them. For example, the sequence of prime numbers, while seemingly random, contains hidden patterns that mathematicians have been studying for centuries.

2. **Infinite Possibilities:** The concept of infinity is closely tied to numbers, and the idea that there are an infinite number of numbers, each with its own unique properties, is a source of wonder and beauty.

3. **Mathematical Art:** Numbers can also be used to create art. Fractals, for example, are complex patterns created using mathematical formulas, and they possess a stunning beauty that is both intricate and infinite.

4. **Universal Language:** Numbers are a universal language that can be understood by people of all cultures and backgrounds. This universality adds to their beauty, as they provide a common ground for people to connect and communicate.

In conclusion, numbers possess a beauty that goes beyond their practical uses. From the patterns and symmetry found within them, to the infinite possibilities they represent, to the art that can be created using them, numbers are truly a thing of beauty.



## More on Numbers

Numbers are mathematical objects used to count, measure, and label. There are different types of numbers, including:

1. **Natural numbers:** These are the counting numbers, starting from 1 and going on indefinitely (1, 2, 3, 4, ...).
2. **Whole numbers:** These are the natural numbers, including 0 (0, 1, 2, 3, 4, ...).
3. **Integers:** These are the whole numbers, including negative numbers (...,-3, -2, -1, 0, 1, 2, 3, ...).
4. **Rational numbers:** These are numbers that can be expressed as the ratio of two integers, such as 1/2, 3/4, and -5/6.
5. **Irrational numbers:** These are numbers that cannot be expressed as the ratio of two integers, such as the square root of 2 or pi.
6. **Real numbers:** These are all the numbers on the number line, including rational and irrational numbers.
7. **Complex numbers:** These are numbers that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit, defined as the square root of -1.

Each type of number has its own properties and is used in different mathematical contexts. Understanding the different types of numbers and their properties is important for solving mathematical problems and for understanding the world around us.



## Factorials

- A factorial is a mathematical operation that is represented by an exclamation mark (!) and is used to find the product of all positive integers less than or equal to a given positive integer.
- For example, the factorial of 5 is represented as 5! and is calculated as 5 x 4 x 3 x 2 x 1 = 120.
- The factorial of 0 is defined as 1, which is represented as 0! = 1.
- Factorials are commonly used in probability and statistics, particularly in calculating permutations and combinations.
- The factorial function grows very quickly, meaning that the value of n! becomes very large even for relatively small values of n.
- Factorials can also be calculated using recursion, where n! = n x (n-1)! for n > 0, with the base case being 0! = 1.
- The gamma function is a continuous extension of the factorial function to non-integer values, defined as (n-1)! = integral from 0 to infinity of t^(n-1) * e^(-t) dt for n > 0.



## String Operations

1. **Concatenation**: The process of combining two or more strings into a single string. This can be done using the `+` operator or the `join()` method.
2. **Slicing**: Extracting a portion of a string by specifying the start and end indices. This can be done using the `[]` operator.
3. **Indexing**: Accessing individual characters in a string by their index. This can be done using the `[]` operator.
4. **Length**: Determining the number of characters in a string. This can be done using the `len()` function.
5. **Splitting**: Dividing a string into a list of substrings based on a specified delimiter. This can be done using the `split()` method.
6. **Replacing**: Replacing all occurrences of a specified substring with another substring. This can be done using the `replace()` method.
7. **Searching**: Finding the index of the first occurrence of a specified substring within a string. This can be done using the `find()` or `index()` methods.
8. **Counting**: Counting the number of occurrences of a specified substring within a string. This can be done using the `count()` method.
9. **Case conversion**: Converting a string to all uppercase or all lowercase characters. This can be done using the `upper()` and `lower()` methods.
10. **Stripping**: Removing leading and trailing whitespace characters from a string. This can be done using the `strip()` method.



## Recursion

Recursion is a programming technique where a function calls itself repeatedly until a base condition is met. This technique is used to solve problems that can be broken down into smaller, repetitive sub-problems.

Here are some key points to remember about recursion:

1. A recursive function must have a base case, which is a condition that stops the function from calling itself indefinitely.
2. The function must change its state and move towards the base case with each recursive call.
3. Recursion can be used to solve problems that can be divided into smaller, similar sub-problems.
4. Recursive solutions can be less efficient than iterative solutions due to the overhead of function calls.
5. Recursion can make code more readable and easier to understand in some cases.

Recursion is a powerful tool in a programmer's toolkit, but it must be used carefully to avoid infinite loops and other issues. It is important to understand the problem at hand and determine if a recursive solution is appropriate.



## Advanced Arithmetic

Advanced arithmetic is a branch of mathematics that deals with the study of numbers and their properties. It includes topics such as:

1. Number theory: the study of the properties of integers and their relationships.
2. Algebra: the study of mathematical symbols and the rules for manipulating these symbols.
3. Geometry: the study of shapes, sizes, and positions of figures.
4. Trigonometry: the study of the relationships between the sides and angles of triangles.
5. Calculus: the study of change and motion, using concepts such as limits, derivatives, and integrals.

Advanced arithmetic is used in many fields, including science, engineering, and finance. It is an essential tool for solving complex problems and making accurate predictions.



## Searching and Sorting

Searching and sorting are fundamental algorithms in computer science. They are used to organize, manipulate, and retrieve data in an efficient manner.

### Searching

Searching algorithms are used to find a specific element or a set of elements in a data structure. There are two main types of searching algorithms: linear search and binary search.

- **Linear search** is a simple algorithm that iterates through each element in the data structure until the desired element is found. It has a time complexity of O(n), where n is the number of elements in the data structure.

- **Binary search** is a more efficient algorithm that works on sorted data structures. It repeatedly divides the data structure in half until the desired element is found. It has a time complexity of O(log n), where n is the number of elements in the data structure.

### Sorting

Sorting algorithms are used to arrange the elements of a data structure in a specific order. There are many different sorting algorithms, each with its own advantages and disadvantages. Some common sorting algorithms include:

- **Bubble sort** is a simple sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order. It has a time complexity of O(n^2), where n is the number of elements in the data structure.

- **Selection sort** is another simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the data structure and swapping it with the first element. It has a time complexity of O(n^2), where n is the number of elements in the data structure.

- **Insertion sort** is a simple sorting algorithm that builds the final sorted data structure one item at a time. It has a time complexity of O(n^2), where n is the number of elements in the data structure.

- **Quick sort** is a more efficient sorting algorithm that uses a divide-and-conquer approach. It works by selecting a pivot element and partitioning the data structure around the pivot. It has an average time complexity of O(n log n), where n is the number of elements in the data structure.

- **Merge sort** is another efficient sorting algorithm that uses a divide-and-conquer approach. It works by dividing the data structure into two halves, sorting each half, and then merging the two halves back together. It has a time complexity of O(n log n), where n is the number of elements in the data structure.

These are just a few examples of searching and sorting algorithms. There are many more algorithms, each with its own strengths and weaknesses. It is important to choose the right algorithm for the specific task at hand.



## Permutation

Permutation is a mathematical concept that deals with the arrangement of objects in a particular order. It is a way of counting the number of ways in which a set of objects can be arranged.

- The number of permutations of n distinct objects taken r at a time is given by the formula: nPr = n! / (n-r)!
- A permutation can also be thought of as a bijection, which is a one-to-one mapping between two sets.
- Permutations can be generated using various algorithms, such as the Heap's algorithm, the Steinhaus–Johnson–Trotter algorithm, and the Lexicographic order algorithm.
- Permutations have applications in various fields, such as cryptography, probability, and combinatorics.



## Sequences

A sequence is an ordered list of numbers or objects. The terms of a sequence are the elements in the list. A sequence can be finite or infinite. A finite sequence has a fixed number of terms, while an infinite sequence has an infinite number of terms.

Some common types of sequences include:

1. Arithmetic sequence: A sequence in which the difference between consecutive terms is constant. The nth term of an arithmetic sequence can be calculated using the formula `an = a1 + (n-1)d`, where `a1` is the first term, `d` is the common difference, and `n` is the term number.

2. Geometric sequence: A sequence in which the ratio between consecutive terms is constant. The nth term of a geometric sequence can be calculated using the formula `an = a1 * r^(n-1)`, where `a1` is the first term, `r` is the common ratio, and `n` is the term number.

3. Fibonacci sequence: A sequence in which each term is the sum of the two preceding terms. The first two terms of the Fibonacci sequence are 0 and 1, and the nth term can be calculated using the formula `Fn = Fn-1 + Fn-2`, where `n` is the term number.

4. Harmonic sequence: A sequence in which the reciprocals of the terms form an arithmetic sequence. The nth term of a harmonic sequence can be calculated using the formula `an = 1 / (a1 + (n-1)d)`, where `a1` is the first term, `d` is the common difference, and `n` is the term number.

Sequences can be used to model and solve real-world problems, such as calculating compound interest, predicting population growth, and analyzing patterns in data. They are also an important concept in mathematics, particularly in the study of calculus and series.



## Course Outcomes:

- A course outcome is a statement that describes the knowledge, skills, and abilities that students should possess upon completion of a course.
- Course outcomes are used to guide the development of course content, assessments, and teaching methods.
- Course outcomes should be specific, measurable, and achievable within the scope of the course.
- Course outcomes should align with program and institutional goals, as well as with relevant professional standards.
- Course outcomes should be regularly reviewed and updated to ensure their continued relevance and effectiveness.
- Course outcomes provide a framework for evaluating student learning and for making improvements to the course.
- Course outcomes help students understand the purpose and value of the course, and can guide their engagement with the course material.
- Course outcomes can be used to communicate the value of the course to external stakeholders, such as employers and accrediting bodies.




## Course Outcome Bloom’s

Course outcomes are statements that describe the knowledge, skills, and abilities that students should possess upon completion of a course. These outcomes are typically aligned with the course objectives and are used to assess the effectiveness of the course in achieving its intended goals.

Bloom’s Taxonomy is a framework for categorizing educational goals and objectives into different levels of complexity and specificity. It is commonly used to design course outcomes and assessments. The taxonomy consists of six levels, arranged in a hierarchy from lower-order thinking skills to higher-order thinking skills:

1. **Remembering**: The ability to recall or retrieve previously learned information.
2. **Understanding**: The ability to comprehend the meaning of material.
3. **Applying**: The ability to use learned material in new and concrete situations.
4. **Analyzing**: The ability to break down material into its component parts so that its organizational structure may be understood.
5. **Evaluating**: The ability to make judgments about the value of ideas or materials.
6. **Creating**: The ability to put parts together to form a new whole.

Course outcomes can be written using verbs from Bloom’s Taxonomy to indicate the level of thinking required for students to achieve the outcome. For example, a course outcome for a history course might be: “Students will be able to analyze primary source documents to construct an argument about a historical event.” This outcome uses the verb “analyze” from the Analyzing level of Bloom’s Taxonomy.

In summary, course outcomes are statements that describe what students should be able to do upon completion of a course, and Bloom’s Taxonomy is a framework that can be used to design and assess these outcomes. By using verbs from Bloom’s Taxonomy, course outcomes can be written to indicate the level of thinking required for students to achieve the outcome.



## Level

- A level is a tool used to determine if a surface is horizontal (level) or vertical (plumb).
- Levels can be used in construction, carpentry, surveying, and many other applications.
- There are several types of levels, including spirit levels, laser levels, and water levels.
- Spirit levels use a liquid-filled vial with an air bubble to indicate levelness.
- Laser levels project a laser beam to provide a visual reference for levelness.
- Water levels use the principle that water will always find its own level to determine levelness.
- Levels can vary in size and accuracy, with larger and more precise levels being used for more demanding applications.
- It is important to use a level when installing objects such as shelves, cabinets, and picture frames to ensure that they are straight and level.
- Levels can also be used to check the levelness of floors, walls, and other surfaces during construction or renovation projects.



## At the end of the course, the student will be able to:

1. Demonstrate a comprehensive understanding of the course material.
2. Apply the knowledge and skills acquired during the course to real-life situations.
3. Analyze and evaluate information critically and effectively.
4. Communicate ideas and arguments clearly and effectively in both written and oral forms.
5. Work collaboratively with others to achieve common goals.
6. Demonstrate ethical and professional behavior in all aspects of their work.
7. Engage in continuous learning and professional development.




## CO 1 Able to implement the algorithms and draw flowcharts for solving Mathematical and Engineering problems.

1. **Algorithms** are step-by-step procedures for solving problems. They can be used to solve mathematical and engineering problems.
2. **Flowcharts** are visual representations of algorithms. They use symbols and arrows to show the flow of the algorithm.
3. To implement an algorithm, one must first understand the problem and identify the steps needed to solve it.
4. Once the steps are identified, they can be written in a programming language or represented visually using a flowchart.
5. Flowcharts are useful for understanding and communicating the logic of an algorithm.
6. Common symbols used in flowcharts include rectangles for processes, diamonds for decisions, and arrows for the flow of control.
7. To solve mathematical and engineering problems using algorithms and flowcharts, one must have a strong understanding of the underlying concepts and principles.
8. Practice and experience are key to becoming proficient in implementing algorithms and drawing flowcharts for solving mathematical and engineering problems.




## K3, K4

K3 and K4 are two types of surface groups in mathematics. They are named after the German mathematician Ernst Kummer.

- K3 surfaces are a type of algebraic surface that can be described as the zero set of a quartic polynomial in three variables.
- K4 surfaces are a type of algebraic surface that can be described as the zero set of a quartic polynomial in four variables.
- Both K3 and K4 surfaces have interesting geometric and topological properties, and they are important objects of study in algebraic geometry and topology.
- K3 surfaces, in particular, have been extensively studied due to their connections to string theory and mirror symmetry.




## CO 2 Demonstrate an understanding of computer programming language concepts. K3, K2

- **Programming languages** are used to write computer programs, which are sets of instructions that tell a computer what to do.
- There are many different programming languages, each with its own syntax, semantics, and features.
- Some common programming language concepts include:
  - **Variables**: used to store data in a program.
  - **Data types**: define the type of data that can be stored in a variable, such as integers, floating-point numbers, and strings.
  - **Operators**: used to perform operations on data, such as addition, subtraction, and comparison.
  - **Control structures**: used to control the flow of a program, such as if-else statements and loops.
  - **Functions**: reusable blocks of code that can be called from other parts of a program.
- Understanding these concepts is important for writing efficient and effective programs.
- Different programming languages may implement these concepts in different ways, so it is important to learn the specifics of the language being used.
- There are also different paradigms of programming, such as procedural, object-oriented, and functional programming, which can influence how these concepts are used in a program.



## CO 3

CO 3 is a chemical formula that represents the carbonate ion. It is composed of one carbon atom and three oxygen atoms, and carries a negative two charge. Carbonates are commonly found in rocks and minerals, and are also present in the shells of many marine organisms. Some common examples of carbonates include calcite, aragonite, and dolomite.

- Carbonate ions are formed when carbon dioxide dissolves in water and reacts with water molecules to form carbonic acid.
- Carbonic acid can then dissociate to form bicarbonate ions and hydrogen ions.
- Bicarbonate ions can further dissociate to form carbonate ions and hydrogen ions.
- Carbonate ions can react with metal ions to form insoluble carbonate salts.
- Carbonate minerals are important in the formation of sedimentary rocks, such as limestone and dolomite.
- Carbonates can also act as a buffer, helping to regulate the pH of a solution.




# Ability to design and develop Computer programs, analyzes, and interprets the concept of pointers, declarations, initialization, operations on pointers and their usage.

- A pointer is a variable that stores the memory address of another variable.
- Pointers are used for dynamic memory allocation, accessing array elements, and implementing data structures such as linked lists and trees.
- To declare a pointer, the data type of the variable it points to is specified, followed by an asterisk (*) and the pointer variable name.
- Pointers must be initialized before they are used. This can be done by assigning the address of a variable to the pointer using the address-of operator (&).
- Operations on pointers include assignment, pointer arithmetic, and dereferencing.
- Dereferencing a pointer means accessing the value stored at the memory location pointed to by the pointer. This is done using the indirection operator (*).
- Pointers can be used to pass variables by reference to functions, allowing the function to modify the value of the variable.
- Pointers must be used with caution, as incorrect usage can lead to undefined behavior and program crashes.




## K6, K4

K6 and K4 are two different types of telephone booths that were introduced in the United Kingdom.

1. The K6 (Kiosk No. 6) was designed by Sir Giles Gilbert Scott and introduced in 1935 to commemorate the Silver Jubilee of King George V. It is made of cast iron and is painted red, with a domed roof and the Royal Crown embossed on the top panels. The K6 was the first telephone kiosk to be installed nationwide and became a familiar sight on the streets of the UK.

2. The K4 (Kiosk No. 4) was also designed by Sir Giles Gilbert Scott and was introduced in 1927. It was larger than the K6 and incorporated a post box and stamp vending machine. However, the K4 was not as successful as the K6 and only around 50 were ever installed.

Both the K6 and K4 are iconic designs and are considered to be important examples of British industrial design. Many of them are still in use today, although some have been repurposed for other uses such as mini-libraries or art installations.



## CO 4

1. CO 4 is a learning outcome that refers to the ability to apply knowledge and skills in a particular subject or field.
2. It is often used in educational settings to assess the progress of students and to determine their level of understanding and mastery of the material.
3. CO 4 can be achieved through various methods, including coursework, exams, projects, and practical assignments.
4. The specific requirements for achieving CO 4 will vary depending on the subject and the educational institution.
5. It is important for students to work towards achieving CO 4 in order to demonstrate their proficiency in the subject and to prepare for further study or employment in the field.
6. Teachers and instructors can use CO 4 as a benchmark to evaluate the effectiveness of their teaching methods and to identify areas where students may need additional support or instruction.
7. CO 4 is just one of many learning outcomes that students may be expected to achieve during their education. It is important for students to strive for excellence in all areas of their studies in order to maximize their potential and achieve their goals.



## Able to define data types and use them in simple data processing applications

- A data type is a classification of data that determines the kind of values that can be stored in a variable, the operations that can be performed on it, and the way the values are stored in memory.
- Common data types include integers, floating-point numbers, characters, and strings.
- Data types can be used in simple data processing applications to store and manipulate data.
- For example, an integer data type can be used to store a count of items, while a floating-point data type can be used to store a measurement with a decimal value.

## Using the concept of array of structures

- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- A structure is a collection of variables of different data types, grouped together under a single name.
- An array of structures is a collection of structures, where each structure in the array is an element.
- This can be useful in data processing applications where multiple records of data need to be stored and manipulated.
- For example, an array of structures could be used to store information about a group of people, where each structure in the array represents a person and contains information such as their name, age, and address.



## K1, K5

K1 and K5 are two different types of visas issued by the United States government. Here are some key points about each type of visa:

- **K1 visa** is also known as a fiancé(e) visa. It is a nonimmigrant visa that allows the foreign fiancé(e) of a United States citizen to enter the United States for the purpose of getting married within 90 days of arrival.
- **K5 visa** is a nonimmigrant visa for the spouse and children of a lawful permanent resident (LPR) of the United States. It allows the spouse and children of an LPR to enter the United States while waiting for their immigrant visa to become available.
- Both K1 and K5 visas require the petitioner (the U.S. citizen or LPR) to file a petition with the United States Citizenship and Immigration Services (USCIS) on behalf of their foreign fiancé(e) or spouse and children.
- The processing time for both K1 and K5 visas can vary, but it typically takes several months.
- Once the K1 or K5 visa is issued, the foreign fiancé(e) or spouse and children can enter the United States and apply for adjustment of status to become a lawful permanent resident.




## CO 5 Develop confidence for self-education and ability for life-long learning needed for Computer language

1. **Set achievable goals**: Start with small, achievable goals to build confidence and momentum. As you achieve these goals, gradually increase their difficulty.

2. **Practice regularly**: Regular practice is essential for developing and maintaining skills. Set aside time each day or week to practice and improve.

3. **Seek feedback**: Seek feedback from others to identify areas for improvement and to track your progress.

4. **Learn from mistakes**: Don't be afraid to make mistakes. Instead, view them as opportunities to learn and improve.

5. **Stay curious**: Stay curious and open-minded. Explore new topics and ideas to keep learning and growing.

6. **Use available resources**: Take advantage of the many resources available for learning, such as online courses, tutorials, and forums.

7. **Stay motivated**: Find ways to stay motivated, such as setting rewards for achieving goals or finding a learning partner to share the journey with.

By following these steps, you can develop the confidence and ability for self-education and life-long learning needed for computer language.



## K3, K4

K3 and K4 are two types of surface groups in mathematics. They are named after the German mathematician Ernst Kummer.

- K3 surfaces are a type of algebraic surface that can be described as the zero set of a quartic polynomial in three variables.
- K4 surfaces are a type of algebraic surface that can be described as the zero set of a quartic polynomial in four variables.
- Both K3 and K4 surfaces have interesting geometric properties and are studied in algebraic geometry.
- K3 surfaces have been used to construct examples of Calabi-Yau manifolds, which play an important role in string theory.
- K4 surfaces have been studied in the context of mirror symmetry, a concept in theoretical physics and mathematics that relates two different Calabi-Yau manifolds.


