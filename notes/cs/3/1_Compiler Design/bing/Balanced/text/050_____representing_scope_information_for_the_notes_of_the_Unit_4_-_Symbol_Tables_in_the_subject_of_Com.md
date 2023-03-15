### Representing Scope Information

- Scope is the region of the program where a name (identifier) is valid and can be used to refer to a declared entity.
- A symbol table is a data structure that stores information about the names and their associated entities in a program.
- A symbol table should be able to handle the following tasks related to scope:
  - Insert a name and its attributes into the symbol table when a declaration is encountered.
  - Look up a name and retrieve its attributes when a reference is encountered.
  - Delete a name and its attributes from the symbol table when the scope of the name ends.
- There are different ways to represent scope information in a symbol table, depending on the scoping rules of the language and the structure of the program.
- Some common methods are:
  - Linear list: A single symbol table is used for the entire program. Each entry has a field to indicate the scope of the name. This method is simple but inefficient for large programs with nested scopes.
  - Nested list: A symbol table is created for each scope in the program. Each table has a pointer to its parent table, forming a tree structure. This method allows fast lookup of names in the current scope, but requires traversing the tree to find names in outer scopes.
  - Hash table: A hash function is used to map names to buckets in a symbol table. Each bucket contains a list of entries with the same hash value. Each entry has a field to indicate the scope of the name. This method allows fast insertion and lookup of names, but requires handling of collisions and rehashing when the table grows or shrinks.
  - Stack: A stack of symbol tables is maintained, where each table corresponds to a scope in the program. A new table is pushed onto the stack when a new scope is entered, and popped off the stack when the scope is exited. This method allows easy insertion and deletion of names, but requires searching the stack from top to bottom to find names in outer scopes.