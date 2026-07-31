### b) Program to recognize a valid variable which starts with a letter followed by any number of letters or digits.

A valid variable name in most programming languages must start with a letter or an underscore, followed by any number of letters, digits, or underscores. Here is an example of a program that checks if a given string is a valid variable name:

```python
import re

def is_valid_variable_name(name):
    # Regular expression to match a valid variable name
    pattern = '^[a-zA-Z_][a-zA-Z0-9_]*$'
    # Check if the given name matches the pattern
    if re.match(pattern, name):
        return True
    else:
        return False
```

This program uses a regular expression to define the pattern of a valid variable name. The `^` symbol at the beginning of the pattern indicates that the match must start at the beginning of the string. The `[a-zA-Z_]` part of the pattern matches a single character that is either a letter or an underscore. The `[a-zA-Z0-9_]*` part of the pattern matches zero or more characters that are either letters, digits, or underscores. The `$` symbol at the end of the pattern indicates that the match must end at the end of the string.

The `re.match` function is used to check if the given `name` matches the defined `pattern`. If it does, the function returns `True`, indicating that the given `name` is a valid variable name. Otherwise, the function returns `False`.

Here are some examples of how this function can be used:

```python
print(is_valid_variable_name('myVariable')) # True
print(is_valid_variable_name('_private_var')) # True
print(is_valid_variable_name('2nd_var')) # False
print(is_valid_variable_name('var-with-hyphen')) # False
```

In these examples, the first two variable names are valid because they start with a letter or an underscore, followed by any number of letters, digits, or underscores. The last two variable names are not valid because they start with a digit or contain a character that is not a letter, digit, or underscore.