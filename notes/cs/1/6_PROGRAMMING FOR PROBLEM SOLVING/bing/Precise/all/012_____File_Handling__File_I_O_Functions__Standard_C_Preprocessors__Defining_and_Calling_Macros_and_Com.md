### File Handling: File I/O Functions, Standard C Preprocessors, Defining and Calling Macros and Command-Line Arguments

#### File I/O Functions
- File I/O functions are used to perform input/output operations on files.
- Some common file I/O functions in C are `fopen()`, `fclose()`, `fread()`, `fwrite()`, `fseek()`, `ftell()`, and `rewind()`.
- `fopen()` is used to open a file. It returns a pointer to the file stream associated with the file.
- `fclose()` is used to close a file. It returns zero if the file is successfully closed.
- `fread()` is used to read data from a file. It returns the number of items successfully read.
- `fwrite()` is used to write data to a file. It returns the number of items successfully written.
- `fseek()` is used to set the file position indicator to a specific location in the file.
- `ftell()` is used to get the current position of the file position indicator.
- `rewind()` is used to set the file position indicator to the beginning of the file.

#### Standard C Preprocessors
- The C preprocessor is a macro processor that is used to transform the source code before it is compiled.
- Some common C preprocessor directives are `#define`, `#include`, `#ifdef`, `#ifndef`, `#if`, `#else`, `#elif`, and `#endif`.
- `#define` is used to define a macro.
- `#include` is used to include a header file.
- `#ifdef` is used to check if a macro is defined.
- `#ifndef` is used to check if a macro is not defined.
- `#if` is used to test if a condition is true.
- `#else` is used to provide an alternative if the condition is false.
- `#elif` is used to test another condition if the previous condition is false.
- `#endif` is used to mark the end of a conditional block.

#### Defining and Calling Macros
- A macro is a fragment of code that is given a name.
- Macros are defined using the `#define` directive.
- When a macro is called, the preprocessor replaces the macro call with the macro definition.
- Macros can take arguments, which are specified in parentheses after the macro name.
- When a macro with arguments is called, the arguments are substituted into the macro definition.

#### Command-Line Arguments
- Command-line arguments are arguments that are passed to a program when it is invoked from the command line.
- In C, command-line arguments are passed to the `main()` function as arguments.
- The first argument, `argv[0]`, is the name of the program.
- The remaining arguments, `argv[1]` to `argv[argc-1]`, are the command-line arguments.
- `argc` is the number of command-line arguments, including the program name.