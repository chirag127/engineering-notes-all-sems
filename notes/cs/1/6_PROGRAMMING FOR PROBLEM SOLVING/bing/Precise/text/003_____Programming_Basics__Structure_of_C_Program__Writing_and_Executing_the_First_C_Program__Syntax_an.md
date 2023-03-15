### Programming Basics: Structure of C Program, Writing and Executing the First C Program, Syntax and Logical Errors in Compilation, Object and Executable Code

1. **Structure of C Program:** A C program consists of one or more functions, with the main function being the entry point of the program. Each function contains a set of statements that perform a specific task. A typical C program has the following structure:
```
#include <stdio.h>
int main()
{
    // statements
    return 0;
}
```
The `#include` directive is used to include the contents of the `stdio.h` header file, which contains the declarations of standard input/output functions such as `printf` and `scanf`. The `main` function is where the execution of the program begins. The `return 0;` statement indicates that the program has executed successfully.

2. **Writing and Executing the First C Program:** To write a C program, you need a text editor to create a source file with a `.c` extension. The source file contains the C code that you write. Once you have written the code, you can compile it using a C compiler, which translates the source code into machine code that the computer can understand and execute. After the program is compiled, you can run it to see the output.

3. **Syntax and Logical Errors in Compilation:** During the compilation process, the compiler checks the source code for syntax errors, which are mistakes in the use of the C language. If the compiler finds any syntax errors, it will generate error messages and stop the compilation process. Logical errors, on the other hand, are mistakes in the program's logic that cause it to produce incorrect results. Logical errors do not prevent the program from compiling, but they can be difficult to find and fix.

4. **Object and Executable Code:** After the source code is compiled, the compiler generates an object file, which contains the machine code for the program. The object file is then linked with other object files and libraries to create the final executable code, which can be run on the computer. The executable code is stored in a file with an `.exe` extension on Windows or with no extension on Unix-like systems.