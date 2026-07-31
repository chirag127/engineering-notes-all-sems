### b) Program to recognize a valid variable which starts with a letter followed by any number of letters or digits.

A valid variable name in most programming languages must start with a letter or an underscore, followed by any number of letters, digits, or underscores. Here is an example of a program that checks if a given string is a valid variable name:

```python
import re

def is_valid_variable_name(name):
    # Regular expression to match a valid variable name
    pattern = '^[a-zA-Z_][a-zA-Z0-9_]*$'
    if re.match(pattern, name):
        return True
    else:
        return False
```

This program uses a regular expression to match the given string against the pattern for a valid variable name. The `^` at the beginning of the pattern indicates that the match must start at the beginning of the string, while the `$` at the end indicates that the match must end at the end of the string. The `[a-zA-Z_]` part of the pattern matches a single letter or underscore, while the `[a-zA-Z0-9_]*` part matches zero or more letters, digits, or underscores.

Here are some examples of how this program can be used:

```python
print(is_valid_variable_name('myVariable')) # True
print(is_valid_variable_name('_private_var')) # True
print(is_valid_variable_name('2nd_var')) # False
print(is_valid_variable_name('var-with-hyphen')) # False
```

In the first two examples, the given strings are valid variable names, so the function returns `True`. In the last two examples, the given strings are not valid variable names, so the function returns `False`.