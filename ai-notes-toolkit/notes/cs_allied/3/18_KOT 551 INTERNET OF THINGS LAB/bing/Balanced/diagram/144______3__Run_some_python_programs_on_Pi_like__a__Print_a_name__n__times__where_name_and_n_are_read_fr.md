#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch any of these editors from the terminal by typing their name followed by the name of the file you want to create or edit. For example, `nano hello.py` will open a new file called hello.py in nano editor. You can save and exit the editor by pressing Ctrl+X, then Y, then Enter.
- To run a python program, you need to type `python3` followed by the name of the file in the terminal. For example, `python3 hello.py` will run the hello.py program. You can also make the file executable by adding a shebang line at the top of the file and changing its permissions. For example, `#!/usr/bin/env python3` is a shebang line that tells the system to use python3 to run the file. You can change the permissions by typing `chmod +x hello.py` in the terminal. Then you can run the file by typing `./hello.py`.
- To print a name 'n' times, where name and n are read from standard input, you can use the following python program:

```python
# Read the name and n from standard input
name = input("Enter a name: ")
n = int(input("Enter a number: "))

# Print the name n times using a for loop
for i in range(n):
    print(name)
```

- To test the program, you can run it in the terminal and enter some values for name and n. For example, if you enter Alice and 3, you will see the following output:

```
Enter a name: Alice
Enter a number: 3
Alice
Alice
Alice
```