### File Handling: File I/O Functions, Standard C Preprocessors, Defining and Calling Macros and Command-Line Arguments

#### File I/O Functions
- `fopen`: Opens a file for reading, writing, or appending.
- `fclose`: Closes a file.
- `fread`: Reads data from a file.
- `fwrite`: Writes data to a file.
- `fseek`: Sets the file position indicator for the stream.
- `ftell`: Returns the current value of the file position indicator for the stream.
- `rewind`: Sets the file position indicator to the beginning of the file.

#### Standard C Preprocessors
- `#define`: Defines a macro.
- `#include`: Includes a header file.
- `#ifdef`: Checks if a macro is defined.
- `#ifndef`: Checks if a macro is not defined.
- `#if`: Tests if a compile-time condition is true.
- `#else`: Specifies a block of code to be executed if the condition tested by `#if` is false.
- `#endif`: Ends a conditional block started by `#if`, `#ifdef`, or `#ifndef`.

#### Defining and Calling Macros
- A macro is a fragment of code that is given a name.
- Macros are defined using the `#define` preprocessor directive.
- When a macro is called, the preprocessor replaces the macro call with the macro definition.
- Macros can take arguments, which are specified in parentheses after the macro name.

#### Command-Line Arguments
- Command-line arguments are passed to the main function of a C program.
- The first argument, `argv[0]`, is the name of the program.
- The remaining arguments are the command-line arguments.
- The number of command-line arguments is stored in the `argc` variable.