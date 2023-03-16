Hello, I am Sydney, your AI assistant. I can help you with your notes on variables and flow control for the Unit 1 - Introduction in the subject of Wearable Computing, Mixed Reality and Internet of Everything. Here is some content that you can use for your notes:

### Variables and Flow Control

- Variables are named containers that store data or values in a program. They can have different types, such as integers, floats, strings, booleans, etc. Variables can be declared, assigned, and used in expressions and statements. For example:

```
int x = 10; // declare and assign an integer variable named x
float y = 3.14; // declare and assign a float variable named y
string name = "Sydney"; // declare and assign a string variable named name
bool flag = true; // declare and assign a boolean variable named flag
```

- Flow control is the process of determining the order of execution of statements or blocks of code in a program. Flow control can be influenced by variables and their values, as well as by control structures that allow branching and looping. For example:

```
if (x > y) { // if statement is a control structure that allows branching based on a condition
  print("x is greater than y"); // this statement is executed only if the condition is true
} else {
  print("x is not greater than y"); // this statement is executed only if the condition is false
}

while (flag) { // while statement is a control structure that allows looping based on a condition
  print("Hello, " + name); // this statement is executed repeatedly as long as the condition is true
  flag = false; // this statement changes the value of the flag variable and affects the loop condition
}
```

- There are different types of control structures in programming languages, such as:

  - Sequence logic, or sequential flow, which is the default order of execution of statements from top to bottom. For example:

  ```
  print("This is the first statement"); // this statement is executed first
  print("This is the second statement"); // this statement is executed second
  print("This is the third statement"); // this statement is executed third
  ```

  - Selection logic, or conditional flow, which is the branching of execution based on one or more conditions. For example:

  ```
  if (x == 10) { // if statement with a single condition
    print("x is equal to 10"); // this statement is executed only if the condition is true
  }

  if (y > 0) { // if statement with a single condition
    print("y is positive"); // this statement is executed only if the condition is true
  } else {
    print("y is not positive"); // this statement is executed only if the condition is false
  }

  if (name == "Sydney") { // if statement with a single condition
    print("Hello, Sydney"); // this statement is executed only if the condition is true
  } else if (name == "Alice") { // else if statement with another condition
    print("Hello, Alice"); // this statement is executed only if the first condition is false and the second condition is true
  } else { // else statement with no condition
    print("Hello, stranger"); // this statement is executed only if both conditions are false
  }
  ```

  - Iteration logic, or repetitive flow, which is the looping of execution based on one or more conditions. For example:

  ```
  while (x < 20) { // while statement with a single condition
    print("x is " + x); // this statement is executed repeatedly as long as the condition is true
    x = x + 1; // this statement changes the value of the x variable and affects the loop condition
  }

  for (int i = 0; i < 10; i++) { // for statement with three parts: initialization, condition, and update
    print("i is " + i); // this statement is executed repeatedly as long as the condition is true
  } // the initialization part is executed once before the loop, the condition part is checked before each iteration, and the update part is executed after each iteration

  do { // do statement with a single condition
    print("y is " + y); // this statement is executed at least once, and then repeatedly as long as the condition is true
    y = y - 1; // this statement changes the value of the y variable