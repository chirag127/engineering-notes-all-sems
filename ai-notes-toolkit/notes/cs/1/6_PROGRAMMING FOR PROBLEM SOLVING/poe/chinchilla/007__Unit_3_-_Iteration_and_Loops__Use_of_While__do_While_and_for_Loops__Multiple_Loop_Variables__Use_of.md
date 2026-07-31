## Unit 3 - Iteration and Loops: Use of While, do While and for Loops, Multiple Loop Variables, Use of Break , Goto and Continue Statements.

In programming, loops are used to execute a block of code repeatedly until a specific condition is met. In this unit, we will study the different types of loops and their use in programming.

### While Loops

A while loop is used to execute a block of code repeatedly as long as a certain condition is true. The syntax for a while loop is as follows:

```
while(condition){
  //code to be executed
}
```

The code inside the loop will be executed repeatedly until the condition becomes false. It is important to ensure that the condition will eventually become false, otherwise the loop will run indefinitely.

### Do While Loops

A do while loop is similar to a while loop, but the code inside the loop is executed at least once before the condition is checked. The syntax for a do while loop is as follows:

```
do{
  //code to be executed
}while(condition);
```

The code inside the loop will be executed at least once, and will continue to be executed as long as the condition is true.

### For Loops

A for loop is used to execute a block of code a specific number of times. The syntax for a for loop is as follows:

```
for(initialization; condition; increment){
  //code to be executed
}
```

The initialization statement is executed only once at the beginning of the loop. The condition is checked before each iteration of the loop, and if it is true, the code inside the loop is executed. The increment statement is executed at the end of each iteration.

### Multiple Loop Variables

In a for loop, multiple loop variables can be used to control the loop. The syntax for using multiple loop variables is as follows:

```
for(initialization; condition; increment1, increment2, ...){
  //code to be executed
}
```

Multiple variables can be used in the increment statement, separated by commas.

### Break Statement

The break statement is used to exit a loop prematurely. When a break statement is encountered inside a loop, the loop is immediately terminated and the program continues with the next statement after the loop. The syntax for a break statement is as follows:

```
while(condition){
  //code to be executed
  if(condition){
    break;
  }
}
```

### Continue Statement

The continue statement is used to skip the current iteration of a loop and move on to the next iteration. The syntax for a continue statement is as follows:

```
for(initialization; condition; increment){
  if(condition){
    continue;
  }
  //code to be executed
}
```

### Goto Statement

The goto statement is used to transfer control to a labeled statement in the program. The syntax for a goto statement is as follows:

```
goto label;
```

The labeled statement must be defined elsewhere in the program. The use of goto statements is generally discouraged, as it can make the program difficult to understand and maintain.

In conclusion, loops are an important construct in programming that allow us to execute a block of code repeatedly. The different types of loops and loop control statements discussed in this unit provide a powerful toolset for controlling the flow of a program.