# Storage Allocation in Block Structured Language

In block structured languages, the storage allocation for variables is done in a hierarchical manner. This means that the variables declared in an inner block are allocated storage within the scope of that block, and are not accessible outside of it. Here are some key points to consider when discussing storage allocation in block structured languages:

1. **Block Structure**: A block structured language is one in which the program is divided into blocks, each of which has its own set of variables and statements. These blocks can be nested within one another, creating a hierarchy of scopes.

2. **Variable Declaration**: In a block structured language, variables must be declared within the block in which they are used. This means that a variable declared in an inner block is not accessible in an outer block.

3. **Storage Allocation**: When a variable is declared in a block, storage is allocated for it within the scope of that block. This means that the variable is only accessible within the block in which it was declared.

4. **Variable Lifetimes**: The lifetime of a variable in a block structured language is determined by the block in which it is declared. When the block is exited, the storage for the variable is deallocated, and the variable is no longer accessible.

5. **Nested Blocks**: In a block structured language, blocks can be nested within one another. This creates a hierarchy of scopes, with inner blocks having access to the variables declared in outer blocks, but not vice versa.

Overall, storage allocation in block structured languages is done in a hierarchical manner, with variables being allocated storage within the scope of the block in which they are declared. This allows for greater control over the accessibility and lifetime of variables within a program.