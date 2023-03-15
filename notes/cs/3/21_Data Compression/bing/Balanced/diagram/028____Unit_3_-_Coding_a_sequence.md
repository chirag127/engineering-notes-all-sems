## Unit 3 - Coding a sequence

- A sequence is a set of ordered values or items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed or unlimited number of terms.
- A sequence can be represented by a formula, a table, a graph, or a list of values.
- To code a sequence, we need to use a loop structure that repeats a set of instructions for each term of the sequence.
- A loop structure can be a for loop, a while loop, or a do-while loop, depending on the programming language and the logic of the sequence.
- A for loop is used when we know the exact number of iterations or the range of values for the sequence.
- A while loop is used when we do not know the exact number of iterations or the range of values for the sequence, but we have a condition that determines when to stop the loop.
- A do-while loop is similar to a while loop, but it executes the instructions at least once before checking the condition.
- To code a sequence, we also need to use a variable that stores the current term of the sequence, and update it according to the formula or the rule of the sequence.
- We can also use another variable to store the index or the position of the current term in the sequence, and increment it by one for each iteration of the loop.
- We can also use an array or a list to store the terms of the sequence, and access them by using the index variable as the subscript or the index of the array or the list.
- We can also use a function or a method to generate the terms of the sequence, and call it inside the loop with the appropriate arguments or parameters.
- We can also use a print statement or a return statement to display or output the terms of the sequence, either individually or as a whole.
- Here is an example of coding a sequence in Python:

```python
# The sequence is the Fibonacci sequence, which starts with 1 and 1, and each term is the sum of the previous two terms.
# The sequence is infinite, but we will only generate the first 10 terms.

# Define a function that takes an index as a parameter and returns the corresponding term of the sequence
def fibonacci(n):
  # Base cases: if n is 1 or 2, return 1
  if n == 1 or n == 2:
    return 1
  # Recursive case: if n is greater than 2, return the sum of the previous two terms
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Use a for loop to iterate from 1 to 10, and call the function with the index as the argument
for i in range(1, 11):
  # Print the term of the sequence
  print(fibonacci(i))
```