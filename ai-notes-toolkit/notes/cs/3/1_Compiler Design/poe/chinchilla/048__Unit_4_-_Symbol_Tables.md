## Unit 4 - Symbol Tables

Symbol tables are data structures that store key-value pairs, where the key is a symbol and the value is some associated data. They are commonly used in compilers, interpreters, and other programming tools to keep track of variables, functions, and other program entities.

Here are some important points to understand about symbol tables:

- A symbol table is a collection of entries, where each entry represents a symbol and its associated data.
- Symbols can be anything that can be used as a unique identifier, such as variable names, function names, and constants.
- The associated data can be any type of data, such as integer values, string values, or even other symbols.
- Symbol tables can be implemented using various data structures, such as hash tables, binary trees, or linked lists.
- The main operations on a symbol table are insertion, lookup, and deletion of entries.
- When a new symbol is encountered, it is added to the symbol table with its associated data.
- When an existing symbol is referenced, its associated data can be retrieved from the symbol table.
- Symbol tables can be scoped, meaning that symbols can have different meanings in different parts of a program. For example, a variable named "x" in one function may be different from a variable named "x" in another function.
- Scoping can be implemented using a stack of symbol tables, where a new symbol table is pushed onto the stack when entering a new scope, and popped off the stack when leaving a scope.
- Symbol tables can also be used to detect errors, such as duplicate symbols or undefined symbols.
- For example, when a symbol is inserted into the symbol table, its name can be checked to see if it already exists in the current scope, and an error can be raised if it does.
- Similarly, when a symbol is referenced, its name can be checked to see if it exists in the current scope, and an error can be raised if it does not.

In summary, symbol tables are an essential tool for managing program entities in compilers, interpreters, and other programming tools. Understanding the principles behind symbol tables and their implementation can help developers write more efficient and error-free programs.