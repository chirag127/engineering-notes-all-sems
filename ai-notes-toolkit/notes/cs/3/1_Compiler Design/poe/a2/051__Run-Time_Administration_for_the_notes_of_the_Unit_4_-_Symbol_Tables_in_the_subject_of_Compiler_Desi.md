 Here is the content in markdown format without any emojis or external links:

### Run-Time Administration for the notes of the Unit 4 - Symbol Tables in Compiler Design:

1. Symbol tables are used to keep track of identifiers (variable and function names) and their attributes.
2. They are used during various phases of compilation -

- Lexical analysis - to check for identifier declaration before use
- Syntax analysis - to resolve identifiers in expressions and statements
- Code generation - to get attributes of identifiers for generating code

3. Some key attributes stored in symbol tables are -

- Name of the identifier
- Type of the identifier (for variables) or return type and parameters (for functions)
- Scope of the identifier
- Memory location (for variables) or address (for functions)

4. Different methods of organizing symbol tables -

- Sequential lists - Easy to implement but time complexity of search, enter and delete is high
- Hashed tables - Fast search but collisions can lead to extra overhead
- Binary search trees - Ordered storage and efficient search, enter and delete but overhead of maintaining order

5. Activation records are used to keep track of information regarding identifiers in the current execution context. They contain -

- Parameters and local variables of the current function
- Return address of the function
- Previous activation record pointer

6. Symbol tables and activation records enable efficient storage and retrieval of information regarding identifiers in a program. This facilitates semantic analysis and code generation in a compiler.

The content is written in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to modify or add anything.