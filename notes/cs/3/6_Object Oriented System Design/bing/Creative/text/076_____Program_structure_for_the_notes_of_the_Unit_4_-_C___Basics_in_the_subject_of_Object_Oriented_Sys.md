Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Program structure for the Unit 4 - C++ Basics in the subject of Object Oriented System Design. Here is the content I have generated for you:

### Program structure

- A C++ program consists of one or more source files, which are also called translation units.
- A source file contains a sequence of declarations and definitions, which are the basic units of the C++ language.
- A declaration introduces a name into the program and specifies its type and properties, such as `int x;` or `void f();`.
- A definition provides the complete information about a name, such as its value, size, or body, such as `int x = 42;` or `void f() { ... }`.
- A declaration can also be a definition, but not vice versa. For example, `int x;` is both a declaration and a definition, but `extern int x;` is only a declaration.
- A source file can also include directives, which are instructions to the compiler or the preprocessor, such as `#include <iostream>` or `#define PI 3.14`.
- A source file can also contain comments, which are ignored by the compiler and are used to document or explain the code, such as `// This is a single-line comment` or `/* This is a multi-line comment */`.
- A C++ program is executed by starting from the main function, which has the signature `int main()` or `int main(int argc, char* argv[])`.
- The main function can call other functions, which can be defined in the same source file or in other source files.
- The main function can also use variables, constants, and objects, which can be defined in the same source file or in other source files.
- The main function can also use standard library functions and classes, which are defined in header files that are included by the `#include` directive.
- The main function can also use user-defined types, such as classes, structs, enums, and unions, which can be defined in the same source file or in other source files.
- The main function can also use templates, which are generic definitions of functions or classes that can be instantiated with different types, such as `template <typename T> T max(T a, T b) { ... }`.
- The main function can also use exceptions, which are special objects that are thrown and caught to handle errors or abnormal situations, such as `throw std::runtime_error("Something went wrong");` or `catch (std::exception& e) { ... }`.
- The main function can also use namespaces, which are named scopes that group related names and avoid name conflicts, such as `namespace std { ... }` or `using namespace std;`.
- The main function returns an integer value, which indicates the status of the program execution, such as `return 0;` for success or `return -1;` for failure.