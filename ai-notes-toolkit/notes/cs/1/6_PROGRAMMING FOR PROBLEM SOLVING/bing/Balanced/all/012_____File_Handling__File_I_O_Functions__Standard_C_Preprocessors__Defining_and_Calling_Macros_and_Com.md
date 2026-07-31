# File Handling: File I/O Functions, Standard C Preprocessors, Defining and Calling Macros and Command-Line Arguments

File handling is the process of manipulating files in a computer system using a programming language. Files are containers that store data in a persistent and organized way. In C, files can be opened, read, written and closed using various functions provided by the standard library.

## File I/O Functions

Some of the common file I/O functions in C are:

- `fopen(filename, mode)`: Opens a file with the given name and mode. The mode can be "r" for reading, "w" for writing, "a" for appending, "r+" for reading and writing, "w+" for writing and reading (overwrites existing file), "a+" for appending and reading. Returns a pointer to the file object or NULL if the file cannot be opened.
- `fclose(file)`: Closes the file pointed by the file object and frees the memory allocated for it. Returns zero on success or EOF on failure.
- `fgetc(file)`: Reads the next character from the file and returns it as an int. Returns EOF if the end of file is reached or an error occurs.
- `fputc(c, file)`: Writes the character c to the file and returns it as an int. Returns EOF if an error occurs.
- `fgets(str, n, file)`: Reads at most n-1 characters from the file and stores them in the string str. Appends a null character at the end of the string. Returns str on success or NULL on failure or end of file.
- `fputs(str, file)`: Writes the string str to the file and returns a non-negative value on success or EOF on failure.
- `fread(buffer, size, count, file)`: Reads count elements of size bytes each from the file and stores them in the buffer. Returns the number of elements read or a smaller value if an error or end of file occurs.
- `fwrite(buffer, size, count, file)`: Writes count elements of size bytes each to the file from the buffer. Returns the number of elements written or a smaller value if an error occurs.
- `fseek(file, offset, origin)`: Moves the file position indicator to the specified offset relative to the origin. The origin can be SEEK_SET (beginning of file), SEEK_CUR (current position) or SEEK_END (end of file). Returns zero on success or a non-zero value on failure.
- `ftell(file)`: Returns the current position of the file position indicator as a long int or -1 on failure.
- `rewind(file)`: Sets the file position indicator to the beginning of the file.
- `feof(file)`: Returns a non-zero value if the end of file has been reached or zero otherwise.
- `ferror(file)`: Returns a non-zero value if an error has occurred or zero otherwise.
- `clearerr(file)`: Clears the end-of-file and error indicators for the file.

## Standard C Preprocessors

Preprocessors are directives that instruct the compiler to perform certain tasks before the actual compilation of the source code. They start with a # symbol and are usually placed at the beginning of the file. Some of the standard C preprocessors are:

- `#include <filename>`: Includes the contents of another file in the current file. The filename can be enclosed in angle brackets (<>) for standard library files or in double quotes ("") for user-defined files.
- `#define name value`: Defines a macro with the given name and value. The value can be a constant, an expression or a function-like macro. The name can be used as a replacement for the value in the source code.
- `#undef name`: Undefines a macro with the given name. The name can no longer be used as a replacement for the value in the source code.
- `#ifdef name`: Checks if a macro with the given name is defined. If yes, the following code until the next #endif or #else is executed. If no, the following code is skipped.
- `#ifndef name`: Checks if a macro with the given name is not defined. If yes, the following code until the next #endif or #else is executed. If no, the following code is skipped.
- `#else`: Marks the alternative branch for the preceding #ifdef or #ifndef. The following code until the next #endif is executed if the condition for the preceding #ifdef or #ifndef is false.
- `#endif`: Marks the end of a conditional block started by #ifdef or #ifndef