## Unit 4 - Symbol Tables

- A symbol table is a data structure that stores information about the identifiers (symbols) used in a program, such as variables, constants, functions, etc.
- A symbol table is typically used by a compiler or an interpreter to perform semantic analysis, such as type checking, scope resolution, and code generation.
- A symbol table can be implemented using various data structures, such as hash tables, binary search trees, or linked lists. The choice of data structure depends on the trade-off between time and space efficiency, as well as the complexity of the operations required on the symbol table.
- A symbol table usually supports the following operations:
  - Insert: add a new symbol and its associated information to the table.
  - Lookup: search for a symbol in the table and return its information, or indicate that the symbol is not found.
  - Delete: remove a symbol and its information from the table.
  - Update: modify the information of an existing symbol in the table.
- A symbol table may also support other operations, such as:
  - Scope: manage the visibility and lifetime of symbols in different parts of the program, such as global, local, or nested scopes.
  - Overloading: handle the case when multiple symbols have the same name but different meanings, such as function overloading or operator overloading.
  - Inheritance: handle the case when symbols are inherited from a parent class or interface, such as in object-oriented programming.
- A symbol table can be organized in different ways, depending on the structure and semantics of the programming language. Some common ways are:
  - Flat symbol table: a single table that contains all the symbols in the program, regardless of their scope or context. This is suitable for simple languages that do not support scoping or overloading.
  - Scoped symbol table: a hierarchy of tables that reflect the nested structure of the program, such as blocks, functions, classes, etc. Each table contains the symbols defined in a specific scope, and can access the symbols in its parent or ancestor scopes. This is suitable for languages that support scoping and inheritance.
  - Overloaded symbol table: a table that contains multiple entries for each symbol name, each with a different signature or type. The table uses a mechanism to resolve the ambiguity when a symbol name is used, such as the number and type of arguments, the return type, or the context. This is suitable for languages that support overloading and polymorphism.