#### 3. Run some python programs on Pi like: a) Print a name 'n' times, where name and n are read from standard input,

- To run a python program on Pi, you need to have a python interpreter installed on your Pi. You can check if you have one by typing `python3 --version` in the terminal. If you see a version number, you have python3 installed. If not, you can install it by typing `sudo apt install python3`.
- To write a python program, you need to use a text editor such as nano, vim, or idle. You can launch any of these editors from the terminal by typing their name followed by the name of the file you want to create or edit. For example, `nano hello.py` will open a new file called hello.py in nano editor.
- To print a name 'n' times, where name and n are read from standard input, you need to use the `input` function to get the user input and store it in variables. Then you need to use a `for` loop to repeat the printing 'n' times. You also need to use the `print` function to display the name on the screen. Here is an example of a python program that does this:

```python
# get the name from the user
name = input("Enter your name: ")

# get the number of times to print from the user
n = int(input("Enter the number of times to print: "))

# use a for loop to print the name n times
for i in range(n):
    print(name)
```

- To run the python program, you need to save the file and exit the editor. Then you need to type `python3` followed by the name of the file in the terminal. For example, `python3 hello.py` will run the hello.py program. You will see the output on the screen. You can press Ctrl+C to stop the program.