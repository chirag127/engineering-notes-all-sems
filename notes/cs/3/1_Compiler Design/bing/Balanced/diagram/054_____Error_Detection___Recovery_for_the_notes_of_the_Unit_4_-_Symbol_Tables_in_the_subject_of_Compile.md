### Error Detection and Recovery in Compiler Design

- Error detection is the process of locating and reporting any errors in the source program that violate the syntax and semantic rules of the language.
- Error recovery is the ability of the compiler to resume parsing of the program after detecting such errors while the compilation process .
- Errors can occur at various phases of compilation, such as lexical analysis, syntax analysis, semantic analysis, code generation, and code optimization.
- The compiler should be able to handle errors gracefully and not terminate abruptly or produce incorrect code.
- There are different strategies for error detection and recovery, depending on the phase and the type of error. Some of the common strategies are  :
  - Panic mode: The parser discards input symbols one at a time until it finds a synchronizing token, such as a semicolon or a right brace, that can help it resume normal parsing. This strategy is simple but may skip a large portion of the input and lose the context of the error.
  - Phrase level recovery: The parser performs local correction on the remaining input by replacing, deleting, or inserting symbols to form a valid phrase. This strategy is more precise but may introduce new errors or require a lot of lookahead.
  - Error productions: The parser uses special grammar rules that generate erroneous constructs and allow the parser to handle them appropriately. This strategy is more flexible but may complicate the grammar and the parsing algorithm.
  - Global correction: The parser tries to find the minimum number of changes required to make the entire input string valid. This strategy is more accurate but may be computationally expensive and require backtracking.
  - Symbol table: The compiler maintains a symbol table that stores information about the identifiers and their attributes in the program. The compiler can use the symbol table to detect and recover from errors such as undeclared variables, type mismatches, or redefinitions. The compiler can also update the symbol table to reflect the corrections made to the errors.