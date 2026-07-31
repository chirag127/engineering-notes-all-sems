# Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

Conditional branching is a programming concept that allows the execution of different blocks of code depending on some conditions. The most common conditional statements are `if` and `switch`, which can be used to test various expressions and values.

## if Statement

The `if` statement is used to execute a block of code only if a certain condition is true. The syntax of the `if` statement is:

```java
if (condition) {
  // code to execute if condition is true
}
```

The condition can be any expression that evaluates to a boolean value (`true` or `false`). The code inside the curly braces `{}` is called the body of the `if` statement, and it will only run if the condition is true. If the condition is false, the `if` statement will be skipped and the program will continue with the next statement.

For example, the following code will print "Hello, Sydney!" only if the variable `name` is equal to "Sydney":

```java
String name = "Sydney";
if (name.equals("Sydney")) {
  System.out.println("Hello, Sydney!");
}
```

## else Statement

The `else` statement is used to execute a block of code if the condition of the `if` statement is false. The syntax of the `else` statement is:

```java
if (condition) {
  // code to execute if condition is true
} else {
  // code to execute if condition is false
}
```

The `else` statement must be placed after the `if` statement, and it does not have a condition of its own. The code inside the `else` block will run only if the condition of the `if` statement is false. If the condition is true, the `else` block will be skipped and the program will continue with the next statement.

For example, the following code will print "Hello, Sydney!" if the variable `name` is equal to "Sydney", and "Hello, stranger!" otherwise:

```java
String name = "Sydney";
if (name.equals("Sydney")) {
  System.out.println("Hello, Sydney!");
} else {
  System.out.println("Hello, stranger!");
}
```

## else if Statement

The `else if` statement is used to test multiple conditions in a sequence. The syntax of the `else if` statement is:

```java
if (condition1) {
  // code to execute if condition1 is true
} else if (condition2) {
  // code to execute if condition2 is true
} else if (condition3) {
  // code to execute if condition3 is true
} ...
else {
  // code to execute if none of the conditions are true
}
```

The `else if` statement must be placed after the `if` statement, and before the `else` statement (if any). The `else if` statement has a condition of its own, which will be evaluated only if the previous conditions are false. The code inside the `else if` block will run only if its condition is true. If the condition is false, the `else if` block will be skipped and the program will continue with the next statement.

For example, the following code will print "Good morning!" if the variable `hour` is less than 12, "Good afternoon!" if the variable `hour` is between 12 and 18, and "Good evening!" otherwise:

```java
int hour = 15;
if (hour < 12) {
  System.out.println("Good morning!");
} else if (hour < 18) {
  System.out.println("Good afternoon!");
} else {
  System.out.println("Good evening!");
}
```

## switch Statement

The `switch` statement is used to execute different blocks of code based on the value of a variable or an expression. The syntax of the `switch` statement is:

```java
switch (expression) {
  case value1:
    // code to execute if expression is equal to value1
    break;
  case value2:
    // code to execute if expression is equal to value2
    break;
  case value3:
    // code to execute if expression is equal to value3
    break;
  ...
  default:
    // code to execute if none of the values match the expression
    break;
}
```

The `switch` statement evaluates the expression and compares it with the values of each `case`. If a match is found, the code inside the corresponding `case` block will run. The `break` statement is used to exit the `switch` statement and prevent the execution of the following `