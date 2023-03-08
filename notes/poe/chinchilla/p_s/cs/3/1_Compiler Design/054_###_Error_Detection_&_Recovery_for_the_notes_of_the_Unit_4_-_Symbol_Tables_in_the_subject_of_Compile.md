### Error Detection & Recovery

Errors can occur in the various phases of the compilation process. Error detection and recovery are important aspects of the design of a compiler. The compiler must be able to detect and report errors in the source code and must also be able to recover from some errors and continue processing the rest of the source code.

#### Error Detection

Errors can be classified into two types: 

- **Syntactic errors**: These are errors that are detected during the parsing phase of the compiler when the source code is being converted into a parse tree or an abstract syntax tree. Syntactic errors occur when the source code violates the grammar rules of the programming language.

- **Semantic errors**: These are errors that are detected during the semantic analysis phase of the compiler. Semantic errors occur when the source code violates the semantics or meaning of the programming language. Examples of semantic errors include type errors, undeclared variables, and out-of-bounds array access.

#### Error Recovery

When an error is detected, the compiler must report the error to the user and attempt to recover from the error. Error recovery techniques can be classified into three types:

- **Panic Mode Recovery**: In this technique, the parser discards input symbols until it finds a token that can be used as a synchronization point. The parser then resumes parsing from that point. This technique is simple and efficient but can lead to cascading errors.

- **Phrase-Level Recovery**: In this technique, the parser discards input symbols until it finds a token that can be used as a synchronization point. The parser then resumes parsing from the beginning of the next phrase. This technique is more sophisticated than panic mode recovery but requires more memory and computation.

- **Error Productions**: In this technique, the grammar of the programming language is augmented with special error productions. These productions are used to recover from errors by generating a valid parse tree or abstract syntax tree even if the source code contains errors. This technique is the most sophisticated but requires significant effort to design and implement.

#### Advantages of Error Recovery

- Error recovery allows the compiler to continue processing the source code even if errors are present. This can save time and effort for the programmer.

- Error recovery can help to identify multiple errors in the source code rather than stopping at the first error.

- Error recovery techniques can be customized for different programming languages and different types of errors.

#### Disadvantages of Error Recovery

- Error recovery can lead to incorrect output or unexpected behavior if the error recovery technique is not designed properly.

- Error recovery can be computationally expensive and can slow down the compilation process.

- Error recovery techniques can be difficult to design and implement, requiring significant effort and expertise.

#### Example

Consider the following C++ code:

```c++
int main() {
    int x = 5;
    int y = "hello";
    int z = x + y;
    return 0;
}
```

This code contains three errors: a type error on line 3, a syntax error on line 4, and a semantic error on line 5. The compiler can use error recovery techniques to report all three errors to the user and continue processing the rest of the source code.

#### Applications

Error detection and recovery are important for any compiler or interpreter that processes source code. They are also important for other software tools that process input data, such as parsers and data validators.