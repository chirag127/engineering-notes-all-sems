### Data structure for symbol tables

- A symbol table is a data structure that stores information about the symbols used in a program, such as variable names, function names, objects, classes, interfaces, etc.    
- A symbol table is used by both the analysis and the synthesis parts of a compiler, to check the validity of the symbols, to resolve their scope and binding, and to generate code for them.   
- A symbol table can be implemented using various data structures, such as arrays, linked lists, hash tables, binary search trees, etc. The choice of the data structure depends on the requirements of the compiler, such as the number of symbols, the frequency of lookup and insertion, the scope rules, the collision handling, etc.    
- A compiler may maintain two types of symbol tables: a global symbol table, which can be accessed by all the procedures and scope symbol tables, that are created for each scope in the program. To determine the scope of a name, symbol tables are arranged in a hierarchical structure, as shown in the example below:

![Symbol table hierarchy](https://www.tutorialspoint.com/compiler_design/images/symbol_table.jpg)

- A symbol table entry typically contains the following information about a symbol:     
  - Name: the identifier of the symbol
  - Type: the data type of the symbol
  - Value: the constant value or the address of the symbol
  - Scope: the region of the program where the symbol is visible
  - Binding: the time when the symbol is bound to a value or an address
  - Attributes: any other information related to the symbol, such as size, offset, alignment, etc.

- A symbol table can be constructed and updated during different phases of the compiler, such as lexical analysis, syntax analysis, semantic analysis, and code generation. The symbol table can also be used for error detection and optimization.