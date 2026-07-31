#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch any of these editors from the terminal by typing their name followed by the name of the file you want to create or edit. For example, `nano hello.py` will open a new file called hello.py in nano editor. You can save and exit the editor by pressing Ctrl+X, then Y, then Enter.
- To run a python program, you need to use the python interpreter by typing `python3` followed by the name of the file you want to run. For example, `python3 hello.py` will run the hello.py program. You can also make the file executable by adding a shebang line at the beginning of the file, such as `#!/usr/bin/env python3`, and changing the file permissions by typing `chmod +x hello.py`. Then you can run the file by typing `./hello.py`.
- To print a name 'n' times, where name and n are read from standard input, you need to use the input() function to get the user input, and the print() function to display the output. You also need to use a loop to repeat the print() function 'n' times. For example, the following program will print a name 'n' times:

```python
# Get the name and n from the user
name = input("Enter a name: ")
n = int(input("Enter a number: "))

# Loop n times
for i in range(n):
  # Print the name
  print(name)
```

- To test the program, you can run it on your Pi and enter some values for the name and n. For example, if you enter Alice and 3, you will see the following output:

```bash
Enter a name: Alice
Enter a number: 3
Alice
Alice
Alice
```