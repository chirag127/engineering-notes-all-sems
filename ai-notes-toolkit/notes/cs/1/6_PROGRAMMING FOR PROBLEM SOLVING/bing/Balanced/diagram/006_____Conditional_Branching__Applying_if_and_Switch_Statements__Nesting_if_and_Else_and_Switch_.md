### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

Conditional branching is a programming concept that allows the execution of different code blocks depending on certain conditions. The most common conditional statements in Java are `if` and `switch`.

- The `if` statement evaluates a boolean expression and executes a code block if the expression is true, or optionally another code block if the expression is false. The syntax of the `if` statement is:

```java
if (condition) {
  // code block to execute if condition is true
} else {
  // code block to execute if condition is false
}
```

- The `switch` statement evaluates an expression and compares it with multiple cases. If a case matches the expression, the corresponding code block is executed. The syntax of the `switch` statement is:

```java
switch (expression) {
  case value1:
    // code block to execute if expression equals value1
    break;
  case value2:
    // code block to execute if expression equals value2
    break;
  ...
  default:
    // code block to execute if none of the cases match the expression
    break;
}
```

- The `break` statement is used to exit the `switch` statement and prevent the execution of the following cases. The `default` case is optional and is executed if none of the other cases match the expression.

- The `if` and `switch` statements can be nested inside each other to create more complex conditional logic. For example:

```java
if (age >= 18) {
  switch (gender) {
    case "male":
      System.out.println("You are an adult man.");
      break;
    case "female":
      System.out.println("You are an adult woman.");
      break;
    default:
      System.out.println("You are an adult of unknown gender.");
      break;
  }
} else {
  System.out.println("You are a minor.");
}
```

- The above code evaluates the age and gender variables and prints different messages depending on their values. The `if` statement checks if the age is greater than or equal to 18, and if so, it executes the `switch` statement that compares the gender with different cases. If the age is less than 18, the `else` block is executed and prints a message indicating that the person is a minor.