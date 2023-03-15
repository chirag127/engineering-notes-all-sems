##### Cyclomatic Complexity Measures in software design

Cyclomatic complexity is a software metric used to measure the complexity of a program. It is calculated by developing a Control Flow Graph of the code that measures the number of linearly-independent paths through a program module. This metric is used to indicate the complexity of a program and can be useful in determining the number of test cases needed to achieve thorough test coverage of a module.

Here is an example of how to calculate the cyclomatic complexity of a program in Python:

```python
def cyclomatic_complexity(code):
    """
    Calculate the cyclomatic complexity of a given code.
    """
    # Count the number of branching statements
    branches = code.count('if') + code.count('elif') + code.count('for') + code.count('while') + code.count('and') + code.count('or') + code.count('case')
    # Add 1 for the implicit entry point of the function
    complexity = branches + 1
    return complexity
```

This function takes in a string containing the code and returns the cyclomatic complexity of the code. It does this by counting the number of branching statements in the code and adding 1 for the implicit entry point of the function. The resulting value is the cyclomatic complexity of the code.