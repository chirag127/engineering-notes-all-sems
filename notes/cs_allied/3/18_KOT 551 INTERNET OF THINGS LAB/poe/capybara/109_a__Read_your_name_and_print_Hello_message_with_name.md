# Read your name and print Hello message with name

When writing a program, it is important to be able to read input from the user and display output. One common task is to ask the user for their name and then print a personalized greeting. Here is how you can read the user's name and print a "Hello" message with their name:

1. Use the `input()` function to ask the user for their name. This function reads a line of text from the user and returns it as a string. For example, `name = input("What is your name? ")` will ask the user to enter their name and store it in the variable `name`.

2. Once you have the user's name, you can print a personalized greeting by using the `print()` function. You can use the `+` operator to concatenate strings, so you can combine the "Hello" message with the user's name. For example, `print("Hello, " + name + "!")` will print a message like "Hello, John!" if the user's name is John.

3. It is important to remember to format the message correctly. You should include a space after the comma in the message so that it looks like a proper sentence. You can also use string formatting to make the code more readable. For example, `print(f"Hello, {name}!")` is equivalent to the previous example but uses the `f` character to indicate that the string should be formatted.

4. Finally, it is good practice to include error handling in case the user enters invalid input. For example, if the user does not enter a name, the program should handle the error gracefully and ask the user to try again. One way to do this is to use a `while` loop to keep asking for input until the user enters a valid name. For example:

```python
name = ""
while not name:
    name = input("What is your name? ")
print(f"Hello, {name}!")
```

By following these steps, you can read the user's name and print a personalized greeting in your program.