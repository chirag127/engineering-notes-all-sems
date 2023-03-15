##### Function Point (FP) Based Measures in software design

Function Point (FP) is a measure of the functionality provided by a software system. It is based on the user's view of the system and is independent of the technology used to implement the system. The FP measure is used to estimate the size of a software project and to measure the productivity of a software development team.

Here is an example of how to calculate the Function Point (FP) for a software project:

```python
# Define the complexity weights for each type of component
complexity_weights = {
    'EI': {'low': 3, 'average': 4, 'high': 6},
    'EO': {'low': 4, 'average': 5, 'high': 7},
    'EQ': {'low': 3, 'average': 4, 'high': 6},
    'ILF': {'low': 7, 'average': 10, 'high': 15},
    'EIF': {'low': 5, 'average': 7, 'high': 10}
}

# Define the number of components for each type and complexity
components = {
    'EI': {'low': 3, 'average': 2, 'high': 1},
    'EO': {'low': 2, 'average': 3, 'high': 1},
    'EQ': {'low': 2, 'average': 2, 'high': 1},
    'ILF': {'low': 1, 'average': 2, 'high': 1},
    'EIF': {'low': 1, 'average': 1, 'high': 1}
}

# Calculate the Unadjusted Function Point (UFP)
UFP = 0
for component_type in components:
    for complexity in components[component_type]:
        UFP += components[component_type][complexity] * complexity_weights[component_type][complexity]

# Define the Technical Complexity Factor (TCF)
TCF = 0.65 + 0.01 * 10 # Assuming all 14 General System Characteristics have an average value of 10

# Calculate the Function Point (FP)
FP = UFP * TCF

print(FP)
```

This code calculates the Function Point (FP) for a software project based on the number and complexity of its components. The complexity weights and the number of components for each type and complexity are defined at the beginning of the code. The Unadjusted Function Point (UFP) is calculated by multiplying the number of components by their complexity weights. The Technical Complexity Factor (TCF) is then calculated based on the General System Characteristics of the project. Finally, the Function Point (FP) is calculated by multiplying the UFP by the TCF. The result is printed at the end of the code.