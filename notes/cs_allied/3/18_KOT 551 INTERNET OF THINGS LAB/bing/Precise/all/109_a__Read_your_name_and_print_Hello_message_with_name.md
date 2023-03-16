# Read your name and print Hello message with name

1. To read your name, you can use the `input()` function in Python. This function allows the user to enter a value, which is then stored as a string.
2. To print a message with the name, you can use the `print()` function. This function outputs the specified message to the screen.
3. You can use string concatenation to combine the "Hello" message with the name entered by the user.

Here is an example of how this can be done:

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

In this example, the user is prompted to enter their name using the `input()` function. The entered name is then stored in the `name` variable. The `print()` function is then used to output a greeting message that includes the user's name. The greeting message is created by concatenating the strings "Hello, ", the value of the `name` variable, and "!".