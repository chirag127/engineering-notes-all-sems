## Unit 3 - Scripting

In this unit, you will learn how to write scripts in Python, a popular programming language. Scripts are files that contain instructions for the computer to execute. Scripts can be used to automate tasks, perform calculations, manipulate data, and more.

To write a script in Python, you need to use a text editor or an integrated development environment (IDE) that supports Python syntax. You also need to have Python installed on your computer or use an online platform that runs Python code.

A Python script has the extension `.py` and usually starts with a line that tells the computer where to find the Python interpreter. This line is called the shebang line and looks like this:

```python
#!/usr/bin/env python3
```

The shebang line is optional, but it is good practice to include it. It allows you to run the script from the command line without specifying the Python program.

The next line of a Python script is usually a comment that describes the purpose of the script. Comments are lines that start with a `#` symbol and are ignored by the computer. Comments help you and other programmers understand the code.

```python
#!/usr/bin/env python3
# This script prints "Hello, world!" to the screen
```

The rest of the script contains the instructions that you want the computer to execute. These instructions are written in Python syntax, which follows certain rules and conventions. For example, Python uses indentation to indicate blocks of code that belong together. Python also uses colons (`:`) to mark the end of a statement that introduces a new block of code.

One of the simplest instructions in Python is the `print` function, which displays a message to the screen. To use the `print` function, you need to write the word `print` followed by parentheses (`()`) that contain the message you want to display. The message can be a string (a sequence of characters enclosed in quotes) or a variable (a name that refers to a value).

```python
#!/usr/bin/env python3
# This script prints "Hello, world!" to the screen
print("Hello, world!")
```

To run the script, you need to save it with a `.py` extension and execute it from the command line or the IDE. For example, if you saved the script as `hello.py`, you can run it from the command line by typing:

```bash
python3 hello.py
```

The output of the script will be:

```bash
Hello, world!
```

This is the basic structure of a Python script. In the following lessons, you will learn how to write more complex and useful scripts that can perform various tasks.