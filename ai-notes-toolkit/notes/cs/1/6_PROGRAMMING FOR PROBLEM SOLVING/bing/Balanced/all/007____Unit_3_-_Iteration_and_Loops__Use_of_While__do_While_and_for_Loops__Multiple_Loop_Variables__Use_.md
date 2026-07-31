## Unit 3 - Iteration and Loops: Use of While, do While and for Loops, Multiple Loop Variables, Use of Break , Goto and Continue Statements.

- Iteration and loops are programming concepts that allow a block of code to be executed repeatedly until a certain condition is met.
- There are different types of loops in programming, such as while, do while, and for loops. Each type has its own syntax and use cases.
- A while loop executes a block of code as long as a given condition is true. The condition is checked before each iteration. For example:

```
int i = 0; // initialize a loop variable
while (i < 10) { // check the condition
  System.out.println(i); // execute the block of code
  i++; // update the loop variable
}
```

- A do while loop executes a block of code at least once, and then repeats it as long as a given condition is true. The condition is checked after each iteration. For example:

```
int i = 0; // initialize a loop variable
do {
  System.out.println(i); // execute the block of code
  i++; // update the loop variable
} while (i < 10); // check the condition
```

- A for loop executes a block of code for a specified number of times, or until a given condition is met. The loop variable, the condition, and the update are specified in the loop header. For example:

```
for (int i = 0; i < 10; i++) { // initialize, check, and update the loop variable
  System.out.println(i); // execute the block of code
}
```

- A loop can have multiple loop variables, separated by commas, in the loop header. For example:

```
for (int i = 0, j = 10; i < j; i++, j--) { // two loop variables
  System.out.println(i + " " + j); // execute the block of code
}
```

- A break statement can be used to terminate a loop prematurely, when a certain condition is met. For example:

```
for (int i = 0; i < 10; i++) {
  System.out.println(i);
  if (i == 5) {
    break; // exit the loop
  }
}
```

- A goto statement can be used to jump to a specific label in the code, skipping the intermediate statements. For example:

```
for (int i = 0; i < 10; i++) {
  System.out.println(i);
  if (i == 5) {
    goto end; // jump to the label
  }
}
end: // the label
System.out.println("The end");
```

- A continue statement can be used to skip the current iteration of a loop, and proceed to the next one. For example:

```
for (int i = 0; i < 10; i++) {
  if (i % 2 == 0) {
    continue; // skip even numbers
  }
  System.out.println(i); // print odd numbers
}
```