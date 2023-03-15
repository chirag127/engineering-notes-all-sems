### Data structure for symbol tables

- A symbol table is a data structure used by a compiler to store information about the symbols used in a program, such as variable names, function names, types, values, scopes, etc.      
- A symbol table is used by both the analysis and the synthesis parts of a compiler. The analysis part uses the symbol table to check the validity and consistency of the symbols, while the synthesis part uses the symbol table to generate the target code.  
- A symbol table can be implemented using various data structures, such as arrays, linked lists, hash tables, binary search trees, etc. The choice of the data structure depends on the trade-off between the time and space complexity of the operations on the symbol table, such as insertion, deletion, lookup, and modification.  
- A compiler may maintain two types of symbol tables: a global symbol table and a scope symbol table. A global symbol table contains the symbols that are visible throughout the program, such as global variables, constants, and functions. A scope symbol table contains the symbols that are local to a specific scope, such as a block, a function, or a class. 
- To determine the scope of a symbol, symbol tables are arranged in a hierarchical structure, where each scope symbol table is linked to its parent scope symbol table. The global symbol table is the root of the hierarchy. When a symbol is encountered, the compiler searches the symbol table of the current scope, and if not found, it searches the symbol table of the parent scope, and so on, until it reaches the global symbol table. 
- A symbol table may also store additional information about the symbols, such as their attributes, offsets, addresses, registers, etc. These information are used by the compiler to generate the target code and optimize the performance of the program.  

The following diagram illustrates the structure of a symbol table:

```
+-----------------+     +-----------------+     +-----------------+
| Global Symbol   |     | Scope Symbol    |     | Scope Symbol    |
| Table           |     | Table           |     | Table           |
+-----------------+     +-----------------+     +-----------------+
| Name | Type | ...|     | Name | Type | ...|     | Name | Type | ...|
|------+------|----|     |------+------|----|     |------+------|----|
| x    | int  | ...|     | x    | char | ...|     | y    | int  | ...|
| y    | float| ...|     | z    | bool | ...|     | z    | float| ...|
| f    | func | ...|     | f    | func | ...|     | g    | func | ...|
| g    | func | ...|     | g    | func | ...|     | h    | func | ...|
+-----------------+     +-----------------+     +-----------------+
         ^                     ^                     ^
         |                     |                     |
         +---------------------+---------------------+
```