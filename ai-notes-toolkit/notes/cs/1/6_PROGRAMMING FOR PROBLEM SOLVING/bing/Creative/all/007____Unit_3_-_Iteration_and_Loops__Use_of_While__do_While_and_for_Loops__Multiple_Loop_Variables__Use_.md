# Unit 3 - Iteration and Loops: Use of While, do While and for Loops, Multiple Loop Variables, Use of Break , Goto and Continue Statements.

- Iteration and loops are programming concepts that allow a block of code to be executed repeatedly based on a condition or a range of values.
- There are three types of loops in C programming: while, do while and for loops.
- A while loop executes a block of code as long as a given condition is true. The syntax of a while loop is:

```c
while (condition) {
  // statements
}
```

- A do while loop executes a block of code at least once, and then repeats it as long as a given condition is true. The syntax of a do while loop is:

```c
do {
  // statements
} while (condition);
```

- A for loop executes a block of code for a specified number of times, or over a range of values. The syntax of a for loop is:

```c
for (initialization; condition; update) {
  // statements
}
```

- The initialization part is executed only once before the loop starts. It is usually used to declare and initialize a loop variable.
- The condition part is evaluated before each iteration of the loop. If it is true, the loop continues; otherwise, the loop ends.
- The update part is executed after each iteration of the loop. It is usually used to modify the loop variable or perform some other action.
- Multiple loop variables can be used in a for loop by separating them with commas. For example:

```c
for (i = 0, j = 10; i < j; i++, j--) {
  // statements
}
```

- This loop uses two variables, i and j, and iterates until i is equal to or greater than j.
- The break statement can be used to exit a loop prematurely. It transfers the control to the statement immediately after the loop. For example:

```c
for (i = 0; i < 10; i++) {
  if (i == 5) {
    break; // exit the loop
  }
  printf("%d\n", i);
}
```

- This loop prints the numbers from 0 to 4, and then stops when i is equal to 5.
- The goto statement can be used to jump to a labeled statement in the same function. It is generally considered a bad practice to use goto, as it can make the code difficult to read and maintain. For example:

```c
for (i = 0; i < 10; i++) {
  if (i == 5) {
    goto end; // jump to the end label
  }
  printf("%d\n", i);
}
end: // label
printf("Loop ended.\n");
```

- This loop prints the numbers from 0 to 4, and then jumps to the end label when i is equal to 5.
- The continue statement can be used to skip the current iteration of a loop and proceed to the next one. It transfers the control to the update part of the loop. For example:

```c
for (i = 0; i < 10; i++) {
  if (i % 2 == 0) {
    continue; // skip even numbers
  }
  printf("%d\n", i);
}
```

- This loop prints the odd numbers from 0 to 9, and skips the even numbers by using continue.