 Here is the content in markdown format with header declarations and case statements for the notes of Unit 3 - Syntax-directed Translation in Compiler Design:

### Declarations

Declarations are statements that declare identifiers and associate attributes with them.
For example:
- Variable declarations: int x; float y; char z; etc.
- Type declarations: typedef int length; typedef char* string; etc.
- Function declarations: int max(int, int); etc.

Declarations are used to introduce new symbols (identifiers) into the program and provide information about them, such as their type, class, etc.

Case: Declarations must appear in the syntax before the declared identifiers are used. Otherwise, the usage of undeclared identifiers results in syntax errors.

### Case statements

Case statements allow the flow of control to jump to different places in the program based on the value of an expression.
For example:
switch (expression) {
  case x:
    statement;
    break;
  case y:
    statement;
    break;
  // ...
  default:
    statement;
}

The expression is evaluated and compared with the values of each case. If a match is found, the statement(s) following that case are executed. The break statement then exits the switch. If no case matches, the default statements are executed (if provided).

Case: The expression in a switch must be of an integer or enumeration type, or a type that can be converted to an integer. The cases must be constant integer expressions. There must not be duplicate cases. A default clause is optional.

[Additional details, diagrams, examples, advantages, disadvantages, applications, etc. can be included here if required to learn and read from for exams.]