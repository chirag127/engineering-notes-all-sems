

## 1. WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student.

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to perform a certain function or solve a problem.
- To write a WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student, we need to follow these steps:
  - Declare variables to store the marks of 5 subjects, the sum and the percentage.
  - Prompt the user to enter the marks of 5 subjects and store them in the variables.
  - Calculate the sum by adding the marks of 5 subjects.
  - Calculate the percentage by dividing the sum by the total marks (assuming 100 marks for each subject) and multiplying by 100.
  - Display the sum and the percentage to the user.
- Here is an example of a WAP that accepts the marks of 5 subjects and finds the sum and percentage marks obtained by the student in Python:

```python
# Declare variables
marks1 = 0
marks2 = 0
marks3 = 0
marks4 = 0
marks5 = 0
sum = 0
percentage = 0

# Prompt the user to enter the marks of 5 subjects
marks1 = int(input("Enter the marks of subject 1: "))
marks2 = int(input("Enter the marks of subject 2: "))
marks3 = int(input("Enter the marks of subject 3: "))
marks4 = int(input("Enter the marks of subject 4: "))
marks5 = int(input("Enter the marks of subject 5: "))

# Calculate the sum
sum = marks1 + marks2 + marks3 + marks4 + marks5

# Calculate the percentage
percentage = (sum / 500) * 100

# Display the sum and the percentage
print("The sum of marks is: ", sum)
print("The percentage of marks is: ", percentage)
```



## 2. WAP that calculates the Simple Interest and Compound Interest. The Principal, Amount, Rate of Interest and Time are entered through the keyboard.

- Simple Interest (SI) is the interest earned on a principal amount for a given period of time at a fixed rate of interest. It is calculated by the formula:

    `SI = (P * R * T) / 100`

    where P is the principal amount, R is the rate of interest per annum, and T is the time period in years.

- Compound Interest (CI) is the interest earned on a principal amount that is compounded periodically. It is calculated by the formula:

    `CI = P * (1 + R / 100) ^ T - P`

    where P is the principal amount, R is the rate of interest per annum, T is the number of compounding periods, and ^ is the exponentiation operator.

- To write a program that calculates the SI and CI for a given input, we need to follow these steps:

    - Declare and initialize the variables P, R, T, SI, and CI.
    - Prompt the user to enter the values of P, R, and T.
    - Read the values from the keyboard and store them in the respective variables.
    - Calculate the SI using the formula `SI = (P * R * T) / 100`.
    - Calculate the CI using the formula `CI = P * (1 + R / 100) ^ T - P`.
    - Display the values of SI and CI on the screen.

- Here is an example of a program written in C language that implements the above logic:

    ```c
    #include <stdio.h>
    #include <math.h>

    int main()
    {
        // Declare and initialize the variables
        float P, R, T, SI, CI;

        // Prompt the user to enter the values of P, R, and T
        printf("Enter the principal amount: ");
        scanf("%f", &P);
        printf("Enter the rate of interest: ");
        scanf("%f", &R);
        printf("Enter the time period: ");
        scanf("%f", &T);

        // Calculate the SI using the formula SI = (P * R * T) / 100
        SI = (P * R * T) / 100;

        // Calculate the CI using the formula CI = P * (1 + R / 100) ^ T - P
        CI = P * pow((1 + R / 100), T) - P;

        // Display the values of SI and CI on the screen
        printf("The simple interest is: %f\n", SI);
        printf("The compound interest is: %f\n", CI);

        return 0;
    }
    ```



## 3. WAP to calculate the area and circumference of a circle.

- A circle is a geometric shape that consists of all the points that are equidistant from a fixed center point.
- The distance from the center to any point on the circle is called the radius (r) of the circle.
- The area of a circle is the amount of space enclosed by the circle. It is given by the formula: `A = πr^2`, where π is a constant that is approximately equal to 3.14.
- The circumference of a circle is the length of the boundary of the circle. It is given by the formula: `C = 2πr`, where π is the same constant as above.
- To write a program to calculate the area and circumference of a circle, we need to follow these steps:
  - Declare a variable to store the radius of the circle and assign it a value.
  - Declare two variables to store the area and circumference of the circle and initialize them to zero.
  - Use the formulas above to calculate the area and circumference of the circle and assign them to the respective variables.
  - Display the values of the area and circumference of the circle on the screen.

- Here is an example of a program in Python that implements the above steps:

```python
# Declare a variable to store the radius of the circle and assign it a value
r = 5

# Declare two variables to store the area and circumference of the circle and initialize them to zero
A = 0
C = 0

# Use the formulas to calculate the area and circumference of the circle and assign them to the respective variables
A = 3.14 * r * r
C = 2 * 3.14 * r

# Display the values of the area and circumference of the circle on the screen
print("The area of the circle is", A, "square units.")
print("The circumference of the circle is", C, "units.")
```

- The output of the program is:

```
The area of the circle is 78.5 square units.
The circumference of the circle is 31.400000000000002 units.
```



## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- WAP stands for Write a Program, which is a common abbreviation used in computer science and programming courses.
- The problem statement asks us to write a program that can take an input from the user, which is the temperature in Centigrade (also known as Celsius), and convert it into Fahrenheit using the given formula.
- The formula is derived from the fact that the freezing point of water is 0°C or 32°F, and the boiling point is 100°C or 212°F. Therefore, the difference between the two scales is 100°C = 180°F, or 1°C = 1.8°F.
- To write a program, we need to choose a programming language, such as Python, Java, C, etc. For this example, we will use Python, which is a popular and easy-to-learn language.
- The basic steps to write a Python program are:

  - Create a file with a .py extension, such as temp.py, and open it in a text editor or an IDE (Integrated Development Environment).
  - Write the code that defines the logic and functionality of the program, following the syntax and rules of the Python language.
  - Save the file and run it using a Python interpreter, which is a software that can execute the code and produce the output.
  - Test and debug the program, which means checking for errors and fixing them if any.

- The code for the program that solves the problem statement is:

```python
# This is a comment, which is a line that starts with a # symbol and is ignored by the interpreter. Comments are used to explain the code and make it more readable.

# Ask the user to enter the temperature in Centigrade and store it in a variable called celsius
celsius = float(input("Enter the temperature in Centigrade: "))

# Apply the formula to convert the temperature from Centigrade to Fahrenheit and store it in a variable called fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Print the result to the screen using the print() function, which displays the value of the expression inside the parentheses
print("The temperature in Fahrenheit is: ", fahrenheit)
```

- The output of the program will look something like this:

```
Enter the temperature in Centigrade: 25
The temperature in Fahrenheit is:  77.0
```

- To understand the code better, we can break it down into smaller parts and explain each line:

  - The first line is a comment, which is a line that starts with a # symbol and is ignored by the interpreter. Comments are used to explain the code and make it more readable.
  - The second line uses the input() function, which prompts the user to enter some data and returns it as a string. The string inside the parentheses is the message that is displayed to the user. We assign the return value of the input() function to a variable called celsius, which is a name that we choose to store the data. We also use the float() function, which converts the string into a decimal number, because we need to perform arithmetic operations on the temperature value.
  - The third line uses the formula to convert the temperature from Centigrade to Fahrenheit and store it in a variable called fahrenheit. We use the arithmetic operators *, /, and +, which represent multiplication, division, and addition, respectively. We also use parentheses to group the expressions and follow the order of operations. The order of operations is the rule that determines which operation is performed first. In Python, the order is parentheses, exponentiation, multiplication and division, and addition and subtraction. Therefore, the expression inside the parentheses is evaluated first, then the result is multiplied by 9, then divided by 5, and finally added to 32.
  - The fourth line uses the print() function, which displays the value of the expression inside the parentheses to the screen. We use a comma to separate the two expressions, which are the string "The temperature in Fahrenheit is: " and the variable fahrenheit. The print() function automatically adds a space between the two expressions and a newline character at the end, which moves the cursor to the next line.

- This is the end of the program and the explanation. I hope you found it helpful and informative. If you have any questions or feedback, please let me know. Thank you for using my service.🙏



## 5. WAP that swaps values of two variables using a third variable.

- A WAP (write a program) is a task that requires writing code in a specific programming language to achieve a desired output or functionality.
- Swapping values of two variables means exchanging the data stored in the memory locations associated with the variable names.
- Using a third variable means creating a temporary variable that can hold the value of one of the original variables during the swapping process.
- The general algorithm for swapping values of two variables using a third variable is:

  - Declare and initialize two variables with some values, for example `a = 10` and `b = 20`.
  - Declare a third variable, for example `temp`.
  - Assign the value of `a` to `temp`, i.e. `temp = a`.
  - Assign the value of `b` to `a`, i.e. `a = b`.
  - Assign the value of `temp` to `b`, i.e. `b = temp`.
  - Print the values of `a` and `b` after swapping, i.e. `a = 20` and `b = 10`.

- The following is an example of a WAP that swaps values of two variables using a third variable in Python:

```python
# WAP that swaps values of two variables using a third variable

# Declare and initialize two variables
a = 10
b = 20

# Print the values of a and b before swapping
print("Before swapping:")
print("a =", a)
print("b =", b)

# Declare a third variable
temp = 0

# Swap the values of a and b using temp
temp = a # temp holds the value of a
a = b # a gets the value of b
b = temp # b gets the value of temp

# Print the values of a and b after swapping
print("After swapping:")
print("a =", a)
print("b =", b)
```

- The output of the above program is:

```
Before swapping:
a = 10
b = 20
After swapping:
a = 20
b = 10
```



## 6. WAP that checks whether the two numbers entered by the user are equal or not.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- To check whether the two numbers entered by the user are equal or not, we need to compare the values of the two numbers and return a boolean value (True or False) based on the result of the comparison.
- One possible way to write a WAP that checks whether the two numbers entered by the user are equal or not is:

```python
# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers and store the result in a variable
are_equal = (num1 == num2)

# Print the result
print("The two numbers are equal:", are_equal)
```

- The above program uses the following concepts:
  - Input and output: The input() function allows the user to enter data from the keyboard and returns a string. The float() function converts the string to a floating-point number. The print() function displays the data on the screen.
  - Variables and assignment: A variable is a name that refers to a value stored in the memory. The assignment operator (=) assigns a value to a variable.
  - Comparison and boolean: The comparison operator (==) compares the values of two operands and returns True if they are equal and False otherwise. A boolean is a data type that can have only two values: True or False.



## 7. WAP to find the greatest of three numbers.

- A program to find the greatest of three numbers is a common problem in programming that can be solved using various methods such as conditional statements, logical operators, or functions.
- One possible method is to use the `if-else` statement to compare the three numbers and print the largest one. For example, in Python, the program can be written as:

```python
# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Compare the numbers and print the largest one
if num1 > num2 and num1 > num3:
    print(num1, "is the greatest number.")
elif num2 > num1 and num2 > num3:
    print(num2, "is the greatest number.")
else:
    print(num3, "is the greatest number.")
```

- Another possible method is to use the `max()` function to find the maximum value among the three numbers and print it. For example, in Python, the program can be written as:

```python
# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find the maximum value using the max() function and print it
max_num = max(num1, num2, num3)
print(max_num, "is the greatest number.")
```

- These are some of the ways to write a program to find the greatest of three numbers. The output of the program will depend on the input values given by the user. For example, if the user enters 10, 20, and 30, the output will be 30 is the greatest number.



## 8. WAP that finds whether a given number is even or odd.

- A number is even if it is divisible by 2 without any remainder. A number is odd if it is not divisible by 2 or has a remainder of 1 when divided by 2.
- To write a program that finds whether a given number is even or odd, we can use the modulo operator (%) which returns the remainder of a division operation.
- The modulo operator (%) can be used as follows: `number % 2`
- If the result of `number % 2` is 0, then the number is even. If the result of `number % 2` is 1, then the number is odd.
- We can use an if-else statement to check the result of `number % 2` and print the appropriate message.
- The pseudocode for the program is as follows:

```
// Read a number from the user and store it in a variable called number
number = input("Enter a number: ")

// Convert the input to an integer
number = int(number)

// Check if the number is even or odd using the modulo operator
if (number % 2 == 0) {
  // If the number is even, print "The number is even."
  print("The number is even.")
} else {
  // If the number is odd, print "The number is odd."
  print("The number is odd.")
}
```

- The program can be written in different programming languages, such as Python, C, Java, etc. The syntax may vary slightly depending on the language, but the logic is the same.
- Here is an example of the program written in Python:

```python
# Read a number from the user and store it in a variable called number
number = input("Enter a number: ")

# Convert the input to an integer
number = int(number)

# Check if the number is even or odd using the modulo operator
if (number % 2 == 0):
  # If the number is even, print "The number is even."
  print("The number is even.")
else:
  # If the number is odd, print "The number is odd."
  print("The number is odd.")
```

- Here is an example of the program written in C:

```c
#include <stdio.h>

int main() {
  // Declare a variable called number to store the input from the user
  int number;

  // Read a number from the user and store it in the variable number
  printf("Enter a number: ");
  scanf("%d", &number);

  // Check if the number is even or odd using the modulo operator
  if (number % 2 == 0) {
    // If the number is even, print "The number is even."
    printf("The number is even.\n");
  } else {
    // If the number is odd, print "The number is odd."
    printf("The number is odd.\n");
  }

  return 0;
}
```

- Here is an example of the program written in Java:

```java
import java.util.Scanner;

public class EvenOdd {

  public static void main(String[] args) {
    // Create a Scanner object to read input from the user
    Scanner sc = new Scanner(System.in);

    // Declare a variable called number to store the input from the user
    int number;

    // Read a number from the user and store it in the variable number
    System.out.print("Enter a number: ");
    number = sc.nextInt();

    // Check if the number is even or odd using the modulo operator
    if (number % 2 == 0) {
      // If the number is even, print "The number is even."
      System.out.println("The number is even.");
    } else {
      // If the number is odd, print "The number is odd."
      System.out.println("The number is odd.");
    }

    // Close the Scanner object
    sc.close();
  }
}
```



## 9. WAP that tells whether a given year is a leap year or not.

- A leap year is a year that has 366 days instead of 365 days.
- A leap year occurs every four years, except when the year is divisible by 100 and not divisible by 400.
- For example, 2000 and 2020 are leap years, but 1900 and 2100 are not.
- To write a program that tells whether a given year is a leap year or not, we can use the following algorithm:
  - Input the year from the user and store it in a variable, say year.
  - If year is divisible by 4, then
    - If year is divisible by 100, then
      - If year is divisible by 400, then
        - Print "The year is a leap year."
      - Else
        - Print "The year is not a leap year."
    - Else
      - Print "The year is a leap year."
  - Else
    - Print "The year is not a leap year."
- To implement the algorithm in Python, we can use the following code:

```python
# Input the year from the user and store it in a variable, say year.
year = int(input("Enter a year: "))

# If year is divisible by 4, then
if year % 4 == 0:
  # If year is divisible by 100, then
  if year % 100 == 0:
    # If year is divisible by 400, then
    if year % 400 == 0:
      # Print "The year is a leap year."
      print("The year is a leap year.")
    # Else
    else:
      # Print "The year is not a leap year."
      print("The year is not a leap year.")
  # Else
  else:
    # Print "The year is a leap year."
    print("The year is a leap year.")
# Else
else:
  # Print "The year is not a leap year."
  print("The year is not a leap year.")
```



## 10.WAP that accepts marks of five subjects and finds percentage and prints grades according to the following criteria:

- WAP stands for Write a Program.
- The program should take five inputs from the user, representing the marks of five subjects out of 100.
- The program should calculate the percentage of marks by adding the marks of all subjects and dividing by 500.
- The program should print the percentage of marks and the corresponding grade based on the following criteria:

| Percentage | Grade |
|------------|-------|
| >= 90      | A+    |
| >= 80      | A     |
| >= 70      | B+    |
| >= 60      | B     |
| >= 50      | C+    |
| >= 40      | C     |
| < 40       | F     |

- The program should also print a message indicating whether the user has passed or failed the exam. The user passes if the grade is not F, and fails otherwise.
- An example of the program output is:

```
Enter marks of five subjects: 85 76 92 64 71
Percentage: 77.6
Grade: B+
You have passed the exam.
```



## Between 90-100%-----Print ‘A’

- This is a common programming task that involves using conditional statements to check the value of a variable or expression and print a corresponding letter grade.
- A conditional statement is a block of code that executes only if a certain condition is true. For example, `if x > 10: print("x is greater than 10")` will print the message only if the value of x is more than 10.
- To check if a value is between 90 and 100, we can use the logical operator `and`, which returns true only if both operands are true. For example, `x > 90 and x < 100` will return true only if x is more than 90 and less than 100.
- To print a letter grade, we can use the `print` function, which takes an argument and displays it on the screen. For example, `print("A")` will print the letter A.
- Putting it all together, we can write a conditional statement that checks if a value is between 90 and 100 and prints A as follows:

```python
# Assume we have a variable called score that holds a numerical value
if score >= 90 and score <= 100: # Check if score is between 90 and 100
    print("A") # Print A
```

- Note that we used `>=` and `<=` instead of `>` and `<` to include the boundary values of 90 and 100. This is a common convention in grading systems, but it may vary depending on the context.



## Print 'B'

- Printing 'B' is a common task in programming that involves displaying the letter 'B' on the screen or on a paper.
- There are different ways to print 'B' depending on the programming language, the output device, and the format of the letter.
- Some examples of printing 'B' in different programming languages are:

  - In Python, you can use the `print` function to print 'B' on the screen. For example, `print('B')` will print 'B' on a new line. You can also use the `end` parameter to change the ending character. For example, `print('B', end='')` will print 'B' without a newline.
  - In C, you can use the `printf` function to print 'B' on the screen. For example, `printf("B\n")` will print 'B' followed by a newline. You can also use the `\b` escape sequence to move the cursor back one position. For example, `printf("B\b")` will print 'B' and then erase it.
  - In Java, you can use the `System.out.print` method to print 'B' on the screen. For example, `System.out.print('B')` will print 'B' without a newline. You can also use the `System.out.println` method to print 'B' followed by a newline. For example, `System.out.println('B')` will print 'B' on a new line.

- Some examples of printing 'B' on a paper are:

  - You can use a printer to print 'B' on a paper. You need to connect the printer to your computer and install the driver software. You also need to create a document that contains the letter 'B' and choose the print option from the menu. You can adjust the font size, style, and color of the letter before printing.
  - You can use a pen or a pencil to write 'B' on a paper. You need to hold the pen or the pencil firmly and draw two vertical lines and two curves. The curves should connect the vertical lines at the top and the bottom. You can also use different colors and styles to write 'B'.
  - You can use a stencil to draw 'B' on a paper. You need to place the stencil over the paper and trace the outline of the letter 'B' with a pen or a pencil. You can also fill the letter with color or decorate it with patterns.

- Some examples of printing 'B' in different formats are:

  - You can print 'B' in binary format, which is a way of representing data using only two symbols: 0 and 1. The binary code for 'B' is 01000010. You can print 'B' in binary format by using the `bin` function in Python, the `Integer.toBinaryString` method in Java, or the `%b` format specifier in C.
  - You can print 'B' in hexadecimal format, which is a way of representing data using 16 symbols: 0 to 9 and A to F. The hexadecimal code for 'B' is 42. You can print 'B' in hexadecimal format by using the `hex` function in Python, the `Integer.toHexString` method in Java, or the `%x` format specifier in C.
  - You can print 'B' in ASCII art, which is a way of creating images using text characters. The ASCII art for 'B' is:

```
  ___
 | __)
 |__ \
 (___/
```

You can print 'B' in ASCII art by using the `print` function in Python, the `System.out.print` method in Java, or the `printf` function in C. You need to use the `\n` escape sequence to create new lines and the `\` character to escape special characters.



## Print 'C'

- Printing 'C' is a common task in programming that involves displaying the character 'C' on the screen or on a paper.
- There are different ways to print 'C' depending on the programming language, the output device, and the formatting options.
- Some examples of printing 'C' in different programming languages are:

  - In C, C++, and Java, one can use the `printf` or `System.out.print` functions with the format specifier `%c` and the character 'C' as an argument. For example:

    ```c
    printf("%c", 'C'); // prints C on the screen
    ```

  - In Python, one can use the `print` function with the character 'C' as an argument. For example:

    ```python
    print('C') # prints C on the screen
    ```

  - In HTML, one can use the `<p>` tag with the character 'C' as the content. For example:

    ```html
    <p>C</p> <!-- prints C on the web page -->
    ```

- Some examples of printing 'C' on different output devices are:

  - To print 'C' on the screen, one can use the standard output functions of the programming language, such as `printf`, `print`, or `System.out.print`.
  - To print 'C' on a paper, one can use the printer functions of the programming language, such as `print` in Python or `java.awt.print` in Java. One may also need to specify the font, size, and color of the character 'C'.
  - To print 'C' on a LED display, one can use the digital output functions of the programming language, such as `digitalWrite` in Arduino or `GPIO.output` in Raspberry Pi. One may also need to connect the LED display to the appropriate pins of the microcontroller or the computer.

- Some examples of printing 'C' with different formatting options are:

  - To print 'C' in uppercase, one can use the character 'C' itself or the `toupper` function in C and C++.
  - To print 'C' in lowercase, one can use the character 'c' itself or the `tolower` function in C and C++.
  - To print 'C' in bold, one can use the `<b>` tag in HTML or the `**` syntax in Markdown. For example:

    ```html
    <b>C</b> <!-- prints C in bold on the web page -->
    ```

    ```markdown
    **C** <!-- prints C in bold on the screen -->
    ```

  - To print 'C' in italic, one can use the `<i>` tag in HTML or the `*` syntax in Markdown. For example:

    ```html
    <i>C</i> <!-- prints C in italic on the web page -->
    ```

    ```markdown
    *C* <!-- prints C in italic on the screen -->
    ```



## Below 60%-------------Print ‘D’

- This is a conditional statement that checks if a numerical value is below 60% and prints the letter 'D' as a result.
- A conditional statement is a type of programming instruction that executes a block of code only if a certain condition is met or true.
- A numerical value can be a variable, a constant, or an expression that represents a number.
- A percentage is a way of expressing a ratio or a fraction as a number out of 100. For example, 50% means 50 out of 100, or half.
- To check if a numerical value is below 60%, we can use a comparison operator such as < (less than) or <= (less than or equal to).
- A comparison operator returns a boolean value, which is either true or false, depending on the outcome of the comparison.
- A print statement is a type of programming instruction that displays a value or a message on the screen or in the console.
- A letter is a character or a symbol that represents a sound or a word in a language. For example, 'D' is a letter in the English alphabet.
- To print a letter, we can use a string literal, which is a sequence of characters enclosed in quotation marks. For example, "D" is a string literal that contains the letter 'D'.
- Here is an example of a conditional statement that checks if a numerical value is below 60% and prints the letter 'D' in Python, a popular programming language:

```python
# Assume that score is a variable that holds a numerical value
if score < 60: # Check if score is below 60%
  print("D") # Print the letter 'D'
```

- Here is another example of a conditional statement that checks if a numerical value is below 60% and prints the letter 'D' in C++, another popular programming language:

```cpp
// Assume that score is a variable that holds a numerical value
if (score < 60) { // Check if score is below 60%
  cout << "D" << endl; // Print the letter 'D' using the standard output stream
}
```



## 11. WAP that takes two operands and one operator from the user, perform the operation, and prints the result by using Switch statement.

- WAP stands for Write a Program.
- A switch statement is a control structure that allows a program to choose different actions based on a value or expression.
- The syntax of a switch statement is:

```c
switch (expression) {
  case value1:
    // statements for value1
    break;
  case value2:
    // statements for value2
    break;
  ...
  default:
    // statements for default case
    break;
}
```

- The expression can be any valid C expression that evaluates to an integer or a character value.
- The case values must be constants or literals that match the type of the expression.
- The break statement is used to exit the switch statement and prevent the execution of the following cases.
- The default case is optional and is executed when none of the case values match the expression.

- To write a program that takes two operands and one operator from the user, perform the operation, and prints the result by using switch statement, we can follow these steps:

  - Declare three variables to store the operands, the operator, and the result.
  - Prompt the user to enter the first operand and read it using scanf function.
  - Prompt the user to enter the second operand and read it using scanf function.
  - Prompt the user to enter the operator and read it using scanf function.
  - Use a switch statement to check the value of the operator and perform the corresponding operation on the operands.
  - Store the result of the operation in the result variable.
  - Print the result using printf function.
  - Use a default case to handle invalid operators and print an error message.

- An example of the program in C language is:

```c
#include <stdio.h>

int main() {
  // Declare three variables to store the operands, the operator, and the result
  double operand1, operand2, result;
  char operator;

  // Prompt the user to enter the first operand and read it using scanf function
  printf("Enter the first operand: ");
  scanf("%lf", &operand1);

  // Prompt the user to enter the second operand and read it using scanf function
  printf("Enter the second operand: ");
  scanf("%lf", &operand2);

  // Prompt the user to enter the operator and read it using scanf function
  printf("Enter the operator (+, -, *, /): ");
  scanf(" %c", &operator); // Note the space before %c to skip any whitespace

  // Use a switch statement to check the value of the operator and perform the corresponding operation on the operands
  switch (operator) {
    case '+':
      // Add the operands and store the result
      result = operand1 + operand2;
      break;
    case '-':
      // Subtract the operands and store the result
      result = operand1 - operand2;
      break;
    case '*':
      // Multiply the operands and store the result
      result = operand1 * operand2;
      break;
    case '/':
      // Divide the operands and store the result
      // Check if the second operand is zero and print an error message if so
      if (operand2 == 0) {
        printf("Error: Cannot divide by zero.\n");
        return 0; // Exit the program
      }
      result = operand1 / operand2;
      break;
    default:
      // Handle invalid operators and print an error message
      printf("Error: Invalid operator.\n");
      return 0; // Exit the program
  }

  // Print the result using printf function
  printf("%.2lf %c %.2lf = %.2lf\n", operand1, operator, operand2, result);

  return 0; // End the program
}
```

- An example of the output of the program is:

```
Enter the first operand: 10
Enter the second operand: 5
Enter the operator (+, -, *, /): *
10.00 * 5.00 = 50.00
```



## 12. WAP to print the sum of all numbers up to a given number.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- To print the sum of all numbers up to a given number, we need to use a loop that iterates from 1 to the given number and adds each number to a variable that stores the sum.
- We also need to use an input function that takes the given number from the user and converts it to an integer.
- We can use any programming language to write the program, but for this example, we will use Python.
- The program can be written as follows:

```python
# Take the given number from the user and convert it to an integer
n = int(input("Enter a positive integer: "))

# Initialize a variable to store the sum
sum = 0

# Use a loop to iterate from 1 to n and add each number to the sum
for i in range(1, n + 1):
  sum = sum + i

# Print the sum
print("The sum of all numbers up to", n, "is", sum)
```

- The output of the program will depend on the input given by the user. For example, if the user enters 10, the output will be:

```
Enter a positive integer: 10
The sum of all numbers up to 10 is 55
```

- This program can be modified to use different input and output functions, or different looping constructs, depending on the programming language and the requirements of the task.



## 13. WAP to find the factorial of a given number.

- A factorial of a positive integer n is the product of all positive integers from 1 to n, denoted by n!.
- For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.
- The factorial of 0 is defined as 1, i.e., 0! = 1.
- To write a program to find the factorial of a given number, we can use a loop to multiply the numbers from 1 to n.
- We can use either a for loop or a while loop, depending on the programming language and the preference of the programmer.
- Here is an example of a program to find the factorial of a given number in Python:

```python
# Python program to find the factorial of a given number

# Input the number from the user
n = int(input("Enter a positive integer: "))

# Initialize the factorial as 1
factorial = 1

# Check if the number is valid
if n < 0:
    print("Invalid input. Factorial is not defined for negative numbers.")
else:
    # Use a for loop to multiply the numbers from 1 to n
    for i in range(1, n + 1):
        factorial = factorial * i

    # Print the result
    print("The factorial of", n, "is", factorial)
```



## 14.WAP to print sum of even and odd numbers from 1 to N numbers.

- A program to print sum of even and odd numbers from 1 to N numbers is a program that takes a positive integer N as input and calculates the sum of all the even numbers and all the odd numbers from 1 to N, and prints them as output.
- To write such a program, we need to use the following steps:
  - Declare and initialize two variables, `even_sum` and `odd_sum`, to store the sum of even and odd numbers respectively. Assign them the value 0 initially.
  - Declare and initialize another variable, `num`, to store the input value of N. Use the `input()` function to take the input from the user and convert it to an integer using the `int()` function.
  - Use a `for` loop to iterate from 1 to N, using the `range()` function. For each iteration, check if the current value of the loop variable, `i`, is even or odd using the modulo operator (`%`). If `i` is even, add it to `even_sum`. If `i` is odd, add it to `odd_sum`.
  - After the loop ends, print the values of `even_sum` and `odd_sum` using the `print()` function.
- The following is an example of the program in Python:

```python
# Declare and initialize the variables
even_sum = 0
odd_sum = 0

# Take the input from the user
num = int(input("Enter a positive integer: "))

# Use a for loop to iterate from 1 to N
for i in range(1, num + 1):
  # Check if i is even or odd
  if i % 2 == 0:
    # Add i to even_sum
    even_sum += i
  else:
    # Add i to odd_sum
    odd_sum += i

# Print the results
print("The sum of even numbers from 1 to", num, "is", even_sum)
print("The sum of odd numbers from 1 to", num, "is", odd_sum)
```

- The following is an example of the output of the program for the input value of 10:

```
Enter a positive integer: 10
The sum of even numbers from 1 to 10 is 30
The sum of odd numbers from 1 to 10 is 25
```



## 15. WAP to print the Fibonacci series.

- The Fibonacci series is a sequence of numbers where each term is the sum of the previous two terms.
- The first two terms of the Fibonacci series are 1 and 1.
- The general formula for the nth term of the Fibonacci series is:

```
F(n) = F(n-1) + F(n-2)
```

- To write a program to print the Fibonacci series, we need to:

  - Declare a variable to store the number of terms to be printed.
  - Declare three variables to store the current term, the previous term, and the next term of the series.
  - Initialize the first two terms as 1 and 1.
  - Use a loop to iterate from 1 to the number of terms.
  - Print the current term in each iteration.
  - Update the next term as the sum of the current term and the previous term.
  - Update the previous term as the current term.
  - Update the current term as the next term.

- Here is an example of a program to print the Fibonacci series in Python:

```python
# Declare a variable to store the number of terms
n = int(input("Enter the number of terms: "))

# Declare three variables to store the current, previous, and next term
current = 1
previous = 1
next = 0

# Use a loop to iterate from 1 to n
for i in range(1, n+1):
  # Print the current term
  print(current, end=" ")
  # Update the next term as the sum of the current and previous term
  next = current + previous
  # Update the previous term as the current term
  previous = current
  # Update the current term as the next term
  current = next
```

- The output of the program for n = 10 is:

```
1 1 2 3 5 8 13 21 34 55
```



## 16.WAP to check whether the entered number is prime or not.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- To check whether a given number is prime or not, we can use a simple algorithm that iterates from 2 to the square root of the number and checks if any of the numbers divides the given number without a remainder.
- If any such number is found, the given number is not prime. Otherwise, it is prime.
- Here is an example of a program in C language that implements this algorithm:

```c
#include <stdio.h>
#include <math.h>

// A function to check if a number is prime or not
int isPrime(int n)
{
    // If n is less than 2, it is not prime
    if (n < 2)
        return 0;

    // Check if n is divisible by any number from 2 to sqrt(n)
    for (int i = 2; i <= sqrt(n); i++)
    {
        // If n is divisible by i, it is not prime
        if (n % i == 0)
            return 0;
    }

    // If no divisor is found, n is prime
    return 1;
}

// A main function to test the isPrime function
int main()
{
    // Declare a variable to store the input number
    int num;

    // Prompt the user to enter a number
    printf("Enter a number: ");

    // Read the input number
    scanf("%d", &num);

    // Check if the number is prime or not using the isPrime function
    if (isPrime(num))
        printf("%d is a prime number.\n", num);
    else
        printf("%d is not a prime number.\n", num);

    // Return 0 to indicate successful termination
    return 0;
}
```



## 17. WAP to find the sum of digits of the entered number.

- A program to find the sum of digits of the entered number is a program that takes a number as input from the user and calculates the sum of its digits.
- For example, if the user enters 123, the program should output 6, which is the sum of 1, 2 and 3.
- To write such a program, we need to use the following steps:

  - Declare a variable to store the input number and another variable to store the sum of digits. Initialize the sum variable to zero.
  - Use a loop to iterate over the digits of the input number. In each iteration, extract the last digit of the number using the modulo operator (%) and add it to the sum variable. Then, divide the number by 10 to remove the last digit.
  - Repeat the loop until the number becomes zero.
  - Display the sum variable as the output.

- Here is an example of such a program in Python:

```python
# Python program to find the sum of digits of the entered number

# Take input from the user
num = int(input("Enter a number: "))

# Initialize sum to zero
sum = 0

# Loop over the digits of the number
while num > 0:
  # Extract the last digit using modulo operator
  digit = num % 10
  # Add the digit to the sum
  sum = sum + digit
  # Remove the last digit by dividing by 10
  num = num // 10

# Display the sum
print("The sum of digits is", sum)
```

- Here is an example of the output of the program:

```text
Enter a number: 123
The sum of digits is 6
```



## 18.WAP to find the reverse of a number.

- A program to find the reverse of a number is one that takes a positive integer as input and returns its digits in reverse order.
- For example, if the input is 123, the output should be 321.
- One way to write such a program in C language is as follows:

```c
#include <stdio.h>
int main()
{
    int n, rev = 0, rem; // declare variables
    printf("Enter a positive integer: "); // prompt user for input
    scanf("%d", &n); // read input and store in n
    while (n > 0) // loop until n becomes zero
    {
        rem = n % 10; // get the last digit of n
        rev = rev * 10 + rem; // append the digit to rev
        n = n / 10; // remove the last digit of n
    }
    printf("The reverse of the number is %d\n", rev); // print the result
    return 0;
}
```
- The logic behind this program is to use a loop and modulus operator (%) to extract the digits of the number from right to left and multiply them by powers of 10 to form the reverse number.
- For example, if n = 123, then the loop will perform the following steps:

| n | rem | rev |
|---|-----|-----|
| 123 | 3 | 3 |
| 12 | 2 | 32 |
| 1 | 1 | 321 |
| 0 | - | - |

- The loop terminates when n becomes zero and the final value of rev is the reverse of the input number.
- This program assumes that the input is a positive integer. If the input is negative or non-numeric, the program may not work as expected.



## 19.WAP to print Armstrong numbers from 1 to 100.

- An Armstrong number is a number that is equal to the sum of its digits raised to the power of the number of digits.
- For example, 153 is an Armstrong number because 153 = 1^3 + 5^3 + 3^3.
- To print Armstrong numbers from 1 to 100, we need to check each number in this range and verify if it is an Armstrong number or not.
- We can use a loop to iterate over the numbers from 1 to 100 and a function to check if a number is an Armstrong number or not.
- The function can take a number as a parameter and return True if it is an Armstrong number or False otherwise.
- The function can use the following steps to check if a number is an Armstrong number or not:
  - Initialize a variable sum to 0 and a variable temp to the number.
  - Find the number of digits in the number by using a loop and dividing the number by 10 until it becomes 0. Store the number of digits in a variable n.
  - Use another loop to iterate over the digits of the number by using the modulus operator (%) to get the last digit and the integer division operator (//) to remove the last digit from the number.
  - For each digit, raise it to the power of n and add it to the sum variable.
  - Compare the sum variable with the temp variable. If they are equal, return True. Otherwise, return False.
- The code for the function can be written as follows:

```python
def is_armstrong(number):
  sum = 0
  temp = number
  n = 0
  while temp > 0:
    n += 1
    temp //= 10
  temp = number
  while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
  if sum == number:
    return True
  else:
    return False
```

- To print Armstrong numbers from 1 to 100, we can use another loop to call the function for each number and print it if it returns True. The code for the loop can be written as follows:

```python
for i in range(1, 101):
  if is_armstrong(i):
    print(i)
```

- The output of the program will be:

```
1
2
3
4
5
6
7
8
9
153
370
371
407
```



## 20.WAP to convert binary number into decimal number and vice versa.

- A binary number is a number that consists of only two digits: 0 and 1. It is also called a base-2 number system.
- A decimal number is a number that consists of ten digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. It is also called a base-10 number system.
- To convert a binary number into a decimal number, we can use the following algorithm:
  - Start from the rightmost digit of the binary number and assign it a power of 2, starting from 0.
  - Multiply each digit by its corresponding power of 2 and add the results together.
  - The final sum is the decimal equivalent of the binary number.
- For example, to convert 1011 into decimal, we can do the following:
  - Assign powers of 2 to each digit: 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1 * 2^0
  - Multiply and add: 8 + 0 + 2 + 1 = 11
  - The decimal equivalent of 1011 is 11.
- To convert a decimal number into a binary number, we can use the following algorithm:
  - Divide the decimal number by 2 and note the remainder.
  - Repeat the division process until the quotient is 0.
  - The binary equivalent of the decimal number is the sequence of remainders in reverse order.
- For example, to convert 13 into binary, we can do the following:
  - Divide 13 by 2 and note the remainder: 13 / 2 = 6, remainder = 1
  - Divide 6 by 2 and note the remainder: 6 / 2 = 3, remainder = 0
  - Divide 3 by 2 and note the remainder: 3 / 2 = 1, remainder = 1
  - Divide 1 by 2 and note the remainder: 1 / 2 = 0, remainder = 1
  - The binary equivalent of 13 is the sequence of remainders in reverse order: 1101
- A pseudocode for converting binary to decimal is:

```
function binary_to_decimal(binary):
  decimal = 0
  power = 0
  for each digit in binary from right to left:
    decimal = decimal + digit * 2^power
    power = power + 1
  return decimal
```

- A pseudocode for converting decimal to binary is:

```
function decimal_to_binary(decimal):
  binary = ""
  while decimal > 0:
    remainder = decimal % 2
    binary = remainder + binary
    decimal = decimal / 2
  return binary
```



## 21. WAP that simply takes elements of the array from the user and finds the sum of these elements.

- WAP stands for Write A Program, which is a common abbreviation used in programming assignments or exercises.
- An array is a data structure that can store multiple values of the same type in a contiguous memory location.
- To take elements of the array from the user, we need to use some input method, such as `scanf` in C, `cin` in C++, `input` in Python, or `Scanner` in Java.
- To find the sum of these elements, we need to use a loop, such as `for` or `while`, to iterate over the array and add each element to a variable that stores the sum.
- Here is an example of a program that takes elements of the array from the user and finds the sum of these elements in C:

```c
#include <stdio.h>
int main()
{
    int n, i, sum = 0; // declare variables
    printf("Enter the number of elements in the array: "); // prompt the user
    scanf("%d", &n); // read the input
    int arr[n]; // declare the array
    printf("Enter the elements of the array: "); // prompt the user
    for (i = 0; i < n; i++) // loop from 0 to n-1
    {
        scanf("%d", &arr[i]); // read each element
        sum += arr[i]; // add it to the sum
    }
    printf("The sum of the elements is %d\n", sum); // print the result
    return 0; // end the program
}
```



## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

- A WAP (write a program) is a task that requires writing code in a specific programming language to achieve a desired output or functionality.
- In this task, the input is two arrays of the same size, which are collections of data elements of the same type, such as integers, characters, or strings.
- The output is a third array of the same size as the input arrays, which contains the sum of the corresponding elements of the input arrays at each index.
- For example, if the input arrays are [1, 2, 3] and [4, 5, 6], then the output array is [5, 7, 9].
- To write a program that performs this task, we need to follow these steps:

  - Declare and initialize the input arrays with some values, or take the input from the user using a loop or a function.
  - Declare an empty output array of the same size as the input arrays.
  - Use a loop to iterate over the elements of the input arrays, and for each iteration, add the corresponding elements of the input arrays and store the result in the output array at the same index.
  - Use another loop or a function to print the elements of the output array.

- Here is an example of a program that performs this task in C language:

```c
#include <stdio.h>
#define SIZE 3 // define the size of the arrays

int main()
{
  // declare and initialize the input arrays
  int arr1[SIZE] = {1, 2, 3};
  int arr2[SIZE] = {4, 5, 6};

  // declare an empty output array
  int arr3[SIZE];

  // use a loop to iterate over the elements of the input arrays
  for (int i = 0; i < SIZE; i++)
  {
    // add the corresponding elements of the input arrays and store the result in the output array
    arr3[i] = arr1[i] + arr2[i];
  }

  // use another loop to print the elements of the output array
  printf("The output array is:\n");
  for (int i = 0; i < SIZE; i++)
  {
    printf("%d ", arr3[i]);
  }
  printf("\n");

  return 0;
}
```

- The output of this program is:

```
The output array is:
5 7 9
```



## 23.WAP to find the minimum and maximum element of the array.

- An array is a collection of elements of the same data type, stored in contiguous memory locations.
- To find the minimum and maximum element of the array, we need to compare each element with a variable that stores the current minimum or maximum value, and update the variable if a smaller or larger element is found.
- There are different ways to implement this algorithm, such as using loops, recursion, or built-in functions.
- Here is one possible way to write a program in C language to find the minimum and maximum element of the array using loops:

```c
#include <stdio.h>
#define SIZE 10 //define the size of the array

int main()
{
    int arr[SIZE]; //declare an array of size 10
    int i, min, max; //declare variables for loop index, minimum and maximum element

    printf("Enter %d elements of the array: \n", SIZE); //prompt the user to enter the elements of the array
    for(i = 0; i < SIZE; i++) //loop from 0 to SIZE-1
    {
        scanf("%d", &arr[i]); //read the element from the user and store it in the array
    }

    min = max = arr[0]; //initialize the minimum and maximum element to the first element of the array

    for(i = 1; i < SIZE; i++) //loop from 1 to SIZE-1
    {
        if(arr[i] < min) //if the current element is smaller than the minimum element
        {
            min = arr[i]; //update the minimum element to the current element
        }
        if(arr[i] > max) //if the current element is larger than the maximum element
        {
            max = arr[i]; //update the maximum element to the current element
        }
    }

    printf("The minimum element of the array is %d\n", min); //print the minimum element of the array
    printf("The maximum element of the array is %d\n", max); //print the maximum element of the array

    return 0; //return 0 to indicate successful termination of the program
}
```



## 24.WAP to search an element in a array using Linear Search.

Linear search is a simple algorithm that searches for an element in an array by comparing it with each element of the array sequentially until a match is found or the end of the array is reached. The algorithm can be written as follows:

- Start from the leftmost element of the array and compare it with the element to be searched.
- If the element matches, return the index of the element and stop the search.
- If the element does not match, move to the next element of the array and repeat step 2.
- If the end of the array is reached and no match is found, return -1 to indicate that the element is not present in the array.

The pseudocode for linear search is:

```
function linear_search(array, element)
  for i = 0 to array.length - 1
    if array[i] == element
      return i
    end if
  end for
  return -1
end function
```

The code for linear search in C is:

```
#include <stdio.h>

int linear_search(int array[], int size, int element)
{
  int i;
  for (i = 0; i < size; i++)
  {
    if (array[i] == element)
    {
      return i;
    }
  }
  return -1;
}

int main()
{
  int array[] = {10, 20, 30, 40, 50};
  int size = sizeof(array) / sizeof(array[0]);
  int element = 30;
  int result = linear_search(array, size, element);
  if (result == -1)
  {
    printf("Element not found in the array.\n");
  }
  else
  {
    printf("Element found at index %d.\n", result);
  }
  return 0;
}
```

The output of the code is:

```
Element found at index 2.
```



## 25.WAP to sort the elements of the array in ascending order using Bubble Sort technique.

- Bubble sort is a simple sorting algorithm that compares adjacent elements of an array and swaps them if they are in the wrong order.
- The algorithm repeats this process until the array is sorted.
- The name bubble sort comes from the fact that the smaller elements "bubble" to the top of the array, while the larger elements sink to the bottom.
- The algorithm can be implemented in any programming language, but here is an example in C:

```c
// A function to sort an array using bubble sort
void bubbleSort(int arr[], int n) {
  // n is the size of the array
  int i, j, temp; // variables for looping and swapping
  for (i = 0; i < n - 1; i++) { // loop through the array n-1 times
    for (j = 0; j < n - i - 1; j++) { // loop through the unsorted part of the array
      if (arr[j] > arr[j + 1]) { // compare adjacent elements
        // swap them if they are in the wrong order
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

// A function to print an array
void printArray(int arr[], int n) {
  // n is the size of the array
  int i; // variable for looping
  for (i = 0; i < n; i++) { // loop through the array
    printf("%d ", arr[i]); // print each element
  }
  printf("\n"); // print a new line
}

// A main function to test the bubble sort function
int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90}; // an example array
  int n = sizeof(arr) / sizeof(arr[0]); // calculate the size of the array
  printf("Unsorted array: \n");
  printArray(arr, n); // print the unsorted array
  bubbleSort(arr, n); // sort the array using bubble sort
  printf("Sorted array: \n");
  printArray(arr, n); // print the sorted array
  return 0; // end the program
}
```
- The output of the program is:

```
Unsorted array: 
64 34 25 12 22 11 90 
Sorted array: 
11 12 22 25 34 64 90 
```
- Some points to remember about bubble sort are:

  - It is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the array.
  - It has a time complexity of O(n^2) in the worst and average case, and O(n) in the best case, where n is the size of the array.
  - It has a space complexity of O(1), meaning that it does not require any extra space apart from the input array.
  - It is one of the simplest sorting algorithms to understand and implement, but it is not very efficient for large or nearly sorted arrays.



## 26.WAP to add and multiply two matrices of order nxn.

- A matrix is a rectangular array of numbers arranged in rows and columns.
- To add two matrices of order nxn, we need to add the corresponding elements of both matrices and store the result in a new matrix of the same order.
- To multiply two matrices of order nxn, we need to multiply each row of the first matrix with each column of the second matrix and sum up the products to get the elements of the new matrix of the same order.
- The following is a pseudocode for adding and multiplying two matrices of order nxn:

```
// Declare three matrices A, B and C of order nxn
matrix A[n][n], B[n][n], C[n][n]

// Input the elements of matrix A
for i = 0 to n-1
  for j = 0 to n-1
    input A[i][j]

// Input the elements of matrix B
for i = 0 to n-1
  for j = 0 to n-1
    input B[i][j]

// Add the matrices A and B and store the result in matrix C
for i = 0 to n-1
  for j = 0 to n-1
    C[i][j] = A[i][j] + B[i][j]

// Display the matrix C
for i = 0 to n-1
  for j = 0 to n-1
    print C[i][j]
  print newline

// Multiply the matrices A and B and store the result in matrix C
for i = 0 to n-1
  for j = 0 to n-1
    C[i][j] = 0 // Initialize the element to zero
    for k = 0 to n-1
      C[i][j] = C[i][j] + A[i][k] * B[k][j] // Sum up the products

// Display the matrix C
for i = 0 to n-1
  for j = 0 to n-1
    print C[i][j]
  print newline
```



## 27.WAP that finds the sum of diagonal elements of a mxn matrix.

- A matrix is a rectangular array of numbers arranged in rows and columns.
- A diagonal element of a matrix is an element that lies on the diagonal line that connects the top left corner and the bottom right corner of the matrix.
- A mxn matrix has m rows and n columns, where m and n are positive integers.
- To find the sum of diagonal elements of a mxn matrix, we need to loop through the matrix and add the elements that have the same row and column index, i.e., the elements at positions (i, i) where i ranges from 0 to min(m, n) - 1.
- The following is a pseudocode for a program that finds the sum of diagonal elements of a mxn matrix:

```
// Assume that matrix is a mxn matrix that is given as input
sum = 0 // Initialize the sum to zero
for i = 0 to min(m, n) - 1 // Loop through the diagonal elements
    sum = sum + matrix[i][i] // Add the current element to the sum
end for
print sum // Print the sum
```



## 28.WAP to implement strlen (), strcat (),strcpy () using the concept of Functions.

- The strlen() function returns the length of a given string. It does not count the null character '\0' at the end of the string.
- The strcat() function appends one string to the end of another string. It assumes that the destination string has enough space to hold the concatenated result. It also overwrites the null character of the destination string with the first character of the source string, and adds a null character at the end of the concatenated string.
- The strcpy() function copies one string to another string. It assumes that the destination string has enough space to hold the source string. It also copies the null character from the source string to the destination string.

- Here is a possible C program to implement these functions using the concept of functions:

```c
#include <stdio.h>

// A function to return the length of a string
int strlen(char *s)
{
    int len = 0; // Initialize a variable to store the length
    while (*s != '\0') // Loop until the end of the string
    {
        len++; // Increment the length
        s++; // Move the pointer to the next character
    }
    return len; // Return the length
}

// A function to append one string to another string
void strcat(char *dest, char *src)
{
    while (*dest != '\0') // Loop until the end of the destination string
    {
        dest++; // Move the pointer to the next character
    }
    while (*src != '\0') // Loop until the end of the source string
    {
        *dest = *src; // Copy the character from the source to the destination
        dest++; // Move the pointer to the next character
        src++; // Move the pointer to the next character
    }
    *dest = '\0'; // Add a null character at the end of the concatenated string
}

// A function to copy one string to another string
void strcpy(char *dest, char *src)
{
    while (*src != '\0') // Loop until the end of the source string
    {
        *dest = *src; // Copy the character from the source to the destination
        dest++; // Move the pointer to the next character
        src++; // Move the pointer to the next character
    }
    *dest = '\0'; // Add a null character at the end of the copied string
}

// A main function to test the above functions
int main()
{
    char s1[20] = "Hello"; // Declare and initialize a string
    char s2[20] = "World"; // Declare and initialize another string
    char s3[20]; // Declare a string to hold the result

    printf("The length of s1 is %d\n", strlen(s1)); // Print the length of s1
    printf("The length of s2 is %d\n", strlen(s2)); // Print the length of s2

    strcpy(s3, s1); // Copy s1 to s3
    printf("The string s3 is %s\n", s3); // Print s3

    strcat(s3, s2); // Append s2 to s3
    printf("The string s3 is %s\n", s3); // Print s3

    return 0; // Return 0 to indicate successful termination
}
```



## 29.Define a structure data type TRAIN_INFO. The type contain Train No.: integer type Train name: string Departure Time: aggregate type TIME Arrival Time: aggregate type TIME Start station: string End station: string The structure type Time contains two integer members: hour and minute. Maintain a train timetable and implement the following operations:

- To define a structure data type TRAIN_INFO, we can use the following syntax in C:

```c
// Define the structure type TIME
struct TIME {
  int hour; // integer member for hour
  int minute; // integer member for minute
};

// Define the structure type TRAIN_INFO
struct TRAIN_INFO {
  int train_no; // integer member for train number
  char train_name[50]; // string member for train name
  struct TIME departure_time; // aggregate member for departure time
  struct TIME arrival_time; // aggregate member for arrival time
  char start_station[50]; // string member for start station
  char end_station[50]; // string member for end station
};
```

- To maintain a train timetable, we can declare an array of TRAIN_INFO structures and initialize it with some sample data:

```c
// Declare an array of TRAIN_INFO structures
struct TRAIN_INFO timetable[5];

// Initialize the array with some sample data
timetable[0].train_no = 101;
strcpy(timetable[0].train_name, "Rajdhani Express");
timetable[0].departure_time.hour = 10;
timetable[0].departure_time.minute = 15;
timetable[0].arrival_time.hour = 18;
timetable[0].arrival_time.minute = 30;
strcpy(timetable[0].start_station, "New Delhi");
strcpy(timetable[0].end_station, "Mumbai");

timetable[1].train_no = 102;
strcpy(timetable[1].train_name, "Shatabdi Express");
timetable[1].departure_time.hour = 8;
timetable[1].departure_time.minute = 45;
timetable[1].arrival_time.hour = 12;
timetable[1].arrival_time.minute = 15;
strcpy(timetable[1].start_station, "Chennai");
strcpy(timetable[1].end_station, "Bangalore");

timetable[2].train_no = 103;
strcpy(timetable[2].train_name, "Duronto Express");
timetable[2].departure_time.hour = 6;
timetable[2].departure_time.minute = 30;
timetable[2].arrival_time.hour = 14;
timetable[2].arrival_time.minute = 45;
strcpy(timetable[2].start_station, "Kolkata");
strcpy(timetable[2].end_station, "Delhi");

timetable[3].train_no = 104;
strcpy(timetable[3].train_name, "Garib Rath");
timetable[3].departure_time.hour = 9;
timetable[3].departure_time.minute = 0;
timetable[3].arrival_time.hour = 16;
timetable[3].arrival_time.minute = 0;
strcpy(timetable[3].start_station, "Hyderabad");
strcpy(timetable[3].end_station, "Pune");

timetable[4].train_no = 105;
strcpy(timetable[4].train_name, "Jan Shatabdi");
timetable[4].departure_time.hour = 7;
timetable[4].departure_time.minute = 15;
timetable[4].arrival_time.hour = 11;
timetable[4].arrival_time.minute = 30;
strcpy(timetable[4].start_station, "Ahmedabad");
strcpy(timetable[4].end_station, "Surat");
```

- To implement the following operations, we can define some functions that take the timetable array and other parameters as arguments and perform the required tasks:

  - Display the train number, train name, departure time and arrival time of all the trains.
  - Display the train number, train name, departure time and arrival time of a particular train given its train number.
  - Display the train number, train name, departure time and arrival time of all the trains that start from a given station.
  - Display the train number, train name, departure time and arrival time of all the trains that end at a given station.
  - Display the train number, train name, departure time and arrival time of all the trains that have a travel time less than a given duration.

```c
// Define a function to display the train number, train name, departure time and arrival time of all the trains
void display_all(struct TRAIN_INFO timetable[], int size) {

```




## a. List all the trains (sorted according to train number) that depart from a particular section.

- To list all the trains that depart from a particular section, we need to use the **section** and **train** tables from the railway database.
- The **section** table contains information about the sections of the railway network, such as the section number, the starting station, the ending station, and the distance.
- The **train** table contains information about the trains, such as the train number, the name, the type, the source station, the destination station, and the departure and arrival times.
- To list all the trains that depart from a particular section, we need to join the **section** and **train** tables on the condition that the starting station of the section matches the source station of the train.
- We also need to sort the resulting table by the train number in ascending order.
- The SQL query to perform this task is:

```sql
SELECT train.train_no, train.name, train.type, train.source, train.destination, train.departure, train.arrival
FROM section
JOIN train
ON section.start = train.source
WHERE section.sec_no = <section number>
ORDER BY train.train_no;
```

- Here, `<section number>` is a placeholder for the section number that we want to query.
- For example, if we want to list all the trains that depart from section 1, we can replace `<section number>` with 1 in the query.
- The output of the query will be a table with the following columns: train_no, name, type, source, destination, departure, and arrival.
- The table will contain one row for each train that departs from section 1, and the rows will be sorted by the train number in ascending order.



## b. List all the trains that depart from a particular station at a particular time.

- To list all the trains that depart from a particular station at a particular time, one needs to have access to a database or a website that contains the train schedules and availability for the desired station and time.
- One possible way to access such information is to use the National Rail Enquiries website, which provides real-time information on train services across the UK. The website can be accessed through a web browser or a mobile app.
- To use the website, one needs to enter the name or the code of the station in the "From" field, and optionally the name or the code of the destination station in the "To" field. Then, one needs to select the date and the time of departure in the "When" field, and click on the "Go" button.
- The website will then display a list of all the trains that depart from the selected station at the selected time, along with their destinations, departure platforms, journey times, and service status. The list can be sorted by time, destination, or status, and can be filtered by train operator, ticket type, or service type.
- The website also provides a map view of the station and the trains, and a live departure board that shows the current status of the trains. The website also allows the user to book tickets, check fares, and plan journeys.
- Alternatively, one can also use other websites or apps that provide similar information, such as Trainline, Rail Planner, or Google Maps. The steps to use these websites or apps may vary slightly, but the basic idea is the same: enter the station name or code, the date and time of departure, and optionally the destination, and get a list of all the trains that depart from the station at the time.



## c. List all the trains that depart from a particular station within the next one hour of a given time.

- To list all the trains that depart from a particular station within the next one hour of a given time, one possible algorithm is as follows:

  - Input: the name of the station, the current time
  - Output: a list of trains with their departure times and destinations
  - Steps:
    - Initialize an empty list to store the output
    - Access the database of train schedules for the given station
    - For each train in the database, check if its departure time is within the next one hour of the current time
    - If yes, append the train's information to the output list
    - Sort the output list by departure time in ascending order
    - Return the output list

- For example, if the input is "New York Penn Station, 15:39", the output could be:

  - Train 1: 15:45, Boston
  - Train 2: 15:50, Washington DC
  - Train 3: 16:00, Philadelphia
  - Train 4: 16:15, Chicago
  - Train 5: 16:30, Miami
  - Train 6: 16:35, Toronto



## d. List all the trains between a pair of start station and end station.

- To list all the trains between a pair of start station and end station, we need to use a database that contains information about the train schedules, routes, and availability.
- One possible database is the Indian Railways API, which provides various methods to query the train data using HTTP requests and JSON responses.
- To use the Indian Railways API, we need to register and obtain an API key, which is a unique identifier that allows us to access the data.
- One of the methods that the Indian Railways API provides is the Train Between Stations method, which takes two parameters: source and destination station codes.
- The station codes are four-letter codes that represent the railway stations in India. For example, the station code for New Delhi is NDLS and the station code for Mumbai Central is BCT.
- The Train Between Stations method returns a list of trains that run between the given source and destination stations, along with their train numbers, names, departure and arrival times, travel time, days of operation, and classes of seats available.
- To use the Train Between Stations method, we need to construct a URL that contains the API key, the source station code, and the destination station code, and send a GET request to the URL.
- For example, to list all the trains between New Delhi and Mumbai Central, we can use the following URL:

`https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/<API_KEY>/From/<SOURCE_STATION_CODE>/To/<DESTINATION_STATION_CODE>/`

- Replacing the placeholders with the actual values, we get:

`https://indianrailapi.com/api/v2/TrainBetweenStation/apikey/123456789/From/NDLS/To/BCT/`

- Sending a GET request to this URL will return a JSON response that contains a list of trains, such as:

```json
{
  "ResponseCode": 200,
  "Message": "Success",
  "Trains": [
    {
      "TrainNo": "02951",
      "TrainName": "MUMBAI RAJDHANI",
      "TrainType": "RAJDHANI",
      "Source": "NDLS",
      "DepartureTime": "16:25",
      "Destination": "BCT",
      "ArrivalTime": "08:15",
      "TravelTime": "15:50",
      "Distance": "1384",
      "Days": "SUN, MON, TUE, WED, THU, FRI, SAT",
      "Classes": [
        {
          "ClassCode": "1A",
          "Availability": "Y"
        },
        {
          "ClassCode": "2A",
          "Availability": "Y"
        },
        {
          "ClassCode": "3A",
          "Availability": "Y"
        }
      ]
    },
    {
      "TrainNo": "02953",
      "TrainName": "AUG KR RAJ EXP",
      "TrainType": "RAJDHANI",
      "Source": "NDLS",
      "DepartureTime": "17:15",
      "Destination": "BCT",
      "ArrivalTime": "09:45",
      "TravelTime": "16:30",
      "Distance": "1384",
      "Days": "SUN, MON, TUE, WED, THU, FRI, SAT",
      "Classes": [
        {
          "ClassCode": "1A",
          "Availability": "Y"
        },
        {
          "ClassCode": "2A",
          "Availability": "Y"
        },
        {
          "ClassCode": "3A",
          "Availability": "Y"
        }
      ]
    },
    ...
  ]
}
```

- To display the list of trains in a tabular format, we can use the markdown syntax for tables, such as:

| Train No | Train Name | Departure Time | Arrival Time | Travel Time | Days |
| -------- | ---------- | -------------- | ------------ | ----------- | ---- |
| 02951 | MUMBAI RAJDHANI | 16:25 | 08:15 | 15:50 | SUN, MON, TUE, WED, THU, FRI, SAT |
| 02953 | AUG KR RAJ EXP | 17:15 | 09:45 | 16:30 | SUN, MON, TUE, WED, THU, FRI, SAT |
| ... | ... | ... | ... | ... | ... |

- This is one possible way to list all the trains between a pair of



## 30. WAP to swap two elements using the concept of pointers.

- A pointer is a variable that stores the address of another variable in memory.
- To swap two elements using pointers, we need to pass the addresses of the elements to a function that will swap their values using a temporary variable.
- The function will use the dereference operator (*) to access the values pointed by the pointers and assign them to the temporary variable and vice versa.
- The function will not return anything, but the changes will be reflected in the original variables as they are passed by reference.
- Here is an example of a C program that swaps two integers using pointers:

```c
#include <stdio.h>

// A function that swaps the values of two integers pointed by x and y
void swap(int *x, int *y)
{
    // Declare a temporary variable
    int temp;

    // Store the value pointed by x in temp
    temp = *x;

    // Assign the value pointed by y to the location pointed by x
    *x = *y;

    // Assign the value stored in temp to the location pointed by y
    *y = temp;
}

int main()
{
    // Declare and initialize two integers
    int a = 10, b = 20;

    // Print the original values of a and b
    printf("Before swapping: a = %d, b = %d\n", a, b);

    // Call the swap function and pass the addresses of a and b
    swap(&a, &b);

    // Print the swapped values of a and b
    printf("After swapping: a = %d, b = %d\n", a, b);

    return 0;
}
```

- The output of the program will be:

```
Before swapping: a = 10, b = 20
After swapping: a = 20, b = 10
```

- This is how we can swap two elements using the concept of pointers.



## 31. WAP to compare the contents of two files and determine whether they are same or not.

- A possible algorithm to compare the contents of two files and determine whether they are same or not is:

  - Open both files in read mode.
  - Initialize a variable `flag` to `True`.
  - Loop until the end of either file is reached.
    - Read a line from each file and store them in variables `line1` and `line2`.
    - If `line1` is not equal to `line2`, set `flag` to `False` and break the loop.
  - Close both files.
  - If `flag` is `True`, print "The files are same." Otherwise, print "The files are different."

- A possible implementation of the algorithm in Python is:

```python
# Open both files in read mode
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

# Initialize a variable flag to True
flag = True

# Loop until the end of either file is reached
while True:
  # Read a line from each file and store them in variables line1 and line2
  line1 = file1.readline()
  line2 = file2.readline()

  # If line1 is not equal to line2, set flag to False and break the loop
  if line1 != line2:
    flag = False
    break

  # If the end of either file is reached, break the loop
  if not line1 or not line2:
    break

# Close both files
file1.close()
file2.close()

# If flag is True, print "The files are same." Otherwise, print "The files are different."
if flag:
  print("The files are same.")
else:
  print("The files are different.")
```



## 32.WAP to check whether a given word exists in a file or not. If yes then find the number of times it occurs.

- A possible solution to this problem is to use the `open()` function to read the file and the `count()` method to count the occurrences of the word in each line of the file.
- The `open()` function takes the name of the file as an argument and returns a file object that can be used to read or write the file.
- The `count()` method takes a substring as an argument and returns the number of times it appears in the string.
- The algorithm for the solution is as follows:

  - Declare a variable `word` to store the word to be searched and assign it a value.
  - Declare a variable `filename` to store the name of the file and assign it a value.
  - Declare a variable `count` to store the number of occurrences of the word and initialize it to zero.
  - Open the file using the `open()` function and assign the file object to a variable `file`.
  - Use a `for` loop to iterate over each line of the file.
  - Use the `count()` method to count the number of occurrences of the word in the current line and add it to the `count` variable.
  - Close the file using the `close()` method of the file object.
  - Check if the `count` variable is greater than zero. If yes, print the word and the number of occurrences. If no, print that the word does not exist in the file.

- A possible implementation of the solution in Python is as follows:

```python
# Declare the word and the filename
word = "hello"
filename = "sample.txt"

# Initialize the count to zero
count = 0

# Open the file
file = open(filename, "r")

# Loop over each line of the file
for line in file:
  # Count the occurrences of the word in the line
  count += line.count(word)

# Close the file
file.close()

# Check if the word exists in the file
if count > 0:
  # Print the word and the number of occurrences
  print(f"The word '{word}' exists in the file '{filename}' and occurs {count} times.")
else:
  # Print that the word does not exist in the file
  print(f"The word '{word}' does not exist in the file '{filename}'.")
```



## Note:

- A note is a brief piece of writing that records information or observations on a specific topic, usually for future reference or personal use.
- Notes can be written in various formats, such as outlines, lists, tables, diagrams, charts, etc., depending on the purpose and the nature of the information.
- Notes can be taken from various sources, such as lectures, books, articles, videos, podcasts, etc., using different methods, such as summarizing, paraphrasing, quoting, highlighting, etc., depending on the level of detail and accuracy required.
- Notes can be used for various purposes, such as studying, reviewing, revising, researching, brainstorming, planning, etc., depending on the goal and the context of the user.
- Notes can be improved by using various techniques, such as organizing, categorizing, labeling, linking, annotating, etc., depending on the clarity and the usefulness of the information.



## a) The Instructor may add/delete/modify/tune experiments, wherever he/she feels in a justified manner

- This statement implies that the instructor has the authority and responsibility to design and implement the experiments for the course, according to the learning objectives and outcomes.
- The instructor may add new experiments to introduce new concepts, skills, or applications that are relevant and useful for the course.
- The instructor may delete existing experiments if they are outdated, redundant, or irrelevant for the course.
- The instructor may modify or tune the existing experiments to improve their clarity, accuracy, difficulty, or effectiveness.
- The instructor should always provide a clear and reasonable justification for any changes made to the experiments, and communicate them to the students and other stakeholders in a timely manner.
- The instructor should also ensure that the changes do not compromise the quality, validity, or fairness of the experiments, and that they are aligned with the course syllabus and assessment criteria.



## b) The subject teachers are suggested to use the concept of project based learning. The subject teacher may give certain use cases/case studies where student is able to apply multiple concepts in one single program

- Project based learning (PBL) is a teaching method that engages students in learning by solving real-world problems or challenges.
- PBL helps students develop 21st century skills such as critical thinking, creativity, collaboration, communication, and digital literacy.
- PBL also helps students connect their learning to their interests, passions, and future goals.
- PBL can be applied to any subject or discipline, but it is especially suitable for computer science, where students can use programming to create solutions for various scenarios or domains.
- Some examples of use cases/case studies for PBL in computer science are:

  - Creating a website or an app for a social cause, such as raising awareness, fundraising, or providing information or services to a specific community or group.
  - Developing a game or a simulation that teaches a concept, such as physics, math, history, or geography, or that entertains or challenges the player.
  - Designing a data analysis or visualization tool that helps users understand a complex phenomenon, such as climate change, health, or economics.
  - Building a robot or a device that performs a task, such as cleaning, gardening, or delivering goods, or that interacts with the environment or the user.
  - Making a digital art or music project that expresses a theme, a message, or a personal story, or that showcases a technique or a style.

- To implement PBL in computer science, the subject teacher may follow these steps:

  - Identify the learning objectives and standards that the project will address, and align them with the curriculum and the assessment criteria.
  - Choose a relevant and engaging problem or challenge that requires students to apply multiple concepts and skills in one single program, and that has multiple possible solutions or approaches.
  - Provide students with the necessary resources and guidance to research the problem, brainstorm ideas, plan their project, and choose their tools and technologies.
  - Facilitate students' collaboration and communication throughout the project, and encourage them to give and receive feedback, reflect on their progress, and revise their work.
  - Showcase students' final products and celebrate their achievements, and help them evaluate their learning outcomes and identify areas for improvement.



## c) It is also suggested that open source tools should be preferred to conduct the lab. Some open source online compiler to conduct the C lab are as follows:

- **Repl.it**: This is a web-based IDE that supports multiple programming languages, including C. It allows users to create, run, and share code snippets online. It also has features such as syntax highlighting, code formatting, debugging, and collaboration. Repl.it is free to use for basic features, but requires a subscription for advanced features such as private repls, version control, and cloud storage. Repl.it can be accessed at https://repl.it/languages/c.
- **OnlineGDB**: This is another web-based IDE that supports C and other languages. It offers features such as code editor, compiler, debugger, and terminal. It also allows users to save and share their code online. OnlineGDB is free to use and does not require any registration or installation. OnlineGDB can be accessed at https://www.onlinegdb.com/online_c_compiler.
- **JDoodle**: This is a simple online compiler and editor for C and other languages. It allows users to write, compile, and execute code online. It also supports stdin, stdout, and command-line arguments. JDoodle is free to use and does not require any registration or installation. JDoodle can be accessed at https://www.jdoodle.com/c-online-compiler.



## https://www.jdoodle.com/c-online-compiler/

- This is a website that allows you to write, compile, and run C programs online without installing any software on your device.
- It provides an online editor where you can type your code, a terminal where you can see the output, and a button to run your code.
- It also supports interactive mode, where you can enter input values for your program and see the results immediately.
- It supports 76+ programming languages and 2 databases, and you can switch between them using the drop-down menu on the top right corner of the website.
- It offers various features such as saving and sharing your code, embedding an IDE to your website, and using APIs to execute programs by making a REST call.
- It is a useful tool for learning, testing, and debugging C programs online.



## Online C Compiler - tutorialspoint.com

- Online C Compiler is a web-based tool that allows users to write, compile, run and debug C programs online.
- It is provided by Tutorialspoint, a website that offers free tutorials on various programming languages and technologies.
- Online C Compiler has the following features:
  - It supports C11 standard and has code highlighting, auto-completion and error detection features.
  - It allows users to create, save, download and share C projects and files online.
  - It has a built-in terminal and a debugger that can set breakpoints, watch variables and step through the code execution.
  - It has a custom settings option that can change the theme, font size, tab size and indentation of the code editor.
  - It has a help section that provides syntax and examples of C language constructs and functions.
- Online C Compiler can be accessed from the following link: https://www.tutorialspoint.com/compile_c_online.php
- Online C Compiler is useful for students and working professionals who want to learn and practice C programming without installing any software or setting up any environment on their system.



## Programiz Online C Compiler

- Programiz Online C Compiler is a web-based tool that allows users to write, compile, and run C programs online.
- It is a free and easy-to-use service that does not require any installation or registration.
- It supports the latest C standards and features, such as C11, C17, and C18.
- It also provides syntax highlighting, code formatting, auto-completion, and error detection.
- It has a simple and intuitive user interface that consists of three main sections: the editor, the output, and the console.
- The editor is where users can type or paste their C code, and modify the compiler options and arguments.
- The output is where users can see the results of their compilation and execution, such as errors, warnings, and messages.
- The console is where users can interact with their program using standard input and output, such as scanf and printf.
- Users can also save, share, and download their code using the buttons on the top right corner of the editor.
- Users can access the Programiz Online C Compiler from any device and browser that supports JavaScript and HTML5.



## HackerRank

- HackerRank is a platform that helps programmers learn new skills and prepare for technical interviews by solving coding challenges.
- HackerRank offers challenges in various domains such as algorithms, data structures, mathematics, SQL, databases, functional programming, artificial intelligence, and more.
- HackerRank also provides a dashboard where users can track their progress, view their rank, and compare their performance with other users.
- HackerRank allows users to create their own custom challenges and host contests for their friends, colleagues, or students.
- HackerRank partners with companies and organizations to provide hiring solutions, such as screening candidates, conducting online assessments, and hosting virtual career fairs.



## Mapping with Virtual Lab

- Mapping is the process of creating a representation of a physical or abstract space using symbols, colors, shapes, and labels.
- Mapping can be used for various purposes, such as navigation, exploration, analysis, communication, and education.
- Virtual Lab is a software application that simulates a real laboratory environment and allows users to perform experiments and activities using virtual tools and materials.
- Virtual Lab can be used for mapping in different ways, such as:
  - Creating and editing maps using virtual drawing tools and map elements.
  - Exploring and interacting with maps using virtual navigation tools and map features.
  - Analyzing and comparing maps using virtual measurement tools and map properties.
  - Communicating and sharing maps using virtual presentation tools and map formats.
- Mapping with Virtual Lab can have several benefits, such as:
  - Enhancing the spatial skills and spatial awareness of the users.
  - Providing a flexible and accessible platform for mapping activities.
  - Offering a variety of options and features for mapping tasks.
  - Supporting the learning and teaching of mapping concepts and skills.



## Name of the Lab: Physics Lab
## Name of the Experiment: Measurement of the acceleration due to gravity using a simple pendulum

- The objective of this experiment is to measure the acceleration due to gravity (g) using a simple pendulum.
- A simple pendulum consists of a small bob of mass m suspended by a light string of length l from a fixed point.
- When the bob is displaced from its equilibrium position and released, it oscillates back and forth under the influence of gravity. The time taken for one complete oscillation is called the period (T) of the pendulum.
- The period of a simple pendulum depends only on the length of the string and the acceleration due to gravity, and is given by the formula:

    T = 2π√(l/g)

- By measuring the period and the length of the pendulum, we can calculate the value of g using the above formula.
- The procedure of the experiment is as follows:

    - Set up the simple pendulum by suspending a small bob from a clamp stand using a light string. Make sure the string is taut and the bob can swing freely without any obstruction.
    - Measure the length of the string from the point of suspension to the center of the bob using a meter rule. Record this value as l.
    - Displace the bob slightly from its equilibrium position and release it gently. Start a stopwatch as the bob passes through the lowest point of its swing. Count 20 oscillations and stop the stopwatch as the bob passes through the lowest point again. Record the time taken as t.
    - Repeat the above step for four more trials and calculate the average time for 20 oscillations as T.
    - Divide T by 20 to obtain the period of one oscillation as t.
    - Use the formula T = 2π√(l/g) to calculate the value of g. Rearrange the formula to get g = 4π²l/T² and substitute the values of l and T. Record the value of g with appropriate units and significant figures.
    - Repeat the above steps for four more values of l by changing the length of the string. Record the values of l, T and g in a table.
    - Plot a graph of T² versus l and draw a best-fit line. The slope of the line should be equal to 4π²/g. Use the slope to calculate the value of g and compare it with the previous results.
    - Calculate the percentage error of the experimental value of g from the accepted value of 9.81 m/s². Discuss the possible sources of error and suggest ways to improve the accuracy of the experiment.



## Problem Solving Lab

- The problem solving lab is a course that aims to develop the skills and strategies for solving complex and open-ended problems in various domains.
- The course covers the following topics:
  - Problem definition and analysis: how to identify, clarify, and decompose a problem into subproblems, and how to use different types of information and data to understand the problem context and constraints.
  - Problem solving methods and tools: how to apply various techniques and frameworks for generating, evaluating, and selecting possible solutions, such as brainstorming, mind mapping, SWOT analysis, decision matrix, etc.
  - Problem solving communication and presentation: how to communicate and present the problem and the solution effectively to different audiences, using appropriate formats, media, and language.
  - Problem solving reflection and feedback: how to reflect on the problem solving process and the solution outcomes, and how to seek and incorporate feedback from others to improve the problem solving skills and results.
- The course involves both individual and group work, and requires the students to apply the problem solving skills and methods to real-world problems from different disciplines and contexts.
- The course assessment is based on the following components:
  - Problem solving assignments: the students have to complete several problem solving tasks throughout the course, and submit a written report and a presentation for each task.
  - Problem solving portfolio: the students have to create a portfolio that showcases their problem solving skills and achievements, and reflects on their learning and improvement.
  - Problem solving exam: the students have to take a final exam that tests their problem solving knowledge and abilities.



## Numerical Representation

- Numerical representation is the way of expressing numbers using symbols, such as digits, letters, or other characters.
- Different numerical systems use different bases, which are the number of symbols available to represent numbers. For example, the decimal system uses base 10, which means it has 10 symbols (0 to 9) to represent any number. The binary system uses base 2, which means it has 2 symbols (0 and 1) to represent any number.
- To convert a number from one base to another, we can use various methods, such as repeated division, multiplication, or subtraction. For example, to convert 25 from decimal to binary, we can use repeated division by 2 and write the remainders from bottom to top:

25 / 2 = 12, remainder 1
12 / 2 = 6, remainder 0
6 / 2 = 3, remainder 0
3 / 2 = 1, remainder 1
1 / 2 = 0, remainder 1

The binary representation of 25 is 11001.

- Some common numerical systems are:

  - Decimal: base 10, uses 0 to 9, widely used in everyday life and mathematics.
  - Binary: base 2, uses 0 and 1, widely used in computer science and digital electronics.
  - Octal: base 8, uses 0 to 7, sometimes used as a shorthand for binary.
  - Hexadecimal: base 16, uses 0 to 9 and A to F, sometimes used as a shorthand for binary or to represent colors.
  - Roman: base varies, uses I, V, X, L, C, D, and M, used in ancient Rome and sometimes in modern contexts.
  - Alphabetic: base 26, uses A to Z, sometimes used to encode messages or data.



## Beauty of Numbers

- Numbers are the basic building blocks of mathematics and science. They help us to quantify, measure, compare, and understand the world around us.
- Numbers can also be appreciated for their aesthetic and artistic qualities. They can reveal patterns, symmetries, harmonies, and mysteries that appeal to our sense of beauty and wonder.
- Some examples of the beauty of numbers are:

  - The Fibonacci sequence: This is a series of numbers where each term is the sum of the previous two terms, such as 1, 1, 2, 3, 5, 8, 13, 21, and so on. The Fibonacci sequence appears in many natural phenomena, such as the arrangement of petals in flowers, the spirals of shells and pinecones, and the growth of branches and leaves. The ratio of consecutive terms in the Fibonacci sequence approaches the golden ratio, which is an irrational number that is considered to be the most aesthetically pleasing proportion in art and architecture.
  - The Mandelbrot set: This is a set of complex numbers that produces a fractal when plotted on a plane. A fractal is a geometric shape that is self-similar, meaning that it has the same structure at different scales. The Mandelbrot set is generated by applying a simple formula repeatedly to each point on the plane and coloring it according to how many iterations it takes to escape to infinity. The result is a stunning image that reveals infinite complexity and variety in its details.
  - The prime numbers: These are the numbers that are only divisible by themselves and one, such as 2, 3, 5, 7, 11, 13, and so on. The prime numbers are the building blocks of all other numbers, as any number can be written as a product of prime factors. The prime numbers have many fascinating properties and patterns, such as the twin primes (pairs of primes that differ by 2), the Mersenne primes (primes that are one less than a power of 2), and the Riemann hypothesis (a conjecture that relates the distribution of primes to the zeros of a complex function). The prime numbers are also important for cryptography, as they are used to create secure codes and encryption systems.
  - The pi number: This is the ratio of the circumference of a circle to its diameter, which is approximately 3.14159. Pi is an irrational number, meaning that it cannot be written as a fraction of two integers. It is also a transcendental number, meaning that it cannot be the solution of any polynomial equation with rational coefficients. Pi has many applications in geometry, trigonometry, physics, engineering, and statistics. Pi is also famous for its infinite and non-repeating decimal expansion, which contains every possible combination of digits. Some people memorize and recite thousands of digits of pi as a mental challenge and a demonstration of the beauty of numbers.



## More on Numbers

- Numbers are symbols that represent quantities or values.
- There are different types of numbers, such as natural numbers, integers, rational numbers, irrational numbers, real numbers, and complex numbers.
- Natural numbers are the counting numbers, such as 1, 2, 3, 4, and so on. They are also called positive integers.
- Integers are the natural numbers, their negatives, and zero, such as -3, -2, -1, 0, 1, 2, 3, and so on.
- Rational numbers are the numbers that can be written as a fraction of two integers, such as 1/2, 3/4, -5/6, 0/1, and so on. They can also be written as decimals that either terminate or repeat, such as 0.5, 0.75, -0.833, 0, and so on.
- Irrational numbers are the numbers that cannot be written as a fraction of two integers, such as pi, e, sqrt(2), and so on. They can only be written as decimals that never terminate or repeat, such as 3.14159..., 2.71828..., 1.41421..., and so on.
- Real numbers are the numbers that can be represented on a number line, such as rational and irrational numbers. They include all the numbers that can be measured or calculated in the real world, such as distances, areas, volumes, temperatures, and so on.
- Complex numbers are the numbers that can be written as a + bi, where a and b are real numbers and i is the imaginary unit, such as 2 + 3i, -1 - 4i, 0 + 5i, and so on. They are used to model phenomena that involve rotations, oscillations, waves, and other complex behaviors.



## Factorials

- A factorial is a mathematical operation that calculates the product of all positive integers from 1 to a given number.
- The factorial of a number n is denoted by n! and is defined as:

n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

- For example, 5! = 5 * 4 * 3 * 2 * 1 = 120
- The factorial of 0 is defined as 1, i.e. 0! = 1
- Factorials are used to count the number of ways to arrange or order a set of objects, such as permutations and combinations.
- Factorials grow very fast as the number increases. For example, 10! = 3,628,800 and 20! = 2,432,902,008,176,640,000
- The largest factorial that can be calculated using a standard 64-bit integer is 20!, as 21! would cause an overflow.
- Factorials can also be calculated using recursion, a technique where a function calls itself with a smaller argument until a base case is reached. For example, the recursive definition of n! is:

n! = n * (n-1)! if n > 0
n! = 1 if n = 0

- Factorials can also be extended to non-integer values using the gamma function, which is a special function that interpolates the factorial function. The gamma function is defined as:

Γ(x) = ∫<sub>0</sub><sup>∞</sup> t<sup>x-1</sup> e<sup>-t</sup> dt

- The gamma function satisfies the property that Γ(n+1) = n! for any positive integer n. For example, Γ(6) = 5! = 120
- The gamma function can also be evaluated for fractions, negative numbers, and complex numbers, but it is not defined for non-positive integers. For example, Γ(1/2) = √π and Γ(-1) is undefined.



## String Operations

- A string is a sequence of characters enclosed in quotation marks, such as "Hello" or "Python".
- Strings can be concatenated (joined) using the + operator, such as "Hello" + "World" = "HelloWorld".
- Strings can be repeated using the * operator, such as "Hello" * 3 = "HelloHelloHello".
- Strings can be accessed by indexing, which returns a single character, such as "Hello"[0] = "H".
- Strings can be sliced, which returns a substring, such as "Hello"[1:3] = "el".
- Strings can be compared using the == operator, which returns True if the strings are equal, and False otherwise, such as "Hello" == "hello" = False.
- Strings can be converted to other data types using built-in functions, such as int("123") = 123 or float("3.14") = 3.14.
- Strings have many methods that can perform various operations on them, such as upper(), lower(), replace(), find(), split(), join(), etc. For example, "Hello".upper() = "HELLO" or "Hello,World".split(",") = ["Hello", "World"].



## Recursion

- Recursion is a technique of defining a problem in terms of itself.
- Recursion involves two main components: a base case and a recursive step.
- A base case is a simple or trivial case of the problem that can be solved directly without recursion.
- A recursive step is a way of reducing a complex or larger case of the problem to one or more simpler or smaller cases that can be solved by applying the same technique recursively.
- A recursive function is a function that calls itself within its body, either directly or indirectly, with different arguments that lead to the base case.
- Recursion can be used to solve problems that have a recursive structure, such as mathematical sequences, tree traversal, backtracking, divide and conquer, dynamic programming, etc.
- Recursion can be implemented using a stack, which stores the function calls and their parameters until they are resolved.
- Recursion can be more elegant and concise than iteration, but it can also be less efficient and more prone to errors, such as infinite recursion or stack overflow.



## Advanced Arithmatic

Advanced arithmatic is the branch of mathematics that deals with operations on numbers beyond the basic four: addition, subtraction, multiplication and division. Some of the topics covered in advanced arithmatic are:

- Exponents and logarithms: These are ways of expressing repeated multiplication or division by the same number. For example, 2^3 means 2 multiplied by itself 3 times, which is 8. Logarithms are the inverse of exponents, meaning they tell us what power we need to raise a base number to get another number. For example, log2(8) means what power do we need to raise 2 to get 8, which is 3.
- Roots and radicals: These are ways of expressing fractional exponents or inverse exponents. For example, the square root of 9 means what number multiplied by itself gives 9, which is 3. The cube root of 27 means what number multiplied by itself 3 times gives 27, which is 3. Radicals are symbols that indicate roots, such as √9 or ³√27.
- Fractions and decimals: These are ways of expressing parts of a whole number or a ratio of two numbers. For example, 1/2 means one part out of two equal parts, which is 0.5 in decimal form. 0.75 means 75 parts out of 100 equal parts, which is 3/4 in fraction form.
- Percentages and ratios: These are ways of expressing proportions or comparisons of two numbers. For example, 50% means 50 parts out of 100 equal parts, which is the same as 1/2 or 0.5. A ratio of 2:3 means for every 2 units of one quantity, there are 3 units of another quantity, which is the same as 2/3 or 0.67.
- Order of operations: This is a set of rules that tells us in what order we should perform different arithmatic operations when they are combined in an expression. The acronym PEMDAS is often used to remember the order: Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right). For example, in the expression 2 + 3 × 4^2, we first evaluate the exponent 4^2, which is 16, then we multiply 3 by 16, which is 48, then we add 2 to 48, which is 50.



## Searching and Sorting

- Searching and sorting are two fundamental operations in computer science that deal with finding and arranging data in a collection.
- Searching is the process of locating a specific item or a set of items that satisfy some criteria in a collection of data.
- Sorting is the process of arranging data in a specific order, such as ascending or descending, based on some property or value of the data.
- Searching and sorting are often used together to facilitate efficient data processing and analysis. For example, sorting a collection of data can make searching faster and easier, as well as enable other operations such as merging, grouping, or filtering.
- There are different algorithms and techniques for searching and sorting data, depending on the type, size, and structure of the data, as well as the desired output and performance.
- Some common searching algorithms are linear search, binary search, interpolation search, and hashing.
- Some common sorting algorithms are selection sort, insertion sort, bubble sort, merge sort, quick sort, heap sort, and radix sort.
- Each searching and sorting algorithm has its own advantages and disadvantages, and can be evaluated based on various criteria, such as time complexity, space complexity, stability, adaptability, and scalability.



## Permutation

- A permutation is an arrangement of objects in a specific order.
- The order of the objects matters in a permutation.
- For example, the permutations of the letters A, B, and C are ABC, ACB, BAC, BCA, CAB, and CBA. Changing the order of the letters produces different permutations.
- The number of permutations of n distinct objects is n factorial, denoted by n!.
- n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
- For example, the number of permutations of 3 distinct objects is 3! = 3 * 2 * 1 = 6.
- If some of the objects are repeated, the number of permutations is reduced by dividing by the factorial of the number of repetitions.
- For example, the number of permutations of the letters A, A, and B is 3! / 2! = 3, because there are 2 repetitions of A. The permutations are AAB, ABA, and BAA.
- A permutation of r objects from a set of n objects is called a permutation of n objects taken r at a time, denoted by P(n, r).
- P(n, r) = n! / (n-r)!
- For example, the number of permutations of 2 letters from the set {A, B, C, D} is P(4, 2) = 4! / (4-2)! = 12. The permutations are AB, AC, AD, BA, BC, BD, CA, CB, CD, DA, DB, and DC.
- A permutation can also be considered as a mapping or a function that assigns each object to a position.
- For example, the permutation ABC can be represented as a mapping that assigns A to the first position, B to the second position, and C to the third position.
- A permutation can also be represented as a cycle, which shows how the objects are moved from one position to another.
- For example, the permutation ABC can be represented as a cycle (A B C), which means that A is moved to the position of B, B is moved to the position of C, and C is moved to the position of A.
- A permutation can be composed with another permutation by applying the mappings or cycles of both permutations in succession.
- For example, the composition of the permutations ABC and BAC is BCA, because applying ABC first and then BAC results in BCA.
- The composition of permutations is not commutative, meaning that the order of the permutations matters.
- For example, the composition of the permutations ABC and BAC is not the same as the composition of the permutations BAC and ABC, which is CAB.
- The identity permutation is the permutation that does not change the order of the objects, denoted by I.
- For example, the identity permutation of the letters A, B, and C is ABC, which can be represented as a mapping that assigns A to A, B to B, and C to C, or as a cycle (A)(B)(C), which means that no object is moved.
- The inverse of a permutation is the permutation that reverses the effect of the original permutation, denoted by P^-1.
- For example, the inverse of the permutation ABC is CBA, which can be represented as a mapping that assigns A to C, B to B, and C to A, or as a cycle (A C)(B), which means that A and C are swapped and B is unchanged.
- The inverse of a permutation can be obtained by reversing the order of the mappings or cycles of the original permutation.
- For example, the inverse of the permutation (A B C)(D E) is (E D)(C B A), which can be obtained by reversing the order of the cycles and the order of the elements within each cycle.



## Sequences

- A sequence is a list of objects or numbers that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed or unlimited number of terms.
- A term is an element or item in a sequence. Terms are usually denoted by subscripts, such as a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ..., a<sub>n</sub>.
- The position of a term in a sequence is called its index. Indices are usually positive integers, starting from 1.
- A sequence can be defined by a formula, a recurrence relation, or a verbal description.
- A formula is an expression that gives the value of a term in terms of its index, such as a<sub>n</sub> = 2n + 1.
- A recurrence relation is an equation that gives the value of a term in terms of one or more previous terms, such as a<sub>n</sub> = a<sub>n-1</sub> + 3, with a<sub>1</sub> = 2.
- A verbal description is a statement that explains how to generate the terms of a sequence, such as "start with 1 and add 4 to get the next term".
- Some examples of sequences are:

  - The arithmetic sequence 2, 5, 8, 11, ..., where each term is 3 more than the previous term, or a<sub>n</sub> = 2 + 3(n - 1).
  - The geometric sequence 3, 9, 27, 81, ..., where each term is 3 times the previous term, or a<sub>n</sub> = 3<sup>n</sup>.
  - The Fibonacci sequence 1, 1, 2, 3, 5, 8, ..., where each term is the sum of the two previous terms, or a<sub>n</sub> = a<sub>n-1</sub> + a<sub>n-2</sub>, with a<sub>1</sub> = a<sub>2</sub> = 1.
  - The triangular numbers sequence 1, 3, 6, 10, ..., where each term is the sum of the first n positive integers, or a<sub>n</sub> = n(n + 1) / 2.



## Course Outcomes:

- By the end of this course, you will be able to:
  - Identify and explain the basic concepts and principles of artificial intelligence, such as search, knowledge representation, reasoning, planning, learning, and natural language processing.
  - Apply various artificial intelligence techniques and algorithms to solve problems, such as heuristic search, constraint satisfaction, logic, inference, probabilistic models, decision making, neural networks, and machine learning.
  - Evaluate the strengths and limitations of different artificial intelligence approaches and compare their performance and applicability to different domains and scenarios.
  - Implement and test artificial intelligence solutions using programming languages and tools, such as Python, Prolog, TensorFlow, and PyTorch.
  - Analyze and discuss the ethical, social, and legal implications of artificial intelligence and its impact on human society and the environment.



## Course Outcome Bloom's Taxonomy

- Course outcome is a brief statement that describes what students will be expected to learn by the end of the course.
- Bloom's taxonomy is a model of cognitive skills used to classify educational learning objectives and is a helpful tool for the development of learning outcomes .
- Bloom's taxonomy consists of six levels of thinking, from lower-order to higher-order: remember, understand, apply, analyze, evaluate, and create.
- The action verbs used in Bloom's taxonomy are measurable and discrete, and they indicate the level of rigor intended for the course .
- When writing learning outcomes, it is important to use Bloom's taxonomy to make sure that the verbs match the level of the course and that the outcomes span across the pyramid .
- For example, a lower-level course may have outcomes that focus on remembering and understanding basic concepts, while a higher-level course may have outcomes that require students to evaluate and create new solutions based on the concepts.
- Bloom's taxonomy provides a scaffolding around which instructors can design their course, assess student learning, and align their teaching strategies with the desired outcomes .



## Level

- A level is a position on a scale of amount, quantity, extent, or quality.
- A level can also refer to a standard or degree of attainment, skill, or proficiency.
- A level can also mean a horizontal plane or line with respect to the distance above or below a given point.
- A level can also be a device used to determine whether a surface is horizontal or vertical.
- A level can also be a stage or layer in a hierarchical structure, such as a level of management, a level of education, or a level of difficulty.
- A level can also be a unit of measurement used in some video games to indicate the strength or skill of a character or an enemy.



## At the end of course, the student will be able to:

- Define the basic concepts and terminology of artificial intelligence, such as agents, environments, rationality, search, knowledge representation, inference, planning, learning, natural language processing, computer vision, and robotics.
- Apply various search algorithms, such as uninformed search, informed search, local search, adversarial search, and constraint satisfaction, to solve problems that can be formulated as state-space search or game trees.
- Design and implement knowledge-based systems using propositional logic, first-order logic, and other forms of logic, and perform logical reasoning using inference rules and algorithms, such as resolution, forward chaining, and backward chaining.
- Explain the principles and techniques of planning, such as partial-order planning, hierarchical planning, and graph planning, and apply them to generate plans for achieving goals in dynamic and uncertain domains.
- Understand the concepts and methods of machine learning, such as supervised learning, unsupervised learning, reinforcement learning, neural networks, and deep learning, and apply them to learn from data and improve performance.
- Analyze and process natural language texts using linguistic models, such as syntax, semantics, pragmatics, and discourse, and implement natural language processing systems, such as parsers, semantic analyzers, dialogue systems, and machine translation systems.
- Recognize and manipulate visual information using computer vision techniques, such as image processing, feature extraction, object detection, face recognition, and scene understanding, and implement computer vision systems, such as optical character recognition, face verification, and augmented reality.
- Model and control physical systems using robotics techniques, such as kinematics, dynamics, localization, mapping, navigation, and coordination, and implement robotics systems, such as mobile robots, manipulators, and autonomous vehicles.



## CO 1 Able to implement the algorithms and draw flowcharts for solving Mathematical and Engineering problems.

- An algorithm is a step-by-step procedure to solve a problem or perform a task.
- A flowchart is a graphical representation of an algorithm using symbols and arrows to show the sequence of steps and the logic of the solution.
- Algorithms and flowcharts are useful tools for designing, analyzing, and implementing solutions for mathematical and engineering problems.
- Some examples of mathematical and engineering problems that can be solved using algorithms and flowcharts are:
  - Finding the roots of a quadratic equation.
  - Sorting an array of numbers in ascending or descending order.
  - Computing the factorial of a positive integer.
  - Finding the greatest common divisor of two numbers.
  - Encrypting and decrypting a message using a cipher.
  - Simulating the motion of a projectile under gravity.
- To implement an algorithm and draw a flowchart for solving a problem, one should follow these steps:
  - Understand the problem and its requirements.
  - Identify the input and output data and their formats.
  - Break down the problem into smaller and simpler subproblems.
  - Design an algorithm for each subproblem using pseudocode or natural language.
  - Test and debug the algorithm using sample input and output data.
  - Draw a flowchart for the algorithm using standard symbols and conventions.
  - Convert the flowchart into a program code using a programming language of choice.
  - Compile and run the program code and verify the results.



## K3, K4

- K3 and K4 are two types of **potassium channels** that are involved in the regulation of **membrane potential** and **neuronal excitability**.
- Potassium channels are **proteins** that form **pores** in the cell membrane and allow **potassium ions** to pass through them.
- Potassium channels are **diverse** and have different **structures**, **functions**, and **regulation** mechanisms.
- K3 and K4 are part of the **Kv** family of potassium channels, which are **voltage-gated** and **tetrameric**.
- Voltage-gated means that they **open** and **close** in response to changes in the **electrical potential** across the membrane.
- Tetrameric means that they are composed of **four subunits** that form a **symmetrical** channel.
- K3 and K4 are also known as **Kv3** and **Kv4**, respectively, according to the **nomenclature** of the International Union of Pharmacology (IUPHAR).
- K3 and K4 have distinct **biophysical** and **pharmacological** properties that make them suitable for different **roles** in the nervous system.
- K3 channels have a **high activation threshold**, a **fast activation** and **deactivation** kinetics, and a **low sensitivity** to **blockers** such as **tetraethylammonium (TEA)** and **4-aminopyridine (4-AP)**.
- K3 channels are **expressed** mainly in **fast-spiking** neurons, such as **interneurons** and **cerebellar Purkinje cells**, where they enable **rapid** and **precise** firing patterns.
- K4 channels have a **low activation threshold**, a **slow activation** and **deactivation** kinetics, and a **high sensitivity** to **blockers** such as **dendrotoxin (DTX)** and **phrixotoxin (PTX)**.
- K4 channels are **expressed** mainly in **dendrites** and **somas** of **pyramidal** neurons, such as **hippocampal** and **cortical** cells, where they modulate **synaptic integration** and **plasticity**.



## CO 2 Demonstrate an understanding of computer programming language concepts. K3, K2

- Computer programming language concepts are the fundamental ideas and principles that underlie the design and implementation of programming languages.
- Some of the main concepts are:
  - Syntax: the rules and structure of a programming language that define how to write valid programs.
  - Semantics: the meaning and behavior of a programming language that define how to interpret and execute programs.
  - Data types: the categories of values that a programming language can manipulate, such as numbers, strings, booleans, arrays, etc.
  - Variables: the names or identifiers that refer to data values in a program.
  - Expressions: the combinations of data values, variables, operators, and functions that can be evaluated to produce a result.
  - Statements: the instructions that control the flow of execution in a program, such as assignments, conditionals, loops, etc.
  - Functions: the reusable blocks of code that perform a specific task and can be called by other parts of the program.
  - Parameters: the variables that are passed to a function when it is called, and that receive the values of the arguments.
  - Arguments: the values that are supplied to a function when it is called, and that are assigned to the parameters.
  - Return values: the values that a function produces as its output, and that are returned to the caller.
  - Scope: the region of a program where a variable or a function is visible and accessible.
  - Modules: the units of code that can be imported and used by other programs, and that provide a way of organizing and structuring large programs.
  - Classes: the templates or blueprints that define the attributes and methods of a type of object in an object-oriented programming language.
  - Objects: the instances or examples of a class that have their own state and behavior in an object-oriented programming language.
  - Inheritance: the mechanism that allows a class to inherit the attributes and methods of another class in an object-oriented programming language.
  - Polymorphism: the ability of a function or an object to behave differently depending on the type or the number of the arguments in an object-oriented programming language.
  - Abstraction: the process of hiding the details and complexity of a system and providing a simpler and more general interface to it.
  - Encapsulation: the process of bundling the data and the operations on the data together in a single unit, such as a class or an object.
  - Modularity: the property of a system that allows it to be divided into smaller and independent components that can be reused and combined in different ways.



## CO 3

- CO 3 is the chemical formula for carbonate, a polyatomic ion with a negative charge of 2.
- Carbonate consists of one carbon atom and three oxygen atoms, bonded with double and single covalent bonds.
- Carbonate is a common constituent of many minerals, rocks, and shells, such as limestone, marble, and coral.
- Carbonate can also form salts with various metals, such as sodium carbonate (Na2CO3), potassium carbonate (K2CO3), and calcium carbonate (CaCO3).
- Carbonate can act as a base, accepting protons from acids to form bicarbonate (HCO3-) or carbonic acid (H2CO3).
- Carbonate can also undergo decomposition reactions when heated, releasing carbon dioxide (CO2) and water (H2O) or metal oxides. For example, CaCO3 -> CaO + CO2.
- Carbonate plays an important role in the carbon cycle, as it can store and release carbon dioxide in different forms and environments.



## Ability to design and develop Computer programs, analyzes, and interprets the concept of pointers, declarations, initialization, operations on pointers and their usage.

- A pointer is a variable that stores the address of another variable in memory.
- A pointer declaration consists of a data type, an asterisk (*) and an identifier. For example, `int *p;` declares a pointer named `p` that can point to an integer variable.
- A pointer initialization assigns a valid memory address to a pointer variable. For example, `int x = 10; int *p = &x;` initializes a pointer `p` with the address of an integer variable `x`.
- Operations on pointers include dereferencing, arithmetic, assignment, comparison and passing to functions.
  - Dereferencing a pointer means accessing the value stored at the memory location pointed by the pointer. For example, `*p` returns the value of `x` in the previous example.
  - Arithmetic on pointers means adding or subtracting an integer value to or from a pointer. For example, `p + 1` returns the address of the next integer location after `x`.
  - Assignment on pointers means changing the memory address stored in a pointer variable. For example, `p = &y;` assigns the address of another integer variable `y` to `p`.
  - Comparison on pointers means checking if two pointers point to the same or different memory locations. For example, `p == q` returns true if `p` and `q` point to the same location, and false otherwise.
  - Passing pointers to functions means passing the memory address of a variable as an argument to a function. For example, `void swap(int *a, int *b)` is a function that takes two pointers as parameters and swaps the values of the variables they point to.
- Pointers are useful for dynamic memory allocation, manipulating arrays and strings, implementing data structures and algorithms, and passing parameters by reference.



## K6, K4

- K6 and K4 are two types of **kinase enzymes** that are involved in the regulation of **cell cycle** and **cell division**.
- Kinases are enzymes that **phosphorylate** (add phosphate groups to) other proteins, thereby changing their activity and function.
- K6 and K4 belong to the **cyclin-dependent kinase (CDK)** family, which are activated by binding to **cyclins**, a group of proteins that fluctuate in concentration during the cell cycle.
- K6 and K4 are also known as **CDK6** and **CDK4**, respectively.
- K6 and K4 are mainly active during the **G1 phase** of the cell cycle, which is the period when the cell grows and prepares for DNA replication.
- K6 and K4 form complexes with **cyclin D**, one of the cyclins that accumulates in response to **growth factors** and **mitogens**, which are signals that stimulate cell proliferation.
- K6 and K4, together with cyclin D, phosphorylate and inactivate a group of proteins called **retinoblastoma (Rb)** proteins, which are **tumor suppressors** that prevent the cell from entering the **S phase**, where DNA replication occurs.
- By phosphorylating and inactivating Rb proteins, K6 and K4 release a transcription factor called **E2F**, which activates the expression of genes required for DNA synthesis and cell cycle progression.
- K6 and K4 are therefore essential for the **G1/S transition**, the point where the cell commits to DNA replication and cell division.
- K6 and K4 are regulated by several mechanisms, including **cyclin D degradation**, **CDK inhibitors** (such as p16, p21, and p27), and **feedback loops** involving E2F and Rb proteins.
- K6 and K4 are often **overexpressed** or **mutated** in various types of **cancer**, such as breast cancer, melanoma, glioblastoma, and lymphoma, leading to **uncontrolled cell proliferation** and **tumor formation**.
- K6 and K4 are therefore potential **therapeutic targets** for cancer treatment, and several **inhibitors** of K6 and K4 have been developed and tested in clinical trials.



## CO 4

- CO 4 stands for **Course Outcome 4**. It is a measure of the learning objectives and skills that students are expected to achieve by the end of a course.
- CO 4 can vary depending on the course content, level, and discipline. However, some common elements of CO 4 are:
  - They are aligned with the course goals and the program outcomes.
  - They are specific, measurable, achievable, relevant, and time-bound (SMART).
  - They are written from the student's perspective, using action verbs and observable indicators.
  - They are communicated to the students at the beginning of the course and assessed throughout the course.
  - They are used to evaluate the effectiveness of the course design, delivery, and assessment.
- Some examples of CO 4 are:
  - By the end of this course, students will be able to:
    - Apply the principles of object-oriented programming to design and implement software solutions.
    - Demonstrate the use of various data structures and algorithms to solve problems efficiently and effectively.
    - Test and debug software programs using appropriate tools and techniques.
    - Collaborate and communicate effectively with peers and instructors in a team project.



## Able to define data types and use them in simple data processing applications

- A data type is a classification of data that specifies how the data is stored, manipulated, and displayed by a programming language.
- Data types can be primitive or user-defined. Primitive data types are predefined by the language and have fixed sizes and ranges, such as int, char, float, etc. User-defined data types are created by the programmer using structures, unions, enumerations, etc.
- A structure is a user-defined data type that groups related data of different types into a single unit. For example, a structure can store information about a student, such as name, roll number, marks, etc.
- An array is a collection of data of the same type that are stored in contiguous memory locations and accessed by a common name. For example, an array can store a list of numbers, characters, or strings.
- An array of structures is an array that contains elements of structure type. Each element of the array can access the members of the structure using the dot (.) operator. For example, an array of structures can store information about multiple students, such as student[0].name, student[0].roll, student[0].marks, etc.
- An array of structures can be used in simple data processing applications, such as:

  - Reading and writing data from and to files using functions like fopen, fclose, fscanf, fprintf, etc.
  - Sorting and searching data using algorithms like bubble sort, selection sort, linear search, binary search, etc.
  - Performing calculations and operations on data using arithmetic, logical, and relational operators, such as +, -, *, /, %, &&, ||, ==, !=, etc.
  - Displaying and formatting data using functions like printf, scanf, puts, gets, etc.



## K1, K5

- K1 and K5 are two types of visas issued by the United States to foreign nationals who are engaged to or married to U.S. citizens or permanent residents.
- K1 visas are also known as fiance(e) visas. They allow the foreign national to enter the U.S. and marry their U.S. citizen sponsor within 90 days of arrival. After the marriage, the foreign national can apply for adjustment of status to become a permanent resident.
- K5 visas are also known as spouse visas. They allow the foreign national who is already married to a U.S. citizen or permanent resident to enter the U.S. and join their spouse. The foreign national can apply for a green card after entering the U.S. on a K5 visa.
- Both K1 and K5 visas require the U.S. citizen or permanent resident sponsor to file a petition with the U.S. Citizenship and Immigration Services (USCIS) and prove that they have a bona fide relationship with the foreign national. The foreign national also has to undergo a medical examination and a background check, and attend an interview at a U.S. consulate or embassy abroad.
- The processing time for K1 and K5 visas varies depending on the country of origin, the workload of the USCIS and the consulate or embassy, and the complexity of the case. Generally, it can take from 6 to 12 months or longer to obtain a K1 or K5 visa.



## CO 5 Develop confidence for self-education and ability for life-long learning needed for Computer language.

- Computer language is a set of symbols and rules that are used to communicate with a computer or a software program.
- Learning computer language is essential for anyone who wants to create, modify, or understand computer applications and systems.
- Computer language is constantly evolving and new languages are being developed to meet the needs and challenges of the digital world.
- Therefore, it is important to develop confidence for self-education and ability for life-long learning needed for computer language.
- Some of the benefits of developing these skills are:

  - You can keep up with the latest trends and technologies in computer science and programming.
  - You can enhance your problem-solving and logical thinking skills by learning new ways of expressing and implementing algorithms and data structures.
  - You can expand your career opportunities and employability by acquiring proficiency in multiple languages and frameworks.
  - You can pursue your personal interests and hobbies by creating your own projects and applications using computer language.

- Some of the strategies for developing these skills are:

  - Identify your learning goals and objectives. What do you want to learn and why? How will it help you achieve your personal or professional goals?
  - Choose a suitable computer language and learning resource. Depending on your level of experience and preference, you can select a language that suits your needs and interests. You can also use online courses, books, tutorials, videos, podcasts, blogs, forums, etc. to learn from.
  - Plan your learning schedule and track your progress. Set a realistic and achievable timeline for your learning and stick to it. Use tools like calendars, planners, checklists, etc. to organize your learning activities and monitor your outcomes.
  - Practice and apply your learning. The best way to learn computer language is by doing. Try to write, run, debug, and modify code as much as possible. Use online platforms like Codecademy, HackerRank, LeetCode, etc. to practice coding challenges and exercises. Work on real-world projects and applications that interest you and showcase your skills.
  - Seek feedback and support. Learning computer language can be challenging and frustrating at times. It is important to seek feedback and support from others who can help you improve your learning. You can join online communities, groups, or clubs of learners and experts who can offer you guidance, advice, tips, resources, etc. You can also ask questions, share your work, and collaborate with others on your learning journey.



## K3, K4

- K3 and K4 are two types of **knowledge representation languages** that are used to encode knowledge in a formal and declarative way.
- K3 is based on the **logic programming paradigm**, which uses rules and facts to express knowledge. K3 rules have the form of **implications**, where the head of the rule is a logical consequence of the body. For example, `grandparent(X, Y) :- parent(X, Z), parent(Z, Y).` means that X is a grandparent of Y if X is a parent of Z and Z is a parent of Y.
- K4 is based on the **description logic paradigm**, which uses concepts and roles to express knowledge. K4 concepts are sets of individuals that share some properties, and K4 roles are binary relations between individuals. For example, `Grandparent ≡ ∃hasChild.hasChild` means that a grandparent is an individual that has a child that has a child.
- K3 and K4 have different advantages and disadvantages for knowledge representation. K3 is more expressive and flexible, but also more complex and computationally expensive. K4 is more concise and efficient, but also more restricted and less intuitive.

