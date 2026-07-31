### Declarations and Case Statements

#### Declarations
- Declarations are used to specify the properties of variables, functions, and other program entities.
- They provide information about the type, storage class, and other attributes of the entities being declared.
- Declarations can appear at the beginning of a block or at the file scope.
- In C, declarations follow the syntax: `storage-class-specifier type-specifier declarator-list;`
- The storage-class-specifier specifies the storage duration and linkage of the declared entities.
- The type-specifier specifies the type of the declared entities.
- The declarator-list is a comma-separated list of declarators, each of which specifies the name and, optionally, the type of one declared entity.

#### Case Statements
- Case statements are used in switch statements to define the actions to be taken for specific values of the controlling expression.
- The syntax of a case statement is: `case constant-expression : statement`
- The constant-expression must be an integer constant expression.
- The statement can be any statement, including a compound statement.
- When the value of the controlling expression of the switch statement matches the value of the constant-expression, the statement following the case label is executed.
- If no case label matches the value of the controlling expression, the default label, if present, is executed.
- If no default label is present, no action is taken and the switch statement is exited.
