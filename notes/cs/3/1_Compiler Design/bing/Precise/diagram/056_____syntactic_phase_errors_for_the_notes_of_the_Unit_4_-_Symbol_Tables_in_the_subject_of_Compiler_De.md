# Unit 4 - Symbol Tables: Syntactic Phase Errors

Syntactic phase errors are detected during the syntax analysis phase of the compiler design process. Syntax analysis is all about discovering structure in text. The general syntax errors are structural errors.

There are several methods for recovering from syntactic phase errors, including:

1. **Panic Mode Recovery**: In this method, successive characters from the input are removed one at a time until a designated set of synchronizing tokens is found.
2. **Statement Mode Recovery**: In this method, when a parser encounters an error, it performs the necessary correction on the remaining input and then continues parsing.
3. **Error Productions**: Syntactic phase errors are generally recovered by error productions. However, this method is very difficult to maintain because if the grammar changes, it becomes necessary to change the corresponding production. It is also difficult to maintain by the developers.

It is important to note that errors may occur in all phases of the compiler design process, including the lexical analyzer, intermediate code generator, and code optimizer.