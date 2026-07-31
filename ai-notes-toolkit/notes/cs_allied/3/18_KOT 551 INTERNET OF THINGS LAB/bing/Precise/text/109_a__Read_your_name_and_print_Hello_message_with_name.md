# Reading your name and printing a Hello message with your name

1. To read your name, you can use the `input()` function in Python. This function prompts the user to enter some text and returns the text entered by the user as a string.

```python
name = input("Enter your name: ")
```

2. Once you have the name stored in a variable, you can use the `print()` function to display a message that includes the name. You can use string concatenation or string formatting to include the name in the message.

```python
# Using string concatenation
print("Hello, " + name + "!")

# Using string formatting
print("Hello, {}!".format(name))
```

3. The above code will prompt the user to enter their name, store the entered name in a variable, and then print a message that includes the name. The final output will look something like this:

```
Enter your name: John
Hello, John!
```

4. This is a simple way to read the user's name and print a personalized greeting message. You can modify the code to include additional information or to format the message differently.