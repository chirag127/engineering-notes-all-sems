

## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

A WAP (Write a Program) is a common term used in computer science and programming to refer to the task of writing a computer program to solve a specific problem or perform a specific task. In this case, the task is to write a program that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

Here are the steps to write this program:

1. Define a variable to store the marks of each subject.
2. Accept the marks of 5 subjects from the user and store them in the respective variables.
3. Calculate the sum of the marks by adding the marks of all 5 subjects.
4. Calculate the percentage marks by dividing the sum of the marks by the total marks and multiplying by 100.
5. Display the sum and percentage marks obtained by the student.

Here is an example of how this program can be written in the Python programming language:

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
print("Sum of marks:", sum_of_marks)
print("Percentage marks:", percentage_marks)
```

This program accepts the marks of 5 subjects from the user, calculates the sum and percentage marks, and displays the result. The percentage marks are calculated by dividing the sum of the marks by the total marks (500 in this case, as there are 5 subjects with a maximum of 100 marks each) and multiplying by 100. The result is then displayed to the user.



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



## 3. WAP to calculate the area and circumference of a circle

To calculate the area and circumference of a circle, you need to know the radius of the circle. The radius is the distance from the center of the circle to its edge.

The formula for calculating the area of a circle is `A = πr^2`, where `A` is the area, `π` is approximately equal to 3.14, and `r` is the radius of the circle.

The formula for calculating the circumference of a circle is `C = 2πr`, where `C` is the circumference, `π` is approximately equal to 3.14, and `r` is the radius of the circle.

Here is an example of a program that calculates the area and circumference of a circle with a radius of 5 units:

```python
radius = 5
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"The area of the circle is {area} square units.")
print(f"The circumference of the circle is {circumference} units.")
```

This program calculates the area and circumference of the circle using the formulas mentioned above and prints the results. The output of this program would be:

```
The area of the circle is 78.5 square units.
The circumference of the circle is 31.400000000000002 units.
```

You can modify the value of the `radius` variable to calculate the area and circumference of a circle with a different radius. You can also use the `math.pi` constant from the `math` module to get a more accurate value of `π`.



## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- WAP stands for Write a Program.
- The formula for converting temperature from Centigrade to Fahrenheit is `C/5=(F-32)/9`.
- To convert a temperature from Centigrade to Fahrenheit, first subtract 32 from the Fahrenheit temperature.
- Then, multiply the result by 5/9.
- The resulting value is the temperature in Centigrade.

Here is an example of a program that accepts the temperature in Centigrade and converts it into Fahrenheit using the formula `C/5=(F-32)/9`:

```python
C = float(input("Enter the temperature in Centigrade: "))
F = (C * 9/5) + 32
print("The temperature in Fahrenheit is:", F)
```

In this program, the user is prompted to enter the temperature in Centigrade. The program then converts the temperature to Fahrenheit using the formula `C/5=(F-32)/9` and displays the result.



## 5. WAP that swaps values of two variables using a third variable.

Swapping the values of two variables means exchanging their values. For example, if variable `a` has the value `5` and variable `b` has the value `10`, after swapping, `a` will have the value `10` and `b` will have the value `5`.

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

In this program, we use a third variable `temp` to temporarily store the value of `a`. Then, we assign the value of `b` to `a` and the value of `temp` (which is the original value of `a`) to `b`. This way, the values of `a` and `b` are swapped.

This method of swapping values using a third variable is commonly used in many programming languages. It is simple and easy to understand. However, there are other methods to swap values without using a third variable, such as using arithmetic operations or bitwise XOR. These methods can be more efficient in some cases, but they may be more difficult to understand for beginners.



## 6. WAP that checks whether the two numbers entered by the user are equal or not.

A WAP (Write a Program) that checks whether the two numbers entered by the user are equal or not can be written in various programming languages. Here is an example of how this can be done in Python:

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

In this program, the user is prompted to enter two numbers. These numbers are then compared using the `==` operator, which checks if the two values are equal. If the values are equal, the program prints "The numbers are equal." Otherwise, it prints "The numbers are not equal."

This is a simple program that can be easily modified to suit the needs of the user. For example, the program can be modified to take more than two numbers as input, or to perform additional operations on the numbers before comparing them. The possibilities are endless.



## 7. WAP to find the greatest of three numbers.

To find the greatest of three numbers, we can use the `if-else` statement in programming. Here is an example of how to do this in Python:

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
```

In this example, we take three numbers as input from the user and store them in the variables `num1`, `num2`, and `num3`. Then, we use the `if-else` statement to compare the three numbers and find the largest among them. The largest number is then stored in the variable `largest` and printed to the screen.



## 8. WAP that finds whether a given number is even or odd.

A WAP (Write a Program) that finds whether a given number is even or odd can be written in many programming languages. Here is an example of how it can be done in Python:

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
```

- The program takes an input from the user and stores it in the variable `num`.
- The `if` statement checks if the remainder of the division of `num` by 2 is equal to 0.
- If the condition is `True`, the program prints that the number is even.
- If the condition is `False`, the program prints that the number is odd.

This is a simple way to determine if a given number is even or odd. The program can be modified and expanded to include more functionality and features.



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

1. First, the program should prompt the user to enter the marks of five subjects.
2. The marks entered by the user should be stored in variables or an array.
3. The program should then calculate the total marks obtained by adding the marks of all five subjects.
4. The percentage can be calculated by dividing the total marks by the maximum possible marks and multiplying the result by 100.
5. Once the percentage is calculated, the program should use conditional statements to determine the grade according to the given criteria.
6. The grade should then be printed to the screen.

Here is an example of how the code for this program might look like in Python:

```python
# Accept marks of five subjects
sub1 = int(input("Enter marks of subject 1: "))
sub2 = int(input("Enter marks of subject 2: "))
sub3 = int(input("Enter marks of subject 3: "))
sub4 = int(input("Enter marks of subject 4: "))
sub5 = int(input("Enter marks of subject 5: "))

# Calculate total marks and percentage
total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100

# Determine grade according to the given criteria
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

# Print the grade
print("Grade:", grade)
```



## Between 90-100%-----Print ‘A’

- This statement appears to be a conditional statement used in programming.
- It specifies that if a certain condition is met, in this case, a value being between 90 and 100 percent, then the program should print the letter 'A'.
- Conditional statements are used to control the flow of a program based on certain conditions being met.
- In this case, the condition is checking if a value falls within a certain range, specifically between 90 and 100 percent.
- If the condition is true, then the program will execute the specified action, which is to print the letter 'A'.
- If the condition is not met, then the program will not execute the specified action and will continue to the next line of code.



## 80-90% - Print 'B'

- The topic appears to be related to a grading system where a score between 80-90% corresponds to a grade of 'B'.
- In many educational systems, grades are assigned based on a student's performance on assessments such as exams, quizzes, and assignments.
- A grade of 'B' typically indicates that the student has demonstrated a good understanding of the material and has met most of the expectations for the course.
- The exact meaning of a 'B' grade can vary depending on the specific grading system used, but it generally falls between an 'A' (excellent) and a 'C' (average).
- It is important for students to understand the grading system used in their courses and to strive for the highest grade they can achieve.



## 60-80%-----------------Print ‘C’

- The percentage range of 60-80% is often used as a benchmark for a passing or satisfactory grade in many educational systems.
- In some grading systems, a grade within this range may be represented by the letter ‘C’.
- A ‘C’ grade typically indicates that the student has met the basic requirements and demonstrated an average understanding of the course material.
- However, grading systems and their interpretation can vary widely between different institutions and countries.
- It is important to note that a ‘C’ grade may have different implications depending on the context in which it is used.



## Below 60%-------------Print ‘D’

- This statement appears to be a conditional statement that checks if a certain value is below 60%.
- If the condition is met, the statement instructs to print the letter 'D'.
- This type of statement is commonly used in programming languages to control the flow of a program based on certain conditions.
- The specific details of the condition and the action to be taken when the condition is met may vary depending on the context in which this statement is used.
- It is important to understand the context and the specific details of the condition and the action to be taken in order to properly implement this statement in a program.



## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

Here is an example of a program that takes two operands and one operator from the user, performs the operation, and prints the result using a switch statement:

```c
#include <stdio.h>

int main() {
    double num1, num2;
    char operator;

    printf("Enter an operator (+, -, *, /): ");
    scanf("%c", &operator);

    printf("Enter two operands: ");
    scanf("%lf %lf", &num1, &num2);

    switch(operator) {
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
            printf("Error! Invalid operator.");
    }

    return 0;
}
```

This program prompts the user to enter an operator and two operands. It then uses a switch statement to perform the operation based on the operator entered by the user. The result of the operation is then printed to the screen.

Some key points to note about this program:
- The `switch` statement is used to perform different actions based on the value of the `operator` variable.
- The `case` statements within the `switch` statement define the actions to be performed for each possible value of the `operator` variable.
- The `break` statement is used to exit the `switch` statement once the appropriate action has been performed.
- If the value of the `operator` variable does not match any of the `case` statements, the `default` statement is executed, which in this case prints an error message to the screen.

This is just one example of how a program can take two operands and one operator from the user, perform the operation, and print the result using a switch statement. There are many other ways to implement this functionality, and the specific details may vary depending on the requirements of the program and the preferences of the programmer.



## 12. WAP to print the sum of all numbers up to a given number.

Here is a program that calculates the sum of all numbers up to a given number:

```python
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of all numbers up to", n, "is", sum)
```

- The program prompts the user to enter a number `n`.
- The variable `sum` is initialized to 0.
- A `for` loop is used to iterate over the range of numbers from 1 to `n`.
- In each iteration, the value of `i` is added to the `sum`.
- After the loop is completed, the final value of `sum` is printed, which is the sum of all numbers up to `n`.

This program can be further optimized by using the formula for the sum of the first `n` natural numbers, which is `n*(n+1)/2`. Here is the optimized version of the program:

```python
n = int(input("Enter a number: "))
sum = n*(n+1)//2
print("The sum of all numbers up to", n, "is", sum)
```

- The program prompts the user to enter a number `n`.
- The formula `n*(n+1)//2` is used to calculate the sum of the first `n` natural numbers.
- The result is stored in the variable `sum` and printed.

Both versions of the program produce the same result, but the second version is more efficient as it does not use a loop and performs the calculation in constant time.



## 13. WAP to find the factorial of a given number.

Factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, the factorial of 5 is 120, or 5! = 5 × 4 × 3 × 2 × 1 = 120.

Here is an example of a program that calculates the factorial of a given number in Python:

```python
n = int(input("Enter a number: "))
factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers")
elif n == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, n + 1):
        factorial = factorial * i
    print(f"The factorial of {n} is {factorial}")
```

This program prompts the user to enter a number, then checks if the number is negative or zero. If the number is negative, the program prints an error message. If the number is zero, the program prints that the factorial of 0 is 1. Otherwise, the program calculates the factorial of the given number using a for loop and prints the result.

- The factorial of a non-negative integer n is denoted by n!.
- The factorial of n is the product of all positive integers less than or equal to n.
- The factorial of 0 is 1.
- The factorial does not exist for negative numbers.
- The above program calculates the factorial of a given number in Python. It prompts the user to enter a number, checks if the number is negative or zero, and calculates the factorial using a for loop if the number is positive.



## 14.WAP to print sum of even and odd numbers from 1 to N numbers.

Here is an example of a program that can be used to print the sum of even and odd numbers from 1 to N numbers:

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

- The program starts by taking the value of N as input from the user.
- Two variables, `even_sum` and `odd_sum`, are initialized to 0 to store the sum of even and odd numbers respectively.
- A for loop is used to iterate over the range of numbers from 1 to N.
- Inside the loop, an if-else statement is used to check if the current number is even or odd.
- If the number is even, it is added to the `even_sum` variable. Otherwise, it is added to the `odd_sum` variable.
- After the loop is completed, the final values of `even_sum` and `odd_sum` are printed to display the sum of even and odd numbers respectively.

This program can be modified according to the specific requirements of the user. For example, the range of numbers can be changed, or the program can be modified to only print the sum of even or odd numbers.



## 15. WAP to print the Fibonacci series

The Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding numbers. The simplest Fibonacci series is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Here is an example of a program that prints the Fibonacci series in Python:

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

- The program starts by initializing the variables `n1` and `n2` to 0 and 1, respectively. These variables represent the first two terms of the Fibonacci series.
- The variable `count` is initialized to 0 and is used to keep track of the number of terms printed.
- The program then checks if the number of terms entered by the user is less than or equal to 0. If it is, the program prints an error message and exits.
- If the number of terms entered by the user is 1, the program prints the first term of the Fibonacci series, which is 0.
- If the number of terms entered by the user is greater than 1, the program enters a while loop that continues until the specified number of terms have been printed.
- Inside the while loop, the program prints the current value of `n1`, which represents the next term in the Fibonacci series.
- The program then calculates the next term in the series by adding `n1` and `n2` and storing the result in the variable `nth`.
- The values of `n1` and `n2` are then updated to `n2` and `nth`, respectively, to prepare for the next iteration of the loop.
- The `count` variable is incremented by 1 to keep track of the number of terms printed.
- The while loop continues until the specified number of terms have been printed.

This is one way to write a program to print the Fibonacci series. There are many other ways to accomplish the same task, and the specific implementation may vary depending on the programming language and the requirements of the specific program.



## 16. WAP to check whether the entered number is prime or not.

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. To check if a number is prime or not, we can follow these steps:

1. Take input from the user and store it in a variable, let's say `n`.
2. Initialize a variable `flag` to 0.
3. Run a loop from 2 to `n/2`.
4. For each iteration, check if `n` is divisible by the current loop variable.
5. If `n` is divisible, set `flag` to 1 and break the loop.
6. After the loop, check the value of `flag`.
7. If `flag` is 0, the number is prime. Otherwise, it is not prime.

Here is an example code in C language that implements the above algorithm:

```c
#include <stdio.h>
int main()
{
    int n, i, flag = 0;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    for(i = 2; i <= n/2; ++i)
    {
        if(n%i == 0)
        {
            flag = 1;
            break;
        }
    }

    if (n == 1) 
    {
        printf("1 is neither prime nor composite.");
    }
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

1. Start by initializing a variable `sum` to 0. This variable will be used to store the sum of the digits of the entered number.
2. Take the input number from the user and store it in a variable `num`.
3. Use a `while` loop to iterate through the digits of the number. The loop should continue until the value of `num` becomes 0.
4. In each iteration of the loop, find the last digit of the number by taking the remainder of the number when divided by 10. This can be done using the modulo operator (`%`).
5. Add the value of the last digit to the `sum` variable.
6. Remove the last digit from the number by dividing it by 10 and taking the integer part of the result. This can be done using the integer division operator (`//`).
7. Repeat steps 4-6 until the value of `num` becomes 0.
8. After the loop ends, the value of the `sum` variable will be the sum of the digits of the entered number.
9. Print the value of the `sum` variable to display the result.

Here is an example implementation of the above algorithm in Python:

```python
sum = 0
num = int(input("Enter a number: "))

while num > 0:
    last_digit = num % 10
    sum += last_digit
    num = num // 10

print("The sum of the digits is:", sum)
```



## 18. WAP to find the reverse of a number.

Here is an algorithm to find the reverse of a number:

1. Initialize a variable `reverse` to 0.
2. While the number is greater than 0:
    1. Multiply `reverse` by 10.
    2. Add the last digit of the number to `reverse`.
    3. Remove the last digit from the number by dividing it by 10.
3. The value of `reverse` is the reverse of the original number.

Here is an example of a program in C language that implements this algorithm:

```c
#include <stdio.h>

int main()
{
    int n, reverse = 0, remainder;

    printf("Enter an integer: ");
    scanf("%d", &n);

    while(n != 0)
    {
        remainder = n % 10;
        reverse = reverse * 10 + remainder;
        n /= 10;
    }

    printf("Reversed number = %d", reverse);

    return 0;
}
```

This program prompts the user to enter an integer, then calculates its reverse using the algorithm described above. The reversed number is then printed to the screen.



## 19.WAP to print Armstrong numbers from 1 to 100.

An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.

Here is a program in C language to print all Armstrong numbers from 1 to 100:

```c
#include <stdio.h>
#include <math.h>

int main() {
    int i, temp, rem, sum, n = 0;

    printf("Armstrong numbers from 1 to 100: ");
    for (i = 1; i <= 100; i++) {
        temp = i;
        sum = 0;
        n = 0;

        while (temp != 0) {
            temp /= 10;
            n++;
        }

        temp = i;

        while (temp != 0) {
            rem = temp % 10;
            sum += pow(rem, n);
            temp /= 10;
        }

        if (sum == i) {
            printf("%d ", i);
        }
    }

    return 0;
}
```

This program uses a `for` loop to iterate through numbers from 1 to 100. For each number, it calculates the sum of its digits raised to the power of the number of digits using a `while` loop. If the calculated sum is equal to the original number, it is printed as an Armstrong number.



## 20. WAP to convert binary number into decimal number and vice versa.

Converting a binary number into a decimal number involves taking the sum of the products of each binary digit by its corresponding power of 2. For example, the binary number 1011 can be converted into a decimal number as follows:

1. Start with the rightmost digit (in this case, 1). Multiply it by 2^0 (which is 1) to get 1.
2. Move to the next digit to the left (in this case, 1). Multiply it by 2^1 (which is 2) to get 2.
3. Move to the next digit to the left (in this case, 0). Multiply it by 2^2 (which is 4) to get 0.
4. Move to the next digit to the left (in this case, 1). Multiply it by 2^3 (which is 8) to get 8.
5. Add all the products together to get the decimal equivalent of the binary number: 1 + 2 + 0 + 8 = 11.

Converting a decimal number into a binary number involves repeatedly dividing the decimal number by 2 and recording the remainder until the decimal number becomes 0. For example, the decimal number 11 can be converted into a binary number as follows:

1. Divide 11 by 2 to get a quotient of 5 and a remainder of 1. Record the remainder (1).
2. Divide 5 by 2 to get a quotient of 2 and a remainder of 1. Record the remainder (1).
3. Divide 2 by 2 to get a quotient of 1 and a remainder of 0. Record the remainder (0).
4. Divide 1 by 2 to get a quotient of 0 and a remainder of 1. Record the remainder (1).
5. Since the quotient is now 0, stop the process. The binary equivalent of the decimal number is obtained by reading the remainders in reverse order: 1011.

Here is an example of a program in Python that converts a binary number into a decimal number and vice versa:

```python
def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += int(binary[i]) * (2 ** (len(binary) - 1 - i))
    return decimal

def decimal_to_binary(decimal):
    binary = ""
    while decimal > 0:
        binary += str(decimal % 2)
        decimal = decimal // 2
    return binary[::-1]

binary = input("Enter a binary number: ")
decimal = binary_to_decimal(binary)
print(f"The decimal equivalent of {binary} is {decimal}.")

decimal = int(input("Enter a decimal number: "))
binary = decimal_to_binary(decimal)
print(f"The binary equivalent of {decimal} is {binary}.")
```



## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

Here is an example of a program that takes elements of an array from the user and finds the sum of these elements:

```python
n = int(input("Enter the number of elements in the array: "))
arr = []
for i in range(n):
    x = int(input("Enter element: "))
    arr.append(x)

sum = 0
for i in arr:
    sum += i

print("Sum of elements in the array:", sum)
```

- The program starts by taking the number of elements in the array as input from the user.
- An empty list `arr` is initialized to store the elements of the array.
- A for loop is used to take `n` elements as input from the user and append them to the list `arr`.
- A variable `sum` is initialized to 0 to store the sum of the elements in the array.
- Another for loop is used to iterate over the elements in the list `arr` and add them to the variable `sum`.
- Finally, the sum of the elements in the array is printed.




## 22. WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

Here is a step-by-step guide to writing a program that inputs two arrays and saves the sum of corresponding elements of these arrays in a third array and prints them:

1. Start by defining the main function and declaring the necessary variables, including the two input arrays, the output array, and the size of the arrays.
2. Prompt the user to enter the size of the arrays and store it in the appropriate variable.
3. Prompt the user to enter the elements of the first array and store them in the first input array.
4. Repeat the previous step for the second input array.
5. Use a loop to iterate over the elements of the input arrays, adding the corresponding elements and storing the result in the output array.
6. Use another loop to print the elements of the output array.
7. End the main function.

Here is an example of what the code might look like in C:

```c
#include <stdio.h>

int main() {
    int size;
    printf("Enter the size of the arrays: ");
    scanf("%d", &size);

    int arr1[size], arr2[size], sum[size];

    printf("Enter the elements of the first array: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr1[i]);
    }

    printf("Enter the elements of the second array: ");
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr2[i]);
    }

    for (int i = 0; i < size; i++) {
        sum[i] = arr1[i] + arr2[i];
    }

    printf("The sum of the corresponding elements of the two arrays is: ");
    for (int i = 0; i < size; i++) {
        printf("%d ", sum[i]);
    }

    return 0;
}
```



## 23. WAP to find the minimum and maximum element of the array.

Here is an example of a program that finds the minimum and maximum elements of an array:

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

This program prompts the user to enter the number of elements in the array and the elements of the array. It then initializes the `min` and `max` variables to the first element of the array. The program then iterates through the rest of the elements of the array, updating the `min` and `max` variables if a smaller or larger element is found, respectively. Finally, the program prints the minimum and maximum elements of the array.

- The time complexity of this program is O(n), where n is the number of elements in the array.
- The space complexity of this program is O(1), as the program uses a constant amount of additional space.



## 24. WAP to search an element in an array using Linear Search

Linear search is a simple search algorithm that is used to search for an element in an array. It works by iterating through the array from the first element to the last element, comparing each element with the value being searched for. If a match is found, the index of the element is returned. If no match is found, the algorithm returns -1.

Here is an example of a program that implements linear search in C:

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

In this example, the `linearSearch` function takes as input an array `arr`, the size of the array `n`, and the value to be searched for `x`. It returns the index of the first occurrence of `x` in `arr`, or -1 if `x` is not present in `arr`.

The `main` function initializes an array `arr` of size `n` and a value `x` to be searched for. It then calls the `linearSearch` function and prints the result.

Linear search has a time complexity of O(n), where n is the size of the array. This means that in the worst case, the algorithm will have to iterate through the entire array to find the value being searched for. As a result, linear search is not efficient for large arrays. However, it is a simple algorithm that is easy to implement and can be useful in certain situations.



## 25. WAP to sort the elements of the array in ascending order using Bubble Sort technique.

Bubble sort is a simple sorting algorithm that compares adjacent elements in an array and swaps them if they are in the wrong order. The algorithm continues to do this until the entire array is sorted in ascending order.

Here is an example of how to implement bubble sort in C++:

```c++
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n)
{
    for (int i = 0; i < n-1; i++)
    {
        for (int j = 0; j < n-i-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    cout << "Sorted array: \n";
    for (int i=0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
    return 0;
}
```

This code defines a function `bubbleSort` that takes an array of integers and its size as arguments. The function uses two nested loops to iterate over the array. In the inner loop, adjacent elements are compared and swapped if they are in the wrong order. The outer loop runs until the entire array is sorted.

In the `main` function, we create an array of integers and call the `bubbleSort` function to sort it. Finally, we print the sorted array.

Bubble sort has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it is easy to understand and implement, making it a good choice for small datasets or for educational purposes.



## 26. WAP to add and multiply two matrices of order nxn.

A matrix is a two-dimensional array of numbers. The order of a matrix is the number of rows and columns it has. For example, a matrix of order 3x3 has 3 rows and 3 columns.

To add two matrices of the same order, we simply add the corresponding elements of the two matrices. For example, if A and B are two matrices of order 3x3, then the sum of the two matrices, C, is given by:

C[i][j] = A[i][j] + B[i][j]

where i and j are the row and column indices, respectively.

To multiply two matrices, the number of columns of the first matrix must be equal to the number of rows of the second matrix. The product of two matrices, A and B, of orders nxm and mxp, respectively, is a matrix C of order nxp, where:

C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] + ... + A[i][m-1] * B[m-1][j]

Here is an example of a program in C that adds and multiplies two matrices of order nxn:

```c
#include <stdio.h>

int main() {
    int n, i, j;
    printf("Enter the order of the matrices: ");
    scanf("%d", &n);
    int A[n][n], B[n][n], C[n][n], D[n][n];
    printf("Enter the elements of the first matrix: ");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &A[i][j]);
    printf("Enter the elements of the second matrix: ");
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            scanf("%d", &B[i][j]);
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
            C[i][j] = A[i][j] + B[i][j];
    printf("The sum of the two matrices is:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
    for (i = 0; i < n; i++)
        for (j = 0; j < n; j++) {
            D[i][j] = 0;
            for (int k = 0; k < n; k++)
                D[i][j] += A[i][k] * B[k][j];
        }
    printf("The product of the two matrices is:\n");
    for (i = 0; i < n; i++) {
        for (j = 0; j < n; j++)
            printf("%d ", D[i][j]);
        printf("\n");
    }
    return 0;
}
```

This program first asks the user to enter the order of the matrices, then the elements of the two matrices. It then calculates the sum and product of the two matrices and prints the results.



## 27. WAP that finds the sum of diagonal elements of a mxn matrix.

A matrix is a two-dimensional array of numbers. A diagonal of a matrix is a set of elements that run from one corner of the matrix to the opposite corner. In a square matrix, there are two diagonals: the main diagonal and the secondary diagonal. The main diagonal runs from the top-left corner to the bottom-right corner, while the secondary diagonal runs from the top-right corner to the bottom-left corner.

Here is an example of a program that finds the sum of the diagonal elements of a mxn matrix in Python:

```python
def diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    for i in range(rows):
        for j in range(cols):
            if i == j:
                main_diagonal_sum += matrix[i][j]
            if i + j == cols - 1:
                secondary_diagonal_sum += matrix[i][j]
    return main_diagonal_sum, secondary_diagonal_sum
```

This program defines a function `diagonal_sum` that takes a matrix as an input and returns the sum of the main diagonal and the secondary diagonal. The function iterates over the rows and columns of the matrix using two nested for loops. If the row and column indices are equal, the element is on the main diagonal and is added to the `main_diagonal_sum`. If the sum of the row and column indices is equal to the number of columns minus one, the element is on the secondary diagonal and is added to the `secondary_diagonal_sum`. Finally, the function returns the sum of the main and secondary diagonals.

Here is an example of how to use the `diagonal_sum` function:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
main_diagonal_sum, secondary_diagonal_sum = diagonal_sum(matrix)
print(f"Main diagonal sum: {main_diagonal_sum}")
print(f"Secondary diagonal sum: {secondary_diagonal_sum}")
```

This code creates a 3x3 matrix and passes it to the `diagonal_sum` function. The function returns the sum of the main and secondary diagonals, which are printed to the console. The output of this code is:

```
Main diagonal sum: 15
Secondary diagonal sum: 15
```

This shows that the sum of the main diagonal is 15 and the sum of the secondary diagonal is also 15.



## 28. WAP to implement strlen(), strcat(), strcpy() using the concept of Functions

`strlen()` is a function that returns the length of a string. It takes a single argument, which is a pointer to the first character of the string. The function counts the number of characters in the string until it reaches the null character, which marks the end of the string.

Here is an example of how to implement `strlen()` using the concept of functions:

```c
#include <stdio.h>

int my_strlen(char *str) {
    int length = 0;
    while (*str != '\0') {
        length++;
        str++;
    }
    return length;
}

int main() {
    char str[] = "Hello, world!";
    printf("Length of string: %d\n", my_strlen(str));
    return 0;
}
```

`strcat()` is a function that concatenates two strings. It takes two arguments: the first is a pointer to the destination string, and the second is a pointer to the source string. The function appends the source string to the destination string.

Here is an example of how to implement `strcat()` using the concept of functions:

```c
#include <stdio.h>

void my_strcat(char *dest, char *src) {
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

int main() {
    char dest[20] = "Hello, ";
    char src[] = "world!";
    my_strcat(dest, src);
    printf("Concatenated string: %s\n", dest);
    return 0;
}
```

`strcpy()` is a function that copies a string. It takes two arguments: the first is a pointer to the destination string, and the second is a pointer to the source string. The function copies the source string to the destination string.

Here is an example of how to implement `strcpy()` using the concept of functions:

```c
#include <stdio.h>

void my_strcpy(char *dest, char *src) {
    while (*src != '\0') {
        *dest = *src;
        dest++;
        src++;
    }
    *dest = '\0';
}

int main() {
    char src[] = "Hello, world!";
    char dest[20];
    my_strcpy(dest, src);
    printf("Copied string: %s\n", dest);
    return 0;
}
```



## TRAIN_INFO Structure Data Type

A structure data type is a user-defined data type that groups together variables of different data types under a single name. The `TRAIN_INFO` structure data type can be defined to contain information about a train, including its train number, train name, departure time, arrival time, start station, and end station.

Here is an example of how the `TRAIN_INFO` structure data type can be defined:

```c
typedef struct {
    int train_no;
    char train_name[50];
    struct TIME departure_time;
    struct TIME arrival_time;
    char start_station[50];
    char end_station[50];
} TRAIN_INFO;
```

The `TIME` structure data type is an aggregate type that contains two integer members: `hour` and `minute`. It can be defined as follows:

```c
typedef struct {
    int hour;
    int minute;
} TIME;
```

Using these structure data types, a train timetable can be maintained and the following operations can be implemented:
- Add a new train to the timetable
- Remove a train from the timetable
- Update the information of a train in the timetable
- Search for a train in the timetable by its train number or train name
- Display the timetable in a user-friendly format

These operations can be implemented using functions that take the `TRAIN_INFO` structure data type as an argument and manipulate the data accordingly. For example, the `add_train` function can take a `TRAIN_INFO` structure as an argument and add it to the timetable. The `remove_train` function can take a train number as an argument and remove the corresponding train from the timetable. The `update_train` function can take a `TRAIN_INFO` structure as an argument and update the information of the corresponding train in the timetable. The `search_train` function can take a train number or train name as an argument and search for the corresponding train in the timetable. The `display_timetable` function can display the timetable in a user-friendly format.



## a. List all the trains (sorted according to train number) that depart from a particular section.

1. To list all the trains that depart from a particular section, first, identify the section from which the trains are departing.
2. Next, access the train schedule database and retrieve the list of trains that depart from the identified section.
3. Sort the retrieved list of trains in ascending order according to their train numbers.
4. The resulting list will contain all the trains, sorted according to their train numbers, that depart from the particular section.



## b. List all the trains that depart from a particular station at a particular time.

1. To list all the trains that depart from a particular station at a particular time, you can navigate to the “Train B/W Stations” section of a railway website or app.
2. Enter the From Station, To Station, and Journey Date and tap on “Check Trains”.
3. You will get a list of trains running on a particular route with details of the arrival and departure time.
4. The list of Passenger, Mail, Express, or Superfast train with their name and number will be displayed on the screen.



## c. List all the trains that depart from a particular station within the next one hour of a given time.

To list all the trains that depart from a particular station within the next one hour of a given time, you can follow these steps:

1. Identify the station from which you want to list the trains.
2. Determine the current time or the given time from which you want to list the trains.
3. Access the train schedule or timetable for the station.
4. Filter the schedule to only include trains that depart within the next one hour from the given time.
5. List the trains that meet the criteria.

It is important to note that train schedules may be subject to change and delays, so it is always a good idea to check for updates and confirm the departure times before making any plans. Additionally, different stations and train companies may have different methods for accessing and displaying train schedules, so it is important to familiarize yourself with the specific process for the station in question.



## d. List all the trains between a pair of start station and end station.

To list all the trains between a pair of start station and end station, you can follow these steps:

1. Visit the official website of the railway company or a third-party website that provides train information.
2. Enter the start station and end station in the search fields.
3. Select the date of travel.
4. Click on the search button to view the list of trains available between the two stations.
5. The list will display the train name, train number, departure time, arrival time, travel time, and availability of seats in different classes.
6. You can also filter the results based on the train type, departure time, arrival time, and travel time.

Alternatively, you can also visit the railway station and inquire at the ticket counter or use the railway inquiry number to get the list of trains between the two stations.



## 30. WAP to swap two elements using the concept of pointers.

Here is an example of a program that swaps two elements using the concept of pointers in C language:

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

- In this program, the `swap` function takes two pointers to integers as arguments.
- The function uses a temporary variable `temp` to store the value of the first integer pointed to by `a`.
- Then, the value of the first integer is changed to the value of the second integer pointed to by `b`.
- Finally, the value of the second integer is changed to the value stored in the temporary variable `temp`.
- In the `main` function, two integers `x` and `y` are declared and initialized.
- The `swap` function is called with the addresses of `x` and `y` as arguments, using the `&` operator.
- After the function call, the values of `x` and `y` are swapped.




## 31. WAP to compare the contents of two files and determine whether they are same or not.

To compare the contents of two files and determine whether they are the same or not, you can use the following steps:

1. Open the two files in read mode.
2. Read the contents of the first file and store it in a variable.
3. Read the contents of the second file and store it in another variable.
4. Compare the contents of the two variables.
5. If the contents are the same, print that the files are the same.
6. If the contents are not the same, print that the files are not the same.
7. Close the files.

Here is an example code in Python that implements the above steps:

```python
# Open the two files in read mode
file1 = open('file1.txt', 'r')
file2 = open('file2.txt', 'r')

# Read the contents of the first file and store it in a variable
file1_contents = file1.read()

# Read the contents of the second file and store it in another variable
file2_contents = file2.read()

# Compare the contents of the two variables
if file1_contents == file2_contents:
    # If the contents are the same, print that the files are the same
    print('The files are the same.')
else:
    # If the contents are not the same, print that the files are not the same
    print('The files are not the same.')

# Close the files
file1.close()
file2.close()
```

This code opens the two files `file1.txt` and `file2.txt` in read mode, reads their contents, and stores them in the variables `file1_contents` and `file2_contents`, respectively. It then compares the contents of these two variables and prints whether the files are the same or not. Finally, it closes the files.



## 32. WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

Here is a program in Python that can check whether a given word exists in a file or not. If the word exists, the program will also find the number of times it occurs in the file.

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

This function will open the file in read mode and read its content. Then, it will split the content into a list of words and count the number of times the given word occurs in the list. If the count is greater than 0, it means the word exists in the file and the function will print a message indicating that the word exists and the number of times it occurs. Otherwise, the function will print a message indicating that the word does not exist in the file.



## Note:
- A note is a brief record of something that has been written down to assist the memory or for future reference.
- Notes can be written on various mediums, including paper, electronic devices, or even on walls or other surfaces.
- Notes can be used for a variety of purposes, including recording important information, making lists, or jotting down ideas or thoughts.
- Taking notes can help improve memory and retention of information.
- There are various methods for taking notes, including the Cornell Method, the Outline Method, and the Mapping Method.
- It is important to develop a note-taking system that works for the individual, as everyone has different learning styles and preferences.
- Notes can be organized and categorized for easier access and retrieval.
- Reviewing and summarizing notes can help consolidate information and improve understanding.




## a) The Instructor may add/delete/modify/tune experiments, wherever he/she feels in a justified manner

- The instructor has the authority to make changes to the experiments in the course.
- These changes can include adding new experiments, deleting existing experiments, modifying the procedure or outcome of the experiments, or tuning the experiments to better fit the course objectives.
- The instructor should make these changes in a justified manner, meaning that the changes should be made for a valid reason and should be beneficial to the students' learning experience.
- The instructor should communicate any changes to the experiments to the students in a timely and clear manner, so that the students are aware of the changes and can prepare accordingly.



## b) The subject teachers are suggested to use the concept of project based learning. The subject teacher may give certain use cases/case studies where student is able to apply multiple concepts in one single program.

Project-based learning is a teaching method that encourages students to learn by actively engaging in real-world and personally meaningful projects. This approach can be particularly effective in helping students apply multiple concepts in one single program. Here are some points to consider:

1. Project-based learning allows students to apply their knowledge and skills to real-world problems and challenges.
2. By working on a project, students can develop a deeper understanding of the subject matter and its relevance to their lives.
3. Projects can be designed to incorporate multiple concepts, allowing students to see the connections between different areas of study.
4. Teachers can provide use cases or case studies to help guide students in their project work.
5. Project-based learning can be a collaborative effort, allowing students to work together and learn from one another.
6. This approach can help students develop critical thinking, problem-solving, and communication skills.

Overall, project-based learning can be a powerful tool for subject teachers to help their students apply multiple concepts in one single program. By providing use cases or case studies, teachers can guide their students in developing projects that are both meaningful and educational.



## c) It is also suggested that open source tools should be preferred to conduct the lab. Some open source online compiler to conduct the C lab are as follows:

1. **Code::Blocks** - It is a free C, C++ and Fortran IDE built to meet the most demanding needs of its users. It is designed to be very extensible and fully configurable.
2. **Eclipse** - It is an open-source Integrated Development Environment (IDE) supported by IBM. Eclipse is popular for Java application development (Java SE and Java EE) and Android apps. It also supports C/C++, PHP, Python, Perl, and other web project developments via extensible plug-ins.
3. **NetBeans** - It is an open-source Integrated Development Environment written in Java. It supports development in Java, but also supports other languages, especially PHP, C/C++, and HTML5.
4. **CodeLite** - It is an open-source, cross-platform IDE for the C/C++ programming languages. It features project management, code completion, and debugging tools.
5. **Geany** - It is a small and lightweight Integrated Development Environment. It was developed to provide a small and fast IDE, which has only a few dependencies from other packages. It supports many filetypes and has some nice features.

These are some of the open-source tools that can be used to conduct the C lab. They provide a range of features and are widely used by developers. It is recommended to use these tools as they are free and provide a good learning environment.



## JDoodle Online C Compiler

JDoodle is an online compiler and editor for various programming languages, including C. It allows users to write, compile, and execute C code directly from their web browser without the need to install any software.

Some of the features of JDoodle's online C compiler include:
- Support for multiple C standards, including C99 and C11.
- The ability to save and share code snippets with others.
- The option to execute code with custom input.
- A simple and easy-to-use interface.

JDoodle's online C compiler can be a useful tool for anyone looking to quickly test and run C code without the need for a local development environment. It is particularly useful for students and learners who are new to the C programming language.



## Tutorialspoint Online C Compiler

Tutorialspoint provides an online C compiler that allows users to write, compile, and execute C programs directly from their web browser. Here are some key features of the Tutorialspoint Online C Compiler:

1. **Easy to use**: The online C compiler has a simple and intuitive interface, making it easy for users to write and run C programs.
2. **No installation required**: Users do not need to install any software on their computer to use the online C compiler. All that is needed is a web browser and an internet connection.
3. **Immediate feedback**: The online C compiler provides immediate feedback on the compilation and execution of C programs, allowing users to quickly identify and fix errors in their code.
4. **Code sharing**: Users can share their C programs with others by providing a link to the code on the Tutorialspoint website.
5. **Multiple languages**: In addition to C, the online compiler also supports several other programming languages, including C++, Java, Python, and Ruby.

Overall, the Tutorialspoint Online C Compiler is a convenient tool for anyone looking to write, compile, and execute C programs without the need for installing any software. It is especially useful for beginners who are just starting to learn the C programming language.



## Online C Compiler

- An online C compiler is a tool that allows you to compile and execute C code from your web browser.
- It is a convenient way to test and debug small C programs without the need to install a compiler on your local machine.
- One such online C compiler is available at Programiz.com.
- To use the online C compiler, simply navigate to the website, enter your C code into the text editor, and click the "Run" button.
- The compiler will then compile and execute your code, displaying the output in the console below the text editor.
- This tool is useful for quickly testing code snippets or for practicing C programming without the need to set up a development environment.
- However, for larger projects or more complex code, it is recommended to use a local compiler and development environment for better performance and debugging capabilities.



## HackerRank

HackerRank is a technology company that focuses on competitive programming challenges for both consumers and businesses. Here are some key points about HackerRank:

1. HackerRank's programming challenges can be solved in a variety of programming languages and span multiple computer science domains.
2. HackerRank also provides a platform for companies to conduct technical interviews and assess coding skills of candidates.
3. HackerRank has a large community of developers who participate in coding challenges and improve their skills.
4. HackerRank's coding challenges are created by its team of content engineers and are based on real-world scenarios.
5. HackerRank also provides a leaderboard for each challenge, allowing users to see how they rank against other participants.




## Mapping with Virtual Lab

1. Virtual labs are computer-based simulations that allow students to conduct experiments and explore scientific concepts in a virtual environment.
2. Mapping with virtual labs involves using these simulations to create visual representations of data or concepts.
3. This can be done by using software tools to create maps, graphs, or other visualizations that help students understand the data or concepts being studied.
4. Virtual labs can be used to teach a wide range of subjects, including geography, geology, and environmental science.
5. By using virtual labs to create maps, students can explore spatial relationships and patterns in data, and can develop their skills in data analysis and interpretation.
6. Virtual labs can also be used to simulate real-world scenarios, allowing students to explore the potential impacts of different decisions or actions on the environment or on human populations.
7. Overall, mapping with virtual labs provides a powerful tool for teaching and learning, allowing students to engage with complex scientific concepts in a visual and interactive way.



## Name of the Lab: Name of the Experiment

1. Introduction: 
    - The experiment is conducted in the lab named "Name of the Lab".
    - The purpose of the experiment is to study and analyze the "Name of the Experiment".
2. Methodology:
    - The experiment is carried out using the following steps:
        1. Step 1
        2. Step 2
        3. Step 3
3. Results:
    - The results of the experiment are as follows:
        1. Result 1
        2. Result 2
        3. Result 3
4. Conclusion:
    - The experiment was successful in achieving its objective.
    - The findings of the experiment provide valuable insights into the "Name of the Experiment".



## Problem Solving Lab

1. **Introduction**: A problem-solving lab is a structured approach to solving problems. It involves identifying the problem, analyzing it, and developing and implementing a solution.

2. **Identifying the problem**: The first step in problem-solving is to identify the problem. This involves defining the problem and understanding its scope and impact.

3. **Analyzing the problem**: Once the problem has been identified, it is important to analyze it to understand its root cause. This can be done by breaking the problem down into smaller parts and examining each part in detail.

4. **Developing a solution**: After analyzing the problem, the next step is to develop a solution. This involves brainstorming possible solutions and evaluating their feasibility.

5. **Implementing the solution**: Once a solution has been developed, it is important to implement it. This involves putting the solution into action and monitoring its effectiveness.

6. **Conclusion**: A problem-solving lab is an effective way to solve problems. It involves identifying the problem, analyzing it, developing a solution, and implementing it. By following this structured approach, it is possible to solve problems effectively and efficiently.



## Numerical Representation

Numerical representation refers to the various methods used to represent numbers in a computer system. These methods include:

1. **Binary:** This is the most common method of representing numbers in a computer system. It uses only two digits, 0 and 1, to represent numbers. Each digit is called a bit, and a group of 8 bits is called a byte.

2. **Octal:** This method uses 8 digits, from 0 to 7, to represent numbers. It is often used as an intermediate step when converting between binary and decimal.

3. **Decimal:** This is the most common method of representing numbers in everyday life. It uses 10 digits, from 0 to 9, to represent numbers.

4. **Hexadecimal:** This method uses 16 digits, from 0 to 9 and A to F, to represent numbers. It is often used in computer programming to represent binary numbers in a more compact and readable form.

Each of these methods has its own advantages and disadvantages, and the choice of which method to use depends on the specific application and requirements. For example, binary is the most efficient method for storing and processing numbers in a computer system, while decimal is the most intuitive for humans to read and understand.



## Beauty of Numbers

Numbers have a unique beauty that has fascinated mathematicians and non-mathematicians alike for centuries. Here are some interesting points about the beauty of numbers:

1. Numbers have an inherent structure and order that can be observed in nature, such as the Fibonacci sequence found in the arrangement of leaves on a stem or the spirals of a seashell.

2. The study of numbers has led to the development of various branches of mathematics, such as number theory, which explores the properties of integers and their relationships.

3. Numbers can be used to create visually stunning patterns and designs, such as fractals, which exhibit self-similarity at different scales.

4. The use of numbers in music, art, and architecture has resulted in some of the most beautiful and enduring works of human creativity.

5. The exploration of numbers has led to the discovery of fascinating mathematical concepts, such as prime numbers, irrational numbers, and transcendental numbers, which continue to captivate and inspire mathematicians and non-mathematicians alike.

In conclusion, the beauty of numbers lies in their structure, order, and ability to inspire creativity and discovery. They are an essential part of our understanding of the world around us and continue to fascinate and delight us with their endless possibilities.



## More on Numbers

1. **Natural Numbers**: The set of natural numbers is denoted by N and includes all positive integers greater than 0 (1, 2, 3, ...).
2. **Whole Numbers**: The set of whole numbers is denoted by W and includes all natural numbers and 0 (0, 1, 2, 3, ...).
3. **Integers**: The set of integers is denoted by Z and includes all whole numbers and their negative counterparts (...-3, -2, -1, 0, 1, 2, 3, ...).
4. **Rational Numbers**: The set of rational numbers is denoted by Q and includes all numbers that can be expressed as the ratio of two integers, where the denominator is not equal to 0.
5. **Irrational Numbers**: The set of irrational numbers includes all numbers that cannot be expressed as the ratio of two integers. Examples include pi and the square root of 2.
6. **Real Numbers**: The set of real numbers is denoted by R and includes all rational and irrational numbers.
7. **Complex Numbers**: The set of complex numbers is denoted by C and includes all numbers that can be expressed in the form a + bi, where a and b are real numbers and i is the imaginary unit, defined as the square root of -1.




## Factorials

- A factorial is a mathematical operation that is represented by an exclamation point (!) and is used to find the product of all positive integers less than or equal to a given positive integer.
- For example, the factorial of 5 is represented as 5! and is calculated as 5 x 4 x 3 x 2 x 1 = 120.
- The factorial of 0 is defined as 1, which is represented as 0! = 1.
- Factorials are commonly used in probability and statistics, particularly in calculating permutations and combinations.
- The factorial function grows very quickly, meaning that the value of n! becomes very large even for relatively small values of n.
- Factorials can also be calculated using recursive functions, where n! is defined as n x (n-1)! for n > 0, with the base case of 0! = 1.
- Factorials have many applications in mathematics, including in the calculation of the number of ways to arrange a set of objects, the coefficients of a polynomial, and the gamma function.



## String Operations

1. **Concatenation**: The process of combining two or more strings to form a new string. This can be done using the `+` operator or the `join()` method.
2. **Slicing**: Extracting a portion of a string by specifying the start and end indices. This can be done using the `[]` operator.
3. **Indexing**: Accessing individual characters in a string by specifying their index. This can be done using the `[]` operator.
4. **Length**: Finding the number of characters in a string. This can be done using the `len()` function.
5. **Splitting**: Dividing a string into a list of substrings based on a specified delimiter. This can be done using the `split()` method.
6. **Replacing**: Replacing all occurrences of a specified substring with another substring. This can be done using the `replace()` method.
7. **Case conversion**: Converting all characters in a string to uppercase or lowercase. This can be done using the `upper()` and `lower()` methods.
8. **Stripping**: Removing leading and trailing whitespace characters from a string. This can be done using the `strip()` method.
9. **Finding**: Finding the index of the first occurrence of a specified substring within a string. This can be done using the `find()` method.
10. **Counting**: Counting the number of occurrences of a specified substring within a string. This can be done using the `count()` method.




## Recursion

Recursion is a programming technique where a function calls itself repeatedly until a base condition is met. It is a powerful tool that can be used to solve problems that can be broken down into smaller, more manageable sub-problems. Here are some key points to remember about recursion:

1. A recursive function must have a base case, which is a condition that stops the recursion from continuing indefinitely.
2. A recursive function must change its state and move towards the base case with each recursive call.
3. Recursion can be used to solve problems that can be broken down into smaller, more manageable sub-problems.
4. Recursion can be more difficult to understand and debug than iterative solutions, so it is important to use it judiciously.
5. Recursion can be less efficient than iterative solutions due to the overhead of function calls, so it is important to consider the trade-offs when deciding whether to use recursion or iteration to solve a problem.



## Advanced Arithmetic

Advanced arithmetic is a branch of mathematics that deals with the study of numbers and their properties. It includes topics such as:

1. Number theory: the study of the properties of integers and their relationships.
2. Algebra: the study of mathematical symbols and the rules for manipulating these symbols.
3. Geometry: the study of shapes, sizes, and positions of figures.
4. Trigonometry: the study of the relationships between the angles and sides of triangles.
5. Calculus: the study of change and motion, using concepts such as limits, derivatives, and integrals.

Advanced arithmetic is used in many fields, including science, engineering, and finance. It is an essential tool for solving complex problems and making accurate predictions. It is also a fascinating subject in its own right, with many interesting and challenging problems to explore.



## Searching and Sorting

Searching and sorting are fundamental algorithms in computer science. They are used to organize, manipulate, and retrieve data efficiently.

### Searching

Searching algorithms are used to find a specific element in a data structure. There are two main types of searching algorithms: linear search and binary search.

- **Linear search** involves iterating through each element in the data structure until the desired element is found. This algorithm has a time complexity of O(n), where n is the number of elements in the data structure.

- **Binary search** involves repeatedly dividing the data structure in half and checking if the desired element is in the left or right half. This algorithm has a time complexity of O(log n), where n is the number of elements in the data structure. However, binary search can only be used on sorted data.

### Sorting

Sorting algorithms are used to arrange elements in a data structure in a specific order. There are many different sorting algorithms, each with its own advantages and disadvantages. Some common sorting algorithms include:

- **Bubble sort** involves repeatedly comparing adjacent elements and swapping them if they are in the wrong order. This algorithm has a time complexity of O(n^2), where n is the number of elements in the data structure.

- **Selection sort** involves finding the smallest element in the data structure and swapping it with the first element, then finding the smallest element in the remaining data and swapping it with the second element, and so on. This algorithm also has a time complexity of O(n^2).

- **Insertion sort** involves iterating through the data structure and inserting each element into its correct position in the sorted list. This algorithm has a time complexity of O(n^2) in the worst case, but can be much faster for nearly sorted data.

- **Quick sort** involves choosing a pivot element and partitioning the data around the pivot, such that all elements less than the pivot are to its left and all elements greater than the pivot are to its right. The pivot is then placed in its final position, and the process is repeated on the left and right partitions. This algorithm has an average time complexity of O(n log n), where n is the number of elements in the data structure.

- **Merge sort** involves dividing the data into two halves, recursively sorting each half, and then merging the two sorted halves back together. This algorithm has a time complexity of O(n log n).

These are just a few examples of searching and sorting algorithms. There are many more algorithms, each with its own strengths and weaknesses, and the choice of algorithm depends on the specific needs of the task at hand. It is important to understand the basics of these algorithms in order to make informed decisions when working with data.



## Permutation

- A permutation is an arrangement of objects in a specific order.
- The number of permutations of n distinct objects taken r at a time is denoted by nPr.
- The formula for calculating nPr is nPr = n! / (n-r)! where n is the total number of objects and r is the number of objects taken at a time.
- Permutations can be with or without repetition.
- Permutations with repetition are calculated using the formula n^r where n is the total number of objects and r is the number of objects taken at a time.
- Permutations without repetition are calculated using the formula n! / (n-r)! where n is the total number of objects and r is the number of objects taken at a time.
- Permutations can also be circular, where the arrangement of objects is in a circle. The number of circular permutations of n distinct objects is (n-1)!.




## Sequences

A sequence is an ordered list of numbers. Each number in the sequence is called a term. The terms are usually denoted by a variable with a subscript, such as a1, a2, a3, ... , an, where n is the number of terms in the sequence.

There are two main types of sequences: finite and infinite. A finite sequence has a fixed number of terms, while an infinite sequence has an infinite number of terms.

Sequences can be defined in several ways, including:

- Explicitly, where each term is given by a formula. For example, the sequence 2, 4, 6, 8, ... can be defined explicitly by the formula an = 2n.
- Recursively, where each term is defined in terms of the previous terms. For example, the Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, ... can be defined recursively by the formula an = an-1 + an-2, with a1 = 0 and a2 = 1.
- By a rule, where the terms are generated by following a specific rule. For example, the sequence of prime numbers 2, 3, 5, 7, 11, ... can be generated by the rule that each term is the next prime number.

Some common types of sequences include arithmetic sequences, geometric sequences, and harmonic sequences. An arithmetic sequence is a sequence where the difference between consecutive terms is constant, a geometric sequence is a sequence where the ratio between consecutive terms is constant, and a harmonic sequence is a sequence where the reciprocals of the terms form an arithmetic sequence.

Sequences have many applications in mathematics and other fields, including in the study of series, calculus, and number theory. They are also used in computer algorithms and data structures.



## Course Outcomes:
- Define and explain the key concepts and principles of the course.
- Demonstrate an understanding of the course material through application and analysis.
- Communicate effectively in written and oral forms.
- Work collaboratively with others to achieve common goals.
- Apply critical thinking skills to solve problems and make decisions.
- Demonstrate ethical behavior and social responsibility.
- Develop and demonstrate skills for lifelong learning.
- Evaluate and integrate information from multiple sources.
- Use technology effectively to enhance learning and communication.
- Demonstrate an understanding of global and cultural perspectives.



## Course Outcome Bloom’s

- Bloom's Taxonomy is a framework for categorizing educational goals and objectives into different levels of complexity and specificity.
- The taxonomy is divided into six levels: Remembering, Understanding, Applying, Analyzing, Evaluating, and Creating.
- Course outcomes can be written using Bloom's Taxonomy to ensure that students are able to achieve the desired level of understanding and mastery of the course material.
- For example, a course outcome for a mathematics course might be: "Students will be able to apply mathematical concepts to solve real-world problems."
- This outcome aligns with the "Applying" level of Bloom's Taxonomy, as it requires students to use their knowledge and understanding of mathematical concepts to solve problems in a practical context.
- By using Bloom's Taxonomy to write course outcomes, educators can ensure that their courses are designed to help students achieve a deep and meaningful understanding of the material.



## Level

- A level is a tool used to determine if a surface is horizontal (level) or vertical (plumb).
- It is commonly used in construction, carpentry, and surveying.
- The most common type of level is the spirit level, which consists of a sealed, curved tube filled with liquid and an air bubble.
- The position of the bubble within the tube indicates whether the surface is level or not.
- Other types of levels include laser levels, water levels, and electronic levels.
- Levels come in various sizes and shapes, from small torpedo levels to long I-beam levels.
- It is important to use a level when installing floors, hanging pictures, or building structures to ensure that they are straight and even.
- Using a level can also help to prevent problems such as water pooling or doors and windows that do not close properly.



## At the end of the course, the student will be able to:

1. Demonstrate a thorough understanding of the course material and its key concepts.
2. Apply the knowledge and skills acquired during the course to real-world scenarios.
3. Analyze and evaluate information critically and effectively.
4. Communicate ideas and arguments clearly and effectively, both in writing and orally.
5. Work collaboratively with others to achieve common goals.
6. Demonstrate the ability to think creatively and solve problems.
7. Develop a lifelong learning habit and continuously improve their knowledge and skills.




## CO 1 Able to implement the algorithms and draw flowcharts for solving Mathematical and Engineering problems.

- An algorithm is a step-by-step procedure for solving a problem or achieving a specific task.
- Flowcharts are visual representations of an algorithm, using shapes and arrows to show the flow of the process.
- To implement an algorithm for solving mathematical and engineering problems, one must first identify the problem and break it down into smaller, manageable steps.
- These steps can then be translated into an algorithm, using logical and mathematical operations to solve the problem.
- Once the algorithm has been developed, it can be represented visually using a flowchart.
- Flowcharts are useful for understanding the logic and flow of the algorithm, and can help identify any potential issues or areas for improvement.
- By implementing algorithms and using flowcharts, mathematical and engineering problems can be solved in a systematic and efficient manner.



## K3, K4

K3 and K4 are two types of surface groups in mathematics. They are named after the German mathematician Ernst Kummer.

- K3 surfaces are a type of algebraic surface that can be described as the zero locus of a quartic polynomial in three variables.
- K4 surfaces are a type of algebraic surface that can be described as the zero locus of a quartic polynomial in four variables.

These surfaces have interesting properties and are studied in algebraic geometry and number theory. They are related to other mathematical objects such as elliptic curves and Calabi-Yau manifolds.

Some properties of K3 surfaces include:

- They are simply connected, meaning they have no holes or handles.
- They have trivial canonical bundle, meaning their cotangent bundle is trivial.
- They have 20-dimensional space of global holomorphic 2-forms.

K4 surfaces, on the other hand, have not been studied as extensively as K3 surfaces. However, they are also of interest to mathematicians due to their rich geometric and arithmetic properties.



## CO 2 Demonstrate an understanding of computer programming language concepts. K3, K2

1. **Programming languages** are used to write computer programs, which are sets of instructions that tell a computer what to do.
2. **Syntax** refers to the rules that define the structure of a programming language. It specifies how statements must be written and how different elements of the language must be combined.
3. **Semantics** refers to the meaning of the statements in a programming language. It specifies what the statements do and how they affect the behavior of the program.
4. **Variables** are used to store data in a program. They have a name and a value, and the value can change during the execution of the program.
5. **Data types** define the kind of data that can be stored in a variable. Common data types include integers, floating-point numbers, characters, and strings.
6. **Control structures** are used to control the flow of execution in a program. They include conditional statements (such as if-else) and loops (such as for and while).
7. **Functions** are used to organize code into reusable blocks. They take input (arguments), perform some computation, and return a result (return value).
8. **Object-oriented programming** is a programming paradigm that uses objects to represent and manipulate data. Objects have properties (data) and methods (functions) that operate on the data.
9. **Debugging** is the process of finding and fixing errors in a program. Common debugging techniques include using print statements, using a debugger, and writing tests.
10. **Comments** are used to document code and explain what it does. They are ignored by the compiler or interpreter and do not affect the behavior of the program.



## CO 3

CO 3 is a chemical formula that represents the carbonate ion. It is a polyatomic ion with a charge of negative two (-2) and is composed of one carbon atom and three oxygen atoms. Carbonate ions are commonly found in various compounds, including calcium carbonate (CaCO3), which is the main component of limestone, marble, and chalk.

Some key points about CO 3 include:
- It is a polyatomic ion with a charge of -2.
- It is composed of one carbon atom and three oxygen atoms.
- It is commonly found in various compounds, including calcium carbonate (CaCO3).
- Calcium carbonate is the main component of limestone, marble, and chalk.




## Ability to design and develop Computer programs, analyzes, and interprets the concept of pointers, declarations, initialization, operations on pointers and their usage.

- **Pointers** are variables that store the memory addresses of other variables.
- Pointers are declared using the `*` symbol, for example, `int *ptr;` declares a pointer to an integer variable.
- Pointers can be initialized by assigning the address of a variable to them using the `&` symbol, for example, `int x = 5; int *ptr = &x;` initializes the pointer `ptr` to point to the variable `x`.
- Operations on pointers include dereferencing, which allows access to the value stored at the memory address pointed to by the pointer, and pointer arithmetic, which allows for the manipulation of the memory address stored in the pointer.
- Pointers are commonly used in dynamic memory allocation, where memory is allocated at runtime and the address of the allocated memory is stored in a pointer.
- Pointers can also be used to pass variables by reference to functions, allowing for the modification of the variable within the function.
- Understanding the concept of pointers and their usage is crucial for the design and development of efficient and effective computer programs.



## K6, K4

K6 and K4 are both types of telephone booths that were introduced in the United Kingdom by the General Post Office (GPO).

- The **K6** (Kiosk No. 6) was designed by Sir Giles Gilbert Scott to commemorate the silver jubilee of King George V in 1935. It is the most common type of telephone booth in the UK and is also known as the "Jubilee Kiosk".
- The **K4** (Kiosk No. 4) was also designed by Sir Giles Gilbert Scott and was introduced in 1927. It was intended to be a multi-functional kiosk that combined a telephone booth, a post box, and a stamp vending machine. However, it was not as successful as the K6 and only a few hundred were produced.

Both the K6 and K4 are made of cast iron and are painted red. They are considered iconic symbols of British design and culture.



## CO 4

1. CO 4 is a learning outcome that refers to the fourth competency or skill that a student is expected to achieve in a particular course or subject.
2. The specific details of CO 4 will vary depending on the course or subject in question.
3. CO 4 may refer to a particular topic or concept that students are expected to understand, or a specific skill or ability that they are expected to demonstrate.
4. In order to achieve CO 4, students may need to engage in various learning activities such as reading, attending lectures, completing assignments, and participating in discussions.
5. Assessment of CO 4 may involve various methods such as written exams, oral presentations, or practical demonstrations.
6. Achieving CO 4 is an important step in demonstrating mastery of the course or subject material and progressing to more advanced levels of study.




## Able to define data types and use them in simple data processing applications

- A data type is a classification of data that determines the kind of value a variable can hold and the operations that can be performed on it.
- Common data types include integers, floating-point numbers, characters, and strings.
- Data types can be used in simple data processing applications to store and manipulate data.
- For example, an integer data type can be used to store a count of items, while a floating-point data type can be used to store a measurement with a decimal value.

## Use the concept of array of structures

- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- A structure is a collection of variables of different data types, grouped together under a single name.
- An array of structures is a collection of structures, where each structure in the array is an element.
- This can be useful in data processing applications where multiple records of data, each with multiple fields, need to be stored and manipulated.
- For example, an array of structures could be used to store information about a group of people, where each structure represents a person and contains fields for their name, age, and address. The array can then be used to perform operations on the data, such as sorting the records by age or searching for a person by name.



## K1, K5

K1 and K5 are two different types of visas issued by the United States government. Here are some key points about each type of visa:

- **K1 visa** is also known as a fiancé(e) visa. It allows a foreign national to enter the United States for the purpose of marrying a U.S. citizen within 90 days of arrival.
- The K1 visa is a nonimmigrant visa, meaning it is temporary and does not provide a direct path to permanent residency or citizenship.
- To be eligible for a K1 visa, the foreign national and the U.S. citizen must have met in person within the past two years and must intend to marry within 90 days of the foreign national's arrival in the United States.
- **K5 visa** is a derivative visa for the children of K1 visa holders. It allows the children of a K1 visa holder to accompany their parent to the United States.
- The K5 visa is also a nonimmigrant visa and does not provide a direct path to permanent residency or citizenship.
- To be eligible for a K5 visa, the child must be under the age of 21 and unmarried.




## CO 5 Develop confidence for self-education and ability for life-long learning needed for Computer language

1. **Set achievable goals**: Start with small, achievable goals to build confidence and momentum. This will help you stay motivated and focused on your learning journey.

2. **Practice regularly**: Regular practice is essential for developing and maintaining skills in computer languages. Make a schedule and stick to it to ensure consistent progress.

3. **Seek feedback**: Seek feedback from peers, mentors, or online communities to identify areas for improvement and to receive encouragement and support.

4. **Embrace challenges**: Don't be afraid to tackle challenging problems or concepts. These experiences can help you grow and develop your skills.

5. **Stay curious**: Keep an open mind and a curious attitude towards learning. This will help you stay engaged and motivated to continue learning.

6. **Use multiple resources**: Utilize a variety of resources such as books, online tutorials, and courses to diversify your learning experience.

7. **Reflect on your progress**: Take time to reflect on your progress and celebrate your achievements. This will help you stay motivated and focused on your goals.

By following these steps, you can develop the confidence and ability for self-education and life-long learning in computer languages. Remember, learning is a journey, and with the right mindset and approach, you can achieve your goals.



## K3, K4

K3 and K4 are two types of surface groups in mathematics. They are named after the German mathematician Ernst Kummer.

- K3 surfaces are a type of algebraic surface that can be described as the zero locus of a quartic polynomial in three variables.
- K4 surfaces are a type of algebraic surface that can be described as the zero locus of a quartic polynomial in four variables.
- Both K3 and K4 surfaces have interesting geometric and topological properties, and they play an important role in the study of algebraic geometry and string theory.
- K3 surfaces, in particular, have been extensively studied and have many fascinating properties. For example, they are Calabi-Yau manifolds, which means they have a Ricci-flat metric and a trivial canonical bundle.
- K4 surfaces are less well-understood than K3 surfaces, but they are also an active area of research.


