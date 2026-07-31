### Conditions Statements for the notes of the Unit 4 - Introduction to Client Side Scripting in the subject of Web Designing

In client-side scripting, conditions statements are used to make decisions based on certain conditions. These statements help to control the flow of the execution of the program based on certain conditions. The following are the types of conditional statements used in client-side scripting:

1. **if statement:** The if statement is used to execute a set of statements if a certain condition is true. The syntax for the if statement is as follows:
   ```
   if (condition){
      statement(s);
   }
   ```
   Here, the condition is evaluated to true or false. If the condition is true, the statement(s) inside the curly braces will be executed.

2. **if-else statement:** The if-else statement is used to execute a set of statements if a condition is true, and another set of statements if the condition is false. The syntax for the if-else statement is as follows:
   ```
   if (condition){
      statement(s);
   } else {
      statement(s);
   }
   ```
   Here, if the condition is true, the first set of statement(s) will be executed, and if the condition is false, the second set of statement(s) will be executed.

3. **else-if statement:** The else-if statement is used to execute multiple sets of statements based on different conditions. The syntax for the else-if statement is as follows:
   ```
   if (condition1){
      statement(s);
   } else if (condition2) {
      statement(s);
   } else {
      statement(s);
   }
   ```
   Here, if condition1 is true, the first set of statement(s) will be executed, if condition1 is false and condition2 is true, the second set of statement(s) will be executed, and if both conditions are false, the third set of statement(s) will be executed.

4. **switch statement:** The switch statement is used to execute different sets of statements based on different cases. The syntax for the switch statement is as follows:
   ```
   switch (expression){
      case value1:
         statement(s);
         break;
      case value2:
         statement(s);
         break;
      ...
      default:
         statement(s);
   }
   ```
   Here, the expression is evaluated and compared with each case value. If the expression matches a case value, the statement(s) inside that case will be executed. If none of the cases match the expression, the statement(s) inside the default case will be executed.

By using these condition statements in client-side scripting, one can create more dynamic and interactive web pages.