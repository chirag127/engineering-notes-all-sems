### Programming Basics: Structure of C Program, Writing and Executing the First C Program, Syntax and Logical Errors in Compilation, Object and Executable Code

#### Structure of C Program
- A C program consists of one or more functions.
- The function named `main` is the starting point of the program.
- Each function contains a sequence of statements enclosed in curly braces `{}`.
- The statements are executed in the order in which they appear in the function.
- A C program can also contain preprocessor directives, which are instructions to the C preprocessor.
- Preprocessor directives begin with a `#` symbol and are processed before the program is compiled.

#### Writing and Executing the First C Program
1. Open a text editor and type in the following code:
```
#include <stdio.h>

int main()
{
    printf("Hello, World!\n");
    return 0;
}
```
2. Save the file with a `.c` extension, such as `hello.c`.
3. Open a command prompt or terminal window and navigate to the directory where the file was saved.
4. Type the command `gcc hello.c` to compile the program using the GNU C Compiler.
5. If the program compiled successfully, an executable file named `a.out` (on Linux or macOS) or `a.exe` (on Windows) will be created.
6. Type the command `./a.out` (on Linux or macOS) or `a` (on Windows) to run the program.
7. The program should output the text `Hello, World!`.

#### Syntax and Logical Errors in Compilation
- Syntax errors are mistakes in the program's source code that prevent it from being compiled.
- Common syntax errors include missing semicolons, mismatched parentheses or braces, and misspelled keywords.
- Logical errors are mistakes in the program's logic that cause it to produce incorrect results.
- Logical errors can be difficult to find because the program may compile and run without any errors, but the output will not be what was expected.
- To find and fix logical errors, it is helpful to use a debugger to step through the program's execution and examine the values of variables.

#### Object and Executable Code
- When a C program is compiled, the compiler translates the source code into object code, which is a low-level representation of the program in machine language.
- The object code is stored in an object file, which has a `.o` extension on Linux and macOS, or a `.obj` extension on Windows.
- The linker combines one or more object files and any required libraries into an executable file, which can be run on the computer.
- The executable file contains the machine code instructions that the computer's processor can execute directly.