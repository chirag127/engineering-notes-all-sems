## Unit 3 - Coding a sequence

- A sequence is a set of ordered items that follow a certain pattern or rule.
- A sequence can be finite or infinite, depending on whether it has a fixed or unlimited number of terms.
- A sequence can be represented by a formula that generates each term from its position or index in the sequence.
- A sequence can also be represented by a list of its terms, separated by commas and enclosed in brackets or parentheses.
- For example, the sequence of even numbers can be represented by the formula 2n, where n is the index, or by the list [2, 4, 6, 8, ...].
- To code a sequence, we need to use a loop that iterates over the indices or positions of the terms, and calculates each term using the formula or rule of the sequence.
- We also need to store the terms in a data structure, such as a list or an array, that can hold multiple values of the same type.
- We can use a for loop or a while loop to code a sequence, depending on the situation and preference.
- A for loop is more suitable when we know the exact number of iterations or terms in the sequence, and we want to use a fixed increment or step for the index.
- A while loop is more suitable when we do not know the exact number of iterations or terms in the sequence, and we want to use a variable or condition to control the loop.
- For example, to code the sequence of even numbers up to 100 using a for loop, we can write:

```python
# create an empty list to store the terms
even_numbers = []

# loop from 1 to 50, since 2 * 50 = 100
for n in range(1, 51):
  # calculate the term using the formula 2n
  term = 2 * n
  # append the term to the list
  even_numbers.append(term)

# print the list of terms
print(even_numbers)
```

- To code the same sequence using a while loop, we can write:

```python
# create an empty list to store the terms
even_numbers = []

# initialize the index to 1
n = 1

# loop until the term exceeds 100
while True:
  # calculate the term using the formula 2n
  term = 2 * n
  # check if the term is greater than 100
  if term > 100:
    # break the loop
    break
  # append the term to the list
  even_numbers.append(term)
  # increment the index by 1
  n = n + 1

# print the list of terms
print(even_numbers)
```