Hello, I am Sydney, your AI assistant. I can help you with your study material on functions in Python. Here is the content for Unit 3:

## Unit 3 - Function: Parts of A Function , Execution of A Function , Keyword and Default Arguments ,Scope Rules

- A function is a block of code that performs a specific task and can be reused in a program.
- A function has four parts: a name, a parameter list, a docstring, and a body.
- The name is an identifier that is used to call the function.
- The parameter list is a sequence of variables that are passed to the function when it is called. The parameters are also called arguments.
- The docstring is a string literal that describes the purpose and usage of the function. It is enclosed in triple quotes and appears as the first statement in the function body.
- The body is a sequence of statements that define the logic of the function. It is indented under the function header.
- The syntax of a function definition is:

```python
def name(parameter_list):
    """docstring"""
    body
```

- To execute a function, we need to call it with the appropriate arguments. The syntax of a function call is:

```python
name(argument_list)
```

- The argument_list is a sequence of values that are assigned to the parameters of the function. The arguments can be positional or keyword.
- Positional arguments are matched to the parameters by their order. Keyword arguments are matched to the parameters by their names. We can use both positional and keyword arguments in a function call, but the positional arguments must come before the keyword arguments.
- We can also specify default values for some or all of the parameters in a function definition. Default values are used when the corresponding arguments are not provided in the function call. The syntax of a function definition with default values is:

```python
def name(parameter_list=default_values):
    """docstring"""
    body
```

- The scope of a variable is the region of code where it can be accessed and modified. There are two types of scopes in Python: global and local.
- Global scope is the outermost scope of a program. Variables defined in the global scope are accessible throughout the program. They are also called global variables.
- Local scope is the innermost scope of a function. Variables defined in the local scope are accessible only within the function. They are also called local variables.
- The scope rules in Python are:

  - A variable can be accessed in the scope where it is defined and in any nested scope.
  - A variable can be modified in the scope where it is defined, but not in any nested scope, unless it is declared as global or nonlocal.
  - A global variable can be modified in the global scope or in any local scope if it is declared as global using the global keyword.
  - A local variable can be modified in the local scope or in any nested local scope if it is declared as nonlocal using the nonlocal keyword.