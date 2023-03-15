# Programming Basics: Structure of C Program, Writing and Executing the First C Program, Syntax and Logical Errors in Compilation, Object and Executable Code

## Structure of C Program
- A C program consists of one or more functions, which are blocks of code that perform a specific task.
- The main function is the starting point of the program, where the execution begins.
- The main function can call other functions, which can call other functions, and so on, forming a hierarchy of function calls.
- A function has a name, a list of parameters, and a body that contains the statements to execute.
- A function can return a value to the caller using the return statement.
- A C program can also have global variables, which are declared outside any function and can be accessed by any function in the program.
- A C program can also have preprocessor directives, which are instructions to the compiler that are processed before the actual compilation.
- Some common preprocessor directives are #include, which tells the compiler to include another file in the program, and #define, which defines a constant or a macro.
- A C program can also have comments, which are ignored by the compiler and are used to explain the code or add notes.
- Comments can be either single-line, starting with //, or multi-line, enclosed by /* and */.

## Writing and Executing the First C Program
- To write a C program, you need a text editor, such as Notepad, and a compiler, such as GCC or Visual Studio.
- A C program is usually saved with a .c extension, such as hello.c.
- A simple C program that prints "Hello, world!" to the standard output is shown below:

```c
// This is a comment
#include <stdio.h> // This is a preprocessor directive that includes the standard input/output library
int main() // This is the main function
{
    printf("Hello, world!\n"); // This is a statement that calls the printf function
    return 0; // This is a statement that returns 0 to the operating system
}
```

- To execute a C program, you need to compile it first, which converts the source code into an executable file that can be run by the computer.
- The compilation process can vary depending on the compiler and the operating system, but a common way to compile a C program on a Linux or Mac terminal is:

```bash
gcc hello.c -o hello
```

- This command tells the GCC compiler to compile the hello.c file and produce an executable file named hello.
- To run the executable file, you can type:

```bash
./hello
```

- This command tells the operating system to execute the hello file in the current directory.
- The output of the program should be:

```bash
Hello, world!
```

## Syntax and Logical Errors in Compilation
- A syntax error is a mistake in the grammar or spelling of the C language, such as a missing semicolon, a mismatched parenthesis, or an invalid keyword.
- A syntax error prevents the compiler from understanding the program and generating the executable file.
- The compiler will report the syntax error and indicate the line number and the position where the error occurred.
- For example, if we forget the semicolon at the end of the printf statement in the hello.c program, the compiler will give an error message like:

```bash
hello.c: In function ‘main’:
hello.c:5:5: error: expected ‘;’ before ‘return’
     return 0;
     ^~~~~~
     ;
```

- A logical error is a mistake in the logic or algorithm of the program, such as a wrong calculation, a wrong condition, or a wrong loop.
- A logical error does not prevent the compiler from generating the executable file, but it causes the program to produce incorrect or unexpected results.
- A logical error is harder to detect and fix than a syntax error, because it requires debugging, which is the process of finding and correcting errors in the program.
- Debugging can be done using various tools, such as print statements, breakpoints, or debuggers, which allow the programmer to examine the values of variables, the flow of execution, and the output of the program.
- For example, if we want to write a C program that calculates the area of a circle given its radius, but we use the wrong formula, we will have a logical error. The correct formula is:

```c
area = pi * radius * radius
```

- But if we use:

```c
area = 2 * pi * radius
```

- The compiler will not report any error, but the program will produce wrong results. For example, if the radius is 5, the correct area