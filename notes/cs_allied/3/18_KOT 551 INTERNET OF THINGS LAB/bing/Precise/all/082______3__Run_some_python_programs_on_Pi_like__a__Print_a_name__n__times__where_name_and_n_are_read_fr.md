#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

To run a Python program on a Raspberry Pi, you will need to have Python installed on the device. Most Raspberry Pi operating systems come with Python pre-installed, but if not, you can install it using the following command:

```
sudo apt-get install python3
```

Once Python is installed, you can create a new Python file using a text editor such as nano. For example, to create a new file called `print_name.py`, you can use the following command:

```
nano print_name.py
```

In the text editor, you can write the following Python code to print a name 'n' times, where name and n are read from standard input:

```python
name = input("Enter a name: ")
n = int(input("Enter a number: "))

for i in range(n):
    print(name)
```

After writing the code, you can save and exit the text editor by pressing `Ctrl + X`, then `Y` to confirm, and `Enter` to save the changes.

To run the Python program, you can use the following command:

```
python3 print_name.py
```

This will prompt you to enter a name and a number, and then it will print the name the specified number of times.