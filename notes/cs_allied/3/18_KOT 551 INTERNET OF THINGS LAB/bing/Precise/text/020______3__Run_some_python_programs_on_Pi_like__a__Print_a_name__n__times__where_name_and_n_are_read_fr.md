#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

To run a Python program on a Raspberry Pi, you will need to have Python installed on the device. Most Raspberry Pi's come with Python pre-installed, but if not, you can install it by running the following command in the terminal:

```
sudo apt-get install python3
```

Once Python is installed, you can create a new Python file using a text editor such as nano. To create a new file called `print_name.py`, run the following command in the terminal:

```
nano print_name.py
```

This will open the nano text editor. In the editor, you can write the following Python code to print a name 'n' times, where name and n are read from standard input:

```python
name = input("Enter a name: ")
n = int(input("Enter a number: "))

for i in range(n):
    print(name)
```

After writing the code, press `Ctrl + O` to save the file, then `Ctrl + X` to exit the nano text editor.

To run the Python program, navigate to the directory where the `print_name.py` file is located using the `cd` command, then run the following command in the terminal:

```
python3 print_name.py
```

This will run the Python program and prompt you to enter a name and a number. The program will then print the entered name the specified number of times.