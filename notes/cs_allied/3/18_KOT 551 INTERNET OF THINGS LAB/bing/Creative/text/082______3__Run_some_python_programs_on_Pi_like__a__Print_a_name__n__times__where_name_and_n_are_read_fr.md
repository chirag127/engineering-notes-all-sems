#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch any of these editors from the terminal by typing their name followed by the name of the file you want to create or edit. For example, `nano hello.py` will open a new file called hello.py in nano editor.
- To print a name 'n' times, where name and n are read from standard input, you can use the following python code:

```python
# Read the name from the user
name = input("Enter your name: ")

# Read the number of times to print from the user
n = int(input("Enter the number of times to print: "))

# Use a for loop to print the name n times
for i in range(n):
    print(name)
```

- To run the python program, you need to save the file and exit the editor. Then, you can type `python3 hello.py` in the terminal and press enter. You will see the prompts for the name and the number, and then the output of the program.
- You can modify the program to print different messages or use different input methods as you wish.