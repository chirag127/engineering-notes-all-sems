 Here is the content in markdown format for the given scope:

### Scope Information for Symbol Tables (Unit 4 Notes)

- A symbol table is a data structure that stores information about identifiers in a program. It maintains a mapping between identifiers and their attributes.
- An important attribute of an identifier is its scope. The scope of an identifier determines the portion of the program in which it is visible and can be accessed.
- There are two types of scopes:
	- Local scope: An identifier has local scope if it is visible only within the block in which it is declared. For example, variables declared inside a function have local scope and are only visible within that function.
	- Global scope: An identifier has global scope if it is visible throughout the entire program. For example, variables declared outside of all functions have global scope.
- Symbol tables must track the scope of each identifier to determine if a reference to it is valid. When compiling code, the symbol table is checked to see if an identifier is declared in the current scope. If so, its attributes can be retrieved; if not, it is a syntax error.
- Accessing an identifier's attributes from the symbol table allows the compiler to resolve references, enforce type checking, and perform other semantic analyses. The scope is a key attribute used to organize symbol tables and lookup identifiers efficiently.
- Examples of symbol tables and scope tracking in compilers can help solidify understanding of this concept. Diagrams of symbol tables and examples of lookups based on scope could be included. The advantages and applications of symbol tables with proper scope tracking are crucial for compilers to function correctly. Overall, scope information is essential data to store and utilize in symbol tables.