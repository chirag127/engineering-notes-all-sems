# Representing Scope Information

In the subject of Compiler Design, Unit 4 - Symbol Tables, representing scope information is an important topic. Here are some key points to consider:

1. **Scope** refers to the region of the program where a name or identifier is visible and can be accessed.
2. A **symbol table** is a data structure used by the compiler to keep track of scope and binding information about names.
3. The symbol table is used to store information about the **type, scope, and location** of each identifier in the program.
4. **Nested scopes** can be represented using a **stack** of symbol tables, where each table corresponds to a different level of nesting.
5. When a new scope is entered, a new symbol table is pushed onto the stack. When the scope is exited, the symbol table is popped from the stack.
6. **Name resolution** involves searching the stack of symbol tables from top to bottom to find the most recent binding for a given name.
7. Some languages, such as C and C++, allow **forward references** to names that have not yet been declared. This requires the use of a **two-pass** compilation process, where the first pass collects information about all names and the second pass resolves references to those names.
