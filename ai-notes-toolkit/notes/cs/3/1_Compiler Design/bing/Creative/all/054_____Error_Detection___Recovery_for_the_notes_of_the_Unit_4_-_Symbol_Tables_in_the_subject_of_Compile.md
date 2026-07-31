# Error Detection and Recovery in Compiler Design

## Introduction

- Error detection and recovery are important aspects of compiler design, as they ensure the correctness and robustness of the compiler.
- Errors can occur at any stage of the compilation process, such as lexical, syntactic, semantic, or code generation.
- Errors can be classified into two types: fatal errors and non-fatal errors.
  - Fatal errors are those that prevent the compiler from continuing the compilation process, such as missing source file, invalid character, or memory overflow.
  - Non-fatal errors are those that can be detected and reported by the compiler, but do not stop the compilation process, such as spelling mistakes, type mismatch, or undeclared variables.
- The compiler should be able to detect and report as many errors as possible, and recover from them gracefully, without affecting the subsequent compilation of the program.
- The compiler should also avoid reporting spurious errors, which are false or misleading errors caused by previous errors.

## Error Detection Techniques

- Error detection techniques are methods used by the compiler to identify and locate errors in the source program.
- Different types of errors require different techniques for detection, such as:
  - Lexical errors: These are errors in the formation of tokens, such as invalid identifiers, keywords, or literals. They can be detected by the lexical analyzer using regular expressions or finite automata.
  - Syntactic errors: These are errors in the structure of the program, such as missing or extra parentheses, semicolons, or braces. They can be detected by the parser using grammar rules or parsing algorithms.
  - Semantic errors: These are errors in the meaning of the program, such as type mismatch, undeclared variables, or invalid operations. They can be detected by the semantic analyzer using symbol tables, type checking, or scope rules.
  - Code generation errors: These are errors in the translation of the intermediate code to the target code, such as invalid instructions, registers, or addresses. They can be detected by the code generator using code optimization techniques or target machine specifications.

## Error Recovery Techniques

- Error recovery techniques are methods used by the compiler to handle and correct errors in the source program, and resume the compilation process.
- Different types of errors require different techniques for recovery, such as:
  - Panic mode: This is the simplest and most common technique, which involves discarding input symbols until a synchronizing token is found, such as a semicolon, a keyword, or an end-of-file marker. This technique is used by most parsers, but it may skip a large portion of the input and generate many spurious errors.
  - Phase level recovery: This technique involves isolating the errors within a phase of the compilation process, such as lexical, syntactic, or semantic, and continuing the compilation with the next phase. This technique may require the use of dummy tokens, default values, or assumptions to fill the gaps caused by the errors.
  - Error productions: This technique involves modifying the grammar rules to include error symbols, which can be used to handle common or expected errors. This technique can provide more meaningful error messages and better recovery, but it may also complicate the grammar and the parser.
  - Global correction: This technique involves finding the minimum number of changes required to correct the errors in the input, such as insertion, deletion, or substitution of symbols. This technique can provide the best recovery, but it is also the most complex and expensive, as it may require backtracking, lookahead, or dynamic programming algorithms.
  - Symbol table: This technique involves updating the symbol table with the information about the errors, such as the location, type, or severity of the errors. This technique can help in avoiding duplicate or spurious errors, and in generating more accurate error messages and code.