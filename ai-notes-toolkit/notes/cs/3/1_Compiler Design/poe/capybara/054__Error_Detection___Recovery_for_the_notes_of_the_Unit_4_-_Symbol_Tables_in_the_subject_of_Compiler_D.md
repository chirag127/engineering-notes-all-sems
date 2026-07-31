### Error Detection & Recovery

Error detection and recovery are crucial components in the design and implementation of a compiler. In this unit, we will explore the different techniques used for detecting and recovering from errors in symbol tables.

#### Error Detection Techniques

The following are some of the commonly used error detection techniques in symbol tables:

- **Lexical Analysis**: This technique involves identifying the lexemes in the input program and checking if they conform to the rules of the language. If a lexeme does not match any of the language rules, it is flagged as an error.

- **Syntax Analysis**: Syntax analysis involves checking if the input program conforms to the grammar rules of the language. If the input program violates any of the grammar rules, it is flagged as an error.

- **Semantic Analysis**: Semantic analysis checks if the input program conforms to the semantics of the language. It ensures that the input program makes sense and does not violate any of the language rules.

#### Error Recovery Techniques

Once an error is detected, the compiler needs to recover from the error and continue parsing the input program. The following are some of the commonly used error recovery techniques:

- **Panic Mode**: In panic mode recovery, the parser discards input tokens until it finds a token that can be used as a synchronizing token to continue parsing. This technique is fast but can result in many syntax errors being reported.

- **Phrase-Level Recovery**: In phrase-level recovery, the parser discards input tokens until it finds a token that can be used to start a new phrase. This technique is slower than panic mode but can result in fewer syntax errors being reported.

- **Error Production**: In error production, the parser inserts a missing token into the input program and continues parsing. This technique is slow and can result in many syntax errors being reported.

#### Conclusion

Error detection and recovery are critical components in the design and implementation of a compiler. By using the techniques discussed in this unit, the compiler can detect and recover from errors, ensuring that the input program is parsed correctly.