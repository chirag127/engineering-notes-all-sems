Hello, I am Sydney, your AI assistant. I can help you with your study material for Object Oriented System Design. Here is the content for the topic of constants in C++ Basics.

### Constants

- Constants are fixed values that do not change during the execution of a program.
- Constants can be of any basic data type, such as int, char, float, double, bool, etc.
- Constants can be declared using the keyword `const` before the data type and the identifier.
- For example, `const int PI = 3.14;` declares a constant named PI of type int with the value 3.14.
- Constants can also be declared using the `#define` preprocessor directive, which replaces all occurrences of the identifier with the value in the source code before compilation.
- For example, `#define PI 3.14` defines a constant named PI with the value 3.14.
- The advantages of using constants are:
  - They improve the readability and maintainability of the code by giving meaningful names to fixed values.
  - They avoid the use of magic numbers or hard-coded values that can cause errors or confusion.
  - They make the code more consistent and easier to debug and modify.
- The disadvantages of using constants are:
  - They occupy memory space and may increase the size of the executable file.
  - They may cause name conflicts or redefinition errors if the same identifier is used for different values in different scopes or files.
  - They may limit the flexibility and functionality of the code if the values need to be changed or updated at runtime.