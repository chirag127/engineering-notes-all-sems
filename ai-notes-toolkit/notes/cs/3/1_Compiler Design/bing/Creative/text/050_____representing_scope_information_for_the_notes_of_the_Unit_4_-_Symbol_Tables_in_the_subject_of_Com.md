### Representing Scope Information

- Scope is the region of the program where a name (identifier) is visible and can be referenced.
- A symbol table is a data structure that stores information about the names and their attributes in a program.
- A symbol table should support the following operations:
  - Insert a name and its attributes into the table.
  - Look up a name and retrieve its attributes from the table.
  - Delete a name and its attributes from the table.
- A symbol table should also handle the scope rules of the programming language, such as:
  - Nested scopes: A scope can be contained within another scope, creating a hierarchy of scopes.
  - Shadowing: A name declared in an inner scope can hide a name declared in an outer scope with the same identifier.
  - Static scoping: The scope of a name is determined by its lexical position in the program, and does not change during execution.
  - Dynamic scoping: The scope of a name is determined by the most recent declaration of that name at run time, and can change during execution.
- There are different ways of representing scope information in a symbol table, such as:
  - Linear symbol table: A single table that stores all the names in the program, with a scope field for each name that indicates its visibility region.
  - Nested symbol table: A tree of tables that reflects the nested structure of scopes in the program, with each table storing the names declared in a particular scope.
  - Symbol table stack: A stack of tables that reflects the dynamic activation of scopes in the program, with each table storing the names declared in a particular scope.