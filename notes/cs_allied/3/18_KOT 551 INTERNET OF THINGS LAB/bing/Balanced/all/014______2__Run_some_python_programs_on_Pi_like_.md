#### 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on the Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on the Pi, you need to have a text editor to write your code, and a terminal to execute it.
- A text editor is a software that allows you to edit plain text files, such as python scripts. There are many text editors available for the Pi, such as Thonny, Geany, Nano, etc. You can choose one according to your preference and skill level.
- A terminal is a software that allows you to interact with the Pi using commands. You can open a terminal by clicking on the icon on the top left corner of the screen, or by pressing Ctrl+Alt+T on the keyboard.
- To run a python program on the Pi, you need to follow these steps:

  - Open a text editor and write your python code. Save the file with a .py extension, such as hello.py, in a folder of your choice.
  - Open a terminal and navigate to the folder where you saved your python file, using the cd command. For example, if you saved your file in a folder called python_projects on the desktop, you can type cd Desktop/python_projects and press Enter.
  - To run your python file, type python3 followed by the name of your file, and press Enter. For example, if your file is called hello.py, you can type python3 hello.py and press Enter. You should see the output of your program on the terminal.
  - To exit the program, press Ctrl+C on the keyboard. To close the terminal, type exit and press Enter, or click on the X button on the top right corner of the window.

- Some examples of python programs that you can run on the Pi are:

  - A program that prints "Hello, world!" on the terminal. You can write this code in your text editor:

    ```python
    print("Hello, world!")
    ```

  - A program that asks for your name and greets you. You can write this code in your text editor:

    ```python
    name = input("What is your name? ")
    print("Hello, " + name + "!")
    ```

  - A program that generates a random number between 1 and 10 and asks you to guess it. You can write this code in your text editor:

    ```python
    import random
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
      print("You got it right!")
    else:
      print("Sorry, the correct number was " + str(number) + ".")
    ```