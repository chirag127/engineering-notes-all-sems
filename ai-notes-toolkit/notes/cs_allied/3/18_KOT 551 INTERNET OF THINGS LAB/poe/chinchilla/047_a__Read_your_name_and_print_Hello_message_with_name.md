# Read your name and print Hello message with name

When it comes to programming, one of the basic tasks is to read user input and display output. In this tutorial, we will learn how to read a user's name and print a greeting message with their name.

## Reading user input

Before we can print a greeting message with the user's name, we need to read their name from the user. In Python, we can use the `input()` function to read user input from the console. Here's how we can use it to read the user's name:

```python
name = input("Please enter your name: ")
```

This code prompts the user to enter their name and stores the input in the `name` variable.

## Printing a greeting message

Once we have the user's name, we can print a greeting message with their name. Here's how we can do that in Python:

```python
print("Hello, " + name + "!")
```

This code uses string concatenation to combine the "Hello, " string with the user's name and the exclamation mark. The resulting string is then printed to the console using the `print()` function.

## Putting it all together

Here's the complete code to read the user's name and print a greeting message with their name:

```python
name = input("Please enter your name: ")
print("Hello, " + name + "!")
```

When you run this code, you should see the following output:

```
Please enter your name: John
Hello, John!
```

Congratulations, you have successfully learned how to read user input and print a greeting message with their name in Python!