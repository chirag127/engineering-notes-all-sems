 Here is the formal content on the given topic in markdown format:

### Conditional Branching: Applying if and Switch Statements, Nesting if and Else and Switch

1. If Statement: The if statement executes a block of code only if a specified condition is true.

Syntax:
if (condition) {
  // block of code to be executed if the condition is true
}

2. Else Statement: The else statement executes a block of code if the same condition is false.

Syntax:
if (condition) {
  // block of code to be executed if the condition is true
} else {
  // block of code to be executed if the condition is false
}

3. Nesting If and Else: You can nest if statements within if statements to create complex logical tests. The inner if statement is only executed if its condition is true and the outer if statement's condition is also true.

Syntax:
if (outer condition) {
  if (inner condition) {
    // run this code only if both conditions are true
  }
}

4. Switch Statement: A switch statement allows a program to evaluate an expression and execute code based on the value of the expression. It's typically used to replace multiple if statements.

Syntax:
switch (expression) {
  case x:
    // code block to be executed if the expression matches x
    break;
  case y:
    // code block to be executed if the expression matches y
    break;
  default:
    // code block to be executed if the expression matches none of the cases
}

The break statements are important to stop the switch from continuing to check cases.

The content is written in formal markdown format without any emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.