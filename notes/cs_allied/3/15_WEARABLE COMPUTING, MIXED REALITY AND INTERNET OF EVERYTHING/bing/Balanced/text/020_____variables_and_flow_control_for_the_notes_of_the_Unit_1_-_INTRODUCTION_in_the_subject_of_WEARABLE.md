### Variables and Flow Control

- Variables are named containers that store data or values in a program. They can have different types, such as integers, floats, strings, booleans, etc. Variables can be declared, assigned, and used in expressions or statements.
- Flow control is the process of determining the order of execution of statements or blocks of code in a program. Flow control can be influenced by conditional or logical expressions that evaluate to true or false, and by looping or iterative structures that repeat a block of code until a condition is met or a break statement is executed.
- There are three basic types of flow control structures in programming languages:
  - Sequence: The default flow of control, where statements are executed in the order they appear in the program. For example:

    ```
    int x = 10; // declare and assign a variable
    x = x + 5; // update the variable
    cout << x; // print the variable
    ```

  - Selection: The flow of control where a block of code is executed only if a certain condition is true, or a different block of code is executed if the condition is false. Selection structures can use keywords such as if, else, switch, case, etc. For example:

    ```
    int x = 10; // declare and assign a variable
    if (x > 0) { // check the condition
      cout << "x is positive"; // execute this block if true
    }
    else {
      cout << "x is negative or zero"; // execute this block if false
    }
    ```

  - Iteration: The flow of control where a block of code is executed repeatedly until a certain condition is met, or a break statement is executed. Iteration structures can use keywords such as for, while, do, etc. For example:

    ```
    int x = 10; // declare and assign a variable
    while (x > 0) { // check the condition
      cout << x << " "; // print the variable
      x = x - 1; // update the variable
    }
    cout << "Done"; // print a message
    ```
- Flow control structures can be nested or combined to create more complex logic and functionality in a program. For example:

    ```
    int x = 10; // declare and assign a variable
    for (int i = 0; i < 5; i++) { // outer loop
      if (x % 2 == 0) { // check if x is even
        cout << x << " is even"; // print a message
      }
      else {
        cout << x << " is odd"; // print a message
      }
      x = x + i; // update x
    }
    ```