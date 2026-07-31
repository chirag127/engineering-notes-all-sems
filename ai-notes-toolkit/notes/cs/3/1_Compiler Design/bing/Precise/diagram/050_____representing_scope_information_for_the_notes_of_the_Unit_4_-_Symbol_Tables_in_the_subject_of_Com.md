### Representing Scope Information for the Notes of the Unit 4 - Symbol Tables in the Subject of Compiler Design

1. **Scope** refers to the region of the program where a name or an identifier is visible and can be accessed.
2. **Symbol tables** are data structures used by compilers to store information about the names used in a program.
3. Symbol tables can be used to represent scope information by associating each name with the scope in which it is visible.
4. There are several ways to represent scope information in symbol tables, including:
    - **Nested symbol tables**: Each scope has its own symbol table, and symbol tables are nested to reflect the nesting of scopes in the program.
    - **Linear symbol tables**: A single symbol table is used for the entire program, and scope information is represented by adding additional attributes to the entries in the table.
    - **Chained symbol tables**: A separate symbol table is used for each scope, and symbol tables are linked together to reflect the nesting of scopes in the program.
5. The choice of representation depends on various factors, including the complexity of the scoping rules of the programming language and the efficiency of the symbol table operations.
6. Regardless of the representation used, the symbol table must be able to efficiently support operations such as inserting a new name, looking up a name, and determining the scope of a name.