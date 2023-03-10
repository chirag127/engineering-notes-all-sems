
### Representing Scope Information for the Notes of the Unit 4 - Symbol Tables in the Subject of Compiler Design 

* Symbol tables are data structures used by compilers to store information about the symbols used in a program. 
* They are used to store information such as the type of a symbol, its scope, its location in memory, and its value.
* Symbol tables can be implemented as either hash tables or binary search trees. 
* Hash tables are fast and easy to implement, but they do not provide any ordering of the symbols. 
* Binary search trees, on the other hand, provide an ordering of the symbols, but they are slower and more complicated to implement.
* Symbol tables are used to keep track of the scope of a symbol. The scope of a symbol is the region of the program in which it is visible. 
* This is important for compilers, as it allows them to distinguish between two symbols with the same name but different scopes. 
* For example, a variable declared in a function has a local scope, while a variable declared outside of any function has a global scope.
* Symbol tables can also be used to store information about the types of symbols. 
* This is important for compilers, as it allows them to detect type mismatch errors. 
* For example, a compiler can detect an error if a variable of type int is assigned a value of type float. 
* Symbol tables can also be used to store information about the location of a symbol in memory. 
* This is important for compilers, as it allows them to generate code that references the correct memory location. 
* Finally, symbol tables can also be used to store information about the values of symbols. 
* This is important for compilers, as it allows them to generate code that uses the correct values.