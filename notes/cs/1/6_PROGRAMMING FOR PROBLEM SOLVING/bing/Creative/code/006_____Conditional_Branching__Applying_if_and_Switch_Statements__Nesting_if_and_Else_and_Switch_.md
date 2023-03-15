Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content on the topic of conditional branching:

### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

Conditional branching is a programming concept that allows the execution of different blocks of code depending on some conditions. The most common conditional statements are `if` and `switch`, which can be used in different scenarios and languages.

- The `if` statement evaluates a boolean expression and executes a block of code if the expression is true. Optionally, it can be followed by an `else` statement that executes a different block of code if the expression is false. For example:

```java
// Java code
int age = 18;
if (age >= 18) {
  System.out.println("You are an adult.");
} else {
  System.out.println("You are a minor.");
}
```

- The `switch` statement evaluates an expression and compares it with multiple cases. It executes the block of code associated with the matching case. Optionally, it can have a `default` case that executes if none of the cases match. For example:

```javascript
// JavaScript code
let day = "Monday";
switch (day) {
  case "Monday":
    console.log("It is the first day of the week.");
    break;
  case "Friday":
    console.log("It is the last day of the week.");
    break;
  default:
    console.log("It is neither the first nor the last day of the week.");
    break;
}
```

- The `if` and `switch` statements can be nested inside each other to create more complex conditional logic. For example:

```python
# Python code
grade = 85
if grade >= 60:
  print("You passed the exam.")
  if grade >= 90:
    print("You got an A.")
  elif grade >= 80:
    print("You got a B.")
  elif grade >= 70:
    print("You got a C.")
  else:
    print("You got a D.")
else:
  print("You failed the exam.")
  switch (grade // 10) {
    case 5:
      print("You were close to passing.");
      break;
    case 4:
      print("You need to study more.");
      break;
    default:
      print("You need to work harder.");
      break;
  }
```

- The `if` and `switch` statements can also be used in combination with other control structures, such as loops, functions, and classes, to create more dynamic and modular programs. For example:

```c
// C code
#include <stdio.h>

// A function that returns the factorial of a number
int factorial(int n) {
  int result = 1;
  for (int i = 1; i <= n; i++) {
    result *= i;
  }
  return result;
}

// A function that prints the menu and returns the user's choice
int menu() {
  int choice;
  printf("Choose an option:\n");
  printf("1. Calculate the factorial of a number\n");
  printf("2. Exit the program\n");
  scanf("%d", &choice);
  return choice;
}

// The main function
int main() {
  int option, number, result;
  while (1) {
    option = menu();
    switch (option) {
      case 1:
        printf("Enter a number: ");
        scanf("%d", &number);
        if (number >= 0) {
          result = factorial(number);
          printf("The factorial of %d is %d\n", number, result);
        } else {
          printf("Invalid input. The number must be non-negative.\n");
        }
        break;
      case 2:
        printf("Thank you for using the program. Goodbye.\n");
        return 0;
      default:
        printf("Invalid option. Please choose 1 or 2.\n");
        break;
    }
  }
}
```
