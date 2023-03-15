### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

- Conditional branching is a programming concept that allows the execution of different code blocks depending on some conditions.
- The most common way to implement conditional branching is using the `if` statement, which has the following syntax:

```java
if (condition) {
  // code block to execute if condition is true
}
```

- The condition is a boolean expression that evaluates to either `true` or `false`. If the condition is `true`, the code block inside the `if` statement is executed. If the condition is `false`, the code block is skipped.
- Sometimes, we need to execute a different code block if the condition is `false`. In that case, we can use the `else` statement, which has the following syntax:

```java
if (condition) {
  // code block to execute if condition is true
} else {
  // code block to execute if condition is false
}
```

- The `else` statement must follow an `if` statement. It cannot be used alone. The code block inside the `else` statement is executed only if the condition in the `if` statement is `false`.
- We can also have multiple conditions to check using the `else if` statement, which has the following syntax:

```java
if (condition1) {
  // code block to execute if condition1 is true
} else if (condition2) {
  // code block to execute if condition1 is false and condition2 is true
} else if (condition3) {
  // code block to execute if condition1 and condition2 are false and condition3 is true
} else {
  // code block to execute if none of the conditions are true
}
```

- The `else if` statement must follow an `if` or another `else if` statement. It cannot be used alone. The code block inside the `else if` statement is executed only if the previous conditions are `false` and the current condition is `true`.
- The `else` statement at the end is optional. It is used to execute a default code block if none of the conditions are `true`.
- The `if`, `else if`, and `else` statements can be nested inside each other to create complex conditional logic. For example:

```java
if (condition1) {
  if (condition2) {
    // code block to execute if condition1 and condition2 are true
  } else {
    // code block to execute if condition1 is true and condition2 is false
  }
} else {
  if (condition3) {
    // code block to execute if condition1 is false and condition3 is true
  } else {
    // code block to execute if condition1 and condition3 are false
  }
}
```

- Another way to implement conditional branching is using the `switch` statement, which has the following syntax:

```java
switch (expression) {
  case value1:
    // code block to execute if expression equals value1
    break;
  case value2:
    // code block to execute if expression equals value2
    break;
  case value3:
    // code block to execute if expression equals value3
    break;
  default:
    // code block to execute if expression does not equal any of the values
    break;
}
```

- The `switch` statement evaluates an expression and compares it with different values using the `case` statements. If the expression matches a value, the code block after the `case` statement is executed. The `break` statement is used to exit the `switch` statement after executing a code block. If the expression does not match any of the values, the code block after the `default` statement is executed. The `default` statement is optional. It is used to execute a default code block if none of the values match the expression.
- The `switch` statement can be nested inside another `switch` statement to create complex conditional logic. For example:

```java
switch (expression1) {
  case value1:
    switch (expression2) {
      case value2:
        // code block to execute if expression1 equals value1 and expression2 equals value2
        break;
      case value3:
        // code block to execute if expression1 equals value1 and expression2 equals value3
        break;
      default:
        // code block to execute if expression1 equals value1 and expression2 does not equal any of the values
        break;
    }
    break;
  case value4:
    switch (expression3) {
      case value5:
        // code block to execute if expression1 equals value4