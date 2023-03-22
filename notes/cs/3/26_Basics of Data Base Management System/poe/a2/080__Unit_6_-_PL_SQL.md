 Here is the formal content written in Markdown format with points on the topic "Unit 6 - PL/SQL" without any emojis or external links:

## Unit 6 - PL/SQL

1. PL/SQL is Oracle's procedural extension to SQL. It allows you to group SQL statements into a block and execute them together. PL/SQL blocks are used to:
- Construct complex logic
- Manipulate data
- Handle errors and exceptions

2. PL/SQL Block Structure: A PL/SQL block has a declarative part, an executable part, and an optional exception-handling part.
Declarative Part: Used to declare constants, variables, exceptions, and cursors.
Executable Part: Contains statements that perform actions.
Exception-Handling Part: Contains statements that deal with errors or exceptions.

3. Variable Declaration: Variables are declared in the declarative part of the PL/SQL block. The syntax is:
variable_name [CONSTANT] datatype [NOT NULL];

Where:
- variable_name is the name of the variable
- CONSTANT means the variable will never change
- datatype is the data type of the variable (e.g. VARCHAR2, NUMBER, DATE, etc.)
- NOT NULL means a value must always be assigned to this variable

4. Comments: Comments in PL/SQL start with -- and continue to the end of the line. They are ignored by the compiler and used to provide notes for the programmer.