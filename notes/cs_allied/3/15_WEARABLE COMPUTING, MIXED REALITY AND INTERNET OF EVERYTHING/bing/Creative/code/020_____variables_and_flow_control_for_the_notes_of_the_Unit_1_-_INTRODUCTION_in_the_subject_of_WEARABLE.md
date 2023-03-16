### Variables and Flow Control

Variables are named containers that store data or values that can change during the execution of a program. Variables have a name, a type, and a value. For example, a variable named `age` of type `int` can store an integer value like `25`.

Flow control is the process of determining the order of execution of statements or instructions in a program based on certain conditions or parameters. Flow control structures are blocks of code that can alter the flow of control in a program. There are three basic types of flow control structures:

- Sequence: The statements are executed in the order they appear in the program. This is the default flow of control in most programming languages. For example, the following statements are executed sequentially:

```
int x = 10; // declare and assign a variable
x = x + 5; // update the variable
print(x); // print the variable
```

- Selection: The statements are executed based on a condition or a choice. This allows the program to branch into different paths of execution depending on the outcome of the condition. For example, the following statements are executed conditionally:

```
int x = 10; // declare and assign a variable
if (x > 0) { // check a condition
  print("x is positive"); // execute if the condition is true
} else {
  print("x is negative or zero"); // execute if the condition is false
}
```

- Iteration: The statements are executed repeatedly until a condition is met or a break is encountered. This allows the program to loop over a set of instructions for a certain number of times or until a certain criterion is satisfied. For example, the following statements are executed iteratively:

```
int x = 10; // declare and assign a variable
while (x > 0) { // check a condition
  print(x); // execute while the condition is true
  x = x - 1; // update the variable
}
```

Flow control structures can be nested or combined to create more complex logic and functionality in a program. For example, the following statements use nested selection and iteration structures:

```
int x = 10; // declare and assign a variable
for (int i = 0; i < 5; i++) { // loop for 5 times
  if (x % 2 == 0) { // check if x is even
    print("x is even"); // execute if x is even
  } else {
    print("x is odd"); // execute if x is odd
  }
  x = x + 1; // update x
}
```