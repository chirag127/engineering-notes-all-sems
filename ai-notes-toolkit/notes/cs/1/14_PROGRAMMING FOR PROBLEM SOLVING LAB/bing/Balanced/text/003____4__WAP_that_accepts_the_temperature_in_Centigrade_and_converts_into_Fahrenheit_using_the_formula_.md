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