## Unit 3 - Coding a sequence

- A sequence is a set of ordered values or items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed or unlimited number of terms.
- A sequence can be represented by a formula, a table, a graph, or a list of values.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python, Java, or C++.
- To code a sequence, we need to follow these steps:
  - Define the first term or the initial value of the sequence.
  - Define the rule or the function that determines the next term based on the previous term or the position of the term in the sequence.
  - Use a loop or a recursion to iterate over the sequence and generate the desired number of terms or until a certain condition is met.
  - Store the sequence in a data structure, such as an array, a list, or a vector, that can hold multiple values of the same type.
  - Display or return the sequence as the output of the program or the function.

- For example, to code the sequence 2, 4, 6, 8, ..., we can use the following Python code:

```python
# Define the first term of the sequence
first_term = 2

# Define the rule of the sequence
def rule(n):
  # The next term is 2 more than the previous term
  return n + 2

# Define the number of terms to generate
num_terms = 10

# Create an empty list to store the sequence
sequence = []

# Use a for loop to iterate over the sequence
for i in range(num_terms):
  # Append the current term to the list
  sequence.append(first_term)
  # Update the first term to the next term using the rule
  first_term = rule(first_term)

# Print the sequence
print(sequence)
```

- The output of the code is:

```python
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

- This is the end of Unit 3 - Coding a sequence.