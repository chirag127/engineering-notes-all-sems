 Here are the notes in markdown format without any emojis or external links and in a formal tone:

### Representing Scope Information for Symbol Tables (Unit 4 - Compiler Design)

1. Symbol tables are data structures used by compilers to keep track of identifiers and their attributes within a program.
2. They store information about names of variables, functions, types, etc. and the attributes associated with them like type, scope, address, etc.
3. The scope of an identifier determines where it is visible or accessible within a program. The symbol table needs to represent the scopes in which the identifiers are defined to determine if a use of an identifier is valid or not.
4. There are typically two approaches to represent scope information in a symbol table:

- Nesting: The symbol table itself is hierarchical or nested, mimicking the nested scope structure of the program. Each entry in the table includes a pointer to its enclosing scope.
- Sequential: Symbol tables are sequentially organized but include an additional scope field to indicate the scope an entry is defined in. The table keeps track of the current scope and searches proceed sequentially but also check the scope field to determine if a declaration is in scope or not.

5. Both approaches have their pros and cons in terms of time and space complexity for searching and inserting entries. The choice depends on the particular implementation and application. But both are used in practice for compiling programming languages.