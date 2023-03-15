## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed number of terms or not.
- A sequence can be represented by a formula, a table, a graph, or a list of terms.
- To code a sequence, we need to use a programming language that can generate and manipulate sequences, such as Python, Java, or C++.
- To code a sequence, we need to follow these steps:
  - Define the first term of the sequence, usually denoted by a<sub>1</sub>.
  - Define the rule or formula that determines the next term of the sequence, usually denoted by a<sub>n</sub>.
  - Use a loop or a recursion to generate the terms of the sequence until a certain condition is met, such as reaching a limit, a target, or an error.
  - Store, display, or return the terms of the sequence as desired.
- For example, to code the sequence of even numbers starting from 2, we can use the following Python code:

```python
# Define the first term of the sequence
a1 = 2
# Define the rule or formula that determines the next term of the sequence
def next_term(a):
  return a + 2
# Use a loop to generate the terms of the sequence until a limit is reached
limit = 20
a = a1
while a <= limit:
  # Display the term of the sequence
  print(a)
  # Update the term of the sequence using the rule or formula
  a = next_term(a)
```

- The output of this code is:

```text
2
4
6
8
10
12
14
16
18
20
```