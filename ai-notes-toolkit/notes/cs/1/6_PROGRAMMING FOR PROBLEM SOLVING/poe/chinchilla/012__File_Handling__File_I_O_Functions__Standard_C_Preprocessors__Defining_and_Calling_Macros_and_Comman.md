### File Handling: File I/O Functions, Standard C Preprocessors, Defining and Calling Macros and Command-Line Arguments.

File Handling:

- File Handling is a process of reading from or writing to a file.
- In C programming language, file handling is done using in-built functions and structures. 
- The file handling functions can be used to open, read, write, and close files.

File I/O Functions:

- File I/O functions are used to perform operations on files in C programming.
- The following are some of the commonly used file I/O functions in C programming:
    - fopen() - used to open a file.
    - fclose() - used to close a file.
    - fread() - used to read data from a file.
    - fwrite() - used to write data to a file.
    - fseek() - used to set the file position indicator.
    - ftell() - used to get the current position of the file pointer.
    
Standard C Preprocessors:

- Preprocessors are a set of directives that are used to modify the source code before it is compiled.
- In C programming, the preprocessor directives begin with a hash (#) symbol.
- The following are some of the commonly used preprocessor directives in C programming:
    - #define - used to define a macro.
    - #include - used to include a header file.
    - #ifdef - used to check if a macro is defined.
    - #ifndef - used to check if a macro is not defined.
    - #endif - used to end a conditional block.
    
Defining and Calling Macros:

- A macro is a fragment of code that is given a name and is replaced by its definition at compile time.
- Macros are defined using the #define preprocessor directive.
- The following is an example of defining a macro:

    ```
    #define PI 3.14159
    ```

- Macros can be called in the code using their names.
- The following is an example of calling a macro:

    ```
    float area = PI * radius * radius;
    ```

Command-Line Arguments:

- Command-line arguments are the arguments passed to a program when it is executed from the command line.
- In C programming language, the main() function can take two arguments: argc and argv.
- The argc argument is an integer that represents the number of arguments passed to the program.
- The argv argument is an array of strings that represents the arguments passed to the program.
- The following is an example of using command-line arguments in C programming:

    ```
    int main(int argc, char *argv[])
    {
        printf("The program name is %s\n", argv[0]);
        printf("The first argument is %s\n", argv[1]);
        printf("The second argument is %s\n", argv[2]);
        return 0;
    }
    ```