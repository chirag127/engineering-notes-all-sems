## Unit 1 - Introduction to Compiler

A compiler is a computer program that translates source code written in a high-level programming language (such as C, Java, Python, etc.) into a low-level language (such as machine code, assembly, bytecode, etc.) that can be executed by a computer or another device  .

The main purpose of a compiler is to make the source code understandable and executable by the target machine or platform. A compiler also performs various tasks such as error checking, optimization, code generation, and linking.

There are many types of compilers, depending on the source and target languages, the operating systems, the architectures, and the compilation methods. Some of the common types of compilers are :

- Cross compiler: A compiler that produces code for a different CPU or operating system than the one on which the compiler runs. For example, a cross compiler can compile a C program written on a Windows machine into an executable file that can run on a Linux machine.
- Source-to-source compiler: Also known as a transcompiler, it translates source code written in one programming language into source code of another programming language. For example, a source-to-source compiler can convert a Python program into a Java program.
- Just-in-time (JIT) compiler: A compiler that defers compilation until runtime. It compiles the source code or an intermediate representation into machine code on the fly, as the program is executed. For example, a JIT compiler can compile Java bytecode into native machine code when a Java program is run.
- Bootstrap compiler: A compiler that is written in the same programming language that it compiles. For example, a bootstrap compiler can compile a C program written in C into an executable file. A bootstrap compiler is often used to create a more permanent or optimized compiler for a language.

The process of compilation involves several phases, each of which performs a specific task on the source code or an intermediate representation. The typical phases of a compiler are:

- Preprocessing: This phase performs tasks such as removing comments, expanding macros, including header files, and resolving directives in the source code.
- Lexical analysis: This phase converts the source code into a sequence of tokens, which are the smallest meaningful units of the language, such as keywords, identifiers, literals, operators, etc.
- Parsing: This phase analyzes the syntactic structure of the token sequence and builds a parse tree, which is a hierarchical representation of the program's grammar.
- Semantic analysis: This phase performs tasks such as type checking, scope resolution, and symbol table construction, which ensure that the program is semantically correct and meaningful.
- Intermediate code generation: This phase converts the parse tree into an intermediate representation, which is a low-level, platform-independent code that is closer to the target machine language.
- Code optimization: This phase applies various techniques to improve the quality and efficiency of the intermediate code, such as eliminating dead code, reducing redundancy, simplifying expressions, etc.
- Code generation: This phase translates the optimized intermediate code into the target machine code, which can be executed by the computer or the device.
- Linking: This phase combines the generated machine code with other libraries or modules that are required for the program's execution.