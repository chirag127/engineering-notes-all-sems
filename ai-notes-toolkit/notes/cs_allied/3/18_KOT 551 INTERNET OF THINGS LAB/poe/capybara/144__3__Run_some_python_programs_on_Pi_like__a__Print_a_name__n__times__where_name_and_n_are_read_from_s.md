### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input

Here are some points to help you run a Python program on a Raspberry Pi that prints a name 'n' times, where name and n are read from standard input:

1. First, open a terminal window on the Raspberry Pi and navigate to the directory where you want to create the Python program.

2. Use a text editor, such as nano or vim, to create a new Python file with a .py extension. For example, you could name the file print_name.py.

3. In the text editor, write the following code to prompt the user to enter a name and a number of times to print the name:

```python
name = input("Enter a name: ")
n = int(input("Enter the number of times to print the name: "))
```

4. Next, use a for loop to print the name the specified number of times:

```python
for i in range(n):
    print(name)
```

5. Save the Python file and exit the text editor.

6. To run the Python program, return to the terminal window and navigate to the directory where the program is saved.

7. Enter the following command to run the program:

```python
python3 print_name.py
```

8. The program will prompt you to enter a name and a number of times to print the name. Enter the values and press enter.

9. The program will then print the name the specified number of times.

By following these steps, you can easily run a Python program on a Raspberry Pi that prints a name 'n' times, where name and n are read from standard input.