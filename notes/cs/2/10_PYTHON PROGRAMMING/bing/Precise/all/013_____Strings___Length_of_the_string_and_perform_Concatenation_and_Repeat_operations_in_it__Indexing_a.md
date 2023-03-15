# Strings in Python

## Length of the string
- The length of a string can be determined using the `len()` function.
- For example, `len('hello')` returns `5`.

## Concatenation and Repeat operations
- Strings can be concatenated using the `+` operator.
- For example, `'hello' + 'world'` returns `'helloworld'`.
- Strings can be repeated using the `*` operator.
- For example, `'hello' * 3` returns `'hellohellohello'`.

## Indexing and Slicing of Strings
- Strings can be indexed using square brackets `[]`.
- For example, `'hello'[0]` returns `'h'`.
- Negative indexing can be used to access characters from the end of the string.
- For example, `'hello'[-1]` returns `'o'`.
- Slicing can be used to extract a substring from a string.
- For example, `'hello'[1:4]` returns `'ell'`.

# Unit 3 - Function

## Parts of A Function
- A function in Python consists of the following parts:
  - The `def` keyword, followed by the function name and parentheses.
  - The parameters of the function, enclosed in the parentheses.
  - A colon `:` to indicate the start of the function body.
  - The function body, indented to the right.
  - The `return` statement, to return a value from the function.

## Execution of A Function
- A function is executed by calling it by its name, followed by the arguments in parentheses.
- For example, `my_function(3, 4)` calls the function `my_function` with the arguments `3` and `4`.

## Keyword and Default Arguments
- Keyword arguments allow you to specify the value of a parameter by its name.
- For example, `my_function(x=3, y=4)` calls the function `my_function` with the keyword arguments `x=3` and `y=4`.
- Default arguments allow you to specify a default value for a parameter.
- For example, `def my_function(x, y=4):` defines a function `my_function` with a default value of `4` for the parameter `y`.

## Scope Rules
- The scope of a variable determines where it can be accessed.
- Variables defined inside a function have local scope and can only be accessed within the function.
- Variables defined outside a function have global scope and can be accessed from anywhere in the code.