# 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input

- To run a python program on Pi, you need to have python installed on your Pi. You can check if python is installed by typing `python --version` in the terminal. If you see the version number, then python is installed. If not, you can install it by typing `sudo apt install python3` in the terminal.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can open a text editor by typing its name in the terminal, such as `nano` or `idle`. You can also use the graphical user interface (GUI) to open a text editor from the menu.
- To save a python program, you need to give it a name with the `.py` extension, such as `print_name.py`. You can save the program by pressing `Ctrl+O` in nano, `:w` in vim, or `File -> Save` in idle.
- To run a python program, you need to type `python3` followed by the name of the program in the terminal, such as `python3 print_name.py`. You can also run the program by double-clicking on it from the GUI, or by choosing `Run -> Run Module` in idle.
- To print a name 'n' times, where name and n are read from standard input, you need to use the `input` function to get the user input, and the `print` function to display the output. You also need to use a `for` loop to repeat the print statement 'n' times. Here is an example of a python program that does this:

```python
# print_name.py
# This program prints a name 'n' times, where name and n are read from standard input

# Get the name from the user
name = input("Enter your name: ")

# Get the number of times to print the name from the user
n = int(input("Enter the number of times to print your name: "))

# Use a for loop to print the name 'n' times
for i in range(n):
    print(name)
```

- To test the program, you can run it and enter some values for the name and n, such as `Alice` and `5`. You should see the output like this:

```bash
Enter your name: Alice
Enter the number of times to print your name: 5
Alice
Alice
Alice
Alice
Alice
```