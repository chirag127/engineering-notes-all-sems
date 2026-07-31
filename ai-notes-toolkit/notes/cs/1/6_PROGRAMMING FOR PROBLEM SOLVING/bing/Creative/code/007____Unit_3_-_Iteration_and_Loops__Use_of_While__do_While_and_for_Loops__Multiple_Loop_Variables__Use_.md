Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn. Here is some content on the topic of Unit 3 - Iteration and Loops:

```markdown
# Unit 3 - Iteration and Loops

## Use of While, do While and for Loops

- Loops are used to repeat a block of code multiple times until a certain condition is met.
- There are three types of loops in C: while, do while and for loops.
- A while loop executes the block of code as long as the condition is true. The condition is checked before each iteration.
- A do while loop executes the block of code at least once, and then checks the condition. If the condition is true, the loop repeats. Otherwise, the loop exits.
- A for loop is a compact way of writing a loop that has a counter variable. It consists of three parts: the initial value, the condition and the increment or decrement of the counter. The loop executes the block of code as long as the condition is true. The counter is updated after each iteration.
- The syntax of the loops are as follows:

```c
// while loop
while (condition) {
  // block of code
}

// do while loop
do {
  // block of code
} while (condition);

// for loop
for (initial value; condition; increment or decrement) {
  // block of code
}
```

## Multiple Loop Variables

- Sometimes, it is useful to have more than one loop variable in a loop. For example, to iterate over a two-dimensional array, we can use two loop variables: one for the rows and one for the columns.
- To use multiple loop variables, we can nest one loop inside another loop. The outer loop controls one variable, and the inner loop controls another variable.
- The syntax of nested loops are as follows:

```c
// nested while loops
while (condition1) {
  // block of code 1
  while (condition2) {
    // block of code 2
  }
  // block of code 3
}

// nested do while loops
do {
  // block of code 1
  do {
    // block of code 2
  } while (condition2);
  // block of code 3
} while (condition1);

// nested for loops
for (initial value 1; condition 1; increment or decrement 1) {
  // block of code 1
  for (initial value 2; condition 2; increment or decrement 2) {
    // block of code 2
  }
  // block of code 3
}
```

## Use of Break, Goto and Continue Statements

- Sometimes, we may want to alter the normal flow of a loop. For example, we may want to exit the loop prematurely, skip an iteration, or jump to another part of the code.
- There are three statements in C that can help us do that: break, goto and continue.
- A break statement terminates the loop immediately and transfers the control to the statement after the loop.
- A goto statement transfers the control to a labeled statement in the same function. A label is a name followed by a colon (:).
- A continue statement skips the rest of the current iteration and moves to the next iteration of the loop.
- The syntax of the statements are as follows:

```c
// break statement
break;

// goto statement
goto label;
// ...
label: // some code

// continue statement
continue;
```
```