### Representing Scope Information

- Scope is the region of the program where a name (identifier) is valid and can be referenced.
- A symbol table is a data structure that stores information about the names and their attributes in a program.
- A symbol table should be able to handle the following operations efficiently:
  - Insert a new name and its attributes into the table.
  - Look up an existing name and retrieve its attributes from the table.
  - Delete a name and its attributes from the table when it goes out of scope.
- There are different ways to represent scope information in a symbol table, depending on the scoping rules of the programming language.
- Some common methods are:
  - Linear list: A single list of names and attributes, where the most recently inserted name is at the front of the list. This method is simple but inefficient for lookup and deletion operations, as it requires scanning the entire list.
  - Hash table: A hash function maps each name to an index in an array of buckets, where each bucket contains a list of names and attributes that hash to the same index. This method is efficient for lookup and insertion operations, but requires handling of collisions and resizing of the array when it becomes full.
  - Tree: A tree structure where each node represents a scope and contains a list of names and attributes defined in that scope. The root node represents the global scope, and the children of a node represent the nested scopes within that scope. This method is efficient for lookup and deletion operations, as it allows searching only the relevant scopes from the current node to the root node. However, it requires maintaining a pointer to the current node and updating it when entering or exiting a scope.