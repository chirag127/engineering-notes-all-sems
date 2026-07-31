## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed number of terms or not.
- A sequence can be represented by a formula, a table, a graph, or a list of terms.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python, Java, or C++.
- To code a sequence, we need to follow these steps:
  - Define the first term of the sequence, usually denoted by a<sub>1</sub>.
  - Define the rule or formula that determines the next term of the sequence, usually denoted by a<sub>n</sub>.
  - Use a loop or a recursion to generate the terms of the sequence until a certain condition is met, such as reaching a certain number of terms, a certain value, or a certain pattern.
  - Store the terms of the sequence in a data structure, such as an array, a list, or a vector.
  - Display or return the sequence as the output of the program.
- For example, to code the sequence 2, 4, 6, 8, ..., we can use the following Python code:

```python
# Define the first term of the sequence
a1 = 2

# Define the rule or formula for the next term
def next_term(a):
  return a + 2

# Define the number of terms to generate
n = 10

# Create an empty list to store the terms
sequence = []

# Use a loop to generate the terms
for i in range(n):
  # Append the current term to the list
  sequence.append(a1)
  # Update the current term by applying the rule
  a1 = next_term(a1)

# Display the sequence
print(sequence)
```