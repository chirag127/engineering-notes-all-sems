### Program structure

- A C++ program consists of one or more source files, which are also called translation units.
- A source file contains a sequence of characters organized into lines, and a line contains a sequence of tokens.
- A token is the smallest unit of a program that has a meaning, such as a keyword, an identifier, a literal, an operator, or a punctuation symbol.
- A source file can be divided into three sections: preprocessor directives, global declarations, and function definitions.
- Preprocessor directives are instructions to the preprocessor, which is a program that processes the source file before the compiler. They begin with a # symbol and end with a newline character. They are used to include header files, define macros, or control conditional compilation.
- Global declarations are declarations of variables, constants, types, or functions that have a global scope, meaning they can be accessed from any part of the program. They are usually placed at the beginning of the source file, after the preprocessor directives.
- Function definitions are the implementations of the functions that are declared in the global section or in a header file. They consist of a function header, which specifies the name, parameters, and return type of the function, and a function body, which contains the statements that perform the task of the function. They are usually placed at the end of the source file, after the global declarations.
- A C++ program must have at least one function, which is the main function. The main function is the entry point of the program, where the execution begins. It has the following syntax:

```cpp
int main()
{
  // statements
  return 0;
}
```

- The main function can also take command-line arguments, which are passed to the program when it is invoked from the terminal. In that case, the syntax is:

```cpp
int main(int argc, char* argv[])
{
  // statements
  return 0;
}
```

- The argc parameter is the number of arguments, and the argv parameter is an array of pointers to the arguments. The first argument is always the name of the program.
- The return statement in the main function indicates the exit status of the program. A return value of 0 means the program terminated normally, and any other value means the program encountered an error.
- A C++ program can also have other functions, which are called by the main function or by other functions. A function can be defined in the same source file where it is called, or in a different source file. In the latter case, the function must be declared in the source file where it is called, or in a header file that is included by that source file. A function declaration has the same syntax as the function header, but without the function body. It ends with a semicolon. For example:

```cpp
// function declaration
void printHello();

// function definition
void printHello()
{
  cout << "Hello, world!" << endl;
}
```

- A function can also have a prototype, which is a function declaration that specifies the types of the parameters and the return type of the function. A prototype is useful to check the compatibility of the function definition and the function call, and to avoid implicit conversions of the arguments. A prototype has the same syntax as the function declaration, but with the parameter names omitted. For example:

```cpp
// function prototype
void printHello();

// function declaration
void printHello();

// function definition
void printHello()
{
  cout << "Hello, world!" << endl;
}
```

- A function can also be overloaded, which means that there can be more than one function with the same name, but with different parameters or return types. The compiler determines which function to call based on the number and types of the arguments. For example:

```cpp
// function prototypes
void print(int x);
void print(double x);
void print(char x);

// function definitions
void print(int x)
{
  cout << "Integer: " << x << endl;
}

void print(double x)
{
  cout << "Double: " << x << endl;
}

void print(char x)
{
  cout << "Character: " << x << endl;
}
```

- A function can also be recursive, which means that it can call itself, either directly or indirectly. A recursive function must have a base case, which is a condition that stops the recursion, and a recursive case, which is a condition that continues the recursion. For example:

```cpp
// function prototype
int factorial(int n);

// function definition
int factorial(int n)
{
  // base case
  if (n == 0 || n == 1)
    return 1;
  // recursive case
  else
    return n