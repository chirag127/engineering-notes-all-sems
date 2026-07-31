### Strings: Length, Concatenation, Repeat, Indexing, and Slicing

- **Length**: The length of a string can be determined using the `len()` function. For example, `len("hello")` returns `5`.
- **Concatenation**: Two or more strings can be combined into a single string using the `+` operator. For example, `"hello" + "world"` returns `"helloworld"`.
- **Repeat**: A string can be repeated a specified number of times using the `*` operator. For example, `"hello" * 3` returns `"hellohellohello"`.
- **Indexing**: Individual characters in a string can be accessed using indexing. For example, `"hello"[0]` returns `"h"`. Negative indexing can also be used to access characters from the end of the string. For example, `"hello"[-1]` returns `"o"`.
- **Slicing**: A substring of a string can be extracted using slicing. For example, `"hello"[1:4]` returns `"ell"`. The start and end indices can be omitted to slice from the beginning or to the end of the string, respectively. For example, `"hello"[:3]` returns `"hel"` and `"hello"[3:]` returns `"lo"`.

### Unit 3 - Functions: Parts, Execution, Keyword and Default Arguments, Scope Rules

- **Parts of a Function**: A function in Python consists of a `def` statement, a function name, parameters, a colon, and an indented block of code.
- **Execution of a Function**: A function is executed by calling it using its name followed by parentheses containing any arguments. For example, `my_function(arg1, arg2)`.
- **Keyword and Default Arguments**: Arguments can be passed to a function using either positional or keyword arguments. Default values can be specified for arguments using the `=` operator in the function definition. For example, `def my_function(arg1, arg2="default")`.
- **Scope Rules**: Variables defined within a function have local scope and are not accessible outside the function. Variables defined outside a function have global scope and are accessible within the function. The `global` keyword can be used to modify a global variable from within a function.
