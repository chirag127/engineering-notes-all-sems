Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of program structure for the notes of the Unit 4 - C++ Basics in the subject of Object Oriented System Design.

# Program structure

- A C++ program consists of one or more source files, which are also called translation units.
- A source file contains a sequence of characters that are grouped into tokens, such as keywords, identifiers, literals, operators, and punctuators.
- A source file is divided into two parts: a preamble and a body.
- The preamble consists of preprocessor directives, such as `#include` and `#define`, that instruct the compiler to perform certain actions before compiling the source code.
- The body consists of one or more declarations and definitions, which specify the types, variables, constants, functions, classes, and objects used in the program.
- A declaration introduces a name and its type to the compiler, but does not allocate any memory or provide any implementation details. For example, `int x;` is a declaration of a variable named `x` of type `int`.
- A definition provides the implementation details of a name that has been declared, such as its initial value, memory allocation, or function body. For example, `int x = 10;` is a definition of a variable named `x` of type `int` with an initial value of `10`.
- A definition is also a declaration, but a declaration is not necessarily a definition. A name can be declared multiple times, but defined only once in a program.
- A source file can contain multiple declarations and definitions, but they must follow certain rules of order and scope.
- The order of declarations and definitions determines the visibility and accessibility of names within a source file. A name must be declared before it can be used, unless it is a built-in type or keyword. A name can be redeclared or redefined in different scopes, but it may cause ambiguity or conflict if not done carefully.
- The scope of a name is the region of the source code where the name is valid and can be referred to. There are different kinds of scopes in C++, such as global scope, namespace scope, class scope, function scope, block scope, and function parameter scope. Each scope has its own rules and limitations for declaring and defining names.
- A source file can also contain comments, which are ignored by the compiler and are used to document or explain the code. Comments can be either single-line comments, starting with `//`, or multi-line comments, enclosed by `/*` and `*/`.
- A source file must end with a newline character, which is usually represented by pressing the Enter key.