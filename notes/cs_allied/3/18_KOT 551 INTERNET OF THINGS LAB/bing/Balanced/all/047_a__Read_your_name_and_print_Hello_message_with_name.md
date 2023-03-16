# Read your name and print Hello message with name

- This is a simple program that takes the user's name as an input and prints a greeting message with the name.
- To write this program, we need to use some basic concepts of programming, such as variables, data types, input/output, and string concatenation.
- A variable is a name that refers to a value stored in the memory. We can assign a value to a variable using the equal sign (=).
- A data type is a category of values that have certain properties and operations. For example, a string is a data type that represents a sequence of characters, such as "Hello" or "Sydney".
- Input/output is the process of getting data from the user or displaying data to the user. We can use the input() function to get data from the user and the print() function to display data to the user.
- String concatenation is the operation of joining two or more strings together using the plus sign (+). For example, "Hello" + "World" is "HelloWorld".

- Here is an example of how to write the program in Python, a popular programming language:

```python
# Ask the user for their name and store it in a variable called name
name = input("What is your name? ")

# Print a greeting message with the name using string concatenation
print("Hello, " + name + "!")
```

- Here is an example of how the program works:

```
What is your name? Alice
Hello, Alice!
```

- Here are some points to remember when writing the program:

  - The input() function returns a string, so we do not need to convert the name to a string.
  - The print() function automatically adds a newline character (\n) at the end of the output, so we do not need to add it manually.
  - The plus sign (+) can also be used for arithmetic operations, such as 2 + 3, but it behaves differently depending on the data types of the operands. For example, 2 + 3 is 5, but "2" + "3" is "23".
  - The program is case-sensitive, which means that uppercase and lowercase letters are different. For example, "Alice" and "alice" are not the same name.