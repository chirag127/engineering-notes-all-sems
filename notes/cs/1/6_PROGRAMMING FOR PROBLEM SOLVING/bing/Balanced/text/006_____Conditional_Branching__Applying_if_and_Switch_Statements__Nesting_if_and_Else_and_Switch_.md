### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

- Conditional branching is a programming concept that allows the execution of different code blocks depending on certain conditions.
- The most common way to implement conditional branching is by using **if** and **switch** statements.
- An **if** statement evaluates a boolean expression and executes a code block if the expression is true, or optionally another code block if the expression is false.
- A **switch** statement compares a value with a set of cases and executes the code block associated with the matching case, or optionally a default code block if no case matches.
- Both **if** and **switch** statements can be nested inside other **if** and **switch** statements, or inside loops, to create more complex branching logic.
- Nesting **if** and **else** statements allows for multiple conditions to be checked and different actions to be taken based on the results.
- Nesting **switch** statements allows for different cases to be handled based on the value of more than one variable.

- Here are some examples of conditional branching in Java:

```java
// Example of an if statement
int age = 18;
if (age >= 18) {
  System.out.println("You are an adult.");
} else {
  System.out.println("You are a minor.");
}

// Example of a switch statement
char grade = 'A';
switch (grade) {
  case 'A':
    System.out.println("Excellent!");
    break;
  case 'B':
    System.out.println("Good!");
    break;
  case 'C':
    System.out.println("Average.");
    break;
  case 'D':
    System.out.println("Poor.");
    break;
  case 'F':
    System.out.println("Fail.");
    break;
  default:
    System.out.println("Invalid grade.");
}

// Example of nesting if and else statements
int x = 10;
int y = 20;
if (x > y) {
  System.out.println("x is greater than y.");
} else if (x < y) {
  System.out.println("x is less than y.");
} else {
  System.out.println("x is equal to y.");
}

// Example of nesting switch statements
int month = 3;
int day = 15;
switch (month) {
  case 1:
    System.out.println("January");
    break;
  case 2:
    System.out.println("February");
    break;
  case 3:
    System.out.println("March");
    switch (day) {
      case 1:
        System.out.println("First day of spring.");
        break;
      case 15:
        System.out.println("Ides of March.");
        break;
      case 31:
        System.out.println("Last day of the month.");
        break;
      default:
        System.out.println("Nothing special.");
    }
    break;
  case 4:
    System.out.println("April");
    break;
  // ... other cases
  default:
    System.out.println("Invalid month.");
}
```