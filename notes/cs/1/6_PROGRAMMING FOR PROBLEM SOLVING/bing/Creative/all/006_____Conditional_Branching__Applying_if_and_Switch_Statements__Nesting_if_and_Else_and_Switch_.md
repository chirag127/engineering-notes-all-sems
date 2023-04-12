# Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

Conditional branching is a programming concept that allows the execution of different code blocks depending on some conditions. Conditional branching can be implemented using two types of statements: if and switch.

## If statement

The if statement is used to execute a code block if a certain condition is true. The syntax of the if statement is:

```java
if (condition) {
  // code block to be executed if condition is true
}
```

The condition can be any expression that evaluates to a boolean value (true or false). The code block can be a single statement or a group of statements enclosed by curly braces. If the condition is true, the code block is executed. If the condition is false, the code block is skipped.

## Else statement

The else statement is used to execute a code block if the condition of the if statement is false. The syntax of the else statement is:

```java
if (condition) {
  // code block to be executed if condition is true
} else {
  // code block to be executed if condition is false
}
```

The else statement must be placed after the if statement. Only one else statement can be used for an if statement. The else statement is optional and can be omitted if there is no code to execute when the condition is false.

## Else if statement

The else if statement is used to check multiple conditions using multiple if statements. The syntax of the else if statement is:

```java
if (condition1) {
  // code block to be executed if condition1 is true
} else if (condition2) {
  // code block to be executed if condition2 is true
} else if (condition3) {
  // code block to be executed if condition3 is true
} ...
else {
  // code block to be executed if none of the conditions are true
}
```

The else if statement must be placed after the if statement and before the else statement. Multiple else if statements can be used for an if statement. The else statement is optional and can be omitted if there is no code to execute when none of the conditions are true.

## Nested if statement

A nested if statement is an if statement inside another if statement. The syntax of a nested if statement is:

```java
if (condition1) {
  // code block to be executed if condition1 is true
  if (condition2) {
    // code block to be executed if condition2 is true
  } else {
    // code block to be executed if condition2 is false
  }
} else {
  // code block to be executed if condition1 is false
}
```

A nested if statement can be used to check more complex conditions that depend on each other. The inner if statement is only executed if the outer if statement is true. The else statement can be used for both the inner and the outer if statement.

## Switch statement

The switch statement is used to execute different code blocks based on the value of a variable or an expression. The syntax of the switch statement is:

```java
switch (variable or expression) {
  case value1:
    // code block to be executed if variable or expression equals value1
    break;
  case value2:
    // code block to be executed if variable or expression equals value2
    break;
  ...
  default:
    // code block to be executed if variable or expression does not match any of the cases
    break;
}
```

The switch statement evaluates the variable or expression and compares it with the values of the cases. If a match is found, the corresponding code block is executed. The break statement is used to exit the switch statement after executing a code block. The default case is optional and can be used to execute a code block if none of the cases match the variable or expression. The default case does not need a break statement.

## Nested switch statement

A nested switch statement is a switch statement inside another switch statement. The syntax of a nested switch statement is:

```java
switch (variable or expression1) {
  case value1:
    // code block to be executed if variable or expression1 equals value1
    switch (variable or expression2) {
      case value2:
        // code block to be executed if variable or expression2 equals value2
        break;
      case value3:
        // code block to be executed if variable or expression2 equals value3
        break;
      ...
      default:
        // code block to be executed if variable or expression2 does not match any of the cases
        break;
    }
    break;
  case value4:
    // code block to be executed if variable or expression1 equals value4

```
