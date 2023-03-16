#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch any of these editors from the terminal by typing their name followed by the name of the file you want to create or edit. For example, `nano hello.py` will open a new file called hello.py in nano editor. You can save your changes by pressing Ctrl+O and exit by pressing Ctrl+X.
- To run a python program, you need to use the python command followed by the name of the file you want to execute. For example, `python3 hello.py` will run the hello.py file in python3 interpreter. You can also make your file executable by adding a shebang line at the beginning of the file and changing its permissions. For example, `#!/usr/bin/env python3` is a shebang line that tells the system to use python3 to run the file. You can change the permissions by typing `chmod +x hello.py` and then run the file by typing `./hello.py`.
- To print a name 'n' times, where name and n are read from standard input, you can use the input function to get the user input and store it in variables. Then you can use a for loop to repeat the print statement n times. For example, the following program will print the name 'n' times:

```python
# get the name and n from the user
name = input("Enter a name: ")
n = int(input("Enter a number: "))

# use a for loop to print the name n times
for i in range(n):
    print(name)
```