### Program structure for the notes of the Unit 4 - C++ Basics in the subject of Object Oriented System Design

- A C++ program is a collection of commands, which tell the computer to do something.
- The basic structure of a C++ program includes the following elements:
  - Preprocessor directives: These are lines included in the code of programs preceded by a hash sign (#). They are used to make the source code more readable and to include libraries.
  - Namespace declaration: This is used to avoid name conflicts between different libraries.
  - Main function: This is the entry point of the program, where the execution of the program begins.
  - Statements and expressions: These are the instructions that are executed by the program.
  - Comments: These are used to explain the code and make it more readable. They are ignored by the compiler.
- The basic structure of a C++ program can be illustrated as follows:

```
// Preprocessor directives
#include <iostream>
using namespace std;

// Main function
int main()
{
    // Statements and expressions
    cout << "Hello, World!" << endl;
    return 0;
}
```

- The above program includes the `iostream` library, which is used for input and output operations.
- The `using namespace std;` line is used to avoid having to write `std::` before every standard library function.
- The `main` function is where the execution of the program begins. In this case, it outputs the text "Hello, World!" to the standard output stream.
- The `return 0;` line indicates that the program has executed successfully.
- The `//` characters are used to indicate a comment. Everything after these characters on the same line is ignored by the compiler.