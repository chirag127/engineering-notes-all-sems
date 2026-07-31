### Nested Loops

- A nested loop is a loop that is placed inside another loop.
- The inner loop is executed once for each iteration of the outer loop.
- The syntax of a nested loop in Python is:

```python
for i in range(n): # outer loop
  for j in range(m): # inner loop
    # do something with i and j
```

- Nested loops can be used to perform various tasks, such as:
  - Printing patterns or shapes
  - Iterating over multidimensional data structures (such as lists of lists, matrices, etc.)
  - Searching or sorting algorithms
  - Simulating complex scenarios (such as games, simulations, etc.)

- Some examples of nested loops are:

```python
# Printing a square of asterisks
n = 5 # size of the square
for i in range(n):
  for j in range(n):
    print("*", end=" ") # print an asterisk and a space
  print() # print a new line

# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
```

```python
# Printing a multiplication table
n = 10 # size of the table
for i in range(1, n+1):
  for j in range(1, n+1):
    print(i*j, end="\t") # print the product and a tab
  print() # print a new line

# Output:
# 1	2	3	4	5	6	7	8	9	10
# 2	4	6	8	10	12	14	16	18	20
# 3	6	9	12	15	18	21	24	27	30
# 4	8	12	16	20	24	28	32	36	40
# 5	10	15	20	25	30	35	40	45	50
# 6	12	18	24	30	36	42	48	54	60
# 7	14	21	28	35	42	49	56	63	70
# 8	16	24	32	40	48	56	64	72	80
# 9	18	27	36	45	54	63	72	81	90
# 10	20	30	40	50	60	70	80	90	100
```

```python
# Finding the maximum element in a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # a 3x3 matrix
max_element = matrix[0][0] # initialize the maximum element to the first element
for i in range(len(matrix)): # iterate over the rows
  for j in range(len(matrix[i])): # iterate over the columns
    if matrix[i][j] > max_element: # compare the current element with the maximum element
      max_element = matrix[i][j] # update the maximum element if needed
print("The maximum element is", max_element) # print the result

# Output:
# The maximum element is 9
```