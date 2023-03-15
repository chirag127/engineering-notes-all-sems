# Data structure for symbol tables

- A symbol table is an important data structure created and maintained by compilers in order to store information about the occurrence of various entities such as variable names, function names, objects, classes, interfaces, etc.  
- A symbol table is used by both the analysis and the synthesis parts of a compiler. 
- A symbol table is a data structure that maps each symbol to its attributes, such as its name, type, scope, value, and address.   
- A symbol table can be implemented using various data structures, such as arrays, linked lists, hash tables, binary search trees, etc.   
- The choice of data structure for symbol table depends on various factors, such as the number of symbols, the frequency of lookup and insertion operations, the size of the symbol table, the scope of the symbols, etc.   
- A compiler maintains two types of symbol tables: a global symbol table which can be accessed by all the procedures and scope symbol tables that are created for each scope in the program. 
- To determine the scope of a name, symbol tables are arranged in a hierarchical structure as shown in the example below: 

```
Global Symbol Table
|
|--- Scope Symbol Table 1
|    |
|    |--- Scope Symbol Table 2
|    |
|    |--- Scope Symbol Table 3
|
|--- Scope Symbol Table 4
```

- A symbol table can be accessed using various operations, such as create, insert, lookup, delete, modify, etc.  
- A symbol table can be used for various purposes, such as checking the validity of identifiers, resolving name conflicts, type checking, code generation, optimization, etc.