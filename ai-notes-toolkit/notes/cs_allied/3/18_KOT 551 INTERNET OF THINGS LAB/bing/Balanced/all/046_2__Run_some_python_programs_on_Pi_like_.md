# 2. Run some python programs on Pi like:

- Python is a popular programming language that can be used to create various applications on Raspberry Pi, such as games, web servers, robots, etc.
- To run a python program on Pi, you need to have python installed on your Pi. You can check if you have python by typing `python --version` in the terminal. If you see a version number, such as `Python 3.7.3`, then you have python installed. If not, you can install python by typing `sudo apt install python3` in the terminal.
- To write a python program, you can use any text editor, such as nano, vim, or IDLE. To open a text editor, you can type its name in the terminal, such as `nano hello.py`. This will create a new file called `hello.py` and open it in nano. You can then type your python code in the editor and save it by pressing `Ctrl+O` and then `Enter`. To exit the editor, press `Ctrl+X`.
- To run a python program, you can type `python3 hello.py` in the terminal, where `hello.py` is the name of your file. This will execute your python code and show the output in the terminal. You can also run a python program in interactive mode by typing `python3` in the terminal. This will open a python shell where you can type python commands and see the results immediately.
- Here are some examples of python programs that you can run on Pi:

  - A program that prints "Hello, world!" to the terminal:

    ```python
    # hello.py
    print("Hello, world!")
    ```

  - A program that asks the user for their name and greets them:

    ```python
    # greet.py
    name = input("What is your name? ")
    print("Hello, " + name + "!")
    ```

  - A program that calculates the area of a circle given its radius:

    ```python
    # area.py
    import math # import the math module
    radius = float(input("Enter the radius of the circle: ")) # get the radius from the user
    area = math.pi * radius ** 2 # calculate the area using the formula
    print("The area of the circle is " + str(area)) # print the area
    ```

  - A program that generates a random number between 1 and 10 and asks the user to guess it:

    ```python
    # guess.py
    import random # import the random module
    number = random.randint(1, 10) # generate a random number between 1 and 10
    guess = int(input("Guess the number: ")) # get the guess from the user
    if guess == number: # check if the guess is correct
      print("You got it!")
    else: # otherwise
      print("Sorry, the number was " + str(number))
    ```