### Nested Loops

- A nested loop is a loop that is placed inside another loop.
- A nested loop can be of any type: for, while, or do-while.
- A nested loop executes the inner loop for each iteration of the outer loop.
- A nested loop can be used to perform repeated tasks on multidimensional data structures, such as lists, tuples, arrays, matrices, etc.
- A nested loop can also be used to create patterns, such as stars, triangles, squares, etc.

#### Syntax of a nested loop

The general syntax of a nested loop is:

```
outer_loop_condition:
    # outer loop body
    inner_loop_condition:
        # inner loop body
```

#### Example of a nested loop

The following example shows how to use a nested loop to print a multiplication table from 1 to 10:

```
# outer loop for rows
for i in range(1, 11):
    # inner loop for columns
    for j in range(1, 11):
        # print the product of i and j
        print(i * j, end="\t")
    # print a new line after each row
    print()
```

The output of the above code is:

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