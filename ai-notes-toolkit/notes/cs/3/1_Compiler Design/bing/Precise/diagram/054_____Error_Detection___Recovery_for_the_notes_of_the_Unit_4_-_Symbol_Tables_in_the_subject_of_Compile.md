### Error Detection & Recovery

Error detection and recovery are important aspects of compiler design. In the context of Unit 4 - Symbol Tables, error detection refers to the process of identifying errors in the source code related to the use of symbols, such as undeclared variables or incorrect data types. Recovery refers to the process of handling these errors in a way that allows the compiler to continue processing the source code.

Some common techniques for error detection and recovery in symbol tables include:

1. **Syntax-directed error recovery**: This technique involves using the grammar of the programming language to detect errors. For example, if the grammar specifies that a variable must be declared before it is used, the compiler can detect an error if it encounters a variable that has not been declared.

2. **Error productions**: Error productions are special rules in the grammar that allow the compiler to recover from certain errors. For example, an error production might specify that if the compiler encounters an undeclared variable, it should insert a declaration for that variable and continue processing.

3. **Panic mode recovery**: In panic mode recovery, the compiler discards input symbols until it reaches a synchronization point, such as a semicolon or a closing brace. This allows the compiler to continue processing the source code, but it may result in the loss of some information.

4. **Phrase level recovery**: Phrase level recovery involves replacing an incorrect portion of the source code with a correct one. This can be done by inserting, deleting, or modifying symbols in the source code.

These are some of the techniques used for error detection and recovery in symbol tables. It is important to note that the specific techniques used may vary depending on the programming language and the design of the compiler.