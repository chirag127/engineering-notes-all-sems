Hello, I am Sydney, your AI assistant. I can help you run some python programs on Pi. Here is how you can print a name 'n' times, where name and n are read from standard input:

- First, you need to connect your Pi to a monitor, keyboard, and mouse. You also need to install the Python interpreter on your Pi if you haven't done so already.
- Second, you need to open a terminal window on your Pi and type `python` to enter the interactive mode. You should see a prompt like `>>>` where you can type your commands.
- Third, you need to use the `input` function to read a name and a number from the standard input. For example, you can type `name = input("Enter a name: ")` and press Enter. Then you can type `n = int(input("Enter a number: "))` and press Enter. The `int` function converts the input string to an integer.
- Fourth, you need to use a `for` loop to print the name 'n' times. For example, you can type `for i in range(n):` and press Enter. Then you can type `print(name)` and press Enter. The `range` function generates a sequence of numbers from 0 to n-1. The `print` function prints the name to the standard output.
- Fifth, you can exit the interactive mode by typing `exit()` and pressing Enter. You have successfully run a python program on Pi.

Here is an example of the output:

```python
>>> name = input("Enter a name: ")
Enter a name: Sydney
>>> n = int(input("Enter a number: "))
Enter a number: 5
>>> for i in range(n):
... print(name)
... 
Sydney
Sydney
Sydney
Sydney
Sydney
>>> exit()
```
