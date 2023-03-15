# Data structure for symbol tables

- A symbol table is an important data structure created and maintained by compilers in order to store information about the occurrence of various entities such as variable names, function names, objects, classes, interfaces, etc.  
- A symbol table is used by both the analysis and the synthesis parts of a compiler. 
- A symbol table helps the compiler to perform various tasks, such as:
  - Checking the validity and scope of identifiers
  - Resolving name conflicts and overloading
  - Type checking and type conversion
  - Code generation and optimization
  - Debugging and error reporting
- A symbol table consists of a set of entries, each of which contains information about a symbol, such as:
  - Name: the identifier of the symbol
  - Type: the data type or structure of the symbol
  - Value: the constant or initial value of the symbol
  - Address: the memory location or offset of the symbol
  - Scope: the region of the program where the symbol is visible
  - Attributes: other properties or flags of the symbol
- A symbol table can be implemented using various data structures, such as:
  - Linear list: a simple array or linked list of symbol entries, which can be searched sequentially or using binary search. This is easy to implement but inefficient for large symbol tables.  
  - Hash table: a data structure that maps each symbol name to a unique hash value, which is used as an index to access the symbol entry in an array. This is efficient for searching and inserting symbols, but requires a good hash function to avoid collisions.  
  - Tree: a data structure that organizes symbol entries in a hierarchical or ordered manner, such as a binary search tree, a trie, or a B-tree. This is efficient for searching and inserting symbols, and can also support range queries and sorting.  
- A compiler maintains two types of symbol tables: a global symbol table which can be accessed by all the procedures and scope symbol tables that are created for each scope in the program. To determine the scope of a name, symbol tables are arranged in hierarchical structure as shown in the example below: 

![Symbol table hierarchy](https://www.tutorialspoint.com/compiler_design/images/symbol_table.jpg)

- A symbol table can be constructed and updated during various phases of the compiler, such as:
  - Lexical analysis: the scanner identifies the tokens and adds them to the symbol table if they are not already present.
  - Syntax analysis: the parser builds the abstract syntax tree and creates scope symbol tables for each block or function.
  - Semantic analysis: the semantic analyzer checks the type and scope of the symbols and assigns them values and addresses.
  - Intermediate code generation: the code generator uses the symbol table to generate intermediate code for each symbol.
  - Optimization: the optimizer uses the symbol table to perform various optimizations, such as constant folding, dead code elimination, etc.
  - Code generation: the code generator uses the symbol table to generate the final target code for each symbol.