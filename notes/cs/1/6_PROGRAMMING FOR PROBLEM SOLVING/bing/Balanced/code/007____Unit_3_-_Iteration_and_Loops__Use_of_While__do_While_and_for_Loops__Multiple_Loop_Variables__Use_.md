## Unit 3 - Iteration and Loops: Use of While, do While and for Loops, Multiple Loop Variables, Use of Break , Goto and Continue Statements.

- Iteration and loops are programming concepts that allow a block of code to be executed repeatedly until a certain condition is met.
- There are different types of loops in programming, such as while, do while, and for loops. Each loop has its own syntax and use cases.
- A while loop executes a block of code as long as a given condition is true. The condition is checked before each iteration. For example:

```c
// A while loop that prints the numbers from 1 to 10
int i = 1; // Initialize a loop variable
while (i <= 10) { // Check the condition
  printf("%d\n", i); // Execute the code block
  i++; // Update the loop variable
}
```

- A do while loop executes a block of code at least once, and then repeats it as long as a given condition is true. The condition is checked after each iteration. For example:

```c
// A do while loop that prints the numbers from 1 to 10
int i = 1; // Initialize a loop variable
do {
  printf("%d\n", i); // Execute the code block
  i++; // Update the loop variable
} while (i <= 10); // Check the condition
```

- A for loop executes a block of code for a specified number of times, or until a given condition is met. The loop variable, the condition, and the update expression are all specified in the loop header. For example:

```c
// A for loop that prints the numbers from 1 to 10
for (int i = 1; i <= 10; i++) { // Initialize, check, and update the loop variable
  printf("%d\n", i); // Execute the code block
}
```

- A loop can have multiple loop variables, as long as they are separated by commas in the loop header. For example:

```c
// A for loop that prints the numbers from 1 to 10 and their squares
for (int i = 1, j = 1; i <= 10; i++, j = i * i) { // Initialize, check, and update two loop variables
  printf("%d %d\n", i, j); // Execute the code block
}
```

- A break statement can be used to terminate a loop prematurely, if a certain condition is met inside the loop body. For example:

```c
// A while loop that prints the numbers from 1 to 10, but breaks if i is 5
int i = 1; // Initialize a loop variable
while (i <= 10) { // Check the condition
  printf("%d\n", i); // Execute the code block
  if (i == 5) { // Check another condition
    break; // Terminate the loop
  }
  i++; // Update the loop variable
}
```

- A continue statement can be used to skip the current iteration of a loop, and proceed to the next one, if a certain condition is met inside the loop body. For example:

```c
// A for loop that prints the odd numbers from 1 to 10, but skips the even ones
for (int i = 1; i <= 10; i++) { // Initialize, check, and update the loop variable
  if (i % 2 == 0) { // Check if i is even
    continue; // Skip the current iteration
  }
  printf("%d\n", i); // Execute the code block
}
```

- A goto statement can be used to transfer the control of the program to a specified label, which can be anywhere in the same function. This can be used to create loops, but it is generally discouraged as it can make the code less readable and more error-prone. For example:

```c
// A goto loop that prints the numbers from 1 to 10
int i = 1; // Initialize a loop variable
start: // Define a label
printf("%d\n", i); // Execute the code block
i++; // Update the loop variable
if (i <= 10) { // Check the condition
  goto start; // Transfer the control to the label
}
```