### File Handling: File I/O Functions, Standard C Preprocessors, Defining and Calling Macros and Command-Line Arguments

- File handling is the process of creating, reading, writing, updating and deleting files using a programming language such as C.
- File I/O functions are the functions that allow a program to perform input and output operations on files. Some of the common file I/O functions in C are:
  - fopen(): opens a file and returns a pointer to it.
  - fclose(): closes a file and frees the resources associated with it.
  - fprintf(): writes formatted data to a file.
  - fscanf(): reads formatted data from a file.
  - fread(): reads a block of data from a file.
  - fwrite(): writes a block of data to a file.
  - fseek(): moves the file pointer to a specified position in a file.
  - ftell(): returns the current position of the file pointer in a file.
  - rewind(): moves the file pointer to the beginning of a file.
- Standard C preprocessors are directives that are processed before the compilation of a C program. They can be used to include header files, define macros, conditionally compile code, etc. Some of the common standard C preprocessors are:
  - #include: includes the contents of another file in the current file.
  - #define: defines a macro that can be used as a shorthand for a constant or an expression.
  - #undef: undefines a macro that was previously defined.
  - #if, #elif, #else, #endif: controls the conditional compilation of code blocks based on the evaluation of expressions.
  - #ifdef, #ifndef: checks whether a macro is defined or not and executes the code accordingly.
  - #error: generates a compile-time error message.
  - #pragma: provides compiler-specific instructions.
- Defining and calling macros is a way of creating reusable code snippets that can be substituted by the preprocessor wherever they are used. A macro can be defined using the #define directive, followed by the macro name and the replacement text. For example:

  ```
  #define PI 3.14 // defines a macro named PI with the value 3.14
  #define SQUARE(x) ((x) * (x)) // defines a macro named SQUARE with a parameter x and the expression (x) * (x) as the replacement text
  ```

  A macro can be called by using its name followed by the optional arguments in parentheses. For example:

  ```
  printf("The value of PI is %f\n", PI); // prints the value of PI
  printf("The square of 5 is %d\n", SQUARE(5)); // prints the square of 5
  ```

- Command-line arguments are the arguments that are passed to a program when it is executed from the command line. They can be used to provide input data, options, flags, etc. to the program. Command-line arguments are stored in an array of strings called argv, and the number of arguments is stored in an integer variable called argc. The first argument in argv is always the name of the program. For example, if a program is executed as:

  ```
  ./myprog arg1 arg2 arg3
  ```

  Then, the values of argc and argv are:

  ```
  argc = 4
  argv = {"./myprog", "arg1", "arg2", "arg3"}
  ```

  Command-line arguments can be accessed and manipulated by using the argv array and the argc variable in the main function of the program. For example:

  ```
  #include <stdio.h>
  int main(int argc, char *argv[])
  {
    printf("The name of the program is %s\n", argv[0]); // prints the name of the program
    printf("The number of arguments is %d\n", argc); // prints the number of arguments
    for (int i = 1; i < argc; i++)
    {
      printf("The argument %d is %s\n", i, argv[i]); // prints each argument
    }
    return 0;
  }
  ```