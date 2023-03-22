 Here are the notes on statements that alter the flow of control for Unit 3 - Syntax-directed Translation in Compiler Design:

### If-then statements

- If-then statements are used to execute a block of code only if a specified condition is true.
- The syntax is:
if ( condition ) {
   // block of code to be executed if condition is true
}
- The code in the block is executed only if the condition evaluates to true.
- If the condition evaluates to false, the block of code is skipped.

### If-then-else statements

- If-then-else statements are used to execute one block of code if a condition is true and another block if the condition is false.
- The syntax is:
if ( condition ) {
   // block of code to be executed if condition is true
} else {
   // block of code to be executed if condition is false
}
- One of the two blocks is always executed depending on whether the condition evaluates to true or false.

### Switch statements

- Switch statements are used to perform different actions based on different possible values of an expression.
- The syntax is:
switch (expression) {
   case x:
      // code block to be executed if expression matches x
      break;
   case y:
      // code block to be executed if expression matches y
      break;
   default:
      // code block to be executed if expression matches none of the cases
}
- The expression is evaluated and matched against the cases.
- If a match is found, the code block for that case is executed.
- The break statement is used to exit the switch and prevent executing more code blocks.
- The default code block is executed if no case matches the expression.

[Further notes on other control flow statements etc.]