# Strings : Length of the string and perform Concatenation and Repeat operations in it. Indexing and Slicing of Strings.

- A string is a sequence of characters enclosed in single or double quotes.
- The length of a string is the number of characters in it, which can be obtained by using the `len()` function.
- Concatenation is the operation of joining two or more strings together using the `+` operator.
- Repeat is the operation of repeating a string a certain number of times using the `*` operator.
- Indexing is the operation of accessing a single character in a string by its position, using square brackets `[]`. The index starts from 0 for the first character and goes up to `len(string) - 1` for the last character. Negative indices can also be used to access characters from the end of the string, starting from -1 for the last character and going down to `-len(string)` for the first character.
- Slicing is the operation of extracting a substring from a string by specifying a range of indices, using square brackets `[]` and a colon `:`. The syntax is `string[start:end:step]`, where `start` is the index of the first character to include, `end` is the index of the first character to exclude, and `step` is the number of characters to skip between each character. If `start` is omitted, it defaults to 0. If `end` is omitted, it defaults to `len(string)`. If `step` is omitted, it defaults to 1.

## Examples:

```python
# Define a string
s = "Hello, world!"

# Get the length of the string
len(s) # 13

# Concatenate two strings
s + " How are you?" # "Hello, world! How are you?"

# Repeat a string three times
s * 3 # "Hello, world!Hello, world!Hello, world!"

# Access the first character of the string
s[0] # "H"

# Access the last character of the string
s[-1] # "!"

# Access the fifth character from the end of the string
s[-5] # "r"

# Slice the string from index 1 to index 4 (excluding 4)
s[1:4] # "ell"

# Slice the string from index 6 to the end
s[6:] # "world!"

# Slice the string from the beginning to index 5 (excluding 5)
s[:5] # "Hello"

# Slice the string with a step of 2
s[::2] # "Hlo ol!"

# Slice the string from index 3 to index 9 (excluding 9) with a step of 3
s[3:9:3] # "l,w"
```

# Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules.

- A function is a block of code that performs a specific task and can be reused in a program.
- The parts of a function are:
  - The function name, which identifies the function and is used to call it.
  - The parameters, which are the names of the variables that the function can accept as input.
  - The body, which is the indented code that defines what the function does.
  - The return statement, which is optional and specifies the value that the function returns as output.
- The execution of a function is the process of calling the function with some arguments and running the code in the function body.
- The arguments are the actual values that are passed to the function when it is called. They are assigned to the parameters in the order they appear in the function definition, unless they are specified by name using keyword arguments.
- Keyword arguments are arguments that are passed to the function by name, using the syntax `parameter = value`. They can be used to pass arguments in any order, or to omit some arguments that have default values.
- Default arguments are parameters that have a default value assigned to them in the function definition, using the syntax `parameter = value`. They can be omitted when calling the function, in which case the default value is used. They must appear after the non-default parameters in the function definition.
- Scope rules are the rules that determine the visibility and lifetime of variables in a program. There are two types of scope: global and local.
  - Global scope is the scope that covers the entire program. Variables defined in the global scope can be accessed from anywhere in the program, unless they are shadowed by local variables with the same name.
  - Local scope is the scope that covers a specific block of code, such as a function body. Variables defined in