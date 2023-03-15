### Declarations and Case Statements

#### Declarations
- Declarations are used to specify the properties of variables, functions, and other identifiers.
- They provide information about the type, storage class, and other attributes of the identifier.
- Declarations can appear at the beginning of a block or at the file scope.
- The syntax for a declaration is: `storage-class-specifier type-specifier declarator-list;`
- The storage-class-specifier can be one of the following: `auto`, `register`, `static`, `extern`, or `typedef`.
- The type-specifier can be a basic type such as `int`, `char`, or `float`, or a derived type such as a `struct`, `union`, or `enum`.
- The declarator-list is a comma-separated list of declarators, each of which specifies the name and, optionally, the dimensions of an array or the arguments of a function.

#### Case Statements
- Case statements are used in switch statements to define the actions to be taken for specific values of the controlling expression.
- The syntax for a case statement is: `case constant-expression : statement`
- The constant-expression must be an integer constant expression.
- The statement can be any statement, including another switch statement or a block of statements enclosed in braces.
- Case statements can only appear within a switch statement.
- The break statement can be used to exit the switch statement and transfer control to the statement following the switch.
- If no case matches the value of the controlling expression, the default statement, if present, is executed. If there is no default statement, control falls through to the statement following the switch.
