### Data structure for symbol tables

- A symbol table is a data structure used by a compiler to store information about the symbols used in a program, such as variable names, function names, types, values, scopes, etc.     
- A symbol table is used by both the analysis and the synthesis parts of a compiler, for tasks such as lexical analysis, syntax analysis, semantic analysis, code generation, and code optimization.   
- A symbol table can be implemented using various data structures, such as arrays, linked lists, hash tables, binary search trees, etc. The choice of data structure depends on the trade-off between time and space complexity, as well as the ease of implementation and maintenance.  
- Some of the common operations performed on a symbol table are:
  - Insertion: adding a new symbol and its information to the table.
  - Lookup: searching for a symbol and retrieving its information from the table.
  - Deletion: removing a symbol and its information from the table.
  - Modification: updating the information of an existing symbol in the table.
- A compiler may maintain two types of symbol tables: a global symbol table, which can be accessed by all the procedures in the program, and scope symbol tables, which are created for each scope in the program, such as a function, a block, or a loop. 
- To determine the scope of a symbol, symbol tables are arranged in a hierarchical structure, where each scope symbol table is linked to its parent scope symbol table. The global symbol table is the root of this hierarchy. 
- An example of a symbol table hierarchy for a C program is shown below:

![Symbol table hierarchy](https://www.tutorialspoint.com/compiler_design/images/symbol_table.jpg)

: https://www.adglob.in/blog/compiler-design-symbol-table/
: https://thecodeblocks.com/compiler-design-symbol-table/
: https://t4tutorials.com/symbol-table-in-compiler-design/
: https://www.geeksforgeeks.org/symbol-table-compiler/
: https://en.wikipedia.org/wiki/Symbol_table
: https://www.tutorialspoint.com/compiler_design/compiler_design_symbol_table.htm