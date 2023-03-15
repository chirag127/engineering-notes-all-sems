## Unit 3 - Iteration and Loops: Use of While, do While and for Loops, Multiple Loop Variables, Use of Break , Goto and Continue Statements.

- Iteration and loops are programming concepts that allow a block of code to be executed repeatedly based on a condition or a range of values.
- There are three types of loops in C++: while, do while and for loops. Each loop has a different syntax and use case.
- A while loop executes a block of code as long as a given condition is true. The condition is checked before each iteration. The syntax of a while loop is:

```cpp
while (condition) {
  // code to be executed
}
```

- A do while loop executes a block of code at least once, and then repeats as long as a given condition is true. The condition is checked after each iteration. The syntax of a do while loop is:

```cpp
do {
  // code to be executed
} while (condition);
```

- A for loop executes a block of code for a specified number of times, or over a range of values. The loop has three parts: an initialization, a condition and an update. The initialization is executed once before the loop starts, the condition is checked before each iteration, and the update is executed after each iteration. The syntax of a for loop is:

```cpp
for (initialization; condition; update) {
  // code to be executed
}
```

- A loop can have multiple loop variables, which are variables that change their values during the loop execution. For example, a for loop can have two loop variables, one for counting and one for accumulating:

```cpp
int sum = 0; // accumulator variable
for (int i = 1; i <= 10; i++) { // loop variable i
  sum += i; // update the accumulator
}
```

- A loop can be terminated or skipped using break, goto and continue statements. These statements alter the normal flow of the loop execution.
- A break statement exits the loop immediately, and transfers the control to the statement following the loop. For example, a break statement can be used to stop a loop when a certain value is found:

```cpp
int x;
bool found = false;
while (!found) {
  cin >> x; // read a value from the user
  if (x == 0) { // check if the value is zero
    found = true; // set the flag to true
    break; // exit the loop
  }
}
```

- A goto statement transfers the control to a labeled statement in the same function. A label is an identifier followed by a colon. For example, a goto statement can be used to repeat a loop from a certain point:

```cpp
int x;
start: // label
cin >> x; // read a value from the user
if (x < 0) { // check if the value is negative
  cout << "Invalid input. Try again." << endl; // print an error message
  goto start; // go back to the label
}
```

- A continue statement skips the current iteration of the loop, and transfers the control to the next iteration. For example, a continue statement can be used to skip even numbers in a loop:

```cpp
for (int i = 1; i <= 10; i++) {
  if (i % 2 == 0) { // check if the number is even
    continue; // skip the current iteration
  }
  cout << i << endl; // print the odd number
}
```