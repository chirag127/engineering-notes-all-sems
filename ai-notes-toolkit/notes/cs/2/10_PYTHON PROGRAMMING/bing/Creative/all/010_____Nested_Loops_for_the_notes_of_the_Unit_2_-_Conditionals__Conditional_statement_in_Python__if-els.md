# Nested Loops

- A nested loop is a loop that is placed inside another loop.
- A nested loop can be of any type: for, while, or do-while.
- A nested loop executes the inner loop for each iteration of the outer loop.
- A nested loop can be used to perform repeated tasks on multidimensional data structures, such as lists, tuples, arrays, matrices, etc.
- A nested loop can also be used to create patterns, such as stars, triangles, squares, etc.

## Syntax of Nested Loops

- The syntax of a nested loop is similar to a single loop, except that the inner loop is indented under the outer loop.
- The general syntax of a nested loop is:

```python
# outer loop
for i in range(n):
    # inner loop
    for j in range(m):
        # loop body
        statement(s)
```

- The above syntax shows a nested for loop, where the outer loop iterates n times and the inner loop iterates m times for each iteration of the outer loop.
- The loop body contains the statements that are executed for each combination of i and j values.
- The loop variables i and j can be used to access the elements of the data structures or to create patterns.

## Example of Nested Loops

- The following example shows how to use a nested loop to print a multiplication table from 1 to 10.

```python
# outer loop
for i in range(1, 11):
    # inner loop
    for j in range(1, 11):
        # print the product of i and j
        print(i * j, end="\t")
    # print a new line after each row
    print()
```

- The output of the above code is:

```
1	2	3	4	5	6	7	8	9	10	
2	4	6	8	10	12	14	16	18	20	
3	6	9	12	15	18	21	24	27	30	
4	8	12	16	20	24	28	32	36	40	
5	10	15	20	25	30	35	40	45	50	
6	12	18	24	30	36	42	48	54	60	
7	14	21	28	35	42	49	56	63	70	
8	16	24	32	40	48	56	64	72	80	
9	18	27	36	45	54	63	72	81	90	
10	20	30	40	50	60	70	80	90	100	
```

- The above example shows how to use a nested loop to create a pattern of stars.

```python
# outer loop
for i in range(1, 6):
    # inner loop
    for j in range(i):
        # print a star
        print("*", end="")
    # print a new line after each row
    print()
```

- The output of the above code is:

```
*
**
***
****
*****
```