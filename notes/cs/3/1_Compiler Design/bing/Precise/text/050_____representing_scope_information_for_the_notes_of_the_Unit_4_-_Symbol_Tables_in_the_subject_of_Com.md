### Representing Scope Information for the Notes of the Unit 4 - Symbol Tables in the Subject of Compiler Design

1. **Scope**: The scope of a symbol refers to the region of the program where the symbol is accessible or visible.
2. **Symbol Table**: A symbol table is a data structure used by the compiler to keep track of the scope and attributes of variables and functions.
3. **Nested Scopes**: Many programming languages allow nested scopes, where a new scope is created within an existing scope. The inner scope can access symbols from the outer scope, but the outer scope cannot access symbols from the inner scope.
4. **Scope Rules**: The rules for determining the scope of a symbol vary between programming languages. Some common rules include:
    - **Block Scope**: A new scope is created for each block of code, such as a function or loop.
    - **Function Scope**: A new scope is created for each function definition.
    - **File Scope**: A new scope is created for each file or compilation unit.
5. **Representing Scope in Symbol Tables**: There are several ways to represent scope information in symbol tables, including:
    - **Linear Symbol Table**: A single symbol table is used for the entire program. Symbols are added to the table as they are encountered, and removed when they go out of scope.
    - **Nested Symbol Tables**: A new symbol table is created for each scope, and nested within the symbol table of the enclosing scope. When a symbol is accessed, the innermost symbol table is searched first, followed by the next outermost symbol table, and so on.
    - **Scope Stack**: A stack of symbol tables is used, with one symbol table for each active scope. When a new scope is entered, a new symbol table is pushed onto the stack. When a scope is exited, the top symbol table is popped from the stack.